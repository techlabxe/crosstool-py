#!/usr/bin/env python

import sys, os, subprocess
import shutil
import glob

VERBOSE = True
make_opt_parallel='-j4'

#export PATH=$PREFIX/bin:$PATH

#export LDFLAGS_FOR_TARGET="-L$PREFIX/sys_root/lib/arm-linux-gnueabihf -L$PREFIX/sys_root/usr/lib/arm-linux-gnueabihf"
#CFLAGS_FOR_TARGET="-I$PREFIX/sys-root/usr/include/arm-linux-gnueabihf"
#CXXFLAGS_FOR_TARGET="-I$PREFIX/sys-root/usr/include/arm-linux-gnueabihf"

def log(string):
  if VERBOSE:
    print(string)
    sys.stdout.flush()


def shell_cmd(prefix, cmds, redirect_stderr=False, args=[],custom_env=[]):
  fullargs = []
  if isinstance(cmds,str):
    fullargs.append(cmds)
  else:
    fullargs += [cmd for cmd in cmds]
  if isinstance(args,str):
    fullargs.append(args)
  else:
    fullargs += [arg for arg in args]

  new_env = os.environ.copy()
  new_env['PATH'] = prefix + '/bin:' + new_env.get('PATH',"")
  retval = 0

  log('## COMMAND: %s' % (fullargs) )

  if redirect_stderr:
    retval = subprocess.call(
      fullargs
      , stderr=subprocess.STDOUT
      , env=new_env
      )
  else:
    retval = subprocess.call(
      fullargs
      , env=new_env
      )

  return retval

def touch(filename):
  fd = os.open(filename, os.O_WRONLY | os.O_CREAT)
  os.close(fd)
  os.utime(filename,None)


def build_module( prefix, srcroot, module_name, build_dirname, module_ver, configure_args, configure_module='', make_target_build=['all'], make_target_install=['install'] ):
  #shutil.rmtree(build_dirname)
  if not os.path.exists(build_dirname):
    os.mkdir(build_dirname)

  retval=0
  cur_dir=os.getcwd()
  os.chdir(build_dirname)
  try:
    need_configure=False
    cmd=os.path.relpath(srcroot) + '/%s-%s/%sconfigure' % (module_name, module_ver, configure_module)
    args=' '.join(configure_args)

    if os.path.exists('config.log'):
      f = open('config.log','r')
      lines = f.readlines()
      f.close
      for line in lines:
        if not line.startswith('TOPLEVEL_CONFIGURE_ARGUMENTS='):
          continue

        line = line.rstrip()
        work='TOPLEVEL_CONFIGURE_ARGUMENTS=\'' + cmd + ' ' + args + '\''
        #print('line=%s' % line)
        #print('work=%s' % work)
        if line == work:
          #print('need_configure=False')
          need_configure=False
          break
        else:
          #print('need_configure=True')
          need_configure=True
          break

    if True == need_configure:
      if os.path.exists('config.status')
        os.remove('config.status')
      for marker_textfile in glob.glob('_success_build_*.txt'):
        os.remove(marker_textfile)
      for marker_textfile in glob.glob('_success_install_*.txt'):
        os.remove(marker_textfile)

    if not os.path.exists('config.status') or not os.path.exists('Makefile'):
      retval=shell_cmd( prefix, cmd, False, configure_args )
      if 0 != retval:
        raise Exception('configure error')

    for make_target in make_target_build:
      if not os.path.exists('_success_build_%s.txt' % make_target):
        cmd='make'
        args=[]
        args.append(make_opt_parallel)
        args.append(make_target)
        retval=shell_cmd( prefix, cmd, False, args )
        if 0 != retval:
          raise Exception('make %s error %s' % (make_target,build_dirname) )
        else:
          touch('_success_build_%s.txt' % make_target)
      else:
        print 'skip %s build %s' % (make_target, build_dirname)

    for make_target in make_target_install:
      if not os.path.exists('_success_install_%s.txt' % make_target):
        cmd='make'
        args=[]
        args.append(make_target)
        retval=shell_cmd( prefix, cmd, False, args )
        if 0 != retval:
          raise Exception('make %s error %s' % (make_target,build_dirname) )
        else:
          touch('_success_install_%s.txt' % make_target)
      else:
        print 'skip install %s' % build_dirname

  except Exception as e:
    log(str(e))
    retval=1
    pass
  os.chdir(cur_dir)

  return retval

def install_module( prefix, module_name, build_dirname, make_target='install' ):
  if not os.path.exists( build_dirname ):
    return 1

  retval=0
  cur_dir=os.getcwd()
  os.chdir(build_dirname)

  cmd='make'
  args=[]
  args.append(make_target)
  retval=shell_cmd( prefix, cmd, False, args )
  if 0 != retval:
    raise Exception('make %s error %s' % (make_target,build_dirname) )

  os.chdir(cur_dir)

  return retval


r'''

# --with-sysroot=$PREFIX/sys-root \
#
#
# --with-dwarf2



#--enable-version-specific-runtime-libs
#with-gxx-include-dir=
#
#with-glibc-version=2.13
#
#
#--with-target-subdir=
#
#LDFLAGS_FOR_TARGET


'''




def installresult( prefix, build_dirname ):
  if os.path.exists( prefix ):
    shutil.rmtree( prefix )

  retval=0
  cur_dir=os.getcwd()
  os.chdir(build_dir)
  try:
    retval=install_module( 'binutils', 'binutils' )
    if 0 != retval:
      raise Exception('install_binutils error')
    retval=build_sysroot()
    if 0 != retval:
      raise Exception('build_sysroot error')
    retval=install_module( 'gcc', 'gcc-stage2' )
    if 0 != retval:
      raise Exception('install_gcc error')
    retval=install_module( 'gdb', 'gdb' )
    if 0 != retval:
      raise Exception('install_gdb error')
    retval=install_module( 'gdbserver', 'gdbserver' )
    if 0 != retval:
      raise Exception('install_gdbserver error')
  except Exception as e:
    log(str(e))
    retval=1
    raise
  os.chdir(cur_dir)

  return retval

if __name__ == '__main__':
  main()

