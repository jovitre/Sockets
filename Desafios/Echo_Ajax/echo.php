<?php
	header('Content-Type: text/html; charset=utf-8');
	$address = "127.0.0.1";
	$port = 6006;
	$arquivo = file_get_contents("dados.json");
	$json_decoded = json_decode($arquivo);

	if(!$_POST["val"]) die(false);

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
	$json_decoded[] = $out;
	$json_encoded = json_encode($json_decoded);
	file_put_contents("dados.json", $json_encoded);

	echo $out;
?>