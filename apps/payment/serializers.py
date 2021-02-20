from rest_framework import serializers  # 序列化
from .models import PaymentModels
from pets.models import PetsModels


class PaymentModelSerializer(serializers.ModelSerializer):
    pet_name = serializers.StringRelatedField(label='所属项目名称', help_text='所属项目名称')
    pet_name_id = serializers.PrimaryKeyRelatedField(queryset=PetsModels.objects.all(),
                                                     label='项目id', help_text='项目id',
                                                     )

    class Meta:
        model = PaymentModels
        fields = ('id', 'pet_name', 'buy_time', 'category',  'product', 'count', 'price', 'use_time', 'pet_name_id')

    def create(self, validated_data):
        pet_name = validated_data.pop('pet_name_id')
        validated_data['pet_name'] = pet_name
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'pet_name_id' in validated_data:
            pet_name = validated_data.pop('pet_name_id')
            validated_data['pet_name'] = pet_name

        return super().update(instance, validated_data)
