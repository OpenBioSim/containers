# Start from the base jupyterhub image.
FROM jupyter/base-notebook:python-3.9
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
RUN mamba install -y -c "openbiosim/label/dev" -c conda-forge \
    biosimspace sire \
    ambertools gromacs plumed patch \
    ipython git nano \
    openblas openmpi-mpicxx && \
    mamba clean -y --all && \
    rm -rf $HOME/.conda/pkgs/*

ADD README.txt $HOME/README.txt

# End as the User to make sure that we don't
# accidentally run the container as root.
USER $NB_USER
