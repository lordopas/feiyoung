#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib import request, parse
import datetime
import hashlib
import re
import argparse
import configparser
import os
import uuid

config = {
    'acname': "058.051.093.016",
    'system': {
        'pc': "CDMA+WLAN(macos)",
        'pe': "CDMA+WLAN(Maod)"
    },
    'prefix': {
        'pc': "!^A6EA0",
        'pe': "!^Maod0"
    },
    'login_url': "http://58.53.199.144:8001/wispr_auth.jsp",
    'logout_url': "http://58.53.199.144:8001/wispr_logout.jsp",
}


class Password:

    @staticmethod
    def get_passwd(passwd, day=datetime.date.today().day):
        passwdbyte = [ord(n) for n in passwd]
        ps_len = len(passwd)

        passwd_token = list(range(0, ps_len))
        date_token = Password.get_date_token(day)
        index1 = 0
        index2 = 0
        for i in range(0, ps_len):
            index1 += 1 & 255
            index1 %= 256
            index2 += date_token[index1] & 255
            index2 %= 256
            temp = date_token[index1]
            date_token[index1] = date_token[index2]
            date_token[index2] = temp
            index = date_token[index1] + date_token[index2] & 255
            index %= 256
            passwd_token[i] = 256 + date_token[index] ^ passwdbyte[i]
            passwd_token[i] %= 256

        m2 = hashlib.md5()
        m2.update(bytes(passwd_token))
        return m2.hexdigest()

    @staticmethod
    def get_date_token(day):
        data = {
            1: '1430782659',
            2: '0267854319',
            3: '9173268045',
            4: '3401978562',
            5: '8174069325',
            6: '8076142539',
            7: '8957612403',
            8: '4573819602',
            9: '3829507461',
            10: '9356078241',
            11: '4791250368',
            12: '6721895340',
            13: '1938567204',
            14: '4195768023',
            15: '2508479316',
            16: '7029183654',
            17: '1876354092',
            18: '1785043926',
            19: '6178093542',
            20: '5643712089',
            21: '1958627043',
            22: '9572314608',
            23: '0841267953',
            24: '7415038296',
            25: '5364107982',
            26: '1328760549',
            27: '1420698537',
            28: '7368240195',
            29: '8314902567',
            30: '0456897213',
            31: '0954761238'
        }
        word = data.get(day)
        word_len = len(word)
        wordbyte = [int(w) for w in word]
        token = [Password.setbyte(n) for n in range(0, 256)]
        index = 0
        for i in range(0, 256):
            index += token[i] + ((wordbyte[i % word_len]) & (255))
            index %= 256
            temp = token[i]
            token[i] = token[index]
            token[index] = temp
        return token

    def setbyte(n):
        if n < 128:
            return n
        else:
            return n - 256


class Feiyoung:
    def __init__(self, username, passwd):
        self.__user = {
            'pc': config['prefix']['pc'] + username,
            'pe': config['prefix']['pe'] + username
        }
        self.__passwd = passwd
        # self.__session = str(uuid.uuid1()).replace('-', '')
        self.__device = "pe"
        self.__ip = ""

    def set_device_pc(self):
        self.__device = "pc"

    def set_device_pe(self):
        self.__device = "pe"

    def set_ip(self, ip):
        self.__ip = ip

    def login(self, day=datetime.date.today().day):
        req = request.Request(config['login_url'])
        req.add_header('User-Agent', config['system'][self.__device])
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')
        login_data = parse.urlencode([
            ('UserName', self.__user[self.__device]),
            ('Password', Password.get_passwd(self.__passwd, day)),
            ('wlanacname', config['acname']),
            ('wlanuserip', self.__ip),
            ('button', 'Login'),
        ])
        with request.urlopen(req, data=login_data.encode('utf-8')) as f:
            info = f.read().decode('utf-8')
            pattern = re.compile(r'<ReplyMessage>([0-9]+)：(.*?)</ReplyMessage>', re.I)
            code, msg = re.findall(pattern, info)[0]
            return int(code), msg

    def relogin(self):
        code, msg = self.login()
        if code == 50:
            print(msg)
            return code, msg
        day = (datetime.date.today().day + 29) % 31 + 1
        for i in range(0, 31):
            code, msg = self.login(day)
            if code == 50:
                print(msg)
                return code, msg
            day = (day + 29) % 31 + 1
        print(msg)
        print("请检查ip or 账户和密码是否正确")
        return code, msg

    def logout(self):
        req = request.Request(config['logout_url'] + "?wlanacname=" + config['acname'] + "&wlanuserip=" + self.__ip)
        req.add_header('User-Agent', config['system'][self.__device])
        with request.urlopen(req) as f:
            info = f.read().decode('utf-8')
            pattern = re.compile(r'<ResponseCode>([0-9]+)</ResponseCode>', re.I)
            code = int(re.findall(pattern, info)[0])
            if code == 150:
                print('退出成功')
            else:
                print('退出失败，请检查ip是否正确')
            return code


def login(args):
    username = ''
    password = ''
    ip = ''
    conf = configparser.ConfigParser()
    if os.path.exists('feiy.conf'):
        conf.read("feiy.conf")
        username = conf.get('user', 'username')
        password = conf.get('user', 'password')
    else:
        conf.read("feiy.conf")
        conf.add_section('user')
        conf.set('user', 'username', '')
        conf.set('user', 'password', '')
        conf.write(open('feiy.conf', 'w'))

    is_exit = False
    if args.ip == None:
        print("需要使用[-i]选项")
        is_exit = True
    else:
        ip = args.ip
    if args.u == None:
        if username == '':
            print("需要使用[-u]选项")
            is_exit = True
    else:
        username = args.u
    if args.p == None:
        if password == '':
            print("需要使用[-p]选项")
            is_exit = True
    else:
        password = args.p
    if is_exit:
        exit(1)

    feiyoung = Feiyoung(username, password)
    feiyoung.set_ip(ip)
    if args.device != None:
        if args.device == 'pc':
            feiyoung.set_device_pc()
        elif args.device == 'pe':
            feiyoung.set_device_pe()
    if args.login:
        code, msg = feiyoung.relogin()
        if code == 50:
            conf.read("feiy.conf")
            conf.set('user', 'username', username)
            conf.set('user', 'password', password)
            conf.write(open('feiy.conf', 'w'))
    elif args.logout:
        feiyoung.logout()


def login_online():
    username = '在这里写账号（181xxxxxxxx）'
    password = '在这里写密码(xxxxxx）'
    ip = '在这里写电信分配给你的ip（100.64.xx.xx）'
    feiyoung = Feiyoung(username, password)
    feiyoung.set_ip(ip)
    feiyoung.relogin()


if __name__ == '__main__':
    a = argparse.ArgumentParser(description='模拟飞扬联网', usage='python3 feiy.py -i 100.64.xx.xx -l')
    a.add_argument('-l', '--login', help='登录', action="store_true")
    a.add_argument('-o', '--logout', help='登出', action="store_true")
    a.add_argument('-i', '--ip', help='使用指定ip')
    a.add_argument('-u', help='使用指定用户')
    a.add_argument('-p', help='使用指定密码')
    a.add_argument('-d', '--device', help='使用指定设备(pc or pe)')
    args = a.parse_args()
    login(args)
    # 使用下面一个函数先要把这个函数中的三个参数填完,把上一行login(args)注释掉，把下一行注释去掉，可以通过在线运行python3的网站上运行
    # login_online()

