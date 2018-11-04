#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from api.utils.factory import create_app
from os import environ

if __name__ == '__main__':  
    app = create_app()
    port_run = environ.get("PORT", 5000)
    if os.environ.get('WORK_ENV') == 'PROD':
        app.run(port=port_run, host="0.0.0.0", use_reloader=False)
    else:
        app.run(port=port_run, host="0.0.0.0", use_reloader=True)
