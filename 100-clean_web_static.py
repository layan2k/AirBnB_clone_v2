#!/usr/bin/python3
"""deletes out-of-date archives,
   using the function do_clean"""

from fabric.api import *
import os
import shlex

env.user = 'ubuntu'
env.hosts = ['3.238.253.91', '35.237.111.104']


def do_clean(number=0):
    if os.path.exists('versions'):
        if int(number) == 0:
            variable = 2
        else:
            variable = int(number) + 1
        command = 'tail -n +{}| xargs rm -rf'.format(variable)
        local('cd versions ; ls -t|{}'.format(command))
        dir = '/data/web_static/releases'
        run('cd {}; ls -t| grep web_static|{}'.format(dir, command))
