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
                if (response == ""){
                    displayNone()
                }
                displayResults(response); // display results using display function
            },
            error: function(xhr, status, error) {
                console.error(error);    
            }
        });
    });
    // function to display the results
     function displayResults(data) {
    
        var searchResultsDiv = document.getElementById("search-results");
        searchResultsDiv.innerHTML = ""; // clear html

        // loop thru list elements and format them 
            data.forEach(function(row) {
                var smithBox = document.createElement("div");
                smithBox.classList.add("smith-box");
        
                var image = document.createElement("img");
                image.src = "static/pfp.jpg";
                image.alt = "Smith";
                smithBox.appendChild(image);

                var nameHeader = document.createElement("h3");
                nameHeader.textContent = row[1] + " " + row[2];
                smithBox.appendChild(nameHeader);

                var detailsParagraph = document.createElement("p");
                detailsParagraph.textContent = "Sex: " + row[3] + ", Nationality: " + row[4];
                smithBox.appendChild(detailsParagraph);
        
                searchResultsDiv.appendChild(smithBox);
        });
    }

    function displayNone() {
        var stp = document.createElement("h3");
        nameHeader.textContent = "No results found.";
    }
}); 