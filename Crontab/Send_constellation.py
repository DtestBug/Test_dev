from email.mime.text import MIMEText  # MIMEText构造协议
import smtplib  # 负责发送邮件
import requests
import time
from pyquery import PyQuery
import json

res_one = {}
URL1 = "https://www.d1xz.net/yunshi/today/Aquarius/"
res_one_data = requests.get(URL1)
res_one_data1 = PyQuery(res_one_data.text)('.det')
res_one['============本站地址============'] = "https://www.d1xz.net/yunshi/today/Aquarius/"
res_one['1'] = str(res_one_data1('.title.fb').text())
res_one['2'] = str(res_one_data1('.time').text())
res_one['3'] = str(res_one_data1('.fraction').text())
res_one['4'] = str(res_one_data1('.txt').text())
res_one['5'] = str(res_one_data1('.quan_yuan').text())
one_res = json.dumps(res_one, indent=0, ensure_ascii=False, sort_keys=False, separators=(',', ':'))


URL2 = "https://www.xzw.com/fortune/aquarius/?appid=bds"
res_two_data = requests.get(URL2)
res_two_res = PyQuery(res_two_data.text)('.c_cont').text()


Time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())


msg_to = ['1210955224@qq.com', '1205900870@qq.com']
msg = MIMEText('%s\n%s' % (one_res, res_two_res), 'plain', 'utf-8')  # 内容，发送内容格式，编码格式

msg['subject'] = '星座助手'  # 标题
msg['from'] = '爸爸'  # 来自爸爸的邮件
msg['To'] = ','.join(msg_to)  # 发送至1125204068
s = smtplib.SMTP_SSL('smtp.qq.com', 465)  # 连接相关邮箱服务器
s.login('1210955224@qq.com', 'ltykkzdhkgcjffjb')  # 登录、获取QQ邮箱授权码
s.sendmail('1210955224@qq.com', msg['To'].split(','), str(msg))  # 从XX发送邮箱到XX   1125204068@qq.com
#            自己邮箱               收件人邮箱           str(发送内容)强制str类型发送

