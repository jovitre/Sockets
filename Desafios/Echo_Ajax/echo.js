$(function(){

	$.getJSON("dados.json", function(dados){
        $("div").html("<p>Palavras já echoadas:</p>");
        $.each(dados, function(i, items){
        	$("div").append(items + ' ');
        });
    });

	$("#log").click(function(){
		$("div").toggle();
	});

	$('form').on('submit', function(ev) {
		action = "echo.php";
		$.ajax({
			url: action,
			data: $(this).serializeArray(),
			method: "POST",
			success: function (data, textStatus, jqXHR) {
				if(!data){
					$("#mostrar_echo").html("Você não digitou nada.");
				} else {
					$("#mostrar_echo").html("ECHO: " + data);
					$("div").append(data + ' ');
				}
	    	}
		});
		ev.preventDefault();
		return false;
	});

});