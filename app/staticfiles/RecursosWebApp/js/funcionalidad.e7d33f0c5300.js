function showPerfil(id_perfil){
    var x = document.getElementById(id_perfil);
    if (x.style.visibility === "hidden") {
      x.style.visibility = "visible";
      x.style.opacity = 1;
    } else {
      x.style.visibility = "hidden";
      x.style.opacity = 0;
    }
}