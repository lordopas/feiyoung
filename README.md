# 飞young破解
# 路由器模拟电脑or手机飞young拨号

## 原理
    通过在mac系统下抓包，并进行过多次实验，发现只要把抓到的登录包(HTTP协议的包)发送一遍就算登录上了，
    然后反复尝试删除其中的一些参数，最后剩下四大部分的参数。
    
    第一个是请求参数，包括5个参数.
    1：wlanacname，这个参数大概是各个市的飞young服务器ip
    2：wlanuserip，电信通过DHCP协议自动分配给你的局域网ip，windows可通过ipconfig命令查看,linux
    和mac可以通过ifconfig命令查看
    3：button，固定为'Login'。
    4：UserName，这个参数由两部分组成，账号前缀+账号。账号前缀有两种（我就只发现两种），分别对应
    电脑[%21%5EA6EA0]和手机[%21%5EMaod0],账号就是手机号，譬如'%21%5EA6EA018111223344'。
    5：Password，这个参数就是你的加密后的密码，为32位十六进制数。大概每一天或两天变一次，一个月为
    一个轮回，就是说你上个月1号的加密密码可能和这个月的加密密码一样。
    
    第二个是cookie参数，就包括1个。(现在好像不需要了)
    1：JSESSIONID，任意的32位十六进制数，譬如'FEC863C6D11D98D580DBFF4FFD01D4AA'。
  
    第三个就是请求头，包括2个。
    1：User-Agent：设备名称,目前就发现两个，电脑[CDMA+WLAN(macos)] and 手机[CDMA+WLAN(Maod)]，
    和上面的请求参数UserName的账号前缀相对应。（可以实现一账号两人(模拟手机和模拟电脑)用）
    2：Content-Type：固定为'application/x-www-form-urlencoded'
    
    第四个就是请求登录的url
    通用 http://58.53.199.144:8001/wispr_auth.jsp
    
    
    
    所以我们目前的思路是：发送登录包，骗过飞young服务器，让它以为我们的路由器是手机或电脑。
    
## 实现方案一：使用shell脚本让路由器发送登录包
    缺点： 需要linux内核的路由器（openwrt之内的），对非专业人事操作困难
    优点： 能实现自动登录
    详情在install目录下
    
## 实现方案二：使用python脚本发送登录包
    缺点： 每次登录都需要手动获取ip，需要使用电脑（带python3环境）或在在线python3网站运行
    优点： 解除了路由器的限制，普通路由器也能行
    详情在python目录下

# 日志记录

[2019.4.24] -- 同省不同市的参数可能会不一样，需要自己抓包然后慢慢实验出必要的参数，然后改写我的脚本或者用别的语言重写。我这边是湖北襄阳，
襄阳的应该能直接使用，其他地区的应该是绝对不能直接使用，我也没有其他地区的实验环境，所以需要你们自己慢慢折腾。
            
    
有什么问题可以联系邮箱`hsernos@163.com`
