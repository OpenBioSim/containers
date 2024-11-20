from condaforge/mambaforge:latest

WORKDIR /root

LABEL maintainer="Christopher Woods <chryswoods@openbiosim.org>, Lester Hedges <lester@openbiosim.org>"

RUN useradd -ms /bin/bash openbiosim
USER openbiosim
WORKDIR /home/openbiosim

RUN mamba create -y -n openbiosim "python<3.12" && \
    mamba install -y -n openbiosim -c conda-forge -c openbiosim "sire==2023.4.0" && \
    mamba install -y -n openbiosim ipython jupyterlab git nano rdkit && \
    mamba clean -y --all && \
    rm -rf /home/openbiosim/.conda/pkgs/*

COPY bashrc /home/openbiosim/.bashrc

ENTRYPOINT /bin/bash
