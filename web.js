// Function to clear local storage
function clearLocalStorage() {
  localStorage.clear();
}

// Add an event listener for the beforeunload event
window.addEventListener("beforeunload", clearLocalStorage);


// Function to request the session token from the user
function requestSessionToken() {
  let existingToken = localStorage.getItem("sessionToken");
  
  // Check if a session token is already set
  if (existingToken) {
    const updateConfirmation = confirm("A session token is already set. Do you want to update it?");
    
    if (updateConfirmation) {
      // User wants to update the token
      let token = null;
      while (!token) {
        token = prompt('Please enter your updated session token:');
        if (token === null) {
          console.log('No session token provided.');
          return null; // Return null to indicate cancellation
        }
      }
      // Update the existing session token
      existingToken = token;
      localStorage.setItem('sessionToken', existingToken);
      console.log('Session token updated:', existingToken);
    }
  } else {
    // If no existing token or user didn't want to update, request a new token
    let token = null;
    while (!token) {
      token = prompt('Please enter your session token:');
      if (token === null) {
        console.log('No session token provided.');
        return null; // Return null to indicate cancellation
      }
    }
    // Store the session token in localStorage
    localStorage.setItem('sessionToken', token);
    console.log('Session token set:', token);
    existingToken = token;
  }

  return existingToken;
}

// Add click event handlers for the buttons
document.getElementById("activateButton1").addEventListener("click", function() {
  let sessionToken = requestSessionToken();
  if (sessionToken) {
    runCommandLocally('l02023', '43');
  }
});

document.getElementById("activateButton2").addEventListener("click", function() {
  let sessionToken = requestSessionToken();
  if (sessionToken) {
    runCommandLocally('l02024', '43');
  }
});

document.getElementById("activateButton3").addEventListener("click", function() {
  let sessionToken = requestSessionToken();
  if (sessionToken) {
    runCommandLocally('l02025', '43');
  }
});

document.getElementById("activateButton4").addEventListener("click", function() {
  let sessionToken = requestSessionToken();
  if (sessionToken) {
    runCommandLocally('l02026', '43');
  }
});



document.addEventListener("DOMContentLoaded", function() {
  var serverSettingsButton = document.getElementById("serverSettingsButton");
  var serverSettingsPage = document.getElementById("serverSettingsPage");
  var serverSettingsClose = document.getElementById("serverSettingsClose");

  serverSettingsButton.addEventListener("click", function() {
    serverSettingsPage.style.display = "block";
  });

  serverSettingsClose.addEventListener("click", function() {
    serverSettingsPage.style.display = "none";
  });

  window.addEventListener("click", function(event) {
    if (event.target === serverSettingsPage) {
      serverSettingsPage.style.display = "none";
    }
  });
});


document.getElementById("searchButton").addEventListener("click", function() {
  var searchInput = document.getElementById("searchInput").value;
  var xhr = new XMLHttpRequest();

  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
      var filteredRepositories = filterRepositories(response.items, searchInput);
      displayResults(filteredRepositories);
    }
  };

  xhr.open("GET", "https://api.github.com/search/repositories?q=" + searchInput, true);
  xhr.send();
});


// Define a variable to store the session token
let sessionToken = null;

// Function to request the session token from the user
function requestSessionToken() {
  const token = prompt('Please enter your session token:');
  if (token) {
    sessionToken = token;
    console.log('Session token set:', sessionToken);
  } else {
    console.log('No session token provided.');
  }
}


function filterRepositories(repositories, searchInput) {
  var filteredRepositories = repositories.filter(function(repository) {
    var fullName = repository.full_name.toLowerCase();
    var owner = repository.owner.login.toLowerCase();
    return fullName.includes(searchInput.toLowerCase()) || owner.includes(searchInput.toLowerCase());
  });

  filteredRepositories.sort(function(a, b) {
    // Sort by most stars
    var starsA = a.stargazers_count;
    var starsB = b.stargazers_count;
    if (starsA > starsB) {
      return -1;
    } else if (starsA < starsB) {
      return 1;
    } else {
      // If stars are equal, sort by most recent update
      var updatedAtA = new Date(a.updated_at).getTime();
      var updatedAtB = new Date(b.updated_at).getTime();
      return updatedAtB - updatedAtA;
    }
  });

  return filteredRepositories;
}

