"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.funcHaddleLine = void 0;
const axios = require("axios");
const line = require("@line/bot-sdk");
const multer = require("multer");
const fs = require('fs');
const CHANNEL_ACCESS_TOKEN = "j1FFtqXACgtEm9QYI5EftbxabDfSP4QBLPuXrGZcpmfMQvuLcgxD124L2d7B87BEkWbmgca9ZLjMU97UXPxH0WZUzWTB8I02o8OYbrp8JdOrhV3Kdj83ulbGCcRbdoinVxbOM87Gl2UkqugZofsCEwdB04t89/1O/w1cDnyilFU=";
const CHANNEL_SECRET = "742379e90fc68902c8c89c8c4588130c";
const CONFIG = {
    channelAccessToken: CHANNEL_ACCESS_TOKEN,
    channelSecret: CHANNEL_SECRET
};
const LINE_CLIENT = new line.Client(CONFIG);
// const upload = multer({ dest: "uploads/" });
const funcHaddleLine = (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    console.log(req.body.events[0].message.type);
    const token = req.body.events[0].replyToken;
    let entropyColor = 0;
    let entropyShadow = 0;
    let netropyShape = 0;
    if (req.body.events[0].message.type === "image") {
        LINE_CLIENT.getMessageContent(req.body.events[0].message.id)
            .then((stream) => {
            stream.on('data', (chunk) => __awaiter(void 0, void 0, void 0, function* () {
                const buff = chunk.toString('base64');
                const warpImg = {
                    data: buff
                };
                try {
                    const valueColorEntropy = yield axios.post(`https://service-entropy-color-krmwbo4bhq-as.a.run.app/api/color_entropy`, warpImg);
                    // console.log(valueColorEntropy.data);
                    entropyColor = valueColorEntropy.data;
                }
                catch (err) {
                    console.log("pass");
                }
                try {
                    const valueColorShadow = yield axios.post(`https://service-entropy-shadow-krmwbo4bhq-as.a.run.app/api/shadows_entropy`, warpImg);
                    // console.log(valueColorShadow.data);
                    entropyShadow = valueColorShadow.data;
                }
                catch (err) {
                    console.log("pass");
                }
                try {
                    const valueColorShape = yield axios.post(`https://service-entropy-shape-krmwbo4bhq-as.a.run.app/api/shape_entropy`, warpImg);
                    // console.log(valueColorShape.data);
                    netropyShape = valueColorShape.data;
                }
                catch (err) {
                    console.log("pass");
                }
                if (entropyColor !== 0 && entropyShadow !== 0 && netropyShape !== 0) {
                    // console.log(entropyColor, entropyShadow, netropyShape)
                    const echo = `${entropyColor},\n${entropyShadow},\n${netropyShape}
                    `;
                    // console.log(echo);
                    // console.log(token)
                    const replyMsg = { type: 'text', text: echo };
                    // console.log(replyMsg)
                    return LINE_CLIENT.replyMessage(token, replyMsg);
                }
                else {
                    console.log("pass");
                }
            }));
            stream.on('error', (err) => {
                // console.log(err)
                // error handling
            });
        });
    }
    else {
        const replyMsg = { type: 'text', text: "ท่านสามารถถ่ายรูปห้องของท่านเพื่อคำนวณหาค่าความไม่เป็นระเบียบ." };
        return LINE_CLIENT.replyMessage(token, replyMsg);
    }
});
exports.funcHaddleLine = funcHaddleLine;
