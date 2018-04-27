FROM ubuntu

RUN apt-get update && apt-get -y install curl gcc-4.8 g++-4.8 cmake python3

RUN apt-get -y install python3-pip git

RUN pip3 install conan

# install IIB at the correct version
RUN cd /opt && curl http://host/iib-image.tar.gz | tar -xjf -

RUN cd /root && git clone https://github.com/ot4i/iib-stats-writer-statsd
CMD [ "/bin/bash" ]

# Run the following in the build container:
#export CC=/usr/bin/gcc-4.8
#export CXX=/usr/bin/g++-4.8
#cd iib-stats-writer-statsd
#conan install . --build missing
#cmake -DIIB_INSTALL_DIR=/opt/iib-10.0.0.11
#cmake --build .
#ctest -V
