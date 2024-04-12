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
            var smithBox = document.createElement("div");
            smithBox.classList.add("smith-box");

            // Create and append profile image
            var anchor = document.createElement("a");
            anchor.href = "http://localhost:8097/" + row[0];
            anchor.target = "_blank";
            var image = document.createElement("img");
            image.src = "static/pfp.jpg";
            image.alt = "Smith";
            anchor.appendChild(image);
            smithBox.appendChild(anchor);

            // Create and append name
            var nameHeader = document.createElement("h3");
            nameHeader.textContent = row[1] + " " + row[2];
            smithBox.appendChild(nameHeader);

            /* Create and append rating stars dynamically
            var ratingStarsDiv = document.createElement("div");
            ratingStarsDiv.classList.add("rating-stars");
            var rating = row[9];
            var numStars = Math.round(rating);
            for (var i = 1; i = numStars; i++) {
                var star = document.createElement("span");
                star.classList.add("star");
                ratingStarsDiv.appendChild(star);
            }
            smithBox.appendChild(ratingStarsDiv);*/

            // Create and append attributes table
            var table = document.createElement("table");
            var attributes = ["Sex", "Nationality", "Occupation", "Age"];
            for (var j = 3; j < 7; j++) {
                var row = document.createElement("tr");
                var header = document.createElement("th");
                header.textContent = attributes[j - 3] + ":";
                var dataCell = document.createElement("td");
                dataCell.textContent = row[j];
                row.appendChild(header);
                row.appendChild(dataCell);
                table.appendChild(row);
            }
            smithBox.appendChild(table);

            // Create and append learn more button
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
