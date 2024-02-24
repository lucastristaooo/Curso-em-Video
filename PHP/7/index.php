<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Informe seu Salário</title>
</head>
<body>
    <header>
        <h1>Informe seu Salário</h1>
    </header>
    <main>
        <form action="<?=$_SERVER["PHP_SELF"]?>" method="post">
            <label for="salario">Digite seu Salário: </label>
            <input type="number" name="salario" id="salario" value="<?=$salario?>">
            <input type="submit" value="Enviar">
        </form>
        <?php
            $salario = $_REQUEST["salario"] ?? 1440;
            $resp = round($salario / 1440);
            $resto =  $salario % 1440;
        ?>
        <section>
            <?php
                echo "Quem recebe um salário de R$$salario,00 ganha $resp salários mínimos + R$$resto,00"; 
            ?>
        </section>
    </main>
</body>
</html>