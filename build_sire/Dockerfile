from condaforge/mambaforge:latest

WORKDIR /root

LABEL maintainer="Christopher Woods <chryswoods@openbiosim.org>, Lester Hedges <lester.hedges@openbiosim.org>"

RUN useradd -ms /bin/bash openbiosim
USER openbiosim
WORKDIR /home/openbiosim

# This is the version of python to build
# Specify it at build time using '--build-arg python_version=value'
# e.g. '--build-arg python_version=3.9'
ARG python_version=3.9

RUN mamba create -y -n openbiosim python==$python_version && \
    mamba install -y -n openbiosim -c conda-forge \
    git nano boa anaconda-client packaging=21 pip-requirements-parser && \
    mamba clean -y --all && \
    rm -rf /home/openbiosim/.conda/pkgs/*

COPY bashrc /home/openbiosim/.bashrc

# This is the branch to build (default 'main')
# Specify it at build time using '--build-arg branch=value',
# e.g. '--build-arg branch=main'
ARG branch=main

# This is the github url to clone
# Specify it at build time using '--build-arg github_url=value',
# e.g. '--build-arg github_url=https://github.com/openbiosim/sire'
ARG github_url=https://github.com/michellab/sire

RUN git clone -b $branch --single-branch $github_url ./source

COPY build.sh /home/openbiosim/build.sh

RUN bash -l -c /home/openbiosim/build.sh

ENTRYPOINT /bin/bash
