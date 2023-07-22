"use strict";
const { app } = require("./router/app");
const PORT = 8084;
app.listen(PORT, () => {
    console.log(`service line listen on port ${PORT}: http://localhost:${PORT}/api/debug`);
});
