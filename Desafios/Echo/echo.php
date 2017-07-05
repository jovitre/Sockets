<html>
	<head>
	<title> Echo </title>
	</head>
	<body>
		<center>
			<?php
				header('Content-Type: text/html; charset=utf-8');
				$address = "127.0.0.1";
				$port = 6006;

				if(!$_POST["val"]) die("Você não digitou nada, tente novamente");

				$in = $_POST["val"];

				$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
				if ($sock === false) {
					die("Não criou o socket");
				}

				$resultado = socket_connect($sock, $address, $port);

				if($resultado === false){
					die("Não conseguiu conectar");
				}

				socket_write($sock, $in, strlen($in));

				$out = socket_read($sock, 2048);
				echo "ECHO: ".$out;
			?>
			<form action="echo.php" method="post">
				<p>Digite alguma coisa:</p><input type="text" name="val"><br><br>
				<input type="submit" id="submitbtn">
			</form>
		</center>
	</body>
</html>