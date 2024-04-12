document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("form");
    var rating = document.getElementById("rate-select");
    var review = document.getElementById("review");
    var idElement = document.getElementById("smith-id"); 
    var id = idElement.value

    console.log("ID: ", id, "\n")
    form.addEventListener("submit", function(event) {
        event.preventDefault();

        var rat = rating.value;
        var rev = review.value;

        var entries = {
            rating5: rat,
            reviewWritten: rev
        };

        console.log("rating:", rat);
        console.log("review:", rev);
        console.log("ID: ", id)

        // Using AJAX to send data to flask
        $.ajax({
            type: "POST",
            url: "/rate/" + id, // route to Flask search
            contentType: "application/json", 
            data: JSON.stringify(entries),
            success: function(response) {
                console.log(response); // print resulting html to console
                // auto reload page here?
                window.location.reload()
            },
            error: function(xhr, status, error) {
                console.error(error);    
            }
        });
    });
});