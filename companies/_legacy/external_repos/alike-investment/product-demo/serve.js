const http = require('http');
const fs = require('fs');
const path = require('path');

const port = process.env.PORT || 3456;
const dir = __dirname;
const mime = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'application/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon'
};

http.createServer((req, res) => {
  let url = req.url === '/' ? '/index-ye.html' : req.url;
  url = decodeURIComponent(url.split('?')[0]);
  const fp = path.join(dir, url);

  fs.readFile(fp, (err, data) => {
    if (err) {
      res.writeHead(404);
      res.end('Not found');
      return;
    }
    const ext = path.extname(fp);
    res.writeHead(200, { 'Content-Type': mime[ext] || 'application/octet-stream' });
    res.end(data);
  });
}).listen(port, () => {
  console.log(`Serving on http://localhost:${port}`);
});