function displayResults(repositories) {
  var repositoryList = document.getElementById("repositoryList");
  repositoryList.innerHTML = "";

  repositories.forEach(function(repository) {
    var listItem = document.createElement("li");
    listItem.className = "repository";

    var header = document.createElement("div");
    header.className = "repository-header";

    var repoLink = document.createElement("a");
    repoLink.href = repository.html_url;
    repoLink.textContent = repository.full_name;

    var description = document.createElement("p");
    description.textContent = repository.description;
    if (description.textContent.length > 150) {
      description.textContent = description.textContent.substring(0, 150) + "...";
    }

    var arrowIcon = document.createElement("span");
    arrowIcon.className = "arrow-icon";

    var downloadButton = document.createElement("button");
    downloadButton.textContent = "Download & Install";
    downloadButton.classList.add("download-button");
    downloadButton.addEventListener("click", function() {
      runCommandLocally(repository.owner.login, repository.name, sessionToken);
    });

    header.appendChild(repoLink);
    header.appendChild(description);
    header.appendChild(arrowIcon);

    listItem.appendChild(header);
    listItem.appendChild(downloadButton);

    var readmeContent = document.createElement("div");
    readmeContent.className = "readme-content";
    listItem.appendChild(readmeContent);

    listItem.addEventListener("click", function() {
      toggleReadmeContent(readmeContent, repository.owner.login, repository.name);
    });

    repositoryList.appendChild(listItem);
  });
}

document.addEventListener("DOMContentLoaded", function() {
  // Load profile settings
  loadProfileSettings();

  var searchButton = document.getElementById("searchButton");
  searchButton.addEventListener("click", searchRepositories);
});

function loadProfileSettings() {
  // Fetch profile settings from storage or set default values
  var serverSetting = localStorage.getItem("downloadServer") || "http://localhost:3000";
  var serverInput = document.getElementById("serverInput");
  serverInput.value = serverSetting;

  // Save profile settings when input changes
  serverInput.addEventListener("change", function() {
    var newServerSetting = serverInput.value;
    localStorage.setItem("downloadServer", newServerSetting);
  });
}

function runCommandLocally(owner, repo) {
  // Check if the session token is already set in localStorage
  let sessionToken = localStorage.getItem("sessionToken");

  // If not set, prompt the user for the session token
  if (!sessionToken) {
    sessionToken = prompt("Please enter your session token:");

    if (!sessionToken) {
      // Handle case where the user cancels the prompt or provides no input
      console.error("Session token is required.");
      return;
    }

    // Store the session token in localStorage for future use
    localStorage.setItem("sessionToken", sessionToken);
  }

  var serverSetting = localStorage.getItem("downloadServer") || "http://localhost:3000";
  var url = `${serverSetting}/clone/${owner}/${repo}`;

  // Add a check for the owner value
  if (owner === 'l02023') {
    // If the owner is 'l02023', add the 'launch' query parameter to the URL
    url += '?launch=true';
  }
  if (owner === 'l02024') {
    // If the owner is 'l02023', add the 'launch' query parameter to the URL
    url += '?install=true';
  }
  if (owner === 'l02025') {
    // If the owner is 'l02023', add the 'launch' query parameter to the URL
    url += '?uninstall=true';
  }
  if (owner === 'l02026') {
    // If the owner is 'l02023', add the 'launch' query parameter to the URL
    url += '?client=true';
  }

  // Create headers to send the session token
  const headers = new Headers({
    'Content-Type': 'application/json',
    'x-session-key': sessionToken, // Send the session token in the headers
  });

  fetch(url, {
    method: 'GET', // Use GET method for your request
    headers: headers, // Attach the headers with the session token
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error(`Command execution failed: ${response.status}`);
      }
      return response.text();
    })
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.error(`Error: ${error.message}`);
    });
}



