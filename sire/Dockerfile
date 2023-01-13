from condaforge/mambaforge:latest

WORKDIR /root

LABEL maintainer="Christopher Woods <chryswoods@openbiosim.org>, Lester Hedges <lester@openbiosim.org>"

RUN useradd -ms /bin/bash openbiosim
USER openbiosim
WORKDIR /home/openbiosim

RUN mamba create -y -n openbiosim "python<3.10" && \
    mamba install -y -n openbiosim -c openbiosim sire && \
    mamba install -y -n openbiosim ipython jupyterlab git nano && \
    mamba clean -y --all && \
    rm -rf /home/openbiosim/.conda/pkgs/*

COPY bashrc /home/openbiosim/.bashrc

ENTRYPOINT /bin/bash
