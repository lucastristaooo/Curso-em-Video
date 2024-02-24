<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <header>
        <h1>Resultado do Processamento</h1>
    </header>
    <main>
        <?php
            /*Três métódos para pegar dados de formulários:
                1. $_GET
                2, $_POST
                3. $_REQUEST
            */
            $nome = $_REQUEST["nome"] ?? "Desconhecido";
            $idade = $_REQUEST["idade"] ?? "?";
            echo "<p>Olá $nome, você tem $idade anos!</p>";
        ?>
        <a href="index.html">Voltar para a página anterior.</a>
    </main>
</body>
</html>