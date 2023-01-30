FROM openbiosim/notebook:latest

# Download everything
RUN git clone https://github.com/plumed/plumed2.git
RUN wget http://ftp.gromacs.org/pub/gromacs/gromacs-2022.4.tar.gz -O gromacs-src.tar.gz && \
    mkdir gromacs-build && \
    tar -xzf gromacs-src.tar.gz -C gromacs-build --strip 1

RUN mamba install -y make gcc gxx openmpi openblas openssh

USER root

RUN cd plumed2 && \
    ./configure --enable-mpi --disable-python --prefix=/opt/plumed && \
    make CC="mpicc" -j 4 LDFLAGS="-L/opt/conda/lib -lgomp -lgsl -lopenblas -lfftw3 -lz" && \
    make install && \
    tar -jcvf /home/jovyan/plumed.tar.bz2 /opt/plumed && \
    cd $HOME && \
    rm -rf plumed2

ENTRYPOINT ["bash"]

