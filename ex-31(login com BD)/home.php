<?php
include 'db.php';

if (!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true) {
    header("Location: index.html");
    exit();
}
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Colégio Alberto Gomes Veiga</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <header class="site-header">
        <h1>Colégio Alberto Gomes Veiga</h1>
        <nav>
            <ul>
                <li><a href="#">Início</a></li>
                <li><a href="#">Sobre</a></li>
                <li><a href="#">Cursos</a></li>
                <li><a href="#">Contato</a></li>
                <li><a href="logout.php">Sair</a></li>
            </ul>
        </nav>
        <p class="login-status">Logado como: <strong><?php echo $_SESSION['username']; ?></strong></p>
    </header>

    <main class="content">
        <section>
            <h2>Bem-vindo ao nosso Colégio!</h2>
            <p>O Colégio Alberto Gomes Veiga oferece ensino de qualidade com foco em inovação e valores humanos. Aqui formamos cidadãos preparados para o futuro.</p>
        </section>
    </main>

    <footer class="site-footer">
        <p>&copy; 2025 Colégio Alberto Gomes Veiga. Todos os direitos reservados.</p>
    </footer>

</body>
</html>