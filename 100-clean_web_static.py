#!/usr/bin/python3
"""deletes out-of-date archives,
   using the function do_clean"""

from fabric.api import *


env.user = 'ubuntu'
env.hosts = ['3.238.253.91', '35.237.111.104']


def do_clean(number=0):
    if number == 0:
        number = 1
    with cd.local('./versions'):
        local("ls -lt | tail -n +{} | rev | cut -f1 -d" " | rev | \
            xargs -d '\n' rm".format(1 + number))
    with cd('/data/web_static/releases/'):
        run("ls -lt | tail -n +{} | rev | cut -f1 -d" " | rev | \
            xargs -d '\n' rm".format(1 + number))
