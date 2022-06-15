# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('ylZk3sAjJBfC72RR5AXBJm7TY0y7FYVf/3fCHwnyYgJzUGu7fkd5ihvQ5yVIUEP0Z3V9riEyTkaOQACfY5pqLrwYgRcW1RHdV/QJXjARNyI00ueOHcsJ2G5srzeRnNwcc5GdH2zSARAsycJl/PUzSwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a171123be2402984805c272aae2f1a61')
# 載入需要的模組
from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('ylZk3sAjJBfC72RR5AXBJm7TY0y7FYVf/3fCHwnyYgJzUGu7fkd5ihvQ5yVIUEP0Z3V9riEyTkaOQACfY5pqLrwYgRcW1RHdV/QJXjARNyI00ueOHcsJ2G5srzeRnNwcc5GdH2zSARAsycJl/PUzSwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('a171123be2402984805c272aae2f1a61')

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

if __name__ == "__main__":
    app.run()

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