function toggleReadmeContent(contentElement, owner, repo) {
  if (contentElement.classList.contains("expanded")) {
    contentElement.innerHTML = "";
    contentElement.classList.remove("expanded");
  } else {
    contentElement.innerHTML = "<em>Loading README...</em>";

    // Fetch the README content
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          contentElement.innerHTML = xhr.responseText;
        } else {
          contentElement.innerHTML = "<em>Failed to load README.</em>";
        }
      }
    };

    xhr.open("GET", `https://api.github.com/repos/${owner}/${repo}/readme`, true);
    xhr.setRequestHeader("Accept", "application/vnd.github.VERSION.html");
    xhr.send();

    contentElement.classList.add("expanded");
  }
}

document.addEventListener("DOMContentLoaded", function() {
  var modal = document.getElementById("readmeModal");
  var closeModal = document.getElementsByClassName("close")[0];

  closeModal.addEventListener("click", function() {
    modal.style.display = "none";
  });

  window.addEventListener("click", function(event) {
    if (event.target === modal) {
      modal.style.display = "none";
    }
  });
});

document.addEventListener("DOMContentLoaded", function() {
  var profileButton = document.getElementById("profileButton");
  var profilePage = document.getElementById("profilePage");
  var closeButton = profilePage.querySelector(".close");
  var serverStatus = document.getElementById("serverStatus");

  profileButton.addEventListener("click", function() {
    profilePage.style.display = "block";
    loadProfileData();
  });

  closeButton.addEventListener("click", function() {
    profilePage.style.display = "none";
  });

  function loadProfileData() {
    // Get user IP
    fetch("https://api.ipify.org/?format=json")
      .then(response => response.json())
      .then(data => {
        var userIP = document.getElementById("userIP");
        userIP.textContent = "User IP: " + data.ip;
      })
      .catch(error => {
        console.error("Error getting user IP:", error);
      });

    // Get download count (replace with your own logic to fetch download count)
    var downloadCount = document.getElementById("downloadCount");
    downloadCount.textContent = "Download Count: 0"; // Replace 0 with actual download count

    // Check server status
    checkServerStatus(serverStatus);
  }

  function checkServerStatus() {
  var serverUrl = "http://localhost:3000/status"; // Replace with your server URL

  fetch(serverUrl)
    .then(response => {
      if (response.status === 200) {
        return response.json(); // Parse the response as JSON
      } else {
        throw new Error("Server response was not OK");
      }
    })
    .then(data => {
      serverStatus.textContent = "Server Status: Online";
    })
    .catch(error => {
      serverStatus.textContent = "Server Status: Offline";
    });
}


  // Initial load of profile data
  loadProfileData();
});


$(document).ready(function() {
  // Profile Button Click Event
  $('#profileButton').click(function() {
    $('#profilePage').toggleClass('active');
    $('#container').toggleClass('background-fade');
  });

  // Close Button Click Event
  $('.close').click(function() {
    $('#profilePage').removeClass('active');
    $('#container').removeClass('background-fade');
  });
});


// Update profile values
document.addEventListener("DOMContentLoaded", function() {
  // Get user IP (replace with your logic to retrieve the user IP)
  var userIP = "123.456.789.0"; // Replace with the actual user IP value
  var userIPElement = document.getElementById("userIP");
  userIPElement.textContent = "User IP: " + userIP;

  // Get download count (replace with your logic to fetch the download count)
  var downloadCount = 100; // Replace with the actual download count value
  var downloadCountElement = document.getElementById("downloadCount");
  downloadCountElement.textContent = "Download Count: " + downloadCount;

  // Check server status
  checkServerStatus()
    .then((status) => {
      var serverStatus = status ? "Online" : "Offline";
      var serverStatusElement = document.getElementById("serverStatus");
      serverStatusElement.textContent = "Server Status: " + serverStatus;
    });
});
