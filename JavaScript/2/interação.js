function verificar(){
    var cor = window.document.querySelector("input#cor")
    var cor1 = Number(cor.value)
    if(cor1 == "1"){
        window.document.body.style.backgroundColor = "Blue"
    }
    else if(cor1 == "2"){
        window.document.body.style.backgroundColor = "Yellow"
    }
    else if(cor1 == "3"){
        window.document.body.style.backgroundColor = "Red"
    }
    else if(cor1 == "4"){
        window.document.body.style.backgroundColor = "Green"
    }
    else{
        window.alert("Cor indisponível")
    }
}