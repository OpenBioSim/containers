# Start from the base jupyterhub image.
FROM jupyter/base-notebook:python-3.9
LABEL maintainer="Christopher Woods <chryswoods@openbiosim.org>, Lester Hedges <lester@openbiosim.org>"

USER $NB_USER
WORKDIR $HOME

RUN conda install -y -c conda-forge mamba

RUN mamba install -y -c "openbiosim/label/dev" -c conda-forge \
    biosimspace sire \
    ambertools gromacs plumed patch \
    ipython git nano && \
    mamba clean -y --all && \
    rm -rf $HOME/.conda/pkgs/*

# Add in our custom notebook config.
USER root

# End as the User to make sure that we don't
# accidentally run the container as root.
USER $NB_USER
