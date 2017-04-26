<?php
header('Content-Type: text/html; charset=utf-8');
// die("No céu tem pão?"); // e morreu
$address = "127.0.0.1";
$port = 6006;

$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if ($sock === false) {
	die("Não criou o socket");
}

$resultado = socket_connect($sock, $address, $port);

if($resultado === false){
	die("Não conseguiu conectar");
}

$in = "SALDO";
socket_write($sock, $in, strlen($in));

$out = socket_read($sock, 2048);
echo "SALDO: ".$out;

?>