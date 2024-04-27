function toggleReservations(yearMonth) {
    var buttonContainer = document.querySelector('#button-' + yearMonth).closest('.button-container');
    var reservations = document.getElementById('reservations-' + yearMonth);
    
    if (reservations.classList.contains('hidden')) {
      // Open the reservations list smoothly
      reservations.classList.remove('hidden');
      reservations.style.maxHeight = reservations.scrollHeight + "px";
      buttonContainer.classList.add('bg-gray-400');
      buttonContainer.classList.remove('bg-blue-500');
    } else {
      
      // Close the reservations list smoothly
      reservations.style.maxHeight = "0";
      buttonContainer.classList.remove('bg-gray-400');
      buttonContainer.classList.add('bg-blue-500');
      reservations.addEventListener('transitionend', function() {
        reservations.classList.add('hidden');
      }, { once: true });
    }
  }