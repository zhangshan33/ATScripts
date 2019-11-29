# -*- coding: utf-8 -*-
# __author__ = "maple"

import subprocess
from settings import conf

class AllureHandler(object):

    def execute_command(self):
        import time
        time.sleep(1)
        subprocess.call(conf.ALLURE_COMMAND, shell=True)

