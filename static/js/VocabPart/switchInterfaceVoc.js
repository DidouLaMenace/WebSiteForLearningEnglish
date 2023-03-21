bouton = document.getElementById('toggle');
apprentissageMode = document.getElementById('apprentissage');
autoapprentissageMode = document.getElementById('autoapprentissage');

if (bouton.checked) {
        apprentissageMode.style.display = 'none';
        autoapprentissageMode.style.display = 'block';
}
else {
    apprentissageMode.style.display = 'block';
    autoapprentissageMode.style.display = 'none';
}

bouton.addEventListener('click', function() {
    if (bouton.checked) {
        apprentissageMode.style.display = 'none';
        autoapprentissageMode.style.display = 'block';
    }
    else {
        apprentissageMode.style.display = 'block';
        autoapprentissageMode.style.display = 'none';
    }
});

  
