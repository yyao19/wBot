# WBOT: 微信聊天机器人 #
[![py27][py27]

## WECHAT BOT ／ 个人微信聊天机器人 ##

* 在itchat和wxpy的基础上实现了一些社交功能
* Version 1.0

## 安装运行 ##

### INSTALL PYTHON 2.7 ###
Use the following guide to install Python 2.7.x on centos:
https://www.digitalocean.com/community/tutorials/how-to-set-up-python-2-7-6-and-3-3-3-on-centos-6-4

Install FFmpeg
https://www.vultr.com/docs/how-to-install-ffmpeg-on-centos

### MAKE VIRTUALENV ###
``` pip install virtualenv
virtualenv wBot
```

### INSTALL OTHER DEPENDENCIES ###
```cd wBot
source bin/activate
pip install package_name && pip freeze > requirements.txt
pip install -r requirements.txt
```

### Make sure before running you ###
```set the configurations in src/config.py
```
=== USER RUN GUIDE ===
 TO RUN:
```source bin/activate
python runWBot.py
```

## 实现功能 ##
* 验证消息"毛豆豆 我爱你", 自动添加好友
* 集成图灵聊天机器人
* 群聊天@毛豆豆 与机器人聊天
* 与机器人毛豆豆 单聊
* 集成百度语音识别
* 单聊中可识别语音消息 并互动聊天
* 可捕捉单聊、群聊撤回消息

