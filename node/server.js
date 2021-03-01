const { fstat } = require("fs");
var http = require("http");

var server = http.createServer(function(req, res){
    if (req.url === "/" ) {
        fs.readFile("./public/index.hmtl", "UTF-8", function(err, body){
            res.writeHead(200, {"Content-Type": "text/html"});
            res.end(body);
        });
    }
    else {
        res.writeHead(404, {"Content-Type":"text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }

});

server.listen(3000);
console.log("Server listening on port 3000");
