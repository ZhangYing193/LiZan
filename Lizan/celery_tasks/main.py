# celery启动文件， 准备celery客户端
from celery import Celery
# 为celery使用django配置文件进行设置
import os
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'Lizan.settings.dev'

# 1。创建celery客户端
# celery_app = Celery('别名')
app = Celery('Lizan')
# 2。加载配置信息
app.config_from_object('celery_tasks.config')
# 3。注册异步任务
app.autodiscover_tasks(['celery_tasks.sms'])
