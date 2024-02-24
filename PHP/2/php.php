<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Antecessor e Sucessor</title>
</head>
<body>
    <header>
        <h1>Antecessor e Sucessor</h1>
    </header>
    <main>
        <?php
            $número = $_REQUEST["número"];
            echo "<p>O número é $número";
            echo "<p>O antecessor é " . $número-1; 
            echo "<p>O sucessor é " . $número+1; 
        ?>
        <p><a href="index.html">Voltar a página anterior.</a></p>
    </main>
</body>
</html>