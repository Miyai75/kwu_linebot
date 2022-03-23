# 学生のバブルメッセージ
def gakusei:
    {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "学生生活に関して知りたいことは何ですか？",
        "weight": "regular",
        "size": "lg",
        "color": "#000000FF",
        "wrap": true,
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
          "label": "進路",
          "text": "進路"
        },
        "height": "sm",
        "style": "link"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "履修",
          "text": "履修"
        },
        "height": "sm",
        "style": "link"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "インターンシップ",
          "text": "インターンシップ"
        },
        "height": "sm"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "学費",
          "text": "学費"
        },
        "height": "sm"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "奨学金",
          "text": "奨学金"
        },
        "height": "sm"
      },
      {
        "type": "button",
        "action": {
          "type": "message",
          "label": "各種証明書",
          "text": "各種証明書"
        },
        "height": "sm"
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ]
  }
}
