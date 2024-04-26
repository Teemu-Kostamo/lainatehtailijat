document.getElementById('searchInput').addEventListener('input', function() {
    var searchInput = this.value.toLowerCase();
    var itemList = document.getElementById('itemList');
    var items = itemList.querySelectorAll('li');
    
    items.forEach(function(item) {
        var itemName = item.querySelector('h2').textContent.toLowerCase();
        if (itemName.includes(searchInput)) {
            item.style.display = 'block';
        } else {
            item.style.display = 'none';
        }
    });
});