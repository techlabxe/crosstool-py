#!/usr/bin/env python

import shutil
from optparse import OptionParser

PREFIX='~/gcc48tegra'
TARGET='arm-linux-gnueabihf'
SRCROOT='~/work/src_root'
TARGETROOT='~/work/target_root/TegraLinuxR21.1.0'

my_ver_binutils='2.24'
my_ver_gmp='5.1.3'
my_ver_mpfr='3.1.2'
my_ver_mpc='1.0.2'
my_ver_isl='0.12.2'
my_ver_cloog='0.18.1'
my_ver_gcc='4.8.3'
my_ver_gdb='7.8.1'

# for canadian cross
my_ver_expat='2.1.0'

build_dir='gcc48-host_mingw-w64-i686'


import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import crosstool_py
import crosstool_py.buildfunc
import crosstool_py.buildmodules

class Builder(crosstool_py.buildmodules.BuildModules):
  def build_sysroot(self):
    """
#Tegra_Linux_Sample-Root-Filesystem_R21.1.0_armhf.tbz2
    """
    super(Builder, self).build_sysroot()

    return 0


  def build(self):
    extra_configure_args=[]
    retval=self.build_binutils( my_ver_binutils, extra_configure_args )
    if 0 != retval:
      raise Exception('build_binutils error')

    extra_configure_args=[]
    retval=self.build_gmp( my_ver_gmp, extra_configure_args )
    if 0 != retval:
      raise Exception('build_gmp error')

    extra_configure_args=[]
    retval=self.build_mpfr( my_ver_mpfr, extra_configure_args )
    if 0 != retval:
      raise Exception('build_mpfr error')

    extra_configure_args=[]
    retval=self.build_mpc( my_ver_mpc, extra_configure_args )
    if 0 != retval:
      raise Exception('build_mpc error')

    extra_configure_args=[]
    retval=self.build_isl( my_ver_isl, extra_configure_args )
    if 0 != retval:
      raise Exception('build_isl error')

    extra_configure_args=[]
    retval=self.build_cloog( my_ver_cloog, extra_configure_args )
    if 0 != retval:
      raise Exception('build_cloog error')


    retval=self.build_sysroot()
    if 0 != retval:
      raise Exception('build_sysroot error')


    extra_configure_args=[]
    extra_configure_args.extend( ['--with-arch=armv7-a', '--with-fpu=vfpv3-d16', '--with-float=hard', '--with-mode=thumb'] )

    retval=self.build_gcc_stage1( my_ver_gcc, extra_configure_args )
    if 0 != retval:
      raise Exception('build_gcc_stage1 error')

    extra_configure_args=[]
    extra_configure_args.extend( ['--with-arch=armv7-a', '--with-fpu=vfpv3-d16', '--with-float=hard', '--with-mode=thumb'] )
    retval=self.build_gcc_stage2( my_ver_gcc, extra_configure_args )
    if 0 != retval:
      raise Exception('build_gcc_stage2 error')

    extra_configure_args=[]
    retval=self.build_gdb( my_ver_gdb, extra_configure_args )
    if 0 != retval:
      raise Exception('build_gdb error')

    extra_configure_args=[]
    retval=self.build_gdbserver( my_ver_gdb, extra_configure_args )
    if 0 != retval:
      raise Exception('build_gdbserver error')
    
    
    extra_configure_args=[]
    retval=self.build_gcczlib_host( my_ver_gcc, extra_configure_args )
    if 0 != retval:
      raise Exception('build_zlib_host error' )
    
    extra_configure_args=[]
    retval=self.build_expat_host( my_ver_expat, extra_configure_args )
    if 0 != retval:
      raise Exception('build_expat_host error' ) 
    
    extra_configure_args=[]
    retval=self.build_binutils_host( my_ver_binutils, extra_configure_args )
    if 0 != retval:
      raise Exception('build_binutils_host error')
    
    extra_configure_args=[]
    retval=self.build_gmp_host( my_ver_gmp, extra_configure_args )
    if 0 != retval:
      raise Exception('build_gmp_host error' )

    extra_configure_args=[]
    retval=self.build_mpfr_host( my_ver_mpfr, extra_configure_args )
    if 0 != retval:
      raise Exception('build_mpfr_host error' )

    extra_configure_args=[]
    retval=self.build_mpc_host( my_ver_mpc, extra_configure_args )
    if 0 != retval:
      raise Exception('build_mpc_host error' )
    
    extra_configure_args=[]
    retval=self.build_isl_host( my_ver_isl, extra_configure_args )
    if 0 != retval:
      raise Exception('build_isl_host error')
    
    extra_configure_args=[]
    retval=self.build_cloog_host( my_ver_cloog, extra_configure_args )
    if 0 != retval:
      raise Exception('build_cloog_host error')
    
    extra_configure_args=[]
    #extra_configure_args.append( '--enable-multiarch' )
    extra_configure_args.append( '--disable-multiarch' )
    extra_configure_args.append( '--with-float=hard' )
    extra_configure_args.extend( ['--with-arch=armv7-a', '--with-fpu=vfpv3-d16'] )
    extra_configure_args.append( '--with-mode=arm' )
    # extra_configure_args.append( '--with-mode=thumb' )
    retval=self.build_gcc_stage1_host( my_ver_gcc, extra_configure_args )
    if 0 != retval:
      raise Exception('build_gcc_stage1_host error' )
    
    retval=self.build_gcc_stage2_host( my_ver_gcc, extra_configure_args )
    if 0 != retval:
      raise Exception('build_gcc_stage2_host error')
    
    extra_configure_args=[]
    retval=self.build_gdb_host( my_ver_gdb, extra_configure_args )
    if 0 != retval:
      raise Exception('build_gdb_host error')



def main():
  parser = OptionParser()
  parser.add_option('-j', '--jobs', dest="jobs", type='int' )

  (options, args) = parser.parse_args()
  if None != options.jobs:
    if 0 < int(options.jobs):
      crosstool_py.buildfunc.make_opt_parallel='-j%d' % options.jobs

  global PREFIX, SRCROOT, TARGETROOT
  PREFIX=os.path.expandvars(os.path.expanduser(PREFIX))
  SRCROOT=os.path.expandvars(os.path.expanduser(SRCROOT))
  TARGETROOT=os.path.expandvars(os.path.expanduser(TARGETROOT))
  #crosstool_py.buildfunc.shell_cmd(PREFIX,['ls'], True, ['-l'] )
  #crosstool_py.buildfunc.shell_cmd(PREFIX,['env'], True )

  if not os.path.exists(build_dir):
    os.mkdir(build_dir)

  retval=0
  cur_dir=os.getcwd()
  os.chdir(build_dir)
  try:
    builder=Builder(PREFIX,TARGET,SRCROOT,TARGETROOT, 'i686-w64-mingw32' )
    retval=builder.build()
  except Exception as e:
    crosstool_py.buildfunc.log(str(e))
    raise
  os.chdir(cur_dir)

  return 0


if __name__ == '__main__':
  main()
