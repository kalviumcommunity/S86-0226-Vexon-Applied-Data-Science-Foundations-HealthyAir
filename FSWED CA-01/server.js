require('dotenv').config();
const express = require('express');
const app = express();
const mongoose = require('mongoose');

const mongoose.connect(mongoose.env.DB_URL)

.then(()=>{
    console.log('Mongodb is connected')
})
.catch(()=>{
    console.log('Mongodb connection is failed')
})

app.use(express.json());
const restaurantData =  require('./restaurant');
app.use('/restaurant')

const PORT = 8000
app.listen((PORT)=>{
    console.log(`server in running at ://localhost:${PORT}`)
})
