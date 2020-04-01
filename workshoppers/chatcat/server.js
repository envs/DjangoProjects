'use strict';
// Import dependencies
const express = require('express');

// Instantiate the app object and set properties
const app = express();
const chatCat = require('./app');

app.set('port', process.env.PORT || 3000);
app.use(express.static('public'));          // Serve static files
app.set('view engine', 'ejs');

app.use('/', chatCat.router);

// App listening on Port and Console output
app.listen(app.get('port'), ()=>{
    console.log('ChatCAT running on port: ', app.get('port'));
});