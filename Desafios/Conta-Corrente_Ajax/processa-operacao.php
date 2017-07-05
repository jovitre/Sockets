<?php
	header('Content-Type: application/json; charset=utf-8');

	$arquivo = file_get_contents("historico.json");
	$json_decoded = json_decode($arquivo, true);

	$address = "127.0.0.1";
	$port = 6006;
	$in = '';
	$in2 = '';

	$in = $_POST["op"];
	$in2 = $_POST["val"];

	if ($in2 == ''){
		$arr = array("saldo" => "Erro, digite um valor.");
		$arr["operacoes"] = $json_decoded["operacoes"];
		echo json_encode($arr);
		die();
	}

	$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);

	if ($sock === false) {
		die("Não criou o socket");
	}

	$resultado = socket_connect($sock, $address, $port);

	if($resultado === false){
		die("Não conseguiu conectar");
	}

	if($in != "debito" && $in != "credito"){
		$in = "saldo";
	}

	array_push($json_decoded["operacoes"], [ucfirst($in), $in2]);

	$in = $in." ".$in2;

	socket_write($sock, $in, strlen($in));

	$out = socket_read($sock, 2048);

	$json_decoded["saldo"] = $out;
	
	$json_encoded = json_encode($json_decoded);
	file_put_contents("historico.json", $json_encoded);
	echo $json_encoded;

?>