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

        
 
    });
});