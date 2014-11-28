#!/usr/bin/env python

import shutil
from optparse import OptionParser

PREFIX='~/gcc48mipsci20'
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


build_dir='gcc48'


import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from crosstool_py import buildfunc

def build_binutils():
  configure_args=[]
  configure_args.append( '--prefix=%s' % PREFIX )
  configure_args.append( '--target=%s' % TARGET )
  configure_args.append( '--with-sysroot' )
  configure_args.append( '--enable-gold' )

  retval=buildfunc.build_module( PREFIX, SRCROOT, 'binutils', 'binutils', my_ver_binutils, configure_args )

  return retval

def build_gmp():
  configure_args=[]
  configure_args.append( '--prefix=%s' % PREFIX )
  configure_args.append( '--disable-shared' )
  configure_args.append( '--disable-fast-install' )

  retval=buildfunc.build_module( PREFIX, SRCROOT, 'gmp', 'gmp', my_ver_gmp, configure_args )

  return retval

def build_mpfr():
  configure_args=[]
  configure_args.append( '--prefix=%s' % PREFIX )
  configure_args.append( '--disable-shared' )
  configure_args.append( '--disable-fast-install' )
  configure_args.append( '--with-gmp=%s' % PREFIX )

  retval=buildfunc.build_module( PREFIX, SRCROOT, 'mpfr', 'mpfr', my_ver_mpfr, configure_args )

  return retval

def build_mpc():
  configure_args=[]
  configure_args.append( '--prefix=%s' % PREFIX )
  configure_args.append( '--disable-shared' )
  configure_args.append( '--disable-fast-install' )
  configure_args.append( '--with-gmp=%s' % PREFIX )
  configure_args.append( '--with-mpfr=%s' % PREFIX )

  retval=buildfunc.build_module( PREFIX, SRCROOT, 'mpc', 'mpc', my_ver_mpc, configure_args )

  return retval

def build_isl():
  configure_args=[]
  configure_args.append( '--prefix=%s' % PREFIX )
  configure_args.append( '--disable-shared' )
  configure_args.append( '--disable-fast-install' )
  configure_args.append( '--with-gmp-prefix=%s' % PREFIX )

  retval=buildfunc.build_module( PREFIX, SRCROOT, 'isl', 'isl', my_ver_isl, configure_args )

  return retval

def build_cloog():
  configure_args=[]
  configure_args.append( '--prefix=%s' % PREFIX )
  configure_args.append( '--disable-shared' )
  configure_args.append( '--disable-fast-install' )
  configure_args.append( '--with-gmp-prefix=%s' % PREFIX )
  configure_args.append( '--with-isl-prefix=%s' % PREFIX )

  retval=buildfunc.build_module( PREFIX, SRCROOT, 'cloog', 'cloog', my_ver_cloog, configure_args )

  return retval

def build_gcc_stage1():
  configure_args=[]
  configure_args.append( '-v' )
  configure_args.append( '--prefix=%s' % PREFIX )
  configure_args.append( '--target=%s' % TARGET )
  configure_args.append( '--with-gmp=%s' % PREFIX )
  configure_args.append( '--with-mpfr=%s' % PREFIX )
  configure_args.append( '--with-mpc=%s' % PREFIX )
  configure_args.append( '--with-isl=%s' % PREFIX )
  configure_args.append( '--with-cloog=%s' % PREFIX )
  configure_args.append( '--enable-languages=c' )
  configure_args.append( '--without-headers' )
  configure_args.append( '--with-sysroot=%s/sys-root' % PREFIX )

  configure_args.append( '--enable-multiarch' )
  ##deb configure_args.append( '--with-multiarch-defaults=mipsel-linux-gnu' )
  #configure_args.append( '--with-float=soft' )
  configure_args.append( '--disable-multilib' )
  #configure_args.append( '--with-multilib-list=m32' )
  configure_args.extend( ['--with-mips-plt', '--with-arch-32=mips2', '--with-tune-32=mips32', '--enable-targets=all'] )
  #configure_args.extend( ['--with-mips-plt', '--with-arch-32=mips2', '--with-tune-32=mips32', '--enable-targets=all', '--with-arch-64=mips3', '--with-tune-64=mips64'] )

  retval=buildfunc.build_module(
    PREFIX, SRCROOT, 'gcc', 'gcc-stage1', my_ver_gcc, configure_args, ''
    , ['all-gcc','all-target-libgcc']
    , ['install-gcc','install-target-libgcc']
    )

  return retval


