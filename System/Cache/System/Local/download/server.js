const { execSync } = require('child_process');

try {
  execSync('npm init -y && npm install express');
  console.log('Dependencies installed successfully');
  // Add your existing code here
} catch (error) {
  console.error(`Error installing dependencies: ${error.message}`);
}

const express = require('express');
const { exec } = require('child_process');
const { promisify } = require('util');

const app = express();
const port = 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.send('Local Server Is Up');
});

app.get('/clone/:owner/:repo', async (req, res) => {
  const { owner, repo } = req.params;
  const command = `cd /Users/maliq/PycharmProjects/GitAPI/GitHub-Package-Manager/System/.Cache/System/GitHub/Download_ && git clone https://github.com/${owner}/${repo}.git`;
  const commandv = `osascript -e 'display notification "Download Complete" with title "Download Complete: ${repo}"'`;
  const commandi = `osascript -e 'display notification "Connection Established" with title "Download started: ${repo}"'`;

  try {
    await promisify(exec)(commandi);
    const { stdout, stderr } = await promisify(exec)(command);

    if (stderr.includes('already exists and is not an empty directory')) {
      console.log('Already downloaded, not installed');
      res.send('Already downloaded, not installed');
    } else {
      await promisify(exec)(commandv);
      console.log('Commands executed successfully');
      res.send('Commands executed successfully');
    }
  } catch (error) {
    console.error(`Error executing commands: ${error.message}`);
    res.status(500).send(`Error executing commands: ${error.message}`);
  }
});

app.get('/status', (req, res) => {
  const status = {
    message: 'Server is running',
    timestamp: new Date().toISOString(),
  };
  res.json(status);
});

app.listen(port, 'localhost', () => {
  console.log('Server is running on http://localhost:3000');
});
