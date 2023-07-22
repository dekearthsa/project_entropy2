"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.app = void 0;
// server // 
const express = require("express");
const cors = require("cors");
// controller // 
const { funcDebug } = require("../controller/controllerTest");
// router setup //
const app = express();
exports.app = app;
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(cors());
// router // 
app.get("/api/debug", funcDebug);
// server listen //
