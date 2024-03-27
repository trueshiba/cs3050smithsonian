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
            url: "/search", //route to flask search
            contentType: "application/json", 
            data: JSON.stringify(entries),
            success: function(response) {
                console.log(response); //log response in console
                
            },
            error: function(xhr, status, error) {
                console.error(error); 
            }
        });
    });
});