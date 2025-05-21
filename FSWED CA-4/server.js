const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const app = express();
const port = 3000;

dotenv.config();
app.use(express.json);

mongoose.connect(express.env.db_url)
.then(() => console.log( {'mongoDB is connected' }))
.catch(() => console.log( {'mongoDb is not connected'}));

const router = require('routes');
app.use('./router', router);

app.listen{(port) =>{
    console.log(`server is running on http//:localhost:${port}`)
}};


