#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Compress the contents of the web_static folder into a .tgz archive.
    Return the path to the archive if successful, None otherwise.
    """
    # Create the versions directory if it doesn't already exist
    if not os.path.exists("versions"):
        os.mkdir("versions")

    # Create the name of the archive with the current timestamp
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_{}.tgz".format(timestamp)

    # Use tar to create the archive
    result = local("tar -cvzf versions/{} web_static".format(archive_name))

    # Check if the archive was created successfully and return the path
    if result.succeeded:
        return "versions/{}".format(archive_name)
    else:
        return None

