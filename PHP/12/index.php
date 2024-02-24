<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conversor de Segundos</title>
</head>
<body>
    <header>
        <h1>Conversor de Segundos</h1>
    </header>
    <main>
        <form action="<?=$_SERVER["PHP_SELF"]?>" method="get">
            <label for="segundos">Qual o total de Segundos: </label>
            <input type="number" name="segundos" id="segundos">
        </form>
        <?php
            $segundos = $_REQUEST["segundos"] ?? 0;
            $semanas = (int)($segundos / 604_800);
            $segundos = ($segundos % 604_800);
            $dias = (int)($segundos / 86_400);
            $segundos = ($segundos % 86_400);
            $horas = (int)($segundos / 3_600);
            $segundos = ($segundos % 3_600); 
            $minutos = (int)($segundos / 60);
            $segundos = ($segundos % 60);
        ?>
        <section>
            <?php
                echo"<ul><li>$semanas semanas<li>$dias dias<li>$horas horas<li>$minutos minutos<li>$segundos segundos</ul>" 
            ?>
        </section>
    </main>
</body>
</html>