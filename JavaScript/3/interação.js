function verificar(){
    var começo = window.document.getElementById("inicio")
    var fim = window.document.querySelector("input#fim")
    var passo = window.document.querySelector("input#passo")
    var resposta = window.document.querySelector("div#resposta")
    if (começo.value.length == 0 || fim.value.length == 0 || passo.value.length == 0){
        window.alert("ERRO, DADOS INVÁLIDOS")
    }
    else{
        resposta.innerHTML = "Contando: "
        var a = Number(começo.value)
        var b = Number(fim.value)
        var d = Number(passo.value)
        for(var c = a; c <= b; c+= d)
            resposta.innerHTML += ` ${c} -`
    }
}