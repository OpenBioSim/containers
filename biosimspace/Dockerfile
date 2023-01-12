from openbiosim/sire:latest

LABEL maintainer="Christopher Woods <chryswoods@openbiosim.org>, Lester Hedges <lester@openbiosim.org>"

USER openbiosim
WORKDIR /home/openbiosim

RUN mamba install -y -n openbiosim -c openbiosim \
    biosimspace ambertools gromacs plumed && \
    mamba clean -y --all && \
    rm -rf /home/openbiosim/.conda/pkgs/*

ENTRYPOINT /bin/bash
