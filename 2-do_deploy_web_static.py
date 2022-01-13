#!/usr/bin/python3
"""
 a Fabric script (based on the file 1-pack_web_static.py)
 that distributes an archive to your web servers
"""
from fabric.api import run, put, env
from os.path import isfile


env.user = 'ubuntu'
env.hosts = ['3.238.253.91', '35.237.111.104']


def do_deploy(archive_path):
    """Do Deply to webserver"""
    if isfile(archive_path) is False:
        return False
    try:
        filename = archive_path.split("/")[-1]
        no_ext = filename.split(".")[0]
        path_no_ext = "/data/web_static/releases/{}/".format(no_ext)
        symlink = "/data/web_static/current"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_no_ext))
        run("tar -xzf /tmp/{} -C {}".format(filename, path_no_ext))
        run("rm /tmp/{}".format(filename))
        run("mv {}web_static/* {}".format(path_no_ext, path_no_ext))
        run("rm -rf {}web_static".format(path_no_ext))
        run("rm -rf {}".format(symlink))
        run("ln -s {} {}".format(path_no_ext, symlink))
        return True
    except Exception:
        return False
