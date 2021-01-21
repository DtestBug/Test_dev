import os
import smtplib  # 负责发送邮件
from email.mime.text import MIMEText  # MIMEText构造协议
from email.mime.multipart import MIMEMultipart  # 添加邮件附件
import requests
# import pymysql


def runApiCase():
    # 项目路径
    obj_path = os.path.abspath('..')
    # 执行文件路径
    file_path = r'\API_httprunner\testsuites\api_testsuite.yml'

    # 绝对路径
    absolute_path = obj_path + file_path

    # 执行脚本
    command_run = os.system(f'hrun {absolute_path}')
    if command_run == 0:
        reports_dir = os.getcwd()
        reports_path = reports_dir + '\\reports\\'
        html_reports = os.listdir(reports_path)[0]
        jd_path = reports_path + html_reports
        return jd_path

    if command_run == 1:
        return f"执行hrun {absolute_path} 失败！"


def send_email(data):
    res = {
        'ret': 'True',
        'data': '邮件已发送'
    }
    try:
        msg_to = ['1210955224@qq.com', ]
        msg_text = MIMEText(f'测试大佬，测试报告请查看附件内容！\n{data}', 'plain', 'utf-8')  # 内容，发送内容格式，编码格式

        msg = MIMEMultipart()  # 添加附件时候需要
        attch = MIMEText(open(data, 'rb').read(), 'base64', 'utf-8')
        # 内容                        #格式    #编码格式
        attch['Content-Type'] = 'application/octet-stream'  # 指定文件格式类型
        attch['Content-Disposition'] = f'attachment;filename={data}'  # Content-Disposition值则出现下载保存对话框，保存的默认文件名使用filename指定
        msg.attach(attch)  # 附加内容
        msg.attach(msg_text)  # 正文
        msg['subject'] = '接口测试报告'  # 标题
        msg['from'] = '九歌'  # 来自xx的邮件
        msg['To'] = ','.join(msg_to)  # 发送至1125204068
        s = smtplib.SMTP_SSL('smtp.qq.com', 465)  # 连接相关邮箱服务器
        s.login('1210955224@qq.com', 'ltykkzdhkgcjffjb')  # 登录、获取QQ邮箱授权码
        s.sendmail('1210955224@qq.com', msg['To'].split(','), str(msg))  # 从XX发送邮箱到XX   1125204068@qq.com
        #            自己邮箱               收件人邮箱           str(发送内容)强制str类型发送
    except Exception as e:
        res = {
            'ret': False,
            'errors': data,
            'need': '需要清除测试数据'
        }
    return res


class delData():
    def __init__(self):
        self.data = 'test111'
        self.url = f'http://www.longboard-jg.ltd:8000/register/{self.data}'


    def delSqlData(self):
        # url = 'http://www.longboard-jg.ltd:8000/register/test111'
        # 数据库连接信息
        res = requests.delete(self.url).status_code.__eq__(204)
        if res:
            return res
        else:
            return "删除失败"


    def delLocalData(self):
        htmlfile_path = os.path.abspath('.')
        file_dir = htmlfile_path + '\\reports\\'
        files = os.listdir(file_dir)
        for file in files:
            file_del_res = os.system(fr'del {file_dir + file}')

            # 删除本地文件
            if file_del_res == 0:
                return f'删除成功 {file_dir + file}'

            if file_del_res == 1:
                return f'执行失败，没有文件{file_dir + file}'


def run():
    res = f"""
    {send_email(runApiCase())}
    {delData().delLocalData()}
    {delData().delSqlData()}
    """
    return res

run()
