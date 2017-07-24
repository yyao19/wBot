# -*- coding: utf-8 -*-
from wxpy import *
import config as config
import re


class WBot(object):
    def __init__(self):
        self.bot = Bot(True, 2)
        self.bot.messages.max_history = config.MAX_HISTORY
        self.tuling = Tuling(api_key=config.TULING_API_KEY)

    def run(self):
        self.auto_reply_tuling_robot()
        self.auto_accept_friends()
        self.recalled_message_helper()
        embed()

    def auto_reply_tuling_robot(self):
        """
        注册图灵机器人聊天对象
        单聊回复
        群聊@回复
        
        Message Type: TEXT
        :return: 
        """
        @self.bot.register(msg_types=TEXT)
        def auto_reply(msg):
            if isinstance(msg.chat, Group) and not msg.is_at:
                return
            else:
                ret = self.tuling.reply_text(msg, True)
                ret = ret.replace(u'图灵机器人', self.bot.self.nick_name)
                msg.reply(ret)

    def auto_accept_friends(self):
        """
        自动接收好友申请
        备注信息需包含 微信昵称 和 '我爱你'
        
        Message Type: FRIENDS
        :return: 
        """
        @self.bot.register(msg_types=FRIENDS)
        def auto_accept(msg):
            if self.bot.self.nick_name in msg.text and u'我爱你' in msg.text:
                new_friend = self.bot.accept_friend(msg.card)
                welcome_msg = new_friend.nick_name + u', 我也爱你！么么哒！'
                new_friend.send(welcome_msg)

    def recalled_message_helper(self):
        """
        对撤回的消息进行处理
        
        Message Type: NOTE
        :return: 
        """
        @self.bot.register(msg_types=NOTE)
        def auto_display(msg):
            msg_content = msg.raw.get('Content')
            if re.search(u'<!\[CDATA\[.*撤回了一条消息\]\]>', msg_content) is not None:
                recalled_msg_id = re.search(u'<msgid>(.*?)</msgid>', msg_content).group(1)
                recalled_msg = self._search_message_by_id(recalled_msg_id)
                if recalled_msg.type == TEXT:
                    if isinstance(msg.chat, Friend):
                        text_msg = recalled_msg.sender.nick_name + \
                                   u' 撤回了一条消息：' + self._message_truncation(recalled_msg.text)
                    elif isinstance(msg.chat, Group):
                        text_msg = recalled_msg.raw.get('ActualNickName') + \
                                   u' 撤回了一条消息：' + self._message_truncation(recalled_msg.text)
                    msg.reply(text_msg)

    def _search_message_by_id(self, message_id):
        """
        从缓存历史消息中根据消息ID查询消息
        
        :return: 
        """
        for msg in self.bot.messages:
            if message_id == str(msg.id):
                return msg
        return None

    @staticmethod
    def _message_truncation(msg):
        """
        消息长度截取，避免消息过长 产生炸群嫌疑
        
        :param msg: 
        :return: 
        """
        message = u''
        if msg and len(msg) > config.MESSAGE_LENGTH:
            message = msg[0:config.MESSAGE_LENGTH] + u'...'

        return message
