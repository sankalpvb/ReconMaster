// reconmaster/static/js/ui.js

document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    if (!themeToggleBtn) return;

    const sunIcon = document.getElementById('sun-icon');
    const moonIcon = document.getElementById('moon-icon');

    const applyTheme = (theme) => {
        if (theme === 'light') {
            document.body.classList.add('light-theme');
            if(sunIcon) sunIcon.style.display = 'inline-block';
            if(moonIcon) moonIcon.style.display = 'none';
        } else {
            document.body.classList.remove('light-theme');
            if(sunIcon) sunIcon.style.display = 'none';
            if(moonIcon) moonIcon.style.display = 'inline-block';
        }
    };

    const savedTheme = localStorage.getItem('theme') || 'dark';
    applyTheme(savedTheme);

    themeToggleBtn.addEventListener('click', () => {
        const currentTheme = document.body.classList.contains('light-theme') ? 'light' : 'dark';
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        
        localStorage.setItem('theme', newTheme);
        applyTheme(newTheme);
    });
});
