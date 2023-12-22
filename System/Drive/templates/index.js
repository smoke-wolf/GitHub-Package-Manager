// Function to display the clients
function displayClients() {
  const clientList = document.getElementById('clientList');
  clientList.innerHTML = '';

  const modules = [
    {
      name: 'GitHub Package Manager',
      description: 'Post Installation Github Resource 📦.',
      image: 'https://github.com/smoke-wolf/GitHub-Package-Manager/blob/v1.5.0/System/Drive/Icon.png?raw=true',
      githubUrl: 'https://github.com/smoke-wolf/GitHub-Package-Manager'
    },

    {
      name: 'Touch Script',
      description: '.touch is a lightweight and user-friendly scripting language designed to automate common tasks on your computer.',
      image: 'https://github.com/smoke-wolf/TouchScript/blob/main/Screen%20Shot%202023-08-24%20at%2011.58.32%20AM.png?raw=true',
      githubUrl: 'https://github.com/smoke-wolf/TouchScript'
    },
    {
      name: 'Alfred',
      description: 'Alfred is a advanced OSINT information gathering tool.',
      image: 'https://user-images.githubusercontent.com/105014217/263033253-04eb051d-15c3-4a32-b10b-dcdb12fee881.PNG',
      githubUrl: 'https://github.com/Alfredredbird/alfred'
    },
  ];

  modules.forEach(module => {
    const listItem = document.createElement('li');
    listItem.className = 'client';

    const clientImage = document.createElement('img');
    clientImage.src = module.image;
    clientImage.alt = module.name;
    clientImage.className = 'client-image';

    const clientDetails = document.createElement('div');
    clientDetails.className = 'client-details';

    const clientName = document.createElement('h2');
    clientName.textContent = module.name;
    clientName.className = 'client-name';

    const clientDescription = document.createElement('p');
    clientDescription.textContent = module.description;
    clientDescription.className = 'client-description';

    const downloadButton = document.createElement('a');
    downloadButton.href = module.githubUrl;
    downloadButton.textContent = 'visit';
    downloadButton.className = 'download-button';

    clientDetails.appendChild(clientName);
    clientDetails.appendChild(clientDescription);
    clientDetails.appendChild(downloadButton);

    listItem.appendChild(clientImage);
    listItem.appendChild(clientDetails);

    clientList.appendChild(listItem);
  });
}

// Display clients on page load
document.addEventListener('DOMContentLoaded', displayClients);

// Generate Shooting Stars
const starContainer = document.getElementById('stars');

function generateRandomStar() {
  const star = document.createElement('div');
  star.classList.add('star');

  // Random size
  const size = Math.random() * 6;
  star.style.width = `${size}px`;
  star.style.height = `${size}px`;

  // Random position
  const posX = Math.random() * 100;
  const posY = Math.random() * 100;
  star.style.left = `${posX}%`;
  star.style.top = `${posY}%`;

  // Random color
  const colors = ['#d17a28','#a15005','#d66331','#8a4f08','#c76734','#7a2c01'];;
  const color = colors[Math.floor(Math.random() * colors.length)];
  star.style.backgroundColor = color;

  // Random velocity
  const velocity = Math.random() * 10 + 5;
  star.style.setProperty('--trans-x', `${posX - 50}%`);
  star.style.setProperty('--trans-y', `${posY + 110 + velocity}vh`);
  star.style.animationDuration = `${Math.random() * 5 + 2}s`;

  starContainer.appendChild(star);
}

for (let i = 0; i < 150; i++) {
  generateRandomStar();
}

// Function to create explosion effect
function createExplosion() {
  const explosionContainer = document.getElementById('explosion');

  // Clear previous explosion
  explosionContainer.innerHTML = '';

  // Generate random number of stars for explosion
  const numStars = Math.floor(Math.random() * 30 + 20);

  for (let i = 0; i < numStars; i++) {
    const star = document.createElement('div');
    star.classList.add('star', 'explosion-star');

    // Random size
    const size = Math.random() * 6;
    star.style.width = `${size}px`;
    star.style.height = `${size}px`;

    // Random position within explosion container
    const posX = Math.random() * 100;
    const posY = Math.random() * 100;
    star.style.left = `${posX}%`;
    star.style.top = `${posY}%`;

    // Random color
    const colors = ['#d17a28', '#a15005', '#d66331', '#8a4f08', '#c76734', '#7a2c01'];
    const color = colors[Math.floor(Math.random() * colors.length)];
    star.style.backgroundColor = color;

    // Random velocity
    const velocity = Math.random() * 10 + 5;
    star.style.setProperty('--trans-x', `${posX - 50}%`);
    star.style.setProperty('--trans-y', `${posY + 110 + velocity}vh`);
    star.style.animationDuration = `${Math.random() * 2 + 0.5}s`;

    explosionContainer.appendChild(star);
  }

  // Show explosion for a short duration
  setTimeout(() => {
    explosionContainer.innerHTML = '';
  }, 2000);
}

// Add explosion effect on click
document.addEventListener('click', createExplosion);
