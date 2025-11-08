const faders = document.querySelectorAll('.fade-in');

window.addEventListener('scroll', () => {
  const triggerBottom = window.innerHeight * 0.85;

  faders.forEach(fader => {
    const top = fader.getBoundingClientRect().top;

    if (top < triggerBottom) {
      fader.classList.add('visible');
    }
  });
});
