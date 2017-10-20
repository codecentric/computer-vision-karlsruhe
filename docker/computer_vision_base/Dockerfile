# python3 opencv3 dockerfile

# Pull base image.
FROM ubuntu:16.04

MAINTAINER Oli Moser <oli.moser@gmail.com>

ENV cv_version 3.3.0

RUN apt-get update
RUN apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    unzip \
    pkg-config \
    libswscale-dev \
    python3-dev \
    python3-numpy \
    python3-pip \
    libtbb2 \
    libtbb-dev \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    libjasper-dev \
    libavformat-dev

RUN apt-get -y clean all
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/${cv_version}.zip
RUN wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/${cv_version}.zip
RUN unzip opencv.zip
RUN unzip opencv_contrib.zip
RUN mkdir /app/opencv-${cv_version}/cmake_binary
RUN cd /app/opencv-${cv_version}/cmake_binary
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-${cv_version}/modules \
    -D BUILD_EXAMPLES=ON /app/opencv-${cv_version}/
RUN make install

RUN rm /app/${cv_version}.zip
RUN rm -r /app/opencv-${cv_version}

RUN pip3 install --upgrade pip
RUN pip3 install virtualenv virtualenvwrapper
RUN pip3 install numpy


