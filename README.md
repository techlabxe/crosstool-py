crosstool-py
============

build crosstool by python script


* CentOS 6.6

```
yum groupinstall 'Development tools'
# required by gdb, not in 'Development tools'...
yum install ncurses-devel expat-devel texinfo
```

* Ubuntu 12.04 LTS

```
apt-get install build-essential
apt-get install bison texinfo
apt-get install libncurses5-dev libexpat1-dev
```

for host_mingw-w64-i686 and host_mingw64-x86_64
```
apt-get install mingw-w64 g++-mingw-w64 g++-mingw-w64-i686 g++-mingw-w64-x86-64
```

Japan user:

if you use 'jp.archive.ubuntu.com',
'apt-get update' and 'apt-get install build-essential' doesn't work.(2014-11-29)

switch to JAIST
```
sudo cp /etc/apt/sources.list /etc/apt/sources.list.orig
sudo chmod 444 /etc/apt/sources.list.orig
sudo sed -i".back" -e "s,//jp.archive.ubuntu.com,//ftp.jaist.ac.jp/pub/Linux,g" /etc/apt/sources.list
```



* expect directory tree

```
~/work/
|-- build
|   |-- mipsci20
|   |-- raspbian
|   `-- tegra
|-- crosstool-py
|   |-- crosstool_py
|   `-- script
|       |-- mipsci20
|       |-- raspbian
|       `-- tegra
|-- src_root
|   |-- binutils-2.24
|   |-- cloog-0.18.1
|   |-- gcc-4.8.3
|   |-- gcc-4.9.2
|   |-- gdb-7.8.1
|   |-- gmp-5.1.3
|   |-- isl-0.12.2
|   |-- mpc-1.0.2
|   |-- mpfr-3.1.2
`-- target_root
    |-- MIPSCreatorCI20_20150115
    |-- raspbian20140909
    `-- TegraLinuxR21.2.0
```

# build

## mipsci20

MIPS Creator CI20

```
 mkdir -p ~/work/build/mipsci20
 cd ~/work/build/mipsci20
 python ~/work/crosstool-py/script/mipsci20/build48mipsel.py 2>&1 | tee _log48mipsel.txt
```

## raspbian

Raspberry Pi

```
 mkdir -p ~/work/build/raspbian
 cd ~/work/build/raspbian
 python ~/work/crosstool-py/script/raspbian/build48armhf.py 2>&1 | tee _log48mipsel.txt
```

build test
```
cp -a ~/work/target_root/raspbian20140909/opt/vc/src/hello_pi .
cd hello_pi
# hello_fft build fail. suppurt self build only
cp hello_fft/makefile hello_fft/makefile.orig
cat hello_fft/makefile.orig | sed -e "s,gcc,\$\(CC\),g" | sed -e "s,-lrt -lm,-lrt -lm -lpthread,g" > hello_fft/makefile
#
PATH=~/gcc48raspbian/bin:$PATH \
CC=~/gcc48raspbian/bin/arm-linux-gnueabihf-gcc \
AR=~/gcc48raspbian/bin/arm-linux-gnueabihf-ar \
LDFLAGS='-ldl -Wl,-trace' \
SDKSTAGE=~/gcc48raspbian/sys-root \
sh rebuild.sh
```

## tegra

Tegra Jetson TK1

```
 mkdir -p ~/work/build/tegra
 cd ~/work/build/tegra
 python ~/work/crosstool-py/script/tegra/build48armhf.py 2>&1 | tee _log48armhf.txt
```

