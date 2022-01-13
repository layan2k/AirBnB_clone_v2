#!/usr/bin/python3
"""
 a Fabric script (based on the file 2-do_deploy_web_static.py)
 that creates and distributes an archive to your web servers,
 using the function deploy
"""
from fabric.api import local, run, put, env
from datetime import datetime
from os.path import isfile

env.user = 'ubuntu'
env.hosts = ['3.238.253.91', '35.237.111.104']


def do_pack():
    """Generates tgz"""
    currentdate = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        file_name = "versions/web_static_{}.tgz".format(currentdate)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None


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


def deploy():
    """Creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
