// Gets called when the HTML page is loaded
window.addEventListener(
  'load',
  // Function to select the flavor of the cable to update
  function () {
    // Get flavor dropdown list element
    var flavorDropdownElement = document.getElementById('flavorDropdown');
    // Get cable_to_update.flavor
    var cableToUpdateFlavor = flavorDropdownElement.getAttribute('data-flavor');
    // Get all available flavor options
    var flavorOptions = flavorDropdownElement.childNodes;
    // Loop through flavorOptions
    for (let i = 0; i < flavorOptions.length; i++) {
      // Check if the cable to update flavor is in options
      if (flavorOptions[i].innerHTML === cableToUpdateFlavor) {
        // Select option
        flavorOptions[i].selected = true;
      }
    }
  },
  false
);
