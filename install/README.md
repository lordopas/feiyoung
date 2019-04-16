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
### 4、运行install.sh(在install目录下运行以下两行)
    chmod u+x install.sh
    sh install.sh