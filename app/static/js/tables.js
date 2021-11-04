// Filter - Submits the filter form
function submitForm() {
  // submits form
  document.getElementById('filterForm').submit();
}

// Filter - Controls submitting the form
// Gets called when the submit button is clicked
function btnFilterClick() {
  if (document.getElementById('datetime').checked) {
    //Datetime radio button is checked
    convertToGPStime();
  } else {
    //GPStime radio button is checked
    convertToDatetime();
  }
  // Delays submit to wait for datetime to gps conversion
  if (document.getElementById('filterForm')) {
    setTimeout('submitForm()', 1000); // set timout 1000 = 1sec
  }
}

// Filter - Date to gps timestamp conversion
function convertToGPStime() {
  var dateTime, unix, gps, floatField, offset;
  // Get the offset value
  offset = parseInt(document.getElementById('offset').innerHTML);
  // Get the value of the time field
  dateTime = document.getElementById('time').value;
  // convert the date to unix in seconds
  unix = new Date(dateTime).getTime() / 1000;
  // convert gps to unix
  gps = unix - offset;
  // Get the time_float field and set the value to gps
  floatField = document.getElementById('time_float');
  floatField.value = gps;
}

// Filter - GPS to date timestamp conversion
function convertToDatetime() {
  var gpsTime, dateTime, unixtime, datetimeField, offset;
  // Get the offset value
  offset = parseInt(document.getElementById('offset').innerHTML);
  // Get the value of the beigntime field
  gpsTime = document.getElementById('time_float').value;
  // convert the date to Unix in seconds
  unixtime = parseInt(gpsTime) + offset;
  // Convert from Unix to datetime
  dateTime = new Date(unixtime * 1000); // * 1000 to convert to milliseconds
  // Format dateTimeMonth
  dateTimeMonth = dateTime.getMonth() + 1;
  if (dateTimeMonth < 10) {
    dateTimeMonth = '0' + dateTimeMonth;
  }
  // Format dateTimeDate
  dateTimeDate = dateTime.getDate();
  if (dateTimeDate < 10) {
    dateTimeDate = '0' + dateTimeDate;
  }
  // Format dateTimeHours
  dateTimeHours = dateTime.getHours();
  if (dateTimeHours < 10) {
    dateTimeHours = '0' + dateTimeHours;
  }
  // Format dateTimeMinutes
  dateTimeMinutes = dateTime.getMinutes();
  if (dateTimeMinutes < 10) {
    dateTimeMinutes = '0' + dateTimeMinutes;
  }
  // Format dateTimeSeconds
  dateTimeSeconds = dateTime.getSeconds();
  if (dateTimeSeconds < 10) {
    dateTimeSeconds = '0' + dateTimeSeconds;
  }
  // Format dateTime to 'yyyy-MM-ddThh:mm');
  dateTime =
    dateTime.getFullYear() +
    '-' +
    dateTimeMonth +
    '-' +
    dateTimeDate +
    'T' +
    dateTimeHours +
    ':' +
    dateTimeMinutes +
    ':' +
    dateTimeSeconds;
  // Get the time field and set the value to dateTime
  datetimeField = document.getElementById('time');
  datetimeField.value = dateTime;
}

// Format datetime values (e.g., 8 -> 08)
function formatDateTime(datetime) {
  if (datetime < 10) {
    datetime = 0 + datetime;
  }
  return datetime;
}

// Filter - Shows GPS field and hides datetime field
// Gets called when gps radio button is checked
function gpstimeChecked() {
  var time = document.getElementById('time');
  var time_float = document.getElementById('time_float');
  time.type = 'hidden';
  time_float.type = 'number';
}

// Filter - Shows Datetime field and hides GPS field
// Gets called when datetime radio button is checked
function datetimeChecked() {
  var time = document.getElementById('time');
  var time_float = document.getElementById('time_float');
  time.type = 'datetime-local';
  time_float.type = 'hidden';
}

