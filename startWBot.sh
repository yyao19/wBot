cd /root/wechat/wBot
source bin/activate
touch wbot.log
nohup python src/runWBot.py >> wbot.log 2>&1 &
sleep 1
ps -ef|grep runWBot
deactivate
