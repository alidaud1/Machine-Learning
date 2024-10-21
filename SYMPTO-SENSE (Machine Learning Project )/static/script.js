function filterFeatures() {
    var input, filter, checkboxes, checkbox, label, parentDiv;
    input = document.getElementById("search");
    filter = input.value.toLowerCase();
    checkboxes = document.querySelectorAll("input[type='checkbox']");
    parentDiv = checkboxes[0].parentNode;

    var matchingItems = [];
    var nonMatchingItems = [];

    for (var i = 0; i < checkboxes.length; i++) {
        checkbox = checkboxes[i];
        label = document.querySelector('label[for="' + checkbox.id + '"]');
        
        if (label.textContent.toLowerCase().indexOf(filter) > -1) {
            matchingItems.push({checkbox: checkbox, label: label});
        } else {
            nonMatchingItems.push({checkbox: checkbox, label: label});
        }
    }

    parentDiv.innerHTML = "";

    for (var i = 0; i < matchingItems.length; i++) {
        parentDiv.appendChild(matchingItems[i].checkbox);
        parentDiv.appendChild(matchingItems[i].label);
    }

    for (var i = 0; i < nonMatchingItems.length; i++) {
        parentDiv.appendChild(nonMatchingItems[i].checkbox);
        parentDiv.appendChild(nonMatchingItems[i].label);
    }
}

function updateCheckedFeatures() {
    var checkedFeatures = document.getElementById("checkedFeatures");
    checkedFeatures.innerHTML = ""; // Clear previous content

    var checkboxes = document.querySelectorAll('input[type="checkbox"]:checked');
    checkboxes.forEach(function(checkbox) {
        var label = document.querySelector('label[for="' + checkbox.id + '"]').textContent;
        checkedFeatures.innerHTML += "<div>" + label + "</div>";
    });
}
