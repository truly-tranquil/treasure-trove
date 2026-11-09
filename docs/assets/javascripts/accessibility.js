// 🔧 Accessibility Fix: Add aria-labels to Material Theme Dynamic Elements
document.addEventListener("DOMContentLoaded", function() {
    
    console.log("Accessibility fix running..."); // Debug line to confirm it loads
    
    // 1. Fix Dark Mode Toggle
    var toggle = document.querySelector('.md-color-toggle, .md-icon--color-mix, [aria-label*="toggle"], [role="switch"]');
    if (toggle) {
        toggle.setAttribute('aria-label', 'Toggle color scheme');
        console.log("Dark mode toggle fixed");
    }

    // 2. Fix Permalink Markers (¶)
    var permalinks = document.querySelectorAll('a[title="Permalink"]');
    permalinks.forEach(function(a) {
        var label = 'Permalink';
        var parentH = a.closest('h1, h2, h3, h4, h5, h6');
        if (parentH) {
            var text = parentH.textContent.trim();
            if (text) {
                label = 'Jump to ' + text;
            }
        }
        a.setAttribute('aria-label', label);
        console.log("Permalink fixed: " + label);
    });

    // 3. Fix Previous/Next Page Arrows
    var prevBtn = document.querySelector('[data-direction="prev"], .md-nav__link--prev, a[aria-label*="prev"]');
    if (prevBtn) {
        prevBtn.setAttribute('aria-label', 'Previous page');
        console.log("Previous arrow fixed");
    }

    var nextBtn = document.querySelector('[data-direction="next"], .md-nav__link--next, a[aria-label*="next"]');
    if (nextBtn) {
        nextBtn.setAttribute('aria-label', 'Next page');
        console.log("Next arrow fixed");
    }

    // 4. Fix Hamburger Menu
    var menuBtn = document.querySelector('.md-icon--menu, [data-action="toggle"]');
    if (menuBtn) {
        menuBtn.setAttribute('aria-label', 'Open navigation menu');
        console.log("Hamburger menu fixed");
    }
    
    console.log("Accessibility fixes complete");
});
