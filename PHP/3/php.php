<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sorteador de Números</title>
</head>
<body>
    <header>
        <h1>Sorteador de Números</h1>
    </header>
    <main>
        <?php
            echo "<p>O número sorteado foi </p>" . rand(1, 100)
        ?>
        <p><button onclick="javascript:document.location.reload()">Gerar outro</button></p>
    </main>
</body>
</html>