def build_gcc_stage2():
  configure_args=[]
  configure_args.append( '-v' )
  configure_args.append( '--prefix=%s' % PREFIX )
  configure_args.append( '--target=%s' % TARGET )
  configure_args.append( '--with-gmp=%s' % PREFIX )
  configure_args.append( '--with-mpfr=%s' % PREFIX )
  configure_args.append( '--with-mpc=%s' % PREFIX )
  configure_args.append( '--with-isl=%s' % PREFIX )
  configure_args.append( '--with-cloog=%s' % PREFIX )
  configure_args.append( '--enable-languages=c,c++' )
  configure_args.append( '--without-headers' )
  configure_args.append( '--with-sysroot=%s/sys-root' % PREFIX )

  configure_args.append( '--enable-multiarch' )
  ##deb configure_args.append( '--with-multiarch-defaults=mipsel-linux-gnu' )
  #configure_args.append( '--with-float=soft' )
  configure_args.append( '--disable-multilib' )
  #configure_args.append( '--with-multilib-list=m32' )
  configure_args.extend( ['--with-mips-plt', '--with-arch-32=mips2', '--with-tune-32=mips32', '--enable-targets=all'] )
  #configure_args.extend( ['--with-mips-plt', '--with-arch-32=mips2', '--with-tune-32=mips32', '--enable-targets=all', '--with-arch-64=mips3', '--with-tune-64=mips64'] )

  retval=buildfunc.build_module( PREFIX, SRCROOT, 'gcc', 'gcc-stage2', my_ver_gcc, configure_args )

  return retval

def build_gdb():
  configure_args=[]
  configure_args.append( '-v' )
  configure_args.append( '--prefix=%s' % PREFIX )
  configure_args.append( '--target=%s' % TARGET )
  configure_args.append( '--disable-sim' )

  retval=buildfunc.build_module( PREFIX, SRCROOT, 'gdb', 'gdb', my_ver_gdb, configure_args )

  return retval

def build_gdbserver():
  configure_args=[]
  configure_args.append( '-v' )
  configure_args.append( '--prefix=%s' % PREFIX )
  configure_args.append( '--target=%s' % TARGET )
  configure_args.append( '--host=%s' % TARGET )

  retval=buildfunc.build_module( PREFIX, SRCROOT, 'gdb', 'gdbserver', my_ver_gdb, configure_args, 'gdb/gdbserver/' )

  return retval





def build_sysroot():
  """
#http://mipscreator.imgtec.com/CI20/images/default_NAND/Debian7_20140611/rootfs-20140625.tar
  """

  import glob

  build_dirname='sysroot'
  if not os.path.exists(build_dirname):
    os.mkdir(build_dirname)

  cur_dir=os.getcwd()
  os.chdir(build_dirname)
  if os.path.exists('_success_build.txt'):
    os.chdir(cur_dir)
    return 0

  if os.path.exists( PREFIX + '/sys-root' ):
    shutil.rmtree( PREFIX + '/sys-root')
  shutil.copytree( TARGETROOT + '/lib', PREFIX + '/sys-root/lib', symlinks=True )
  if os.path.exists( PREFIX + '/sys-root/usr' ):
    shutil.rmtree( PREFIX + '/sys-root/usr' )
  shutil.copytree( TARGETROOT + '/usr/include', PREFIX + '/sys-root/usr/include', symlinks=True )
  shutil.copytree( TARGETROOT + '/usr/lib', PREFIX + '/sys-root/usr/lib', symlinks=True )

  for dir in ['asm', 'bits', 'gnu', 'sys' ]:
    if not os.path.exists( PREFIX + '/sys-root/usr/include/' + dir ):
      os.symlink( 'mipsel-linux-gnu/' + dir, PREFIX + '/sys-root/usr/include/' + dir )

  for so in glob.glob( PREFIX + '/sys-root/usr/lib/mipsel-linux-gnu/*.so' ):
    if not os.path.islink(so):
      continue

    if not os.path.exists(so):
      old_symlink=os.readlink(so)
      #print '%s => %s' % (old_symlinlk)
      destso=os.path.basename(os.readlink(so))
      #print 'basename=%s' % (os.path.basename(so))
      #print 'destso=%s' % (destso)
      relpath=os.path.relpath(os.path.dirname( PREFIX + '/sys-root' + os.readlink(so)), os.path.dirname(so))
      #print 'relpath=%s' % (relpath)
      destlink=relpath + '/' + destso
      print 'ln -s %s %s' % (destlink, so)
      try:
        os.unlink(so)
        os.symlink( destlink, so )
      except OSError:
        os.symlink( old_symlink, so )
    else:
      continue

  if os.path.exists( PREFIX + '/sys-root/usr/lib/gcc' ):
    shutil.rmtree( PREFIX + '/sys-root/usr/lib/gcc' )

