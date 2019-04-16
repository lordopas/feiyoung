## 使用
    必须要的有三个参数，账户，密码和ip。其中因为ip在你下次登录时会变，所有需要进入路由器查看电信分配给你的ip，一般是100.64.xx.xx
    第一次登录需要账户和密码，登录成功后，会自动生成一个配置文件保存账户和密码。以后每次登录就只需要ip了。
    使用命令查看帮助： python3 feiy.py -h 
    ==>usage: python3 feiy.py -i 100.64.xx.xx -l
    ==>
    ==>模拟飞扬联网
    ==>
    ==>optional arguments:
    ==>  -h, --help            show this help message and exit
    ==>  -l, --login           登录
    ==>  -o, --logout          登出
    ==>  -i IP, --ip IP        使用指定ip
    ==>  -u U                  使用指定用户
    ==>  -p P                  使用指定密码
    ==>  -d DEVICE, --device DEVICE
    ==>                        使用指定设备(pc or pe)
    第一次登录：    python3 feiy.py -i 100.64.xx.xx -u 账户 -p 密码 -l
    记住密码后登录： python3 feiy.py -i 100.64.xx.xx -l
    登出：         python3 feiy.py -i 100.64.xx.xx -o