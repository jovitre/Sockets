<?php
	header('Content-Type: application/json; charset=utf-8');

	
	$arquivo = file_get_contents("historico.json");
	$json_decoded = json_decode($arquivo, true);

	$address = "127.0.0.1";
	$port = 6006;
	$in = 'Saldo';

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

	$json_decoded["saldo"] = $out;
	
	$json_encoded = json_encode($json_decoded);
	file_put_contents("historico.json", $json_encoded);
	echo $json_encoded;
?>