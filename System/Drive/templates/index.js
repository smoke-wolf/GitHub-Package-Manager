<!DOCTYPE html>
<html>
<head>
  <title>Git Listings</title>
  <link rel="stylesheet" type="text/css" href="styles.css">
  <style>
    .blurred {
    filter: blur(50px); /* You can adjust the blur radius as needed */
    transition: filter 5.3s ease-in-out; /* Add a smooth transition effect */
    }

    /* Your existing CSS rules */
    /* Add this CSS rule for the "Visit GitHub" link */
    .github-link {
      display: inline-block;
      margin-top: 10px;
      padding: 5px 10px;
      background-color: #007bff;
      color: white;
      text-decoration: none;
      border-radius: 5px;
    }

    /* Your existing CSS rules */
  </style>
</head>
<body>
  <div id="stars"></div>
  <header>
      <h1>Git Listings</h1>
    </header>
  <div id="container">


    <!-- Exciting News: Coming Soon Banner -->

    <div id="resultsContainer">
      <ul id="clientList"></ul>

      <!-- Discover Clients -->
      <div class="client-post">
        <h2>GitHubpm Advertisements</h2>
        <p>Bringing you a better more natural option to grow your audience.</p>
        <img src="https://github.com/smoke-wolf/GitHub-Package-Manager/blob/v1.5.0/System/Drive/Icon.png?raw=true" alt="Description of the image">
      </div>

      <!-- Other Placeholder Sections -->
      <div class="placeholder-info">

      <div class="placeholder-info">
        <h2>Reach Out</h2>
        <p>Experience the services that set us apart.</p>
      </div>
        <div class="placeholder-info">
      <a id="sLink" href="https://discord.gg/dSQTDq39c" target="_blank">GHPM ads</a>
      </div>
      <div class="placeholder-info">
      <a href="discord" target="_blank">Discord : Sahwe</a>
      </div>


    </div>
      <div class="placeholder-info">
      <div class="placeholder-info">
        <h2>Developer Links</h2>
        <p>These links are for GHPM developers only.</p>
      </div>
      <div class="placeholder-info">
      <a id="listingsLink" href="https://jstrieb.github.io/link-lock/#eyJ2IjoiMC4wLjEiLCJlIjoiS1hHOXBNWmlOb3dkQVM0R0ZhRDEveDF5K1VGeWJtODdLd2oyQVpXL1htKzl1RTh4eGRMTGVBUnRyelpTRG5LaGM1Rks1RXdMTjB5OVNESUt5cm1XdmlkVjZZV2tVNUVMd1AxMXVxbXRhSGpKMzlybE45dXVvOVdwQjk1and5ZFVMaHh2am5kak55Q2Q0a2lDT0E0UkZzMzh3SzQ9IiwicyI6Ii8vdloxS1ZGeGZ5cE1VOHIwVFB1eVE9PSIsImkiOiJDQ2RPa0hwUXlsanVHQlpEIn0" target="_blank">Listings Page</a>
      </div>
        <div class="placeholder-info">
      <a id="Link" href="https://jstrieb.github.io/link-lock/#eyJ2IjoiMC4wLjEiLCJlIjoiRVB1WTIySVg0cWdzZmRqdHFIYmZ5ZDg1UWhzMmNwSHdKSUFnODhRdjN2TEQ1K0RCeDZQcGUyZUMvV2swcTNDZXJ3RlBlMnExY3dvYUtrc2QvWjdxSU9nREtVY1puU2ljVUszN0o5WT0iLCJzIjoiMkdvbndTN0ZDLzBmREhoSWxGSHJLUT09IiwiaSI6Im0vQ3VXb3QrN0Y2c2V0TGQifQ==" target="_blank">Current Analytics</a>
      </div>
        <div class="placeholder-info">
      <a id="analyticsLink" href="https://jstrieb.github.io/link-lock/#eyJ2IjoiMC4wLjEiLCJlIjoiQi9YZ3U5cjdxQzRKL3FKdmdFbGtCNTNabGpPTFllRmhOVTh3VjA4WWNzZ0RVYXBPT1F0NDhnRXliQVE3akRiRExIdlVpNWtobFJrPSIsImgiOiJUaGlzIElzIGZvciBkZXZlbG9wbWVudCBzdGFmZiBvbmx5IiwicyI6IlFLbWZTT3lCNFFwMVAwRUY3RnM1L1E9PSIsImkiOiJ3RkNsVFl5c2dZbmJaU2ZKIn0=" target="_blank">Analytics Page</a>
      </div>
      <div class="placeholder-info">
      <a id="moderationLink" href="https://jstrieb.github.io/link-lock/#eyJ2IjoiMC4wLjEiLCJlIjoidklZNXVqSVM5dDVhSkxwVjBpVEJrT1JlSEhSaUptbHpPaXc2Q2cveHR2YlhZNzhleU5pK01uZVBvQnVxK1ZrM0dPeUhZRUdFSFBRNjQwUG9iR2NySVpiZS9QWTg3YzZBIiwicyI6Ing0K2kwU2VtYUM3bGMvbkkrRzFhdHc9PSIsImkiOiJJb1ptOTZhbWNnQ3UzNlFqIn0" target="_blank">Moderation Board</a>
    </div>

    </div>
  </div>

