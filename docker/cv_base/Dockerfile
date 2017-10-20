# codecentric images for computer vision and deep learning
# base image provides ssh access to container
# create ssh-keypair and put publick key in files/authorized_keys

# Pull base image.
FROM ubuntu:16.04

MAINTAINER Oli Moser <https://twitter.com/moseroli>

RUN apt-get update
RUN apt-get install -y \
    build-essential \
    cmake \
    git \
    wget \
    unzip \
    openssh-server

RUN apt-get -y clean all
RUN rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/sshd

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

RUN useradd -ms /bin/bash cv_user

RUN mkdir -p /home/cv_user/.ssh/
RUN chmod 500 /home/cv_user/.ssh/
ADD files/authorized_keys /home/cv_user/.ssh/authorized_keys

RUN chown -R cv_user:cv_user /home/cv_user/


EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
