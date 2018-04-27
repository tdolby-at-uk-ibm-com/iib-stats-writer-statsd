FROM centos:7

RUN yum -y install bzip2 less gcc gcc-c++ git lftp which make
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && python get-pip.py
RUN pip install conan

# install IIB at the correct version
RUN cd /opt && curl http://host/iib-image.tar.gz | tar -xjf -

# Install appropriate CMake level
RUN cd /opt && curl https://cmake.org/files/v3.5/cmake-3.5.0-Linux-x86_64.tar.gz | tar -xzf -

RUN cd /root && git clone https://github.com/ot4i/iib-stats-writer-statsd
CMD [ "/bin/bash" ]

#cd iib-stats-writer-statsd
#export PATH=/opt/cmake-3.5.0-Linux-x86_64/bin:$PATH
#conan install . --build missing
#cmake -DIIB_INSTALL_DIR=/opt/10.0.0.11
#cmake --build .
#ctest -V
