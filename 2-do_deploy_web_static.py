#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static """
from datetime import datetime
from fabric.api import local, run, env, put
import os

env.hosts = ['35.229.103.77', '35.185.39.172']


def do_pack():
    """ generates a .tgz archive from the contents of the web_static """
    try:
        if not os.path.exists('./versions'):
            os.makedirs('./versions')

        now = datetime.now()

        fmat = now.strftime("%Y%m%d%H%M%S")

        local("tar -cvzf versions/web_static_{}.tgz web_static".format(fmat))

        return "versions/web_static_{}.tgz".format(fmat)

    except:
        return None


def do_deploy(archive_path):
    """ distributes an archive to web servers """
    filename = archive_path.split("/")[-1]
    filename_no_ext = filename.split(".")[0]
    dest = "/data/web_static/releases/"
    new_path = dest + filename_no_ext

    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(dest, filename_no_ext))
        run('tar -xzf /tmp/{} -C {}{}'.format(filename, dest, filename_no_ext))
        run('rm -rf /tmp/{}'.format(filename))
        run('mv {}/web_static/* {}/'.format(new_path, new_path))
        run('rm -rf {}/web_static'.format(new_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(new_path))
        return True
    except:
        return False
