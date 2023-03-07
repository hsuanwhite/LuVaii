from flask import Flask
from flask import request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

linebot_api = LineBotApi('qjm1/50yBH8MgR3Dv6XtN40Mzq5XPGMQmenKqnl0EhIlPg44lyV56GL4FzbUN8wHYZ85Bc1KoGkOzes3YZpIkNspz/FxdRFoDpE8QTYd/n1zab6/+dO1bBaxiSc0sU6pYM5GyR+rDsbQZSki8OP3bwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e9181648daab45e00fdbe57b0994ca68')

@app.route('/callback', methods=['POST'])

def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text = True)
#     print ("BODY", body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handler_message(event):
    input_str = event.message.text
    print (input_str)
    if input_str == "我要預約":
        linebot_api.reply_message(event.reply_token, TextSendMessage(text="請選擇預約時間"))
    else:
        linebot_api.reply_message(event.reply_token, TextSendMessage(text=event.message.text))
    
if __name__ == '__main__':
    print ("hihi~111")
    app.run()
