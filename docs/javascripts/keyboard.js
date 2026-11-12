document.addEventListener("keydown", function (e) {
  if (e.key !== " ") return;
  var el = e.target;
  if (el.tagName === "LABEL" && el.hasAttribute("tabindex") && el.htmlFor) {
    e.preventDefault();
    el.click();
  }
});

(function () {
  function addTocToggle() {
    var sidebar = document.querySelector('.md-sidebar--secondary[data-md-type="toc"]');
    if (!sidebar || !sidebar.querySelector('[data-md-component="toc"] a')) return;

    var wide = window.matchMedia("(min-width: 60em)");
    var isCollapsed = false;
    var storageKey = "treasure-trove-toc";
    try {
      isCollapsed = window.localStorage.getItem(storageKey) === "closed";
    } catch (error) {
      console.warn("Could not read the table-of-contents preference.", error);
    }

    var button = document.createElement("button");
    var arrow = document.createElement("span");
    button.className = "tt-toc-toggle";
    button.type = "button";
    button.hidden = true;
    if (!sidebar.id) sidebar.id = "tt-toc-sidebar";
    button.setAttribute("aria-controls", sidebar.id);
    arrow.setAttribute("aria-hidden", "true");
    button.appendChild(arrow);

    function update() {
      sidebar.hidden = wide.matches && isCollapsed;
      button.hidden = !wide.matches;
      button.setAttribute("aria-expanded", String(!isCollapsed));
      button.setAttribute(
        "aria-label",
        isCollapsed ? "Expand the on-this-page table of contents" : "Collapse the on-this-page table of contents"
      );
      arrow.textContent = isCollapsed ? "‹" : "›";
      button.style.right = "0";
      if (!isCollapsed && wide.matches) {
        window.setTimeout(function () {
          if (!isCollapsed && wide.matches) {
            button.style.right =
              document.documentElement.clientWidth - sidebar.getBoundingClientRect().left + "px";
          }
        }, 0);
      }
    }

    button.addEventListener("click", function () {
      isCollapsed = !isCollapsed;
      update();
      try {
        window.localStorage.setItem(storageKey, isCollapsed ? "closed" : "open");
      } catch (error) {
        console.warn("Could not save the table-of-contents preference.", error);
      }
    });

    document.body.appendChild(button);
    window.addEventListener("resize", update);
    if (wide.addEventListener) wide.addEventListener("change", update);
    else wide.addListener(update);
    update();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", addTocToggle);
  } else {
    addTocToggle();
  }
})();