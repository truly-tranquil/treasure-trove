document.addEventListener("keydown", function (e) {
  if (e.key !== " ") return;
  var el = e.target;
  if (el.tagName === "LABEL" && el.hasAttribute("tabindex") && el.htmlFor) {
    e.preventDefault();
    el.click();
  }
});