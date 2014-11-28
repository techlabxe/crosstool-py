crosstool-py
============

build crosstool by python script


* CentOS 6.6

```
yum groupinstall 'Development tools'
# required by gdb, not in 'Development tools'...
yum install ncurses-devel,expat-devel
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
    |-- MIPSCreatorCI20
    |-- raspbian20140909
    `-- TegraLinuxR21.1.0
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

## tegra

Tegra Jetson TK1

```
 mkdir -p ~/work/build/tegra
 cd ~/work/build/tegra
 python ~/work/crosstool-py/script/tegra/build48armhf.py 2>&1 | tee _log48mipsel.txt
```