// Sort table (numbers only)
// Source(https://www.w3schools.com/howto/howto_js_sort_table.asp)
function sortTableNum(n) {
  var table,
    rows,
    switching,
    i,
    x,
    y,
    shouldSwitch,
    dir,
    switchcount = 0;
  table = document.getElementById('databaseTable');
  switching = true;
  // Set the sorting direction to ascending:
  dir = 'asc';
  /* Make a loop that will continue until
  no switching has been done: */
  while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /* Loop through all table rows (except the
    first, which contains table headers): */
    for (i = 1; i < rows.length - 1; i++) {
      // Start by saying there should be no switching:
      shouldSwitch = false;
      /* Get the two elements you want to compare,
      one from current row and one from the next: */
      x = rows[i].getElementsByTagName('TD')[n];
      y = rows[i + 1].getElementsByTagName('TD')[n];
      /* Check if the two rows should switch place,
      based on the direction, asc or desc: */
      if (dir == 'asc') {
        if (Number(x.innerHTML) > Number(y.innerHTML)) {
          //if so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      } else if (dir == 'desc') {
        if (Number(x.innerHTML) < Number(y.innerHTML)) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /* If a switch has been marked, make the switch
      and mark that a switch has been done: */
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      // Each time a switch is done, increase this count by 1:
      switchcount++;
    } else {
      /* If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again. */
      if (switchcount == 0 && dir == 'asc') {
        dir = 'desc';
        switching = true;
      }
    }
  }
}

// Sort table (begintime and endtime only)
// Source(https://www.w3schools.com/howto/howto_js_sort_table.asp)
function sortTableDate(n) {
  var table,
    rows,
    switching,
    i,
    x,
    y,
    shouldSwitch,
    dir,
    switchcount = 0;
  table = document.getElementById('databaseTable');
  switching = true;
  // Set the sorting direction to ascending:
  dir = 'asc';
  /* Make a loop that will continue until
  no switching has been done: */
  while (switching) {
    // Start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /* Loop through all table rows (except the
    first, which contains table headers): */
    for (i = 1; i < rows.length - 1; i++) {
      // Start by saying there should be no switching:
      shouldSwitch = false;
      /* Get the two elements you want to compare,
      one from current row and one from the next: */
      x = rows[i].getElementsByTagName('TD')[n];
      y = rows[i + 1].getElementsByTagName('TD')[n];
      x = x.getAttribute('data-time');
      y = y.getAttribute('data-time');
      /* Check if the two rows should switch place,
      based on the direction, asc or desc: */
      if (dir == 'asc') {
        if (Number(x) > Number(y)) {
          //if so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      } else if (dir == 'desc') {
        if (Number(x) < Number(y)) {
          // If so, mark as a switch and break the loop:
          shouldSwitch = true;
          break;
        }
      }
    }
    if (shouldSwitch) {
      /* If a switch has been marked, make the switch
      and mark that a switch has been done: */
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      // Each time a switch is done, increase this count by 1:
      switchcount++;
    } else {
      /* If no switching has been done AND the direction is "asc",
      set the direction to "desc" and run the while loop again. */
      if (switchcount == 0 && dir == 'asc') {
        dir = 'desc';
        switching = true;
      }
    }
  }
}

// Convert gps time to human readable time
function convertGPS(gpstime) {
  // Get the offset value
  var offset = parseInt(document.getElementById('offset').innerHTML);
  // Convert from GPS to Unix
  var unixtime = parseInt(gpstime) + offset;
  // Convert from Unix to datetime
  var dateTime = new Date(unixtime * 1000); // * 1000 to convert to milliseconds
  // return datetime as a string
  return dateTime.toUTCString();
}

// Gets called when the HTML page is loaded
window.addEventListener(
  'load',
  // Function to convert gps timestamps to datetime
  function () {
    // Begintimes
    var begintimes = document.querySelectorAll('.begintime');
    for (let i = 0; i < begintimes.length; i++) {
      let humanDate = convertGPS(begintimes[i].innerHTML);
      begintimes[i].innerHTML =
        humanDate + '<br>GPS: ' + begintimes[i].innerHTML;
    }
    // Endtimes
    var endtimes = document.querySelectorAll('.endtime');
    for (let i = 0; i < endtimes.length; i++) {
      if (endtimes[i].innerHTML != 9e99 && endtimes[i].innerHTML != 'None') {
        let humanDate = convertGPS(endtimes[i].innerHTML);
        endtimes[i].innerHTML = humanDate + '<br>GPS: ' + endtimes[i].innerHTML;
      }
    }
  },
  false
);
