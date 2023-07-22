// server // 
const express = require("express");
const cors = require("cors");

// controller // 
const {funcDebug} = require("../controller/controllerTest");

// router setup //
const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(cors());


// router // 
app.get("/api/debug",funcDebug);

export {app}

// server listen //
