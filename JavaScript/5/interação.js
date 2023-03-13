var números = window.document.getElementById("inicio")
var mostrarnúmeros = window.document.getElementById("números")
var resposta = window.document.getElementById("resposta")
var valores = []
function isNumero(n){
    if(Number(n) >= 1 && Number(n) <= 100){
        return true
    }else{
        return false
    }
}
function inLista(n, l){
    if(l.indexOf(Number(n)) != -1){
        return true
    }else{
        return false
    }
}
function adicionar(){
    if(isNumero(números.value) && !inLista(números.value, valores)){
        valores.push(Number(números.value))
        mostrarnúmeros.innerHTML += ` ${Number(números.value)}`
        resposta.innerHTML = " "
}else{
    window.alert("Valor inválido ou já encontrado na lista")
    }
números.value = " "
números.focus()
}
function calcular(){
    if(valores.length == 0){
        window.alert("Adicione valores antes de finalizar")
    }
    else{
        var total = valores.length
        var soma = 0
        var média = 0
        var maior = valores[0]
        var menor = valores[0]
        for(var c in valores){
            soma += valores[c]
            if(valores[c] > maior){
                maior = valores[c]
            }
            if(valores[c] < menor){
                menor = valores[c]
            }
        }
        média = soma / valores.length
        resposta.innerHTML = " "
        resposta.innerHTML += `<p>O total de números é de ${total}</p>`
        resposta.innerHTML += `<p>O maior número é ${maior}</p>`
        resposta.innerHTML += `<p>O menor número é ${menor}</p>`
        resposta.innerHTML += `<p>A soma dos números é ${soma}</p>`
        resposta.innerHTML += `<p>A média dos valores digitados é de ${média}</p>`
    }
}