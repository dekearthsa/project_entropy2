const funcFlexHaddlePhoto = () => {
    return  {
        "type": "bubble",
        "direction": "ltr",
        // "hero": {
        //     "type": "image",
        //     "url": "https://i.ibb.co/2F6ttJX/Group-834.png",
        //     "size": "full",
        // },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
                "type": "image",
                "url": "https://i.ibb.co/2F6ttJX/Group-834.png",
                "size": "full",
            },
            {
                "type": "text",
                "text": "ทำการถ่ายรูปห้อง",
                "align": "center",
                "gravity": "center",
                "contents": []
            },
            {
                "type": "text",
                "text": "เพื่อดูระดับความไม่เป็นระเบียบ",
                "align": "center",
                "gravity": "center",
                "contents": []
            },
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
                "type": "button",
                "action": {
                  "type": "message",
                  "label": "วิธีการถ่ายรูป",
                  "text": "วิธีการถ่ายรูป"
                },
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "เปิดกล้องเพื่อถ่ายรูป",
                "uri": "https://line.me/R/nv/camera/"  
              },
            }
          ]
        }
      }
}

export {funcFlexHaddlePhoto}