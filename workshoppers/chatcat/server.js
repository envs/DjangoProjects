'use strict';
// Import dependencies
const express = require('express');

// Instantiate the app object and set properties
const app = express();
app.set('port', process.env.PORT || 3000);
app.set('view engine', 'ejs');

// Basic Routes
app.get('/', (req, res, next) => {
    //res.send('<h1>Hello Express</h1>');
    //res.sendFile(__dirname + '/views/login.htm');
    res.render('login', {
        pageTitle: "My Login Page"
    });
});

// App listening on Port and Console output
app.listen(app.get('port'), ()=>{
    console.log('ChatCAT running on port: ', app.get('port'));
});