# 登下校のバブルメッセージ
def tougekou:
    {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "登校しますか？下校しますか？",
        "weight": "regular",
        "size": "lg",
        "color": "#000000FF",
        "contents": []
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "flex": 0,
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "登校",
          "text": "登校"
        },
        "height": "sm",
        "style": "link"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "下校",
          "text": "下校"
        },
        "height": "sm",
        "style": "link"
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ]
  }
}
