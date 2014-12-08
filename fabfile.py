from fabric.api import *
import os

@task
def convert():
    for f in os.listdir('src'):
        fname, _ = os.path.splitext(f)
        local('pandoc -f html -t markdown src/%(f)s -o markdown/%(fname)s.md' % {'f': f, 'fname': fname})
