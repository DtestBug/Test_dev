from rest_framework import serializers  # 序列化
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler


class RegisterSerializer(serializers.ModelSerializer):
    datetime_fmt = '%Y年%m月%d日 %H:%M:%S'
    datetime = serializers.DateField(label='创建时间', help_text='创建时间', format='%Y-%m-%d %H:%M:%S', required=False, read_only=True)

    # 表里新增字段
    password_confirm = serializers.CharField(label='确认密码', help_text='确认密码',
                                             min_length=6,
                                             max_length=20,
                                             write_only=True,
                                             error_messages={
                                                 'min_length': '密码最小长度为6个字符',
                                                 'max_length': '密码最大长度为20个字符'
                                             })
    token = serializers.CharField(label='生成token', read_only=True)

    class Meta:
        model = User  # django自带的User方法

        # 展示给前端的信息
        fields = ('id', 'username', 'password', 'password_confirm', 'email', 'token', 'datetime', 'is_superuser')

        # 已有字段再加限制
        extra_kwargs = {
            'username': {
                'label': '用户名',
                'help_text': '用户名',
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '用户名最小长度为6个字符',
                    'max_length': '用户名最大长度为20个字符'
                                    }
                        },

            'email': {
                'label': '邮箱',
                'help_text': '邮箱',
                'write_only': True,
                'required': True,

                'validators': [UniqueValidator(queryset=User.objects.all(), message='此邮箱已注册')]
                     },

            'password': {
                'label': '密码',
                'help_text': '密码',
                'write_only': True,
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '密码最小长度为6个字符',
                    'max_length': '密码最大长度为20个字符'
                                    }
                        }
        }

    def validate(self, attrs):

        # 上传的密码与确认密码不一致的时候
        if attrs.get('password') != attrs.get('password_confirm'):
            raise serializers.ValidationError('两次密码输入不一致，请重新输入。')

        # 上传的密码与确认密码一致的时候，将数据返回
        return attrs

    # 将上一步通过校验的数据创建到数据表
    def create(self, validated_data):
        validated_data.pop('password_confirm')

        # 创建数据到表,创建用户时一定要用User.objects.create_user，少一个_user不会报错，但是密码不会加密
        user = User.objects.create_user(**validated_data)

        # 创建用户token
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token

        # 创建用户
        return user

