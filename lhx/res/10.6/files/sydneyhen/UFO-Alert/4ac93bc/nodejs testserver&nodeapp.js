// Web Services for Huzzah Test project
// Runs on Node.JS (used version was 4.2.6)
// you need to run in the folder where the web files such as index.html are the command "npm install node-static"


var http = require('http');
var static = require('node-static');
var fileServer = new static.Server('./');
var url = require('url');

function randomInt (low, high) {
    return Math.floor(Math.random() * (high - low) + low);
}

http.createServer(function (request, response) {
	var parsedUrl = url.parse(request.url);
	var query = url.parse(request.url, true).query;
	console.log(parsedUrl.path);
	console.log(parsedUrl.pathname);
	console.log(parsedUrl.query);
	console.log("query: " + query);
	if(parsedUrl.pathname === "/api") {
     	console.log("acessing api! " + query);
		/*if (query.led == "on") {
			console.log("turn LED ON");
		} else {
			console.log("turn LED off!!!");
		}*/
		response.write("<html><body>sepperl greets from node js</body></html>");
		response.end();
	} else 	if(parsedUrl.pathname === "/info") {
		response.setHeader('Content-Type', 'text/json');
		response.setHeader('cache-control', 'private, max-age=0, no-cache, no-store')
		response.write('{ "ssid": "testssid", "ipaddress": "10.10.10.10", "heap": "' + randomInt(2000, 50000) + '"}');
		response.end();
	} else {
		request.addListener('end', function () {
		   fileServer.serve(request, response, function (err, result) {
				if (err) { // There was an error serving the file
					console.error("Error serving " + request.url + " - " + err.message);

					// Respond to the client
					response.writeHead(err.status, err.headers);
					response.end();
				}
			});

		}).resume();
	}
}).listen(80);

/**
http.createServer(function(request, response) {
	  var body = [];
	  request.on('data', function(chunk) {
		body.push(chunk);
	  }).on('end', function() {
		body = Buffer.concat(body).toString();
		body="<html><body>sepperl greets from node js</body></html>";
		response.end(body);
	  });
}).listen(80); **/