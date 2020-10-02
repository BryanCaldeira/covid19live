// Loading Part

window.addEventListener("load", () => {
    setInterval(function () {
        const loader = document.querySelector(".loader");
        loader.className += " hidden"; //class "loader hidden"
        document.body.style.overflow = "scroll";
    }, 2000);
})