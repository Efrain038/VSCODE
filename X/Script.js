function Ver_mas() {
    const info = document.getElementById("infoextra")
    const btn = document.querySelector("button")

    if (info.style.display === "none" || info.style.display==="") {
        info.style.display = "block"
        btn.textContent = "ocultar"
    }else {
        info.style.display="none"
        btn.textContent= "Ver mas"
    }
}

