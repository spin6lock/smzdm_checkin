#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import urllib2
from config import * 
import datetime
import time
import random
import json
 
# COOKIE_SESS_VALUE 可以通过chrome查看cookies的sess字段获得
COOKIE_SESS = 'sess=' + COOKIE_SESS_VALUE
 
if __name__ == '__main__':
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    opener.addheaders = [
        ('User-Agent', USER_AGENT),
        ('Cookie', COOKIE_SESS)
    ]
    sleep_time = random.randint(0, 60)
    time.sleep(sleep_time)
    with open(CHECKIN_RESULT, "w") as fh:
        result = opener.open('http://www.smzdm.com//user/qiandao/jsonp_checkin').read()[1:-1]
        fh.write(str(datetime.datetime.now()) + " " + json.dumps(json.loads(result), ensure_ascii = False))
