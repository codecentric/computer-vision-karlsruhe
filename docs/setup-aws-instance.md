# AWS GPU Instanz mit OpenCV und Tensorflow einrichten

## Überblick

* Setze AWS GPU Instanz mit Ubuntu 16.04 auf
* Server updaten und rebooten
* Installiere CUDA und cuDNN (von NVIDIA)
* Installiere OpenCV 3.3 mit Python 3.5
* Installiere Tensorflow
* (Installiere Caffe)

### GPU Instanz einrichten 

* starte p2.xlarge Instanz
* erstelle Keypair "gpu-instance.pem"
* EBS Festplatte mit 30 GB (30 GB sind im Free-Tier enthalten und verursachen so keine Kosten, 
  wenn Instanz gestoppt ist)
* mit Ubuntu Server 16.04 LTS
* mit öffentlich erreichbarer IP Adresse

### Auf Server anmelden und auf neuesten Stand bringen

```
ssh -i ~/.ssh/gpuserver.pem ubuntu@54.154.14.XXX

sudo -i
apt update
apt dist-upgrade
reboot
```

### Installiere Dependencies

```
sudo -i
apt install -y gcc g++ gfortran build-essential \
    git wget linux-image-generic libopenblas-dev \
    liblapack-dev libblas-dev cmake unzip \
    pkg-config libopenblas-dev linux-source linux-headers-generic \
    python3 python3-pip libffi-dev libssl-dev tmux emacs24-nox liblapacke-dev checkinstall \
    virtualenvwrapper libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev \
    libjasper-dev libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
    libxvidcore-dev libx264-dev libgtk-3-dev libatlas-base-dev gfortran \
    python3.5-dev libcupti-dev gstreamer1.0 ffmpeg libhdf5-serial-dev

``` 
    
## Installiere CUDA

* Download CUDA 8 und cuDNN 6 von NVIDIA
http://docs.nvidia.com/cuda/cuda-installation-guide-linux/#axzz4WNL7OgLr

```


```

Die Fragen beantworten:

``` 
Do you accept the previously read EULA?
accept/decline/quit: accept  

Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 384.81?
(y)es/(n)o/(q)uit: y

Do you want to install the OpenGL libraries?
(y)es/(n)o/(q)uit [ default is yes ]: 

Do you want to run nvidia-xconfig?
This will update the system X configuration file so that the NVIDIA X driver
is used. The pre-existing X configuration file will be backed up.
This option should not be used on systems that require a custom
X configuration, such as systems with multiple GPU vendors.
(y)es/(n)o/(q)uit [ default is no ]: 

Install the CUDA 9.0 Toolkit?
(y)es/(n)o/(q)uit: y

Enter Toolkit Location
 [ default is /usr/local/cuda-9.0 ]: 

Do you want to install a symbolic link at /usr/local/cuda?
(y)es/(n)o/(q)uit: y

Install the CUDA 9.0 Samples?
(y)es/(n)o/(q)uit: y

Enter CUDA Samples Location
 [ default is /home/ubuntu ]: 

```

Test:

```
root@ip-172-31-1-253:~# nvidia-smi 
Thu Oct 19 11:34:32 2017       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 384.81                 Driver Version: 384.81                    |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla K80           Off  | 00000000:00:1E.0 Off |                    0 |
| N/A   45C    P0    74W / 149W |      0MiB / 11439MiB |     99%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

## Pfade

``` 
echo "/usr/local/cuda-9.0/lib64" >> /etc/ld.so.conf
ldconfig
echo 'PATH=$PATH:/usr/local/cuda-9.0/bin' >> /etc/profile
```

## cuDNN
``` 
scp Downloads/cudnn-9.0-linux-x64-v7.3.tgz ubuntu@YOUR_PUB_IP:~
ssh ubuntu@YOUR_PUB_IP
tar -xvf cudnn-9.0-linux-x64-v7.3.tgz 

sudo cp cuda/lib64/* /usr/local/cuda/lib64
sudo cp cuda/include/* /usr/local/cuda/include/
```

## Get Python 3.6

mkdir my_libs
wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
ubuntu@ip-172-31-1-253:~/my_libs/Python-3.6.3$ ./configure --enable-optimizations

make
sudo make install

logout/login

mkvirtualenv -p /usr/local/bin/python3.6 computer-vision


``` 
wget -O opencv.zip https://github.com/opencv/opencv/archive/3.3.0.zip
unzip opencv.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.3.0.zip
unzip opencv_contrib.zip
```

pip install numpy h5py

``` 
cd opencv-3.3.0
$ mkdir build
$ cd build
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D WITH_CUDA=ON \
    -D ENABLE_FAST_MATH=1 \
    -D CUDA_FAST_MATH=1 \
    -D WITH_CUBLAS=1 \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.3.0/modules \
    -D BUILD_EXAMPLES=ON ..
    ```