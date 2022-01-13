#!/usr/bin/python3
"""deletes out-of-date archives,
   using the function do_clean"""

from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['3.238.253.91', '35.237.111.104']


def do_clean(number=0):
    """Clean"""
    no = int(number)

    if no == 0:
        no == 2
    else:
        no += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(no))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, no))
