# 编写异步任务代码，名称只能叫tasks
from .yuntongxun.sms import CCP
import logging
# from Lizan.celery_tasks.sms.yuntongxun.sms import CCP
from celery_tasks.main import app
logger = logging.getLogger("django")
# 验证码短信模板
SMS_CODE_TEMP_ID = 1

@app.task(name='send_sms_code')  # 用celery_app调用task方法装饰我们的函数为一个异步任务
def send_sms_code(mobile, sms_code):
    """
    发送短信验证码
    :param mobile: 手机号
    :param code: 验证码
    :param expires: 有效期
    :return: None
    """
    # 4。利用容联云通讯发短信， 阻塞主进程
    # CCP().send_template_sms(mobile, {sms_code, 5分钟}, 1)
    print(mobile, sms_code)

    # try:
        # ccp = CCP()
    #     result = ccp.send_template_sms(mobile, [code, expires], SMS_CODE_TEMP_ID)
    # except Exception as e:
    #     logger.error("发送验证码短信[异常][ mobile: %s, message: %s ]" % (mobile, e))
    # else:
    #     if result == 0:
    #         logger.info("发送验证码短信[正常][ mobile: %s ]" % mobile)
    #     else:
    #         logger.warning("发送验证码短信[失败][ mobile: %s ]" % mobile)
