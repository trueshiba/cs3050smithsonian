document.addEventListener("DOMContentLoaded", function() {
    // Get the rating value from the HTML
    var rating = parseFloat(document.querySelector('.rating').textContent);
    
    // Call the generateStars function with the rating value
    generateStars(rating);
});

function generateStars(rating) {
    var starsContainer = document.querySelector('.rating-stars');
    
    // Clear previous stars
    starsContainer.innerHTML = '';

    // Calculate the number of stars based on the rating
    var numStars = Math.round(rating);

    // Generate filled stars
    for (var i = 0; i < numStars; i++) {
        var star = document.createElement("span");
        star.classList.add("star");
        star.style.backgroundImage = "url('star.png')"; // Set star image background
        starsContainer.appendChild(star);
    }
}
