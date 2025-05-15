function configurarBuscador() {
  const formulario = document.getElementById('formulario-busqueda');
  
  if (formulario) {
    formulario.addEventListener('submit', function(e) {
      e.preventDefault();
      const termino = document.getElementById('busqueda-input').value.trim().toLowerCase();
      
      // Redirige a productos.html con el término de búsqueda
      if (termino) {
        window.location.href = `productos.html?busqueda=${encodeURIComponent(termino)}`;
      }
    });
  }
}

// Ejecutar al cargar y también cuando se navega en SPA
document.addEventListener('DOMContentLoaded', configurarBuscador);
document.addEventListener('pageLoad', configurarBuscador); // Para frameworks