#  ## workaround multiarch
#  workaround_multiarch=[]
#  workaround_multiarch.extend(['crt1.o','crti.o','crtn.o'])
#  workaround_multiarch.extend(['libc.so','libm.so'])
#  workaround_multiarch.extend(['libdl.so'])
#  workaround_multiarch.extend(['libpthread.so','libthread_db.so'])
#  for obj in workaround_multiarch:
#    os.symlink( 'mipsel-linux-gnu/' + obj, PREFIX + '/sys-root/usr/lib/' + obj )
#  os.symlink( 'mipsel-linux-gnu/' + 'libstdc++.so.6', PREFIX + '/sys-root/usr/lib/' + 'libstdc++.so' )

  buildfunc.touch('_success_build.txt')
  os.chdir(cur_dir)

  return 0



def main():
  parser = OptionParser()
  parser.add_option('-j', '--jobs', dest="jobs", type='int' )

  (options, args) = parser.parse_args()
  if None != options.jobs:
    if 0 < int(options.jobs):
      buildfunc.make_opt_parallel='-j%d' % options.jobs

  global PREFIX, SRCROOT, TARGETROOT
  PREFIX=os.path.expandvars(os.path.expanduser(PREFIX))
  SRCROOT=os.path.expandvars(os.path.expanduser(SRCROOT))
  TARGETROOT=os.path.expandvars(os.path.expanduser(TARGETROOT))
  #buildfunc.shell_cmd(PREFIX,['ls'], True, ['-l'] )
  #buildfunc.shell_cmd(PREFIX,['env'], True )

  if not os.path.exists(build_dir):
    os.mkdir(build_dir)

  retval=0
  cur_dir=os.getcwd()
  os.chdir(build_dir)
  try:
    retval=build_binutils()
    if 0 != retval:
      raise Exception('build_binutils error')

    retval=build_gmp()
    if 0 != retval:
      raise Exception('build_gmp error')
    retval=build_mpfr()
    if 0 != retval:
      raise Exception('build_mpfr error')
    retval=build_mpc()
    if 0 != retval:
      raise Exception('build_mpc error')
    retval=build_isl()
    if 0 != retval:
      raise Exception('build_isl error')
    retval=build_cloog()
    if 0 != retval:
      raise Exception('build_cloog error')
    retval=build_sysroot()
    if 0 != retval:
      raise Exception('build_sysroot error')
    retval=build_gcc_stage1()
    if 0 != retval:
      raise Exception('build_gcc_stage1 error')
    retval=build_gcc_stage2()
    if 0 != retval:
      raise Exception('build_gcc_stage2 error')
    retval=build_gdb()
    if 0 != retval:
      raise Exception('build_gdb error')
    retval=build_gdbserver()
    if 0 != retval:
      raise Exception('build_gdbserver error')
  except Exception as e:
    buildfunc.log(str(e))
    raise
  os.chdir(cur_dir)

  return 0


if __name__ == '__main__':
  main()
