<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Médias Aritméticas</title>
</head>
<body>
    <header>
        <h1>Médias Aritméticas</h1>
    </header>
    <main>
        <form action="<?=$_SERVER["PHP_SELF"]?>" method="post">
            <label for="n1">Nota 1: </label>
            <input type="number" name="n1" id="n1" value="<?=$n1?>">
            <label for="n1">Peso 1: </label>
            <input type="number" name="p1" id="p1" value="<?=$p1?>">
            <label for="n1">Nota 2: </label>
            <input type="number" name="n2" id="n2" value="<?=$n2?>">
            <label for="n1">Peso 2: </label>
            <input type="number" name="p2" id="p2" value="<?=$p2?>">
            <input type="submit" value="Enviar">
        </form>
        <?php
            $n1 = $_REQUEST["n1"] ?? 0;
            $p1 = $_REQUEST["p1"] ?? 1;
            $n2 = $_REQUEST["n2"] ?? 0;
            $p2 = $_REQUEST["p2"] ?? 1;
            $mas = ($n1 + $n2) / 2;
            $map = (($n1 * $p1) + ($n2 * $p2)) / 2;
        ?>
        <section>
            <?php
                echo "Analisando os valores $n1 e $n2 <br>";
                echo "<ul><li>A Média Aritmética Simples entre os valores é igual a $mas <li>A Média Aritmética Ponderada com pesos $p1 e $p2 é igual a $map</ul>"; 
            ?>
        </section>
    </main>
</body>
</html>