#!/bin/sh

# 安装curl
info=`opkg list_installed | grep "curl"`
if [ ${#info} == 0 ]; then
	opkg install libpolarssl.ipk libcurl.ipk curl.ipk
fi

# 复制相关文件到对应位置
chmod u+x feiy
cp feiy /bin
cp feiy.conf /etc/

# 设置开机自启
sed -i "/^feiy -login/ c\ " /etc/rc.local
echo "feiy -login" >> /etc/rc.local
