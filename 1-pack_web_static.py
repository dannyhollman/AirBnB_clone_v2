#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static """
from datetime import datetime
from fabric.operations import local
import os


def do_pack():
    """ generates a .tgz archive from the contents of the web_static """
    try:
        if not os.path.exists('./versions'):
            os.makedirs('./versions')

        now = datetime.now()

        fmat = now.strftime("%Y%m%d%H%M%S")

        local("tar -cvzf web_static_{}.tgz ./web_static".format(fmat))

        return "versions/web_static_{}.tgz".format(fmat)

    except:
        return None
