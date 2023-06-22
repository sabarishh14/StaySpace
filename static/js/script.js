// Function to handle button click events
function handleButtonClick() {
    var acButton = document.getElementById("acButton");
    var acCountInput = document.getElementById("acCountInput");

    

    if (acButton && acCountInput) {
      var acCount = 0; // Initialize the count
  
      acButton.addEventListener("click", function (e) {
        acCount++; // Increment the count on each button click
      });
    }
    var geyserButton = document.getElementById("geyserButton");
    var geyserCountInput = document.getElementById("geyserCountInput");
  
    if (geyserButton && geyserCountInput) {
      var geyserCount = 0; // Initialize the count
  
      geyserButton.addEventListener("click", function (e) {
        geyserCount++; // Increment the count on each button click
      });
    }
    var lockerButton = document.getElementById("lockerButton");
    var lockerCountInput = document.getElementById("lockerCountInput");
  
    if (lockerButton && lockerCountInput) {
      var lockerCount = 0; // Initialize the count
  
      lockerButton.addEventListener("click", function (e) {
        lockerCount++; // Increment the count on each button click
      });
    }
    var wifiButton = document.getElementById("wifiButton");
    var wifiCountInput = document.getElementById("wifiCountInput");
  
    if (wifiButton && wifiCountInput) {
      var wifiCount = 0; // Initialize the count
  
      wifiButton.addEventListener("click", function (e) {
        wifiCount++; // Increment the count on each button click
      });
    }
    var securityButton = document.getElementById("securityButton");
    var securityCountInput = document.getElementById("securityCountInput");
  
    if (securityButton && securityCountInput) {
      var securityCount = 0; // Initialize the count
  
      securityButton.addEventListener("click", function (e) {
        securityCount++; // Increment the count on each button click
      });
    }
    var commonButton = document.getElementById("commonButton");
    var commonCountInput = document.getElementById("commonCountInput");
  
    if (commonButton && commonCountInput) {
      var commonCount = 0; // Initialize the count
  
      commonButton.addEventListener("click", function (e) {
        commonCount++; // Increment the count on each button click
      });
    }

    var foodButton = document.getElementById("foodButton");
    var foodCountInput = document.getElementById("foodCountInput");
  
    if (foodButton && foodCountInput) {
      var foodCount = 0; // Initialize the count
  
      foodButton.addEventListener("click", function (e) {
        foodCount++; // Increment the count on each button click
      });
    }

    var searchWrapperButton = document.querySelector(".search-wrapper");
    if (searchWrapperButton) {
      searchWrapperButton.addEventListener("click", function (e) {
        // Assign the count value to the hidden input field
        acCountInput.value = acCount;
        geyserCountInput.value = geyserCount;
        lockerCountInput.value = lockerCount;
        commonCountInput.value = commonCount;
        wifiCountInput.value = wifiCount;
        securityCountInput.value = securityCount;
        foodCountInput.value = foodCount;
      });
    }
  }
  
  // Call the function when the DOM is ready
  document.addEventListener("DOMContentLoaded", handleButtonClick);
  