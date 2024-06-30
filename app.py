from flask import Flask, request, abort
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, ReplyMessageRequest, TextMessage
from linebot.v3.webhooks import MessageEvent, TextMessageContent

app = Flask(__name__)

configuration = Configuration(access_token='wWVOtzSlJUIqvp08utM8UZ49PCnDKD36LLTScL/eO0VwTNIQj1RAqc8JazzEmocyAs56fs78Ww7GxT6E7E7IJzUaVNQyQ0liLK41wmG/Dd4S7w/dhFEV26zz3xvjuq3Fwctt45n3Wcr0f8Z5pvaKZAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d566b3af8cc3ac52bda02a020c740d8f')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
    
    