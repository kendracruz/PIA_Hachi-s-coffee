document.addEventListener("DOMContentLoaded", () => {
  const elements = document.querySelectorAll(".fade-in");

  function checkVisible() {
    const triggerBottom = window.innerHeight * 0.9;
    elements.forEach(el => {
      const top = el.getBoundingClientRect().top;
      if (top < triggerBottom) {
        el.classList.add("visible");
      }
    });
  }

  window.addEventListener("scroll", checkVisible);
  checkVisible();
});
