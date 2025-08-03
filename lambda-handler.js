exports.handler = async (event) => {
  const https = require('https');

  const options = {
    hostname: 'your-gcp-cloudrun-url.a.run.app',
    port: 443,
    path: '/',
    method: 'GET',
    headers: {
      'Authorization': 'Bearer YOUR_TOKEN'
    }
  };

  return new Promise((resolve, reject) => {
    const req = https.request(options, res => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve({ statusCode: 200, body: data }));
    });

    req.on('error', reject);
    req.end();
  });
};
