function calcular(){
    var resp = window.document.getElementById("resposta")
    var numero = window.document.querySelector("input#inicio")
    var num = Number(numero.value)
    resp.innerHTML = "Começando: <br>"
    for(var c=1; c <=10; c++){
        var resposta = num * c
        resp.innerHTML += `${num} x ${c} = ${resposta} <br>`
    }
}