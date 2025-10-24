document.addEventListener('DOMContentLoaded', () => {
    const continuarBtn = document.getElementById('continuarBtn');
    const bienvenida = document.querySelector('.bienvenida');
    const contenido = document.getElementById('contenido');

    continuarBtn.addEventListener('click', () => {
        bienvenida.style.display = 'none';
        contenido.classList.remove('oculto');
        contenido.classList.add('visible');
    });
});
