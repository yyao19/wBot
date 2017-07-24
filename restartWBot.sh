cd /root/wechat/wBot
WBOT_LOC=`date +wbot.log-%m-%d`

mv wbot.log logs/$WBOT_LOC
kill `ps -ef|grep '/runWBot.py'|awk '!/awk/ && !/grep/ {print $2}'`

/root/wechat/wBot/startWBot.sh
