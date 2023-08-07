const funcFlexHaddleEntropy = (entropyColor:string, entropyShadow:string, netropyShape:string) => {
  // console.log()
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
                "url": "https://i.ibb.co/hBRTs9v/Screenshot-2566-08-04-at-19-46-21.png",
                "size": "full",
            },
            {
                "type": "text",
                "text": "ระดับความรกคิดเป็น xx%",
                "align": "start",
                "contents": []
            },
            {
                "type": "text",
                "text": "Messy scale: xx",
                "align": "start",
                "contents": []
            },
            {
                "type": "text",
                "text": "Many scale: ",
                "align": "start",
                "contents": []
            },
            {
                "type": "text",
                "text": "ควรได้รับการจัดระเบียบ",
                "align": "start",
                "contents": []
            },
            {
                "type": "text",
                "text": "ควรได้รับการจัดระเบียบ",
                "align": "start",
                "contents": []
            },
            {
                "type": "text",
                "text": `entropy color: ${entropyColor}`,
                "align": "start",
                "contents": []
            },
            {
                "type": "text",
                "text": `entropy shadow: ${entropyShadow}`,
                "align": "start",
                "contents": []
            },
            {
                "type": "text",
                "text": `entropy shape: ${netropyShape}`,
                "align": "start",
                "contents": []
            },
            {
              "type": "text",
              "text": `!!! The value is in alpha test !!!`,
              "align": "center",
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
                  "type": "uri",
                  "label": "อยากลองจัดเอง",
                  "uri": "https://drive.google.com/file/d/1_AGQUowrZtI9ww9V2aEvlT9-Zy8kixJD/view?usp=sharing"
                },
            },
            {
              "type": "button",
              "action": {
                "type": "uri",
                "label": "จัดบ้านกับเรา",
                "uri": "https://forms.gle/weThZDcQyPiXAfkh8"  
              },
            }
          ]
        }
      }
}
export {funcFlexHaddleEntropy}