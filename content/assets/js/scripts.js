var simulateClick = function (elem) {
	// Create our event (with options)
	var evt = new MouseEvent('click', {
		bubbles: true,
		cancelable: true,
		view: window
	});
	// If cancelled, don't dispatch our event
	var canceled = !elem.dispatchEvent(evt);
};

function addRowHandlers() {
  var table = [...document.querySelectorAll("table.clickable")];
  table.forEach((table) => {
     var rows = table.querySelectorAll("tbody tr");
     console.log(rows);
      for (i = 0; i < rows.length; i++) {
        var currentRow = table.rows[i+1];
        var createClickHandler = function(row) {
          return function() {
              var rows = [...table.querySelectorAll("tbody tr")];
              console.log(rows);
            rows.forEach((all_rows) => {
                if(all_rows != row) {
                    all_rows.classList.remove('active');
                }
            });

            row.classList.toggle('active');
          };
        };
        currentRow.onclick = createClickHandler(currentRow);
      }
  });
}

addRowHandlers();

var editButton = document.querySelectorAll('.box__actions .edit')[0];
if(editButton) {
    editButton.addEventListener('click', function() {
        currentEditLink = document.querySelectorAll('table tr.active .actions .edit');
        if(currentEditLink[0]) {
            simulateClick(currentEditLink[0]);
        } else {
            alert("Vorher bitte Element wählen!");
        }
    }, false);
}

var deleteButton = document.querySelectorAll('.box__actions .delete')[0];
if(deleteButton) {
    deleteButton.addEventListener('click', function() {
        currentDeleteLink = document.querySelectorAll('table tr.active .actions .delete');
         if(currentDeleteLink[0]) {
            simulateClick(currentDeleteLink[0]);
        } else {
            alert("Vorher bitte Element wählen!");
        }
    }, false);
}
