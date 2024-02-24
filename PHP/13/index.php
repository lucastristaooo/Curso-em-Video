<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Caixa Eletrônico</title>
</head>
<body>
    <header>
        <h1>Caixa Eletrônico</h1>
    </header>
    <main>
        <form action="<?=$_SERVER["PHP_SELF"]?>" method="post">
            <label for="valor">Quanto deseja sacar: </label>
            <input type="number" name="valor" id="valor" required min="5" step="5">
            <input type="submit" value="Sacar">
        </form>
        <?php
            $valor = $_REQUEST["valor"] ?? 0;
            $cem = floor((int) $valor / 100);
            $valor = $valor % 100;
            $cinquenta = floor((int) $valor / 50);
            $valor = $valor % 50;
            $dez = floor((int) $valor / 10);
            $valor = $valor % 10;
            $cinco = floor($valor);
        ?>
        <section>
            <?php
                echo "<ul><li>$cem notas de 100 <li> $cinquenta notas de 50 <li> $dez notas de 10 <li> $cinco notas de 5";
            ?>
        </section>
    </main>
</body>
</html>