### 前言
基于pyqt5和pyjwt实现的jwt加解密爆破一体化工具(ps:其实是水的python课设 ps2：发现最新用处，在全内网的线下赛中，收手机，出不去外网，出到jwt题目不会写脚本直接gg，该款工具就能派上用场hhh,也许有用~) 功能自己研究吧，图形化的应该一看就清楚。RS加密就是加密RS HS加密就是加密HS 注意算法选择和加密必须对应上，对应不上会报错。 爆破：纯数字爆破不用设置字典，点击就可以，纯字母爆破其实是同目录下存在弱口令字典
### 下载地址
[https://github.com/Aiyflowers/JWT_GUI](https://github.com/Aiyflowers/JWT_GUI)

### 软件截图
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29434471/1689933097657-397a5e93-a11e-44fd-9dec-7d0ced0ec5f9.png#averageHue=%23f6f6f5&clientId=u31fd5186-6b41-4&from=paste&height=860&id=u862e6a79&originHeight=1075&originWidth=1122&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=79682&status=done&style=none&taskId=u36c9fdd7-b827-4614-b9de-4f5999ad0f7&title=&width=897.6)

### 功能介绍
#### 加解密/jwt伪造
由于针对ctf比赛，一般我们是进行jwt篡改。输入jwt解密后可直接进行篡改
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29434471/1689933276085-c73c5f4e-98d0-44e6-bac6-f8ce84fcbce8.png#averageHue=%23f4f2f1&clientId=u31fd5186-6b41-4&from=paste&height=860&id=u9ac5d2d2&originHeight=1075&originWidth=1122&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=139728&status=done&style=none&taskId=u7d0ed7dc-1a02-4c80-9abc-83100ddaab9&title=&width=897.6)
可直接进行自由篡改


### ctfshow题目示例
#### web345
获得jwt后点击解密再点击none攻击,不过这道题似乎是用php的jwt加密的，格式很奇怪哈。还有[]包裹，这里工具虽然不能一把梭，但是我放个可以过的payload
```python
W3siYWxnIjoiTm9uZSIsInR5cCI6Imp3dCJ9.eyJzdWIiOiJhZG1pbiJ9XQ
```
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29434471/1690179213566-03ee6474-2c61-4aa1-b5c9-09f6d0e28048.png#averageHue=%23f6f6f6&clientId=u9c43d47f-1fdb-4&from=paste&height=74&id=u94d77ed0&originHeight=93&originWidth=609&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=5123&status=done&style=none&taskId=u9b79c1ff-96de-4270-b4a2-1c166e9ed15&title=&width=487.2)
只能说格式很奇怪。。不是标准的json格式
#### web346 None攻击示例
先获取到jwt，注意它给的cookie形式 是否是x.x.x 或者x.x.    我们的运行提示里也会显示格式不对的话是无法运行的。如果格式没问题直接点击解密即可，格式如果不符合上述两种，请自己加上.
解密后你会看到显示HS256算法
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29434471/1690161908984-8cf44b2a-52d0-4403-a385-929791b356aa.png#averageHue=%23f4f3f3&clientId=u0667b037-8a9b-4&from=paste&height=860&id=ue622c963&originHeight=1075&originWidth=1122&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=106206&status=done&style=none&taskId=u79f4686c-0153-484e-befd-9d81341bbad&title=&width=897.6)
一种错误的解题顺序方式：我们直接在payload一栏中篡改"sub":"user"为"sub":"admin" 接着点击None攻击
此时生成的结果解密后Headers一栏中为单引号包裹，是不符合json要求的。
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29434471/1690162426257-0a328169-ea96-4505-ae71-783f40b859eb.png#averageHue=%23f3f0ef&clientId=u0667b037-8a9b-4&from=paste&height=179&id=ufc60e0d0&originHeight=224&originWidth=869&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=22160&status=done&style=none&taskId=u97a16e35-78eb-40eb-abf3-46c6b24bb3f&title=&width=695.2)
(之所以产生这种工具特性~，是因为代码流程导致。懒得修改了直接用正常解题顺序就没得问题)
正确的解题顺序方式：先点击None攻击，将None攻击生成的数据拿到输入JWT中解密再进行篡改。
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29434471/1690162524756-98facf2e-d62a-4cd3-9c1d-b81b2c60a29a.png#averageHue=%23f4f2f1&clientId=u0667b037-8a9b-4&from=paste&height=860&id=u89f86f27&originHeight=1075&originWidth=1122&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=126270&status=done&style=none&taskId=ubdc777fe-f9b6-4ca3-9e48-5dfb8bda7ba&title=&width=897.6)
我们点击了None攻击后，运行提示中会有提示格式可能不对，这时候可能需要我们自己补全.了
接着把None的输出放到输入jwt中补全格式后点击解密，自己再随意的篡改user为admin，然后点击HS加密即可得到篡改后的cookie，放到cookieedtor或者bp抓包放包即可得到flag
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29434471/1690162649099-8905a7db-3fbb-4ded-afcb-cad99c23a846.png#averageHue=%23f6f4f4&clientId=u0667b037-8a9b-4&from=paste&height=830&id=u2a46762d&originHeight=1038&originWidth=1600&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=215613&status=done&style=none&taskId=ud31612f4-800d-495c-bb58-01e3fdafea4&title=&width=1280)
#### 347 爆破key开始
本工具的爆破有三种

1. 基于for循环的纯数字前5位爆破  （从第6位开始，时间就不可控了）
2. 基于字典的纯字母爆破，前3位    （从第四位开始 时间就不可控了）
3. 基于自定义弱口令字典的密钥爆破  (只要你字典够强大，我就能爆)

而本题目我们需要弱口令字典去加载爆破，点击使用默认字典
点击爆破，即可爆破出来
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29434471/1690174137311-2327109b-cd35-4ac4-979d-f158f736d335.png#averageHue=%23f4f3f3&clientId=uea3afa28-9e9a-4&from=paste&height=860&id=uc8fdf6b5&originHeight=1075&originWidth=1122&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=112112&status=done&style=none&taskId=u65e51b77-8c0c-437b-bc26-6f6a03dbcac&title=&width=897.6)
默认字典就是我提供的当前目录下的password.txt
爆破得到key后，即可篡改jwt，这里就不需要None攻击了而是利用HS加密即可
##### 爆破易错点(修改软件爆破失败特性)
因为key的生成与headers，payload的base64编码有关系，那么headers和payload中字段的顺序也影响着key的爆破！，这里不同jwt加密库的写法不同可能导致出现未预料的软件特性(bug)
比如pyjwt中默认的headers顺序是{typ,alg} 而且我们无法修改这个顺序。这就导致我们爆破key时候，比如说本题，我们的headers顺序是{alg,typ} 那么我们就不可以爆破到密钥。（实际测试是可以的，但是打包后的exe却不可以。解决办法如下）
[解决Python修改pyjwt模块默认header无效的问题_python acmev2 no key id in jws header_ithomia的博客-CSDN博客](https://blog.csdn.net/m0_46261074/article/details/104165261)
进入到源代码中，以防止出问题，先留个备份
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29434471/1690169480857-37d8288a-ed33-490e-990c-037a61a1b2ac.png#averageHue=%23272b30&clientId=uf7df05b3-a6b0-4&from=paste&height=860&id=ufac0ce03&originHeight=1075&originWidth=1915&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=2066197&status=done&style=none&taskId=u8eb1287d-8e5e-4118-9dbd-f62b42ee0c8&title=&width=1532)
这里需要注意的是，有可能你用pyinstaller打包所使用到的api_jwts.py不是当前目录下的，比如我的电脑就是这样，因此我建议用everything搜索电脑上所有的该文件，都进行更改再重新打包文件。
其实这里面还有个python小特性，json.loads处理出来的字典顺序是随机的！这里不多介绍
#### 348
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29434471/1690174360023-61dd4498-29fa-4390-81c8-9b3e6b8324ec.png#averageHue=%23f4f3f3&clientId=uea3afa28-9e9a-4&from=paste&height=860&id=ud2fc65b5&originHeight=1075&originWidth=1122&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=106257&status=done&style=none&taskId=uab224cda-44f8-4ee9-b296-bc50e73b612&title=&width=897.6)
和上题目一样。
#### 349 获取到私钥一把梭
app.js下载看一下
访问/private.key 加载上私钥
即可一把梭了,记得根据headers里面显示的加密算法选择上加密算法
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29434471/1690178976339-3395e0f2-f44e-47c5-a10d-fe4a2a823685.png#averageHue=%23f3f1f0&clientId=u9c43d47f-1fdb-4&from=paste&height=860&id=ud4c66a5a&originHeight=1075&originWidth=1122&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=130267&status=done&style=none&taskId=uc97fef6b-9906-4708-a242-0e3fc1e2361&title=&width=897.6)
![image.png](https://cdn.nlark.com/yuque/0/2023/png/29434471/1690178955670-8708fd00-ad98-458b-b274-a9de229dd46f.png#averageHue=%23f5f3f3&clientId=u9c43d47f-1fdb-4&from=paste&height=834&id=u5500690f&originHeight=1042&originWidth=1600&originalType=binary&ratio=1.25&rotation=0&showTitle=false&size=215697&status=done&style=none&taskId=u1f0e4462-eda2-4855-97ac-3bc35b38fca&title=&width=1280)
#### 350
必须用node.js去加解密，本工具暂时无法解决。
