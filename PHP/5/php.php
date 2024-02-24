<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Analisador de Número Real</title>
</head>
<body>
    <header>
        <h1>Analisador de Número Real</h1>
    </header>
    <main>
        <?php
            $numero = $_REQUEST["numero"];
            $int = (int) $numero;
            $real = $numero - $int;
            echo "<ul><li>O inteiro é $int <li>O real é $real<ul>";
        ?>
    </main>
</body>
</html>