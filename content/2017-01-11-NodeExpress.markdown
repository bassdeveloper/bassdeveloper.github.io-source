Title: Onboard the Node Express
Date: 2017-01-23 16:00
Modified: 2017-01-23 16:00
Category: Learning
Tags: Node, JS, Express
Slug: node-xpress
Authors: Rishabh Chakrabarti
Summary: Conversations summary from the documentation.

# All aboard!

Express is a minimal and flexible Node.js web application framework that providesa robust set of features to develop web and mobile applications. It facilitates the rapid development.

**Server.js file**
This file is used to run the whole application. It hosts a server and listens to it on a particular port.

## Request & Response
Express application uses a callback function whose parameters are **request** and **response** objects:

```javascript
app.get('/', function (req, res) {
   // --
})
```
 * **Request Object** : The request object represents HTTP request and has properties for the request query string, parameters, body, HTTP headers and so on..
 * **Response Object** : The response object represents the HTTP response that an Express app sends when it gets an HTTP request.

You can print **req** and **res** objects which provide a lot of information related to HTTP request and response including cookies, sessions, URl, etc.

## Basic Routing:

Routing refers to determining how an applicatoin responds to a client request to a particular endpoint, which is a URI ( or path) and a specific HTTP request method (GET, POST, and so on)

```js
var express = require('express');
var app = express();

// This responds with "Hello World" on the homepage
app.get('/', function (req, res) {
   console.log("Got a GET request for the homepage");
   res.send('Hello GET');
})

// This responds a POST request for the homepage
app.post('/', function (req, res) {
   console.log("Got a POST request for the homepage");
   res.send('Hello POST');
})

// This responds a DELETE request for the /del_user page.
app.delete('/del_user', function (req, res) {
   console.log("Got a DELETE request for /del_user");
   res.send('Hello DELETE');
})

// This responds a GET request for the /list_user page.
app.get('/list_user', function (req, res) {
   console.log("Got a GET request for /list_user");
   res.send('Page Listing');
})

// This responds a GET request for abcd, abxcd, ab123cd, and so on
app.get('/ab*cd', function(req, res) {   
   console.log("Got a GET request for /ab*cd");
   res.send('Page Pattern Match');
})

var server = app.listen(8081, function () {

   var host = server.address().address
   var port = server.address().port

   console.log("Example app listening at http://%s:%s", host, port)
})
```
