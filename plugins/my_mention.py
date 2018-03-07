# coding: utf-8
import sys ,os
sys.path.append( os.pardir )

from slackbot.bot import respond_to     # @botname: で反応するデコーダ
from slackbot.bot import default_reply

from plugins.docomo_dialogue import DdialogueDriver

# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」

ddialogue = DdialogueDriver()

@default_reply()
def question_talk( message ):
    text = message.body['text']
    ddialogue.listen( text )
    # 表示
    message.reply( "%s" % ddialogue.speak())
