document.addEventListener('DOMContentLoaded', function () {
    const nightdarkBtn = document.getElementById('nightdarkBtn');
    const settingsBtn = document.getElementById('settingsBtn');
    const settingsMenu = document.getElementById('settingsMenu');

    nightdarkBtn.addEventListener('click', function () {
        document.body.classList.toggle('light-mode');
    });

    settingsBtn.addEventListener('click', function (event) {
        event.stopPropagation();
        settingsMenu.style.display = (settingsMenu.style.display === "block") ? "none" : "block";
    });

    window.addEventListener("click", function (event) {
        if (!event.target.closest('#settingsBtn') && !event.target.closest('#settingsMenu')) {
            settingsMenu.style.display = "none";
        }
    });
});