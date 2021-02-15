#!/usr/bin/env python3

import blessed
import yaml
import ruamel.yaml
from deps.host_exec import execSilent
import subprocess
import os
import sys
import traceback

hostUser = os.getenv('HOSTUSER')
iotstackPwd = os.getenv('IOTSTACKPWD')
hostAddress = os.getenv('HOSTSSH_ADDR')
hostPort = os.getenv('HOSTSSH_PORT')

print('blessed Version:', blessed.__version__)
print('ruamel.yaml Version:', ruamel.yaml.__version__)
print('PyYAML Version:', yaml.__version__)
print('')
print('hostUser: ', hostUser)
print('iotstackPwd: ', iotstackPwd)
print('SSH hostAddress: ', hostAddress)
print('SSH hostPort: ', hostPort)

print('')
try:
  print('Checking connectivity to host...') 
  touchRes = execSilent('touch ./.tmp/rtest.file')
  touchRes = execSilent('echo "exec success" >> ./.tmp/rtest.file')
  readRes = execSilent('cat ./.tmp/rtest.file')
  rmRes = execSilent('rm ./.tmp/rtest.file')

  if readRes == 'exec success':
    print('Connection and remote command execution successful') 
  else:
    print('Error attempting to execute commands on the host. You may need to regenerate SSH keys by running:')
    print('  ./menu.sh --run-env-setup')
    print('')
    print('Or configure SSH to use correct ports.')
    input("Press Enter to continue to menu...")

except Exception:
  print('Error attempting to execute commands on the host. You may need to regenerate SSH keys by running:')
  print('  ./menu.sh --run-env-setup')
  print('')
  print('Or configure SSH to use correct ports.')
  print('')
  print('Error reported:')
  print(sys.exc_info())
  traceback.print_exc()
  print('')
  input("Press Enter to continue to menu...")

os.system('python menu_main.py')