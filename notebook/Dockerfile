# Start from the base jupyterhub image.
FROM jupyter/base-notebook:python-3.10
LABEL maintainer="Christopher Woods <chryswoods@openbiosim.org>, Lester Hedges <lester@openbiosim.org>"

USER $NB_USER
WORKDIR $HOME

# Install gromacs and plumed into /opt
ADD gromacs.tar.gz /opt
ADD plumed2.tar.gz /opt

# Set the environment variables so these two will work
ENV LD_LIBRARY_PATH=/opt/plumed2/lib:/opt/conda/lib.AVX_256:/opt/conda/lib
ENV PATH=/opt/gromacs/bin:/opt/plumed2/bin:$PATH
ENV PLUMED_KERNEL=/opt/plumed2/libplumedKernel.so

# Install mamba for faster installs
RUN conda install -y -c conda-forge mamba

# Now install BioSimSpace, sire and other useful tools
RUN mamba install -y -c openbiosim -c conda-forge \
    biosimspace==2023.3.0 sire==2023.3.0 \
    ambertools gromacs plumed patch \
    ipython git nano \
    openblas openmpi-mpicxx && \
    mamba clean -y --all && \
    rm -rf $HOME/.conda/pkgs/*

# Now install tutorial dependencies
RUN mamba install -y -c conda-forge \
    cinnabar==0.3.0 alchemlyb==2.1.0

ADD README.txt $HOME/README.txt
ADD TUTORIALS.txt $HOME/TUTORIALS.txt

# Add extra environment variables as needed
ENV AMBERHOME=/opt/conda
ENV PLUMED_ROOT=/opt/plumed2/lib/plumed

# End as the User to make sure that we don't
# accidentally run the container as root.
USER $NB_USER
