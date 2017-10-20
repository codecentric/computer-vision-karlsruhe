# codecentric images for computer vision and deep learning
# base image provides ssh access to container
# create ssh-keypair and put publick key in files/authorized_keys

# Pull base image.
FROM codecentric/cv_base:latest

MAINTAINER Oli Moser <https://twitter.com/moseroli>

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
    libavformat-dev x11-apps libgtk2.0-dev pkg-config

RUN apt-get -y clean all
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install numpy

RUN wget -O opencv.zip https://github.com/opencv/opencv/archive/${cv_version}.zip
RUN wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/${cv_version}.zip
RUN unzip opencv.zip
RUN unzip opencv_contrib.zip
RUN mkdir /app/opencv-${cv_version}/cmake_binary
RUN cd /app/opencv-${cv_version}/cmake_binary
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=/app/opencv_contrib-${cv_version}/modules \
    -D BUILD_EXAMPLES=ON /app/opencv-${cv_version}/
RUN make install -j4

RUN rm /app/opencv_*.zip
RUN rm -r /app/opencv-${cv_version}

RUN chown cv_user:cv_user /app/.


