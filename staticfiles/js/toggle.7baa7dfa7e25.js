document.addEventListener('DOMContentLoaded', function() {
  const themeToggle = document.getElementById('theme-toggle');
  const body = document.body;

  // Verifica si el modo oscuro está habilitado en el almacenamiento local
  if (localStorage.getItem('dark-mode') === 'true') {
    body.classList.add('dark-mode');
    document.getElementById('theme-icon').classList.add('fa-sun');
    document.getElementById('theme-icon').classList.remove('fa-moon');
  } else {
    document.getElementById('theme-icon').classList.add('fa-moon');
    document.getElementById('theme-icon').classList.remove('fa-sun');
  }

  themeToggle.addEventListener('click', function() {
    body.classList.toggle('dark-mode');
    const isDarkMode = body.classList.contains('dark-mode');
    
    // Guarda la preferencia del usuario en el almacenamiento local
    localStorage.setItem('dark-mode', isDarkMode);
    
    if (isDarkMode) {
      document.getElementById('theme-icon').classList.add('fa-sun');
      document.getElementById('theme-icon').classList.remove('fa-moon');
    } else {
      document.getElementById('theme-icon').classList.add('fa-moon');
      document.getElementById('theme-icon').classList.remove('fa-sun');
    }
  });
});
