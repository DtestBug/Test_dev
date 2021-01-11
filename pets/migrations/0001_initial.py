# Generated by Django 3.1.3 on 2021-01-11 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PetsModels',
            fields=[
                ('id', models.AutoField(help_text='id', primary_key=True, serialize=False, verbose_name='id')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('name', models.CharField(help_text='宠物名', max_length=10, unique=True, verbose_name='宠物名')),
                ('weight', models.TextField(help_text='体重', max_length=3, verbose_name='体重')),
                ('age', models.TextField(help_text='出生时长', max_length=3, verbose_name='出生时长')),
                ('varieties', models.TextField(help_text='品种', max_length=50, verbose_name='品种')),
                ('color', models.TextField(help_text='颜色', max_length=20, verbose_name='颜色')),
            ],
            options={
                'verbose_name': '宠物信息表',
                'db_table': 'pets_data',
            },
        ),
    ]
