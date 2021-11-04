// Gets called when the checkbox to delete a receiver is ticked
function handleDeleteReceiver() {
  var checkbox = document.getElementById('deleteReceiver');
  var disableableList = document.querySelectorAll('.disableable');

  // If 'delete' is ticked, grey/hide connection info forms
  if (checkbox.checked == true) {
    document.getElementById('submitUpdate').classList.add('invisible'); //hide update button
    document.getElementById('submitDelete').classList.remove('invisible'); //show delete button
    for (var i = 0, len = disableableList.length; i < len; ++i) { //loop through table
      disableableList[i].disabled = true;
    }
  } else { //if 'delete' is not ticked/unticked
    document.getElementById('submitUpdate').classList.remove('invisible'); //unhide update button
    document.getElementById('submitDelete').classList.add('invisible'); //hide delete button
    for (var i = 0, len = disableableList.length; i < len; ++i) { //loop through table
      disableableList[i].disabled = false;
    }
  }
}

document
  .getElementById('deleteReceiver')
  .addEventListener('click', handleDeleteReceiver, false);
