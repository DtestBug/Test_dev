from django.db.models.signals import post_save  # 信号
from django.dispatch import receiver  # 发送信号到注册者

from django.contrib.auth.models import User


@receiver(post_save, sender=User)  # 接收者为注册用户，需要在_init_.py设置default_app_config = 'register.apps.RegisterConfig'
def after_register(sender, **kwargs):
    print('邮箱发送右键的逻辑')
