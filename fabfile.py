__author__ = 'hari'
from fabric.api import local

def prepare_deploy(message):
    local("git add index.html")
    local("git add gridzilla_main.css")
    local("git add fabfile.py")
    local("""git commit -m "%s" """ % message)
  