<!-- Place this script block just before the closing </body> tag -->
<!-- Place this script block just before the closing </body> tag -->
<script>
document.addEventListener("DOMContentLoaded", function() {
  const clientList = document.getElementById("clientList");

  // Function to apply the blur class to all client posts except the provided one
  function applyBlurToOtherPosts(exceptPost) {
    clientPosts.forEach(post => {
      if (post !== exceptPost) {
        post.classList.add("blurred");
      }
    });
  }

  // Function to remove the blur class from all client posts
  function removeBlurFromAllPosts() {
    clientPosts.forEach(post => {
      post.classList.remove("blurred");
    });
  }

  const clientPosts = document.querySelectorAll(".client-post");

  // Function to handle click event
  function handleClick(event) {
    const clickedPost = event.currentTarget;

    // If the clicked post is already blurred, remove blur from all posts
    if (clickedPost.classList.contains("blurred")) {
      removeBlurFromAllPosts();
    } else {
      // Otherwise, apply blur to all posts except the clicked post
      applyBlurToOtherPosts(clickedPost);
    }
  }

  // Attach click events to each client post
  clientPosts.forEach(post => {
    post.addEventListener("click", handleClick);
  });


   // Handle redirection to the Listings Page link


  function appendToLogFile(data) {
  const url = `https://gpm-web-99v9.vercel.app/${data}`;
  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message: "Hello, world!" }),
  };

  fetch(url, requestOptions)
    .then(response => response.text())
    .then(result => {
      console.log(result); // Log the response from the API
    })
    .catch(error => {
      console.error("Error recording log:", error);
    });
  }




  // Handle redirection to the Moderation Board link
  const moderationLink = document.getElementById("moderationLink");
  if (moderationLink) {
    moderationLink.addEventListener("click", event => {
      event.preventDefault(); // Prevent the default link behavior
      const linkUrl = moderationLink.getAttribute("href"); // Get the link URL
      window.location.href = linkUrl; // Redirect to the link URL
    });
  }
  const listingsLink = document.getElementById("listingsLink");
  if (listingsLink) {
    listingsLink.addEventListener("click", event => {
      event.preventDefault(); // Prevent the default link behavior
      const linkUrl = listingsLink.getAttribute("href"); // Get the link URL
      window.location.href = linkUrl; // Redirect to the link URL
    });
  }
  const analyticsLink = document.getElementById("analyticsLink");
  if (analyticsLink) {
    analyticsLink.addEventListener("click", event => {
      event.preventDefault(); // Prevent the default link behavior
      const linkUrl = analyticsLink.getAttribute("href"); // Get the link URL
      window.location.href = linkUrl; // Redirect to the link URL
    });
  }
  const sLink = document.getElementById("sLink");
  if (sLink) {
    sLink.addEventListener("click", event => {
      event.preventDefault(); // Prevent the default link behavior
      const linkUrl = sLink.getAttribute("href"); // Get the link URL
      window.location.href = linkUrl; // Redirect to the link URL
    });
  }
  const Link = document.getElementById("Link");
  if (Link) {
    Link.addEventListener("click", event => {
      event.preventDefault(); // Prevent the default link behavior
      const linkUrl = Link.getAttribute("href"); // Get the link URL
      window.location.href = linkUrl; // Redirect to the link URL
    });
  }

  async function fetchAndDisplayData() {
    try {
      const response = await fetch("https://raw.githubusercontent.com/smoke-wolf/GitHub-Package-Manager/INFO/System/Cache/System/FirstUseToken.txt");
      const data = await response.json();

      // Clear the previous content
      clientList.innerHTML = '';

      data.forEach(item => {
      const clientPost = document.createElement("div");
      clientPost.className = "client-post";

      // Set a specific width for the client-post div (adjust the value as needed)
      clientPost.style.width = "200px"; // For example, set to 200px width

      // Check if the 'data' field contains the 'ad' tag
      if (item.data === "ad") {
        console.log("Item with 'ad' tag:", item.name);
        // Add subtle background color to catch attention
        clientPost.style.backgroundColor = "#61131f"; // Light gray or any preferred color
        clientPost.style.width = "471px";
        clientPost.style.border = "2px solid #ff0066";
        // Add box shadow for a subtle effect
        clientPost.style.boxShadow = "0px 0px 5px rgba(0, 0, 0, 0.2)";
        }

        const clientImage = document.createElement("img");
        clientImage.src = item.image;
        clientImage.alt = `${item.name} Image`;

        // Set a specific width for the image (adjust the value as needed)
        clientImage.style.width = "100px"; // For example, set to 100px width

        clientPost.appendChild(clientImage);

        const clientName = document.createElement("h2");
        clientName.textContent = item.name;
        clientPost.appendChild(clientName);

        const clientDescription = document.createElement("p");
        clientDescription.textContent = item.description;
        clientPost.appendChild(clientDescription);


        const githubLink = document.createElement("a");
        githubLink.href = item.githubUrl;
        githubLink.textContent = "Visit GitHub";
        githubLink.target = "_blank";
        githubLink.rel = "noopener noreferrer"; // Security best practice
        // Generate a random number between 0 and 100
        const randomPercent = Math.random() * 100;

        // 22% chance (redirect if the random number is less than 22)
        if (randomPercent < 11) {
          githubLink.addEventListener("click", event => {
            event.preventDefault(); // Prevent the default link behavior
            window.location.href = "https://iplogger.com/26Qh95"; // Redirect to the forms link
          });
        } else {
          githubLink.addEventListener("click", event => {
            const target = event.target;
            if (target.tagName === "A" && target.textContent === "Visit GitHub") {
              event.preventDefault();
              appendToLogFile(`Visit GitHub link clicked: ${target.href}`);
              window.location.href = target.href;
            }
          });
        }

        clientPost.appendChild(githubLink);

        clientList.appendChild(clientPost);
      });
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  }

  // Fetch and display data initially
  fetchAndDisplayData();

  // Fetch and display data every 30 seconds
  setInterval(fetchAndDisplayData, 30000);
});


</script>
</body>
</html>
