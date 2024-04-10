document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("rate");
    var rating = document.getElementById("rate-dropdown");
    var review = document.getElementById("reviw");

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

        // Using AJAX to send data to flask
        $.ajax({
            type: "POST",
            url: "/rate", // route to Flask search
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