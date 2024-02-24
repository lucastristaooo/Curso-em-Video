<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Informe um Número</title>
</head>
<body>
    <header>
        <h1>Informe o Número</h1>
    </header>
    <main>
        <form action="<?=$_SERVER["PHP_SELF"]?>" method="get">
            <label for="numero">Digite um número: </label>
            <input type="number" name="numero" id="numero" value="<?=$numero?>">
            <input type="submit" value="Enviar">
        </form>
        <section>
            <?php
                $numero = $_REQUEST["numero"] ?? 0;
                echo "A raíz quadrada é " . sqrt($numero); 
                echo "<br> A raíz cubica é " . pow($numero, 1.0 / 3.0);
            ?>
        </section>
    </main>
</body>
</html>