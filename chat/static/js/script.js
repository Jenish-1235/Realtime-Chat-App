document.addEventListener('DOMContentLoaded', () => {
  /* ========== SCREEN-BASED RESIZING ========== */
  function resizePage() {
    const width = window.innerWidth;
    let scale = 1; // default to 100%

    if (width >= 992 && width <= 1600) {
      scale = 0.9;
    } else if (width >= 700 && width <= 767) {
      scale = 0.8;
    } else if (width >= 600 && width < 700) {
      scale = 0.75;
    } else if (width <= 600) {
      scale = 0.5;
    }

    // Apply transform to the entire body
    document.body.style.transform = `scale(${scale})`;
    document.body.style.transformOrigin = 'top left';
  }

  // Run once on page load
  resizePage();
  // Also run on window resize
  window.addEventListener('resize', resizePage);

  /* ========== COLLAPSIBLE LEFT MENU ========== */
  const toggleMenuBtn = document.getElementById('toggleMenuBtn');
  const leftMenu = document.getElementById('leftMenu');

  if (toggleMenuBtn && leftMenu) {
    toggleMenuBtn.addEventListener('click', () => {
      leftMenu.classList.toggle('collapsed');
      // (Optional) If you want the main content to expand/shrink too,
      // you could toggle a class on main-content here as well.
    });
  }
});
