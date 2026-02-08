  const header = document.querySelector("svg");
  const headerLinks = document.querySelector(".header_ul");
  const headerAnchors = document.querySelectorAll(".header__anchor");
  const dropButtons = document.querySelectorAll('.dropbtn');
  const subLists = document.querySelectorAll('.sub__list');

  header?.addEventListener("click", (e) => {
    e.stopPropagation(); 
    headerLinks?.classList.toggle("hidden");
  });

  dropButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const menu = btn.nextElementSibling;

      subLists.forEach(otherMenu => {
        if (otherMenu !== menu) otherMenu.classList.remove('shown');
      });

      menu?.classList.toggle('shown');
    });
  });

  window.addEventListener('click', () => {
    headerLinks?.classList.add("hidden");
    subLists.forEach(menu => menu.classList.remove('shown'));
  });
