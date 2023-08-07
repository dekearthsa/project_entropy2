// // https://service-line-webhook-krmwbo4bhq-as.a.run.app/api/line // //
const axios = require("axios");
const line = require("@line/bot-sdk");
const {funcFlexHaddlePhoto} = require("../struct/flexHaddlePhoto");
const {funcFlexHaddleEntropy} = require("../struct/flexHaddleEntropy");
const fs = require('fs');
// const { Storage } =  require('@google-cloud/storage');
const {Datastore} = require('@google-cloud/datastore');
// const multer = require("multer");
// const fs = require('fs');

const datastore = new Datastore();
const CHANNEL_ACCESS_TOKEN = ""
const CHANNEL_SECRET = ""
const CONFIG = {
    channelAccessToken: CHANNEL_ACCESS_TOKEN,
    channelSecret: CHANNEL_SECRET
}

function downloadContent(messageId:string, downloadPath:string) {
    return LINE_CLIENT.getMessageContent(messageId)
      .then((stream:any) => new Promise((resolve, reject) => {
        const writable = fs.createWriteStream(downloadPath);
        stream.pipe(writable);
        stream.on('end', () => resolve(downloadPath));
        stream.on('error', reject);
      }));
  }

const LINE_CLIENT = new line.Client(CONFIG);
// const upload = multer({ dest: "uploads/" });

const funcHaddleLine = async (req: any, res: any) => {
    console.log(req.body.events[0].message);
    const messageId = req.body.events[0].message.id;
    const date = new Date();
    const ms = date.getTime();
    const setRdNum = String((Math.random() * 100000).toFixed(0))
    const token = req.body.events[0].replyToken;
    let entropyColor = 0;
    let entropyShadow = 0;
    let entropyShape = 0;
    const isActiveImageCalculate = true;
    try{
        const isDownloadPath = `image_${ms}_${setRdNum}.png`
        if(req.body.events[0].message.type === "image"){
            if(isActiveImageCalculate){
                let getContent = await downloadContent(messageId, isDownloadPath);
                // console.log(getContent);
                const fileBuff  = fs.readFileSync(getContent);
                const base64Data = fileBuff.toString('base64');
                // console.log(buff)
                const warpImg = {
                    data: base64Data
                }

                try{
                    const valueColorEntropy = await axios.post(`https://service-entropy-color-krmwbo4bhq-as.a.run.app/api/color_entropy`, warpImg);
                    // console.log("valueColorEntropy => ",valueColorEntropy.data);
                    entropyColor = valueColorEntropy.data?valueColorEntropy.data:'0';
                }catch(err){
                    console.log("valueColorEntropy", err);
                }
            
                try{
                    const valueColorShadow = await axios.post(`https://service-entropy-shadow-krmwbo4bhq-as.a.run.app/api/shadows_entropy`, warpImg);
                    // console.log("valueColorShadow => ",valueColorShadow.data);
                    entropyShadow = valueColorShadow.data?valueColorShadow.data:'0';
                    
                }catch(err){
                    console.log("entropyShadow", err);
                }
            
                try{
                    const valueColorShape = await axios.post(`https://service-entropy-shape-krmwbo4bhq-as.a.run.app/api/shape_entropy`, warpImg);
                    // console.log("valueColorShape => ",valueColorShape.data);
                    entropyShape = valueColorShape.data?valueColorShape.data:'0';
                }catch(err){
                    // console.log("pass");
                    console.log("entropyShape", err);
                }

                // if(Number(entropyColor) !== 0 && Number(entropyShadow) !== 0 && Number(entropyShape) !== 0){
                    // console.log("loop")
                    const kind = "result_calculate_v2"
                    const taskKey = datastore.key([kind]);
                    const task = {
                        key: taskKey,
                        excludeFromIndexes: ['img_base64'],
                        data: {
                            createTime: ms,
                            entropyShape: entropyShape,
                            entropyShadow:entropyShadow,
                            entropyColor: entropyColor,
                            img_base64:base64Data,
                            label: "-",
                            }
                        }
                    try{
                        await datastore.save(task)
                        // console.log("craed")
                    }catch(err){
                        console.log("datastore.save => ",err)
                    }
                // }
                
                fs.unlinkSync(getContent)
                const setFlex = funcFlexHaddleEntropy(entropyColor, entropyShadow, entropyShape);
                // console.log("setFlex => ",setFlex )
                const echo = { type: 'flex', altText: 'ทางเลือก', contents: setFlex }
                return LINE_CLIENT.replyMessage(token, echo);
            // }
            }else{
                const echo = {type: "text", text: "ขออภัยด้วยค่ะ ฟีเจอร์จะเปิดให้บริการเร็วๆนี้ ขอบคุณมากค่ะ"}
                return LINE_CLIENT.replyMessage(token, echo)
            }
        }else if(req.body.events[0].message.text === "ทดลองวัดความไม่เป็นระเบียบ"){
            const msg = `ขออภัยด้วยค่ะ ฟีเจอร์จะเปิดให้บริการเร็วๆนี้ ขอบคุณมากค่ะ`
            // const setFlex =  funcFlexHaddlePhoto();
            // const echo = { type: 'flex', altText: 'เปิดกล้อง', contents: setFlex }
            const echo = {type: 'text', text: msg};
            return LINE_CLIENT.replyMessage(token, echo);
        }else if(req.body.events[0].message.text === "วิธีการถ่ายรูป"){
            const replyMsg = {type: 'text', text: "ท่านสามารถเลือกตำแหน่งห้องที่ท่านต้องการถ่ายรูปโดยมีวิธีการดังต่อไปนี้ \n \n1.เปิดไฟภายในห้องให้สว่าง \n2.ถ่ายรูปในบริเวณที่ทั่วถึงห้อง"};
            return LINE_CLIENT.replyMessage(token, replyMsg);
        }
        else{
            const replyMsg = {type: 'text', text: "ท่านสามารถถ่ายรูปห้องของท่านเพื่อคำนวณหาค่าความไม่เป็นระเบียบ."};
            return LINE_CLIENT.replyMessage(token, replyMsg);
        }
    }catch(err){

    }
    
}

export {funcHaddleLine}

