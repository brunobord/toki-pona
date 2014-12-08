# -*- encoding: utf8 -*-
import requests as r

root = 'http://lvogel.free.fr/tokipona/'

with open('index.html', 'wb') as fd:
    fd.write(r.get(root).content)

for x in range(1, 10):
    lecon = 'lecon0%d.html' % x
    with open('src/' + lecon, 'wb') as fd:
        fd.write(r.get(root + lecon).content)

for x in range(10, 18):
    lecon = 'lecon%d.html' % x
    with open('src/' + lecon, 'wb') as fd:
        fd.write(r.get(root + lecon).content)
