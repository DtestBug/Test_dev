from rest_framework import serializers  # 序列化
from rest_framework.validators import UniqueValidator
from .models import PetsModels
from utils.is_number import isnumber
import datetime


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = PetsModels
        # 不需要返回到json的内容
        exclude = ('create_time', 'update_time')

        # 已有字段再加限制
        extra_kwargs = {
            'name': {
                'label': 'name',
                # 'help_text': '宠物的名字',
                'min_length': 1,
                'max_length': 10,
                # 'write_only': False,  # 为True的时候不返回到json
                'required': True,  # 为True输入时必填字段
                'validators': [UniqueValidator(queryset=PetsModels.objects.all(), message='宠物名已存在，请换一个再试试。')],
                'error_messages': {
                    'min_length': '最少输入1个字符',
                    'max_length': '输入不能超出10个字符'
                                    }
                        },

            'weight': {
                'label': 'weight',
                # 'help_text': '宠物的当前体重',

                # 'write_only': False,  # 为True的时候不返回到json
                'required': False,   # 为True输入时必填字段
                'min_length': 1,
                'max_length': 3,
                'error_messages': {
                    'min_length': '最少输入1个字符',
                    'max_length': '输入不能超出3个字符'
                }
                     },

            'birthday': {
                'label': 'birthday',
                # 'help_text': '宠物出生到现在多久',

                # 'write_only': False,  # 为True的时候不返回到json
                'required': False,  # 为True输入时必填字段
                'error_messages': {
                    'min_length': '最少输入1个字符',
                    'max_length': '输入不能超出3个字符'
                                    }
                        },
            'varieties': {
                'label': 'varieties',
                # 'help_text': '宠物是什么品种',

                # 'write_only': False,  # 为True的时候不返回到json
                'required': False,  # 为True输入时必填字段
                'max_length': 50,
                'error_messages': {
                    'max_length': '输入不能超出50个字符'
                }
            },

            'color': {
                'label': 'color',
                # 'help_text': '宠物的颜色',

                # 'write_only': False,  # 为True的时候不返回到json
                'required': False,  # 为True输入时必填字段
                'max_length': 20,
                'error_messages': {
                    'max_length': '输入不能超出20个字符'
                }
            },

        }

    # 在序列化器类中对单字段进行校验
    # 必须要以validate_作为前缀,(self, value)
    @staticmethod  # 将方法静态，不需要添加self
    def validate_weight(value):
        if isnumber(value):
            return value
        else:
            raise serializers.ValidationError("请输入数字")

    @classmethod  # 将方法静态，需要将self改为cls
    def validate_birthday(cls, value):
        # isinstance判断value是否时间类型
        if isinstance(value, datetime.date):
            return str(value)
        else:
            raise serializers.ValidationError("非日期类型")





