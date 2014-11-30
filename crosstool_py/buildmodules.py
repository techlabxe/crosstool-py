#!/usr/bin/env python

import os
import shutil
import glob

from . import buildfunc

class BuildModules(object):
  def __init__(self,prefix,target,srcroot,targetroot,host=None):
    self.PREFIX=prefix
    self.TARGET=target
    self.SRCROOT=srcroot
    self.TARGETROOT=targetroot
    self.HOST=host

    configure_args=[]
    configure_args.append( '--prefix=%s' % self.PREFIX )
    configure_args.append( '--target=%s' % self.TARGET )
    configure_args.append( '--with-sysroot' )
    configure_args.append( '--enable-gold' )
    self.configure_args_binutils=configure_args

    configure_args=[]
    configure_args.append( '--prefix=%s/tmp-rootbuild' % self.PREFIX )
    configure_args.append( '--disable-shared' )
    configure_args.append( '--disable-fast-install' )
    self.configure_args_gmp=configure_args

    configure_args=[]
    configure_args.append( '--prefix=%s/tmp-rootbuild' % self.PREFIX )
    configure_args.append( '--disable-shared' )
    configure_args.append( '--disable-fast-install' )
    configure_args.append( '--with-gmp=%s/tmp-rootbuild' % self.PREFIX )
    self.configure_args_mpfr=configure_args

    configure_args=[]
    configure_args.append( '--prefix=%s/tmp-rootbuild' % self.PREFIX )
    configure_args.append( '--disable-shared' )
    configure_args.append( '--disable-fast-install' )
    configure_args.append( '--with-gmp=%s/tmp-rootbuild' % self.PREFIX )
    configure_args.append( '--with-mpfr=%s/tmp-rootbuild' % self.PREFIX )
    self.configure_args_mpc=configure_args

    configure_args=[]
    configure_args.append( '--prefix=%s/tmp-rootbuild' % self.PREFIX )
    configure_args.append( '--disable-shared' )
    configure_args.append( '--disable-fast-install' )
    configure_args.append( '--with-gmp-prefix=%s/tmp-rootbuild' % self.PREFIX )
    self.configure_args_isl=configure_args

    configure_args=[]
    configure_args.append( '--prefix=%s/tmp-rootbuild' % self.PREFIX )
    configure_args.append( '--disable-shared' )
    configure_args.append( '--disable-fast-install' )
    configure_args.append( '--with-gmp-prefix=%s/tmp-rootbuild' % self.PREFIX )
    configure_args.append( '--with-isl-prefix=%s/tmp-rootbuild' % self.PREFIX )
    self.configure_args_cloog=configure_args

    configure_args=[]
    configure_args.append( '-v' )
    configure_args.append( '--prefix=%s' % self.PREFIX )
    configure_args.append( '--target=%s' % self.TARGET )
    configure_args.append( '--with-gmp=%s/tmp-rootbuild' % self.PREFIX )
    configure_args.append( '--with-mpfr=%s/tmp-rootbuild' % self.PREFIX )
    configure_args.append( '--with-mpc=%s/tmp-rootbuild' % self.PREFIX )
    configure_args.append( '--with-isl=%s/tmp-rootbuild' % self.PREFIX )
    configure_args.append( '--with-cloog=%s/tmp-rootbuild' % self.PREFIX )
    configure_args.append( '--enable-languages=c' )
    configure_args.append( '--without-headers' )
    configure_args.append( '--with-sysroot=%s/sys-root' % self.PREFIX )
    self.configure_args_gcc_stage1=configure_args

    configure_args=[]
    configure_args.append( '-v' )
    configure_args.append( '--prefix=%s' % self.PREFIX )
    configure_args.append( '--target=%s' % self.TARGET )
    configure_args.append( '--with-gmp=%s/tmp-rootbuild' % self.PREFIX )
    configure_args.append( '--with-mpfr=%s/tmp-rootbuild' % self.PREFIX )
    configure_args.append( '--with-mpc=%s/tmp-rootbuild' % self.PREFIX )
    configure_args.append( '--with-isl=%s/tmp-rootbuild' % self.PREFIX )
    configure_args.append( '--with-cloog=%s/tmp-rootbuild' % self.PREFIX )
    configure_args.append( '--enable-languages=c,c++' )
    configure_args.append( '--without-headers' )
    configure_args.append( '--with-sysroot=%s/sys-root' % self.PREFIX )
    self.configure_args_gcc_stage2=configure_args

    configure_args=[]
    configure_args.append( '-v' )
    configure_args.append( '--prefix=%s' % self.PREFIX )
    configure_args.append( '--target=%s' % self.TARGET )
    configure_args.append( '--disable-sim' )
    self.configure_args_gdb=configure_args

    configure_args=[]
    configure_args.append( '-v' )
    configure_args.append( '--prefix=%s' % self.PREFIX )
    configure_args.append( '--target=%s' % self.TARGET )
    configure_args.append( '--host=%s' % self.TARGET )
    self.configure_args_gdbserver=configure_args




    configure_args=[]
    configure_args.append( '--prefix=%s/tmp-roothost' % self.PREFIX )
    if None != host:
      configure_args.append( '--host=%s' % self.HOST )
    configure_args.append( '--target=%s' % self.HOST )
    #configure_args.append( '--with-cross-host=%s' % self.HOST )
    configure_args.append( '--disable-shared' )
    self.configure_args_gcczlib_host=configure_args

    configure_args=[]
    configure_args.append( '--prefix=%s/tmp-roothost' % self.PREFIX )
    if None != host:
      configure_args.append( '--host=%s' % self.HOST )
    configure_args.append( '--target=%s' % self.HOST )
    configure_args.append( '--disable-shared' )
    configure_args.append( '--disable-fast-install' )
    self.configure_args_expat_host=configure_args


    configure_args=[]
    configure_args.append( '-v' )
    configure_args.append( '--prefix=%s' % self.PREFIX )
    if None != host:
      configure_args.append( '--host=%s' % self.HOST )
    configure_args.append( '--target=%s' % self.TARGET )
    configure_args.append( '--with-sysroot' )
    configure_args.append( '--enable-gold' )
    configure_args.append( '--with-zlib=yes' )
    self.configure_args_binutils_host=configure_args

    configure_args=[]
    configure_args.append( '--prefix=%s/tmp-roothost' % self.PREFIX )
    if None != host:
      configure_args.append( '--host=%s' % self.HOST )
    configure_args.append( '--disable-shared' )
    configure_args.append( '--disable-fast-install' )
    self.configure_args_gmp_host=configure_args

    configure_args=[]
    configure_args.append( '--prefix=%s/tmp-roothost' % self.PREFIX )
    if None != host:
      configure_args.append( '--host=%s' % self.HOST )
    configure_args.append( '--disable-shared' )
    configure_args.append( '--disable-fast-install' )
    configure_args.append( '--with-gmp=%s/tmp-roothost' % self.PREFIX )
    self.configure_args_mpfr_host=configure_args

    configure_args=[]
    configure_args.append( '--prefix=%s/tmp-roothost' % self.PREFIX )
    if None != host:
      configure_args.append( '--host=%s' % self.HOST )
    configure_args.append( '--disable-shared' )
    configure_args.append( '--disable-fast-install' )
    configure_args.append( '--with-gmp=%s/tmp-roothost' % self.PREFIX )
    configure_args.append( '--with-mpfr=%s/tmp-roothost' % self.PREFIX )
    self.configure_args_mpc_host=configure_args

    configure_args=[]
    configure_args.append( '--prefix=%s/tmp-roothost' % self.PREFIX )
    if None != host:
      configure_args.append( '--host=%s' % self.HOST )
    configure_args.append( '--disable-shared' )
    configure_args.append( '--disable-fast-install' )
    configure_args.append( '--with-gmp-prefix=%s/tmp-roothost' % self.PREFIX )
    self.configure_args_isl_host=configure_args

    configure_args=[]
    configure_args.append( '--prefix=%s/tmp-roothost' % self.PREFIX )
    if None != host:
      configure_args.append( '--host=%s' % self.HOST )
    configure_args.append( '--disable-shared' )
    configure_args.append( '--disable-fast-install' )
    configure_args.append( '--with-gmp-prefix=%s/tmp-roothost' % self.PREFIX )
    configure_args.append( '--with-isl-prefix=%s/tmp-roothost' % self.PREFIX )
    self.configure_args_cloog_host=configure_args

    configure_args=[]
    configure_args.append( '-v' )
    configure_args.append( '--prefix=%s' % self.PREFIX )
    if None != host:
      configure_args.append( '--host=%s' % self.HOST )
    configure_args.append( '--target=%s' % self.TARGET )
    configure_args.append( '--with-gmp=%s/tmp-roothost' % self.PREFIX )
    configure_args.append( '--with-mpfr=%s/tmp-roothost' % self.PREFIX )
    configure_args.append( '--with-mpc=%s/tmp-roothost' % self.PREFIX )
    configure_args.append( '--with-isl=%s/tmp-roothost' % self.PREFIX )
    configure_args.append( '--with-cloog=%s/tmp-roothost' % self.PREFIX )
    configure_args.append( '--enable-languages=c' )
    configure_args.append( '--without-headers' )
    configure_args.append( '--with-sysroot=%s/sys-root' % self.PREFIX )
    configure_args.append( '--with-zlib=%s/tmp-roothost' % self.PREFIX )
    self.configure_args_gcc_stage1_host=configure_args

    configure_args=[]
    configure_args.append( '-v' )
    configure_args.append( '--prefix=%s' % self.PREFIX )
    if None != host:
      configure_args.append( '--host=%s' % self.HOST )
    configure_args.append( '--target=%s' % self.TARGET )
    configure_args.append( '--with-gmp=%s/tmp-roothost' % self.PREFIX )
    configure_args.append( '--with-mpfr=%s/tmp-roothost' % self.PREFIX )
    configure_args.append( '--with-mpc=%s/tmp-roothost' % self.PREFIX )
    configure_args.append( '--with-isl=%s/tmp-roothost' % self.PREFIX )
    configure_args.append( '--with-cloog=%s/tmp-roothost' % self.PREFIX )
    configure_args.append( '--enable-languages=c,c++' )
    configure_args.append( '--without-headers' )
    configure_args.append( '--with-sysroot=%s/sys-root' % self.PREFIX )
    configure_args.append( '--with-zlib=%s/tmp-roothost' % self.PREFIX )
    self.configure_args_gcc_stage2_host=configure_args

    configure_args=[]
    configure_args.append( '-v' )
    configure_args.append( '--prefix=%s' % self.PREFIX )
    if None != host:
      configure_args.append( '--host=%s' % self.HOST )
    configure_args.append( '--target=%s' % self.TARGET )
    configure_args.append( '--disable-sim' )
    configure_args.append( '--with-zlib=%s/tmp-roothost' % self.PREFIX )
    configure_args.append( '--with-expat=%s/tmp-roothost' % self.PREFIX )
    self.configure_args_gdb_host=configure_args





  def build_binutils(self,ver_binutils, extra_configure_args=[]):
    configure_args=self.configure_args_binutils
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'binutils', 'build-binutils', ver_binutils, configure_args )

    return retval

  def build_gmp(self,ver_gmp, extra_configure_args=[]):
    configure_args=self.configure_args_gmp
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'gmp', 'build-gmp', ver_gmp, configure_args )

    return retval

  def build_mpfr(self,ver_mpfr, extra_configure_args=[]):
    configure_args=self.configure_args_mpfr
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'mpfr', 'build-mpfr', ver_mpfr, configure_args )

    return retval

  def build_mpc(self,ver_mpc, extra_configure_args=[]):
    configure_args=self.configure_args_mpc
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'mpc', 'build-mpc', ver_mpc, configure_args )

    return retval

  def build_isl(self,ver_isl, extra_configure_args=[]):
    configure_args=self.configure_args_isl
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'isl', 'build-isl', ver_isl, configure_args )

    return retval

  def build_cloog(self,ver_cloog, extra_configure_args=[]):
    configure_args=self.configure_args_cloog
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'cloog', 'build-cloog', ver_cloog, configure_args )

    return retval

  def build_gcc_stage1(self,ver_gcc, extra_configure_args=[]):
    configure_args=self.configure_args_gcc_stage1
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module(
      self.PREFIX, self.SRCROOT, 'gcc', 'build-gcc-stage1', ver_gcc, configure_args, ''
      , ['all-gcc','all-target-libgcc']
      , ['install-gcc','install-target-libgcc']
      )

    return retval

  def build_gcc_stage2(self,ver_gcc, extra_configure_args=[]):
    configure_args=self.configure_args_gcc_stage2
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'gcc', 'build-gcc-stage2', ver_gcc, configure_args )

    return retval

  def build_gdb(self,ver_gdb, extra_configure_args=[]):
    configure_args=self.configure_args_gdb
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'gdb', 'build-gdb', ver_gdb, configure_args )

    return retval

  def build_gdbserver(self,ver_gdb, extra_configure_args=[]):
    configure_args=self.configure_args_gdbserver
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'gdb', 'target-gdbserver', ver_gdb, configure_args, 'gdb/gdbserver/' )

    return retval






  def build_zlib_host(self,ver_zlib, extra_configure_args=[]):
    if None == self.HOST:
      return 0
    configure_args=self.configure_args_zlib_host
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'zlib', 'host-zlib', ver_zlib, configure_args )

    return retval

  def build_gcczlib_host(self,ver_gcc, extra_configure_args=[]):
    if None == self.HOST:
      return 0
    configure_args=self.configure_args_gcczlib_host
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'gcc', 'host-zlib', ver_gcc, configure_args, 'zlib/' )

    buildfunc.log('retval=%d' % retval)
    if 0 == retval:
      includedir='%s/tmp-roothost/include' % self.PREFIX
      if not os.path.exists(includedir):
        os.mkdir(includedir)
      shutil.copy( '%s/gcc-%s/zlib/zconf.h' % (self.SRCROOT,ver_gcc), '%s/tmp-roothost/include/' % self.PREFIX )
      shutil.copy( '%s/gcc-%s/zlib/zlib.h' % (self.SRCROOT,ver_gcc), '%s/tmp-roothost/include/' % self.PREFIX )

    return retval

  def build_expat_host(self,ver_expat, extra_configure_args=[]):
    if None == self.HOST:
      return 0
    configure_args=self.configure_args_expat_host
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'expat', 'host-expat', ver_expat, configure_args )

    return retval


  def build_binutils_host(self,ver_binutils, extra_configure_args=[]):
    if None == self.HOST:
      return 0
    configure_args=self.configure_args_binutils_host
    configure_args.extend( extra_configure_args )


    save_env=os.environ.copy()

    if not 'CPPFLAGS' in os.environ:
      os.environ['CPPFLAGS']=''
    else:
      os.environ['CPPFLAGS']+=' '
    os.environ['CPPFLAGS']+='-I%s/tmp-roothost/include' % self.PREFIX

    if not 'LDFLAGS' in os.environ:
      os.environ['LDFLAGS']=''
    else:
      os.environ['LDFLAGS']+=' '
    os.environ['LDFLAGS']+='-L%s/tmp-roothost/lib' % self.PREFIX

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'binutils', 'host-binutils', ver_binutils, configure_args )

    os.environ=save_env


    return retval

  def build_gmp_host(self,ver_gmp, extra_configure_args=[]):
    if None == self.HOST:
      return 0
    configure_args=self.configure_args_gmp_host
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'gmp', 'host-gmp', ver_gmp, configure_args )

    return retval

  def build_mpfr_host(self,ver_mpfr, extra_configure_args=[]):
    if None == self.HOST:
      return 0
    configure_args=self.configure_args_mpfr_host
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'mpfr', 'host-mpfr', ver_mpfr, configure_args )

    return retval

  def build_mpc_host(self,ver_mpc, extra_configure_args=[]):
    if None == self.HOST:
      return 0
    configure_args=self.configure_args_mpc_host
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'mpc', 'host-mpc', ver_mpc, configure_args )

    return retval

  def build_isl_host(self,ver_isl, extra_configure_args=[]):
    if None == self.HOST:
      return 0
    configure_args=self.configure_args_isl_host
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'isl', 'host-isl', ver_isl, configure_args )

    return retval

  def build_cloog_host(self,ver_cloog, extra_configure_args=[]):
    if None == self.HOST:
      return 0
    configure_args=self.configure_args_cloog_host
    configure_args.extend( extra_configure_args )

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'cloog', 'host-cloog', ver_cloog, configure_args )

    return retval

  def build_gcc_stage1_host(self,ver_gcc, extra_configure_args=[]):
    if None == self.HOST:
      return 0
    configure_args=self.configure_args_gcc_stage1_host
    configure_args.extend( extra_configure_args )

    save_env=os.environ.copy()

    if not 'CPPFLAGS' in os.environ:
      os.environ['CPPFLAGS']=''
    else:
      os.environ['CPPFLAGS']+=' '
    os.environ['CPPFLAGS']+='-I%s/tmp-roothost/include' % self.PREFIX

    if not 'LDFLAGS' in os.environ:
      os.environ['LDFLAGS']=''
    else:
      os.environ['LDFLAGS']+=' '
    os.environ['LDFLAGS']+='-L%s/tmp-roothost/lib' % self.PREFIX

    retval=buildfunc.build_module(
      self.PREFIX, self.SRCROOT, 'gcc', 'host-gcc-stage1', ver_gcc, configure_args, ''
      #, ['all-gcc','all-target-libgcc']
      #, ['install-gcc','install-target-libgcc']
      , ['all-gcc']
      , ['install-gcc']
      )

    os.environ=save_env

    return retval

  def build_gcc_stage2_host(self,ver_gcc, extra_configure_args=[]):
    if None == self.HOST:
      return 0
    configure_args=self.configure_args_gcc_stage2_host
    configure_args.extend( extra_configure_args )

    save_env=os.environ.copy()

    if not 'CPPFLAGS' in os.environ:
      os.environ['CPPFLAGS']=''
    else:
      os.environ['CPPFLAGS']+=' '
    os.environ['CPPFLAGS']+='-I%s/tmp-roothost/include' % self.PREFIX

    if not 'LDFLAGS' in os.environ:
      os.environ['LDFLAGS']=''
    else:
      os.environ['LDFLAGS']+=' '
    os.environ['LDFLAGS']+='-L%s/tmp-roothost/lib' % self.PREFIX

    #retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'gcc', 'host-gcc-stage2', ver_gcc, configure_args )
    retval=buildfunc.build_module(
      self.PREFIX, self.SRCROOT, 'gcc', 'host-gcc-stage2', ver_gcc, configure_args, ''
      #, ['all-gcc','all-target-libgcc']
      #, ['install-gcc','install-target-libgcc']
      , ['all-gcc']
      , ['install-gcc']
      )

    os.environ=save_env

    return retval

  def build_gdb_host(self,ver_gdb, extra_configure_args=[]):
    if None == self.HOST:
      return 0
    configure_args=self.configure_args_gdb_host
    configure_args.extend( extra_configure_args )

    save_env=os.environ.copy()

    if not 'CPPFLAGS' in os.environ:
      os.environ['CPPFLAGS']=''
    else:
      os.environ['CPPFLAGS']+=' '
    os.environ['CPPFLAGS']+='-I%s/tmp-roothost/include' % self.PREFIX

    if not 'LDFLAGS' in os.environ:
      os.environ['LDFLAGS']=''
    else:
      os.environ['LDFLAGS']+=' '
    os.environ['LDFLAGS']+='-L%s/tmp-roothost/lib' % self.PREFIX

    retval=buildfunc.build_module( self.PREFIX, self.SRCROOT, 'gdb', 'host-gdb', ver_gdb, configure_args )

    os.environ=save_env

    return retval






  def build_sysroot(self):

    build_dirname='sysroot'
    if not os.path.exists(build_dirname):
      os.mkdir(build_dirname)

    targetarch=self.TARGET

    cur_dir=os.getcwd()
    os.chdir(build_dirname)
    if os.path.exists('_success_build.txt'):
      os.chdir(cur_dir)
      return 0

    if os.path.exists( self.PREFIX + '/sys-root' ):
      shutil.rmtree( self.PREFIX + '/sys-root')
    shutil.copytree( self.TARGETROOT + '/lib', self.PREFIX + '/sys-root/lib', symlinks=True )
    if os.path.exists( self.PREFIX + '/sys-root/usr' ):
      shutil.rmtree( self.PREFIX + '/sys-root/usr' )
    shutil.copytree( self.TARGETROOT + '/usr/include', self.PREFIX + '/sys-root/usr/include', symlinks=True )
    shutil.copytree( self.TARGETROOT + '/usr/lib', self.PREFIX + '/sys-root/usr/lib', symlinks=True )

    for dir in ['asm', 'bits', 'gnu', 'sys' ]:
      if not os.path.exists( self.PREFIX + '/sys-root/usr/include/' + dir ):
        os.symlink( targetarch + '/' + dir, self.PREFIX + '/sys-root/usr/include/' + dir )

    for so in glob.glob( self.PREFIX + '/sys-root/usr/lib/' + targetarch + '/*.so' ):
      if not os.path.islink(so):
        continue

      if not os.path.exists(so):
        old_symlink=os.readlink(so)
        #print '%s => %s' % (old_symlinlk)
        destso=os.path.basename(os.readlink(so))
        #print 'basename=%s' % (os.path.basename(so))
        #print 'destso=%s' % (destso)
        relpath=os.path.relpath(os.path.dirname( self.PREFIX + '/sys-root' + os.readlink(so)), os.path.dirname(so))
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

    if os.path.exists( self.PREFIX + '/sys-root/usr/lib/gcc' ):
      shutil.rmtree( self.PREFIX + '/sys-root/usr/lib/gcc' )

    buildfunc.touch('_success_build.txt')
    os.chdir(cur_dir)

    return 0



if __name__ == '__main__':
  main()

