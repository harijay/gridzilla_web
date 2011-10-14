__author__ = 'hari'
from fabric.api import local

def prepare_deploy(message):
    local("git add index.html")
    local("git add gridzilla_main.css")
    local("git add fabfile.py")
    local("git add .idea/workspace.xml")
    local( "git add .idea/misc.xml")
    local("git add .gitignore")
    local("""git commit -m "%s" """ % message)

def deploy():
    local("rsync -av index.html bioscree@code-itch.com:~bioscree/public_html/codeitch/gridzilla_web/")
    local("rsync -av gridzilla_main.css bioscree@code-itch.com:~bioscree/public_html/codeitch/gridzilla_web/")