const express = require('express');
const cors = require('cors');
const { promisify } = require('util');
const { exec } = require('child_process');

const app = express();
const port = 3000;

// Enable CORS for all routes
app.use(cors());

// Generate a random session key when the server starts
const sessionKey = generateSessionKey();

// Define the optional stepOver flag
const stepOver = false; // Change this value as needed

const bodyParser = require('body-parser');

// Parse incoming request data as JSON
app.use(bodyParser.urlencoded({ extended: true }));

// Function to generate a random session key
function generateSessionKey() {
  // Generate a random session key (you can use a more secure method)
  const randomBytes = require('crypto').randomBytes(16);
  return randomBytes.toString('hex');
}


// Middleware for authentication and authorization
app.use((req, res, next) => {
  const clientSessionKey = req.headers['x-session-key'];
  console.error(`SessionID: ${clientSessionKey}`);

  // Check if the stepOver flag is set to true
  if (stepOver) {
    next(); // Skip authentication and authorization if stepOver is true
  } else {
    // Check if the session key is provided in the request headers
    if (!clientSessionKey || clientSessionKey !== sessionKey) {
      // Use a callback-based approach for executing the notification command
      executeNotificationCommand((err) => {
        if (err) {
          console.error(`Error displaying notification: ${err.message}`);
        }
        res.status(401).json({ message: 'Unauthorized' });
      });
    } else {
      next();
    }
  }
});



// Function to execute the notification command
function executeNotificationCommand(callback) {
  const commandDisplayConnection = `osascript -e 'display notification "Request Blocked: Unauthorized" with title "GHPM Request"'`;
  const child = exec(commandDisplayConnection, (error) => {
    if (error) {
      callback(error);
    } else {
      callback(null);
    }
  });
}

app.get('/', (req, res) => {
  res.send('Local Server Is Up');
});


app.get('/clone/:owner/:repo', async (req, res) => {
  const { owner, repo } = req.params;

  // Define the variables here, initializing them to 'false' by default.
  const commandClone = `git clone https://github.com/${owner}/${repo}.git`;
  const launch = req.query.launch === 'true';
  const install = req.query.install === 'true';
  const uninstall = req.query.uninstall === 'true';
  const client = req.query.client === 'true';

  try {
    if (launch) {
      const commandDisplayConnection = `osascript -e 'display notification "Launching" with title "Beginning Activator"'`;
      await promisify(exec)(commandDisplayConnection);
      const currentWorkingDirectory = process.cwd();
      console.log(`Current Working Directory: ${currentWorkingDirectory}`);

      const commandDisplayConnection1 = `osascript -e 'tell application "Terminal" to do script "cd ${currentWorkingDirectory} && cd ..&& cd .. && cd .. && cd .. && cd .. &&python3 System/Drive/webkit/l.py"'`;
      await promisify(exec)(commandDisplayConnection1);
    }

    if (install) {
      const commandDisplayConnection = `osascript -e 'display notification "Launching" with title "Beginning Installer"'`;
      await promisify(exec)(commandDisplayConnection);
      const currentWorkingDirectory = process.cwd();
      console.log(`Current Working Directory: ${currentWorkingDirectory}`);

      const commandDisplayConnection1 = `osascript -e 'tell application "Terminal" to do script "cd ${currentWorkingDirectory} && cd ..&& cd .. && cd .. && cd .. && cd .. &&python3 System/Drive/webkit/l002.py"'`;
      await promisify(exec)(commandDisplayConnection1);
    }

    if (uninstall) {
      const commandDisplayConnection = `osascript -e 'display notification "Launching" with title "Beginning uninstaller"'`;
      await promisify(exec)(commandDisplayConnection);
      const currentWorkingDirectory = process.cwd();
      console.log(`Current Working Directory: ${currentWorkingDirectory}`);

      const commandDisplayConnection1 = `osascript -e 'tell application "Terminal" to do script "cd ${currentWorkingDirectory} && cd ..&& cd .. && cd .. && cd .. && cd .. &&python3 System/Drive/webkit/l003.py"'`;
      await promisify(exec)(commandDisplayConnection1);
    }

    if (client) {
      const commandDisplayConnection = `osascript -e 'display notification "Launching Client" with title ""'`;
      await promisify(exec)(commandDisplayConnection);
      const currentWorkingDirectory = process.cwd();
      console.log(`Current Working Directory: ${currentWorkingDirectory}`);

      const commandDisplayConnection1 = `osascript -e 'tell application "Terminal" to do script "cd ${currentWorkingDirectory} && cd ..&& cd .. && cd .. && cd .. && cd .. &&python3 Start.py"'`;
      await promisify(exec)(commandDisplayConnection1);
    }

    const { stdout, stderr } = await promisify(exec)(commandClone);
    const commandDisplayyConnection = `osascript -e 'display notification "Connection Established" with title "Download started: ${repo}"'`;
    await promisify(exec)(commandDisplayyConnection);
    if (stderr.includes('already exists and is not an empty directory')) {
      console.log('Already downloaded, not installed');
      res.send('Already downloaded, not installed');
    } else {
      if (launch) {
        await promisify(exec)(commandDisplayNotification);
      }
      console.log('Commands executed successfully');
      res.send('Commands executed successfully');
    }
  } catch (error) {
    console.error(`Error executing commands: ${error.message}`);
    res.status(500).send(`Error executing commands: ${error.message}`);
  }
});

// Exclude the /status route from session key authorization
app.get('/status', (req, res) => {
  const status = {
    message: 'Server is running',
    timestamp: new Date().toISOString(),
  };
  res.json(status);
});

app.listen(port, 'localhost', async () => {
  console.log(`Server is running on http://localhost:${port}`);
  console.log(`Session Key: ${sessionKey}`);
  const commandDisplayNotification = `osascript -e 'display notification "Session Key: ${sessionKey}" with title "Connected"'`;
  await promisify(exec)(commandDisplayNotification);
});
