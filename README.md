# smzdm_checkin
auto checkin to smzdm
The cookies change every two week, so you'll need to check the checkin result periodly and copy the new sess value of cookies to config.py.


什么值得买签到机器人，因为现在每两周左右cookies里的sess值都会变化，所以需要定时更换sess值。后续可能会加一个登录过程来获取sess值

使用时请新建config.py，格式如下:

```python
COOKIE_SESS_VALUE = 'your_sess_value'
CHECKIN_RESULT = 'your_checkin_result_location'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; rv:20.0) Gecko/20100101 Firefox/20.0'
```
