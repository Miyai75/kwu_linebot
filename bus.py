# バスのバブルメッセージ
def busJson():
  busload = {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "市バスを利用しますか？プリンセスバスを利用しますか？",
            "weight": "regular",
            "size": "lg",
            "color": "#000000FF",
            "wrap": True,
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
              "label": "市バス",
              "text": "市バス"
            },
            "height": "sm",
            "style": "link"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "プリンセスバス",
              "text": "プリンセスバス"
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
  return busload

# print(busJson())