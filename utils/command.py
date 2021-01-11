import os

# 批处理文件创建，路径为vbs需要隐藏的路径
dosfile_path = r"D:\jiuge.bat"
with open(dosfile_path, 'w+') as dos_file:
    # 批处理命令 #
    msg = r"""mkdir D:\test1"""
    dos_file.write(msg)

# 创建vbs脚本路径
desktop_path = r"D:\hide.vbs"
file = open(desktop_path, 'w+')
# msg为vbs脚本，目的是为了隐藏bat文件执行时候打开dos窗口
msg = rf"""createobject("wscript.shell").run "{dosfile_path}",0"""
file.write(msg)
file.close()
dos_command = rf'start {desktop_path}'

# 执行dos命令：执行vbs文件
start_command = os.system(dos_command)
