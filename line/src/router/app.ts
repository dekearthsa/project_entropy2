// server // 
const express = require("express");
const cors = require("cors");


// controller // 
const {funcDebug} = require("../controller/controllerTest");
const {funcHaddleLine} = require("../controller/controllerLine");

// router setup //
const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(cors());


// router // 
app.get("/api/debug",funcDebug);
app.post("/api/line", funcHaddleLine);

export {app}

// server listen //
