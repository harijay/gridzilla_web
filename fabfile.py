__author__ = 'hari'
from fabric.api import local

def prepare_deploy():
    local("git add *")
  