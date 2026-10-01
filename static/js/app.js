document.addEventListener("DOMContentLoaded", () => {

    const menuButton =
        document.getElementById("menuButton");

    const sidebar =
        document.getElementById("sidebar");


    if (menuButton && sidebar) {

        menuButton.addEventListener("click", () => {
            sidebar.classList.toggle("open");
        });


        document.addEventListener("click", (event) => {

            if (window.innerWidth > 900) {
                return;
            }

            const clickedInsideSidebar =
                sidebar.contains(event.target);

            const clickedMenuButton =
                menuButton.contains(event.target);

            if (
                !clickedInsideSidebar &&
                !clickedMenuButton
            ) {
                sidebar.classList.remove("open");
            }

        });

    }

});