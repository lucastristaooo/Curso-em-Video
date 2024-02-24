<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anatomia de uma Divisão</title>
</head>
<body>
    <header>
        <h1>Anatomia de uma Divisão</h1>
    </header>
    <main>
        <form action="<?=$_SERVER["PHP_SELF"]?>" method="post">
            <label for="dividendo">Dividendo: </label>
            <input type="number" name="dividendo" id="dividendo" value="<?=$dividendo?>">
            <label for="divisor">Divisor: </label>
            <input type="number" name="divisor" id="divisor" value="<?=$divisor?>">
            <input type="submit" value="Dividir">
        </form>
        <?php
            $dividendo = $_REQUEST["dividendo"];
            $divisor = $_REQUEST["divisor"];
            $resultado = floor($dividendo / $divisor);
            $resto = $dividendo % $divisor;
        ?>
        <section>
            <?php
                echo"O dividendo é $dividendo <br> O divisor é $divisor <br> O resultado é $resultado <br> O resto é $resto";
            ?>
        </section>
    </main>
</body>
</html>