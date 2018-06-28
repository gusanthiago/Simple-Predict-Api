#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from api.utils.factory import create_app

if __name__ == '__main__':  
    app = create_app()
    if os.environ.get('WORK_ENV') == 'PROD':
        app.run(port=5000, host="0.0.0.0", use_reloader=False)
    else:
        app.run(port=5000, host="0.0.0.0", use_reloader=True)
