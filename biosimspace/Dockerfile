from openbiosim/sire:latest

LABEL maintainer="Christopher Woods <chryswoods@openbiosim.org>, Lester Hedges <lester@openbiosim.org>"

USER openbiosim
WORKDIR /home/openbiosim

ADD install_biosimspace.py /home/openbiosim/install_biosimspace.py
RUN python install_biosimspace.py && rm install_biosimspace.py

ENTRYPOINT /bin/bash
