<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculando sua Idade</title>
</head>
<body>
    <header>
        <h1>Calculando sua Idade</h1>
    </header>
    <main>
        <form action="<?=$_SERVER["PHP_SELF"]?>" method="post">
            <label for="anonasc">Digite seu ano de nascimento: </label>
            <input type="number" name="anonasc" id="anonasc" required> <br>
            <label for="ano">Quer saber sua idade em que ano (Atualmente estamos em <?=date("Y")?>)</label>
            <input type="number" name="ano" id="ano" required>
            <input type="submit" value="Enviar">
        </form>
        <?php
            $anonasc = $_REQUEST["anonasc"] ?? 2024;
            $ano = $_REQUEST["ano"] ?? 2024;
        ?>
        <section>
            <?php
                echo "Quem nasceu em $anonasc vai ter " . $ano - $anonasc . " anos em $ano";
            ?>
        </section>
    </main>
</body>
</html>