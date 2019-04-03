# 路由器模拟电脑or手机拨号

## 原理
    通过在mac系统下抓包，并进行过多次实验，发现只要把抓到的登录包(HTTP协议的包)发送一遍就算登录上了，
    然后反复尝试删除其中的一些参数，最后剩下三大部分的参数。
    
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
    
    
    
