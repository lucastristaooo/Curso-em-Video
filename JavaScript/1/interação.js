function executar(){
    var msg = window.document.getElementById("msg")
    var foto = window.document.getElementById("foto")
    var data = new Date()
    var horas = data.getHours()
    var minutos = data.getMinutes()
    msg.style.textAlign = "center"
    msg.innerHTML = `Agora são ${horas}:${minutos}`
    foto.style.textAlign = "center"
    if(horas >= 0 && horas < 12){
        foto.innerHTML = "Agora é de dia!"
    }
    else if(horas >= 12 && horas < 18){
        foto.innerHTML = "Agora é de tarde!"
    }
    else{
        foto.innerHTML = "Agora é de noite!"
    }
}