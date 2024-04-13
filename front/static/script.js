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
                } else {
                    displayResults(response); // display results using display function
                } 
            },
            error: function(xhr, status, error) {
                console.error(error);    
            }
        });
    });

    // Function to display the results
    function displayResults(data) {
        var searchResultsDiv = document.getElementById("search-results");
        searchResultsDiv.innerHTML = ""; // Clear previous results
        
        data.forEach(function(row) {
            console.log(row)
            var smithBox = document.createElement("div");
            smithBox.classList.add("smith-box");
            var id = row[0]


            // Create and append profile image
            var anchor = document.createElement("a");
            anchor.href = `http://localhost:8097/${id}`;
            anchor.target = "_blank";
            var image = document.createElement("img");
            image.src = "static/img/pfp.jpg";
            image.alt = "Smith";
            anchor.appendChild(image);
            smithBox.appendChild(anchor);

            // Create and append name
            var nameHeader = document.createElement("h3");
            nameHeader.classList.add("names");
            nameHeader.textContent = row[1] + " " + row[2];
            smithBox.appendChild(nameHeader);

            var table = document.createElement("table");

            // Create and append row for lived
            var livedRow = document.createElement("tr");
            var livedDataCell = document.createElement("td");
            livedDataCell.classList.add("lived");
            livedDataCell.textContent = `${row[6]} - ${row[7]}`;
            livedRow.appendChild(livedDataCell);
            table.appendChild(livedRow);

            //manually creating rows for each attribute
            var sexRow = document.createElement("tr");
            var sexDataCell = document.createElement("td");
            sexDataCell.textContent = row[3];
            sexRow.appendChild(sexDataCell);
            table.appendChild(sexRow);

            var nationalityRow = document.createElement("tr");
            var nationalityDataCell = document.createElement("td");
            nationalityDataCell.textContent = row[4].split(';')[0];
            nationalityRow.appendChild(nationalityDataCell);
            table.appendChild(nationalityRow);

            smithBox.appendChild(table);

            // Create and append button container
            var btnContainer = document.createElement("div");
            //btnContainer.classList.add("btn-container");

            //create and append learn more button
            var learnMoreButton = document.createElement("a");
            learnMoreButton.href = `http://localhost:8097/${id}`;
            learnMoreButton.classList.add("btn-container"); // Add container styling
            var button = document.createElement("button");
            button.classList.add("button");
            button.textContent = "Learn More";
            learnMoreButton.appendChild(button);
            smithBox.appendChild(learnMoreButton);
            searchResultsDiv.appendChild(smithBox);
        });
    }


    // Function to display a message when no results are found
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
