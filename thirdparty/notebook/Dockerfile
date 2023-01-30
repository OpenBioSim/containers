FROM openbiosim/notebook:latest

# Download everything
RUN git clone https://github.com/plumed/plumed2.git
RUN wget http://ftp.gromacs.org/pub/gromacs/gromacs-2022.4.tar.gz -O gromacs-src.tar.gz && \
    mkdir gromacs-build && \
    tar -xzf gromacs-src.tar.gz -C gromacs-build --strip 1

ENTRYPOINT ["bash"]
