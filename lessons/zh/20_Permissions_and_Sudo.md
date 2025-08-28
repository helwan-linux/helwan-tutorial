第14课：权限和 Sudo
Linux 权限控制对文件和目录的访问。理解权限是基础。

权限类型
r: 读取权限。

w: 写入权限。

x: 执行权限。

权限格式
示例: -rwxr-xr--

所有者权限: rwx

组权限: r-x

其他人权限: r--

更改权限
使用 chmod 命令:

chmod u+x script.sh  # 为所有者添加执行权限
chmod 755 file.txt   # 设置 rwxr-xr-x 权限

更改所有权
使用 chown 命令:

sudo chown user:group file.txt

使用 sudo
sudo 以超级用户身份运行命令:

sudo apt update
sudo systemctl restart nginx

总结
权限保护文件，而 sudo 允许安全地执行管理任务。