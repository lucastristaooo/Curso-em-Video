<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conversor de Dólar</title>
</head>
<body>
    <header>
        <h1>Conversor de Dólar</h1>
    </header>
    <main>
        <?php
            $real = $_GET["valor"];
            $cotacao = 4.8;
            $operacao = $real / $cotacao;
            echo "R$$real convertidos para dólar é igual a U$" . $operacao;
        ?>
    </main>
</body>
</html>