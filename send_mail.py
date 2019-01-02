import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    send_mail(
        '来自lhw测试邮件',
        'hello word！',
        'hzaulhw@sina.com',
        ['1451308045@qq.com'],
    )
