#!/usr/bin/env python

import shutil
from optparse import OptionParser

PREFIX='~/gcc48mipsci20-mingw-w64-x86_64'
TARGET='mipsel-linux-gnu'
SRCROOT='~/work/src_root'
TARGETROOT='~/work/target_root/MIPSCreatorCI20'

my_ver_binutils='2.24'
my_ver_gmp='5.1.3'
my_ver_mpfr='3.1.2'
my_ver_mpc='1.0.2'
my_ver_isl='0.12.2'
my_ver_cloog='0.18.1'
my_ver_gcc='4.8.3'
my_ver_gdb='7.8.1'

# canadian cross
my_ver_expat='2.1.0'

build_dir='gcc48-host_mingw-w64-x86_64'


import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import crosstool_py
import crosstool_py.buildfunc
import crosstool_py.buildmodules

class Builder(crosstool_py.buildmodules.BuildModules):
  def build_sysroot(self):
    """
#http://mipscreator.imgtec.com/CI20/images/default_NAND/Debian7_20140611/rootfs-20140625.tar
    """
    super(Builder, self).build_sysroot()

#    ## workaround multiarch
#    workaround_multiarch=[]
#    workaround_multiarch.extend(['crt1.o','crti.o','crtn.o'])
#    workaround_multiarch.extend(['libc.so','libm.so'])
#    workaround_multiarch.extend(['libdl.so'])
#    workaround_multiarch.extend(['libpthread.so','libthread_db.so'])
#    for obj in workaround_multiarch:
#      os.symlink( 'mipsel-linux-gnu/' + obj, PREFIX + '/sys-root/usr/lib/' + obj )
#    os.symlink( 'mipsel-linux-gnu/' + 'libstdc++.so.6', PREFIX + '/sys-root/usr/lib/' + 'libstdc++.so' )

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
    extra_configure_args.append( '--enable-multiarch' )
    ##deb extra_configure_args.append( '--with-multiarch-defaults=mipsel-linux-gnu' )
    #extra_configure_args.append( '--with-float=soft' )
    extra_configure_args.append( '--disable-multilib' )
    #extra_configure_args.append( '--with-multilib-list=m32' )
    extra_configure_args.extend( ['--with-mips-plt', '--with-arch-32=mips2', '--with-tune-32=mips32', '--enable-targets=all'] )
    #extra_configure_args.extend( ['--with-mips-plt', '--with-arch-32=mips2', '--with-tune-32=mips32', '--enable-targets=all', '--with-arch-64=mips3', '--with-tune-64=mips64'] )

    retval=self.build_gcc_stage1( my_ver_gcc, extra_configure_args )
    if 0 != retval:
      raise Exception('build_gcc_stage1 error')

    extra_configure_args=[]
    extra_configure_args.append( '--enable-multiarch' )
    ##deb extra_configure_args.append( '--with-multiarch-defaults=mipsel-linux-gnu' )
    #extra_configure_args.append( '--with-float=soft' )
    extra_configure_args.append( '--disable-multilib' )
    #extra_configure_args.append( '--with-multilib-list=m32' )
    extra_configure_args.extend( ['--with-mips-plt', '--with-arch-32=mips2', '--with-tune-32=mips32', '--enable-targets=all'] )
    #extra_configure_args.extend( ['--with-mips-plt', '--with-arch-32=mips2', '--with-tune-32=mips32', '--enable-targets=all', '--with-arch-64=mips3', '--with-tune-64=mips64'] )
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
      raise Exception('build_zlib_host error')

    extra_configure_args=[]
    retval=self.build_expat_host( my_ver_expat, extra_configure_args )
    if 0 != retval:
      raise Exception('build_expat_host error')


    extra_configure_args=[]
    retval=self.build_binutils_host( my_ver_binutils, extra_configure_args )
    if 0 != retval:
      raise Exception('build_binutils_host error')

    extra_configure_args=[]
    retval=self.build_gmp_host( my_ver_gmp, extra_configure_args )
    if 0 != retval:
      raise Exception('build_gmp_host error')

    extra_configure_args=[]
    retval=self.build_mpfr_host( my_ver_mpfr, extra_configure_args )
    if 0 != retval:
      raise Exception('build_mpfr_host error')

    extra_configure_args=[]
    retval=self.build_mpc_host( my_ver_mpc, extra_configure_args )
    if 0 != retval:
      raise Exception('build_mpc_host error')

    extra_configure_args=[]
    retval=self.build_isl_host( my_ver_isl, extra_configure_args )
    if 0 != retval:
      raise Exception('build_isl_host error')

    extra_configure_args=[]
    retval=self.build_cloog_host( my_ver_cloog, extra_configure_args )
    if 0 != retval:
      raise Exception('build_cloog_host error')

    extra_configure_args=[]
    extra_configure_args.append( '--enable-multiarch' )
    ##deb extra_configure_args.append( '--with-multiarch-defaults=mipsel-linux-gnu' )
    #extra_configure_args.append( '--with-float=soft' )
    extra_configure_args.append( '--disable-multilib' )
    #extra_configure_args.append( '--with-multilib-list=m32' )
    extra_configure_args.extend( ['--with-mips-plt', '--with-arch-32=mips2', '--with-tune-32=mips32', '--enable-targets=all'] )
    #extra_configure_args.extend( ['--with-mips-plt', '--with-arch-32=mips2', '--with-tune-32=mips32', '--enable-targets=all', '--with-arch-64=mips3', '--with-tune-64=mips64'] )
    retval=self.build_gcc_stage1_host( my_ver_gcc, extra_configure_args )
    if 0 != retval:
      raise Exception('build_gcc_stage1_host error')

    extra_configure_args=[]
    extra_configure_args.append( '--enable-multiarch' )
    ##deb extra_configure_args.append( '--with-multiarch-defaults=mipsel-linux-gnu' )
    #extra_configure_args.append( '--with-float=soft' )
    extra_configure_args.append( '--disable-multilib' )
    #extra_configure_args.append( '--with-multilib-list=m32' )
    extra_configure_args.extend( ['--with-mips-plt', '--with-arch-32=mips2', '--with-tune-32=mips32', '--enable-targets=all'] )
    #extra_configure_args.extend( ['--with-mips-plt', '--with-arch-32=mips2', '--with-tune-32=mips32', '--enable-targets=all', '--with-arch-64=mips3', '--with-tune-64=mips64'] )
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
    builder=Builder(PREFIX,TARGET,SRCROOT,TARGETROOT,'x86_64-w64-mingw32')
    retval=builder.build()
  except Exception as e:
    crosstool_py.buildfunc.log(str(e))
    raise
  os.chdir(cur_dir)

  return 0


if __name__ == '__main__':
  main()
