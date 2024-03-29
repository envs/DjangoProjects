'use strict';
const http = require('http');
const url = require('url');
const fs = require('fs');
const path = require('path');

// Mime Types
let mimes = {
    '.htm': 'text/html',
    '.css': 'text/css',
    '.js': 'text/javascript',
    '.gif': 'image/gif',
    '.jpg': 'image/jpeg',
    '.png': 'image/png'
}

function fileAccess(filepath) {
    return new Promise( (resolve, reject) => {
        fs.access(filepath, fs.F_OK, error => {
            if (!error) {
                resolve(filepath);
            } else {
                reject(error);
            }
        });
    });
}

function streamFile(filepath) {
    return new Promise( (resolve, reject) => {
        let fileStream = fs.createReadStream(filepath);
        // Stream is an event emitter, and throws events like open,error, etc. which we would use below
        fileStream.on('open', () => {
            resolve(fileStream);
        });
        fileStream.on('error', () => {
            reject(error);
        });
    });
}

function webserver(req, res) {
    // if the route requested is '/', then load 'index.htm', else load the requested files
    let baseURI = url.parse(req.url);
    let filepath = __dirname + (baseURI.pathname === '/' ? '/index.htm' : baseURI.pathname);
    
    // Resolve the content type
    let contentType = mimes[path.extname(filepath)];

    // Chaining the Promises together
    fileAccess(filepath)
        .then(streamFile)
        .then(fileStream => {
            res.writeHead(200, {'Content-type': contentType});
            fileStream.pipe(res);   // this replace the res.end() because stream don't have end.
        })
        .catch(error => {
            res.writeHead(404);
            res.end(JSON.stringify(error));
        });
}

http.createServer(webserver).listen(3000, () => console.log('WebServer running on port 3000'));