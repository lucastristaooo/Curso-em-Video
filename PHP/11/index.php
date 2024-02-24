<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reajustador de Preços</title>
</head>
<body>
    <header>
        <h1>Reajustador de Preços</h1>
    </header>
    <main>
        <form action="<?=$_SERVER["PHP_SELF"]?>" method="get">
            <p>
                <label for="preco">Preço do Produto: </label>
                <input type="number" name="preco" id="preco">
            </p>
            <p>
                <label for="percent">Qual será o percentual de reajuste? <span id="p"></span></label> <br>
                <input type="range" name="percent" id="percent" min="0" max="100" oninput= mudavalor()>
            </p>
            <p>
                <input type="submit" value="Enviar">
            </p>
        </form>
        <?php
            $preco = $_REQUEST["preco"] ?? 0;
            $percent = $_REQUEST["percent"] ?? 0;
            $resp = $preco + ($preco * ($percent / 100)); 
        ?>
        <script>
            mudavalor()
            function mudavalor(){
                p.innerText = percent.value + "%"

            }
        </script>
        <section>
            <?php
                echo "Com o reajuste de $percent% o novo valor é de $resp"; 
            ?>
        </section>
    </main>
</body>
</html>