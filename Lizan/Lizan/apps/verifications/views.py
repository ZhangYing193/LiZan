from random import randint

# Create your views here.
from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import constants
from celery_tasks.sms import tasks as sms_tasks


class SMSCodeView(APIView):
    """发送短信验证码"""

    def get(self, request, mobile):
        # 获取手机号是否以发送的标记，以发送则提前响应
        redis_conn = get_redis_connection('verify_codes')
        send_flg = redis_conn.get('send_flg_%s' % mobile)
        if send_flg:
            return Response({'message': '频繁发送短信'}, status=status.HTTP_400_BAD_REQUEST)
        # 1。生成短信验证码
        sms_code = '%06d' % randint(0, 999999)
        print(sms_code)
        # 2。创建redis连接对象
        redis_conn = get_redis_connection('verify_codes')
        # ++添加管道，减少redis的连接访问
        pl = redis_conn.pipeline()
        # 3。把验证码存储到redis
        pl.setex('sms_%s' % mobile, constants.SMS_CODE_REDIS_EXPIRES, sms_code)
        # 添加标记
        pl.setex('send_flg_%s' % mobile, constants.SMS_CODE_REDIS_EXPIRES, 1)
        # +++执行管道
        pl.execute()
        # 4。利用容联云通讯发短信， 阻塞主进程,使用celery异步发送
        # CCP().send_template_sms(mobile, {sms_code, 5分钟}, 1)
        # print(mobile, sms_code)
        # 触发异步任务，让发短信不要阻塞主线程,delay才能真正触发异步任务
        # # 发送短信验证码
        # sms_code_expires = str(constants.SMS_CODE_REDIS_EXPIRES // 60)
        # sms_tasks.send_sms_code.delay(mobile, sms_code, sms_code_expires)

        sms_tasks.send_sms_code.delay(mobile, sms_code)
        # 5。响应
        return Response({"message": "OK"})
