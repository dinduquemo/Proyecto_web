document.querySelectorAll('.redes span').forEach(span => {
    span.addEventListener('click', () => {
      const url = span.getAttribute('data-url');
      window.open(url, '_blank');
    });
  });




