document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("form");
    var queryInput = document.getElementById("query");
    var filterDropdown = document.getElementById("filter-dropdown-select");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        var query = queryInput.value;
        var filter = filterDropdown.value;

        var entries = {
            searchQuery: query,
            sortMethod: filter
        };

        console.log("Search Query:", query);
        console.log("Filter Choice:", filter);

        // Using AJAX to send data to flask
        $.ajax({
            type: "POST",
            url: "/search", // route to Flask search
            contentType: "application/json", 
            data: JSON.stringify(entries),
            success: function(response) {
                console.log(response); // print resulting html to console
                if (response.length === 0) { // if there are no results
                    displayNone(); //display a message that no results were found
                } 
                else {
                    displayResults(response); // display results using display function
                    } 
            },
            error: function(xhr, status, error) {
                console.error(error);    
            }
        });
    });
    // function to display the results
    function displayResults(data) {
        var searchResultsDiv = document.getElementById("search-results");
        searchResultsDiv.innerHTML = ""; // Clear previous results
        
        data.forEach(function(row) {
            var smithBox = document.createElement("div");
            smithBox.classList.add("smith-box");
    
            var anchor = document.createElement("a");
            anchor.href = "http://localhost:8097/" + row[0];
            anchor.target = "_blank";
            smithBox.appendChild(anchor);
    
            var image = document.createElement("img");
            image.src = "static/pfp.jpg";
            image.alt = "Smith";
            anchor.appendChild(image);
    
            var nameHeader = document.createElement("h3");
            nameHeader.textContent = row[1] + " " + row[2];
            smithBox.appendChild(nameHeader);
    
            var table = document.createElement("table");
            smithBox.appendChild(table);
    
            var idRow = document.createElement("tr");
            var idHeader = document.createElement("th");
            idHeader.textContent = "ID:";
            var idData = document.createElement("td");
            idData.textContent = row[0];
            idRow.appendChild(idHeader);
            idRow.appendChild(idData);
            table.appendChild(idRow);
    
            var sexRow = document.createElement("tr");
            var sexHeader = document.createElement("th");
            sexHeader.textContent = "Sex:";
            var sexData = document.createElement("td");
            sexData.textContent = row[3];
            sexRow.appendChild(sexHeader);
            sexRow.appendChild(sexData);
            table.appendChild(sexRow);
    
            var nationalityRow = document.createElement("tr");
            var nationalityHeader = document.createElement("th");
            nationalityHeader.textContent = "Nationality:";
            var nationalityData = document.createElement("td");
            nationalityData.textContent = row[4].split(';')[0];
            nationalityRow.appendChild(nationalityHeader);
            nationalityRow.appendChild(nationalityData);
            table.appendChild(nationalityRow);
    
            var learnMoreButton = document.createElement("a");
            learnMoreButton.href = "http://localhost:8097/" + row[0];
            var button = document.createElement("button");
            button.classList.add("button");
            button.textContent = "Learn More";
            learnMoreButton.appendChild(button);
            smithBox.appendChild(learnMoreButton);
    
            searchResultsDiv.appendChild(smithBox);
        });
    }
    

    function displayNone() {
        var searchResultsDiv = document.getElementById("search-results");
        searchResultsDiv.innerHTML = ""; // Clear previous results

        var none = document.createElement("h3"); //adding text indicating no results found
        none.textContent = "No results found.";
        none.style.color = "white";                 //changing text color and border for visibility
        none.style.textShadow = "2px 2px 0 black"; 
        searchResultsDiv.appendChild(none);

    
    }
}); 
