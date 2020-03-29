'use strict';

const http = require('http');
const url = require('url');
const qs = require("querystring")

let routes = {
    
    'GET': {
        '/': (req, res) => {
            res.writeHead(200, {'Content-type': 'text/html'});
            res.end('<h1>Hello Router</h1>');
        },
        '/about': (req, res) => {
            res.writeHead(200, {'Content-type': 'text/html'});
            res.end('<h1>This is the about page</h1>');
        },
        '/api/getinfo': (req, res) => {
            // fetch data from DB and respond as JSON
            res.writeHead(200, {'Content-type': 'application/json'});
            res.end(JSON.stringify(req.queryParams));
        }
    },
    'POST': {
        '/api/login': (req, res) => {       // still an imaginary api
            let body = '';
            // Listeners
            req.on('data', data => {        // If event contain data, capture it
                body += data;
                if (body.length > 2097152) {    // 2097152 is 2MB
                    res.writeHead(413, {'Content-type': 'text/html'});
                    res.end('<h3>The file being uploaded exceeds the 2MB limit</h3>', 
                        () => req.connection.destroy());
                }
            });
            req.on('end', () => {
                let params = qs.parse(body);
                console.log('Username: ', params['username']);
                console.log('Password: ', params['password']);
                // Query a DB to see if the user exists
                // If so, send a JSON response to the SPA
                res.end();
            });
        }
    },
    'NA': (req, res) => {
        res.writeHead(404);
        res.end('Content not found!');
    }
}

function router(req, res) {
    let baseURI = url.parse(req.url, true);
    let resolveRoute = routes[req.method][baseURI.pathname];
    if (resolveRoute != undefined) {
        req.queryParams = baseURI.query;
        resolveRoute(req, res);
    } else {
        routes['NA'](req, res);
    }
    
}

http.createServer(router).listen(3000, () => {
    console.log('Server running on port 3000');
});