# 路由器模拟电脑or手机拨号

## 原理
    通过在mac系统下抓包，并进行过多次实验，发现只要把抓到的登录包(HTTP协议的包)发送一遍就算登录上了，
    然后反复尝试删除其中的一些参数，最后剩下四大部分的参数。
    
    第一个是请求参数，包括5个参数.
    1：wlanacname，这个参数貌似是固定的，不知道不同地方会不会不一样。
    2：wlanuserip，电信通过DHCP协议自动分配给你的局域网ip，windows可通过ipconfig命令查看,linux
    和mac可以通过ifconfig命令查看
    3：button，固定为'Login'。
    4：UserName，这个参数由两部分组成，账号前缀+账号。账号前缀有两种（我就只发现两种），分别对应
    电脑[%21%5EA6EA0]和手机[%21%5EMaod0],账号就是手机号，譬如'%21%5EA6EA018111223344'。
    5：Password，这个参数就是你的加密后的密码，为32位十六进制数。大概每一天或两天变一次，一个月为
    一个轮回，就是说你上个月1号的加密密码可能和这个月的加密密码一样。
    
    第二个是cookie参数，就包括1个。
    1：JSESSIONID，任意的32位十六进制数，譬如'FEC863C6D11D98D580DBFF4FFD01D4AA'。
  
    第三个就是请求头，包括2个。
    1：User-Agent：设备名称,目前就发现两个，电脑[CDMA+WLAN(macos)] and 手机[CDMA+WLAN(Maod)]，
    和上面的请求参数UserName的账号前缀相对应。（可以实现一账号两人(模拟手机和模拟电脑)用）
    2：Content-Type：固定为'application/x-www-form-urlencoded'
    
    第四个就是请求登录的url
    我这边[湖北]是 http://58.53.199.144:8001/wispr_auth.jsp（可能随地域变化）
    
    
    
    通过上面，我们现在需要的是一个能让路由器(类似openwrt的linux嵌入式的路由器)模拟并发送http包的软件，
    通过查询我找到了curl这个命令（需要路由器安装软件curl）。所以我们目前的思路是：通过curl发送登录包
    骗过飞young服务器，让它以为我们的路由器是手机或电脑。
    

## 路由器配置

### 1、下载相关系列curl安装包
    包括相关依赖有三个软件包，分别是libpolarssl.ipk,libcurl.ipk,curl.ipk。安装时必须按照这个顺序安装。
    下载时注意自己路由器是什么系列的，install目录下的是ralink系列的。

### 2、填写配置文件
    修改install目录下的配置文件feiy.conf。
    第一处是用户，一般是电信卡号码。
    第二处是每日的加密后密码，配齐31天，可以通过运行java目录的Password.java获得，(没安装jdk的可以把代
    码复制，搜索能在线运行java的网站。)
    
### 3、将install目录（包括文件）复制到路由器里
    // TODO
### 4、运行install.sh(在install目录下运行一下两行)
    chmod u+x install.sh
    sh install.sh
    
有什么问题可以联系邮箱`hsernos@163.com`