# Start from the base jupyterhub image.
FROM jupyter/base-notebook:python-3.9
LABEL maintainer="Christopher Woods <chryswoods@openbiosim.org>, Lester Hedges <lester.hedges@openbiosim.org>"

USER $NB_USER
WORKDIR $HOME

RUN pip install --upgrade pip && \
    pip install jupyterhub-tmpauthenticator && \
    rm -rf $HOME/.cache

RUN conda install -y -c conda-forge mamba

RUN mamba install -y -c michellab -c conda-forge \
    biosimspace ambertools gromacs plumed patch \
    ipython git nano && \
    mamba clean -y --all && \
    rm -rf $HOME/.conda/pkgs/*

ADD patches .patches

# Patch the BioSimSpace install so that we restrict GROMACS to use a single
# MPI thread and four OpenMP thread per MPI thread.
RUN patch /opt/conda/lib/python3.9/site-packages/BioSimSpace/Process/_gromacs.py .patches/_gromacs.py.patch
RUN patch /opt/conda/lib/python3.9/site-packages/BioSimSpace/Metadynamics/_metadynamics.py .patches/_metadynamics.py.patch

# Add in our custom notebook config.
USER root

# Copy acrross JupyterHub configuration.
COPY jupyterhub_config.py /etc/jupyter/

# End as the User to make sure that we don't
# accidentally run the container as root.
USER $NB_USER
