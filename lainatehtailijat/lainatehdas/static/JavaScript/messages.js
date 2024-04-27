document.addEventListener('DOMContentLoaded', function() {
    const popupContainer = document.getElementById('popupContainer');
    const popupMessage = document.getElementById('popupMessage');

    function showPopup(message, color) {
        popupMessage.textContent = message;
        popupMessage.style.backgroundColor = color;
        popupContainer.classList.remove('opacity-0');
        popupContainer.classList.add('opacity-100');
        setTimeout(function() {
            popupContainer.classList.remove('opacity-100');
            popupContainer.classList.add('opacity-0');
        }, 3000);
    }

    // Processing messages from Django
    if (djangoMessages) {
        djangoMessages.forEach(function(message) {
            if (message.tags) {
                if (message.tags.includes('normal')) {
                    showPopup(message.message, "rgb(34,197,94)");
                } else if (message.tags.includes('late')) {
                    showPopup(message.message, "rgb(251,191,36)");
                }
            }
        });
    }
});