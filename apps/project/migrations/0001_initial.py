# Generated by Django 3.1.3 on 2021-02-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(help_text='id', primary_key=True, serialize=False, verbose_name='id')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='create_time')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='update_time')),
                ('name', models.CharField(help_text='项目名', max_length=200, unique=True, verbose_name='项目名')),
                ('leader', models.TextField(help_text='负责人', verbose_name='负责人')),
                ('tester', models.TextField(help_text='测试人员', verbose_name='测试人员')),
                ('programmer', models.TextField(help_text='开发人员', verbose_name='开发人员')),
                ('desc', models.TextField(help_text='描述', verbose_name='描述')),
            ],
            options={
                'verbose_name': '项目信息',
                'verbose_name_plural': '项目信息',
                'db_table': 'project',
            },
        ),
    ]
