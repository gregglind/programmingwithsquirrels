from fabric.api import env,lcd,cd,run,task,local
from contextlib import contextmanager
import os

def here():
    return os.path.dirname(env['real_fabfile'])

@task
def build(force=False):
    "cd book && rm -rf build/* && make html && cd -"
    with lcd(here()) as s:
        with lcd("book") as d:
            if force:
                local("rm -rf build/*")
            
            local("make html")

@task
def rebuild():
    """ "force" build, rm-ing first"""
    build(force=True)

@task
def deploy():
    "rsync -av book gregg@69.164.205.89:~/public_html"  
    with lcd(here()) as s:
        local("rsync -av book gregg@69.164.205.89:~/public_html")
