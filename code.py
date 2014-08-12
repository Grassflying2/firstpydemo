# coding=utf-8
__author__ = 't00202151'

import sys
import os

cur_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(cur_dir, "model"))
from usermgr import userDb

urls = ('/([a-zA-Z0-9_\-/.]*)', 'main')

import web

app = web.application(urls, globals())

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

service = userDb()


class main(object):
    def GET(self, req_path):
        if req_path != '':
            return env.get_template(req_path + '.html').render(title=req_path)
        else:
            web.seeother('/signin')
            #raise web.notfound()

    def POST(self, req_path):
        if req_path == 'signin':
            i = web.input()
            name = i.login_name
            pwd = i.login_password
            val = 'UserName: [%s]\n Password:[%s]' % (name, pwd)
            if userDb().check(name, pwd):
                web.seeother('main')
            else:
                return env.get_template('success.html').render(status='Error', val=val)
        elif req_path == 'signup':
            i = web.input()
            name = i.signup_email
            pwd = i.signup_password
            if userDb().setUser(name, pwd):
                return web.seeother('signin')
            else:
                return env.get_template('success.html').render(status='Error', val=None)
        else:
            raise web.notfound()


def notfound():
    return web.notfound(env.get_template('e404.html').render())


if __name__ == '__main__':
    app.notfound = notfound
    app.run()
