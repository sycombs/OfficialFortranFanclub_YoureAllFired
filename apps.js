const hostname = '127.0.0.1';
const port = 3000;

var http = require('http');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  //Return the url part of the request object:
  res.write(req.url);
  console.log("Winter ripost");
  res.end();
}).listen(8080);


getData = function() {
  return "Ayyyy";
}
