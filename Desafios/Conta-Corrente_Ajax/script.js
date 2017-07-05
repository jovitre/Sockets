$(function(){

	var action = "processa-saldo.php";
	$.ajax({
		url: action,
		method: "POST",
		success: function (data, textStatus, jqXHR) {
			$("#valor_saldo").html(data.saldo);
			$.each(data.operacoes, function(i, items){
				var op = items[0];
				var val = items[1];
			    $("tbody").prepend("<tr><td>" + op + "</td><td>" + val + "</td></tr>");
	    	});
	    }
	});
	

	$("button[name = 'log']").click(function(){
		$("table").toggle();
	});

	$('form').on('submit', function(ev) {
		action = "processa-operacao.php";
		$.ajax({
			url: action,
			data: $(this).serializeArray(),
			method: "POST",
			success: function (data, textStatus, jqXHR) {
				console.log(data);
				$('#valor_saldo').html(data.saldo);
				$("tbody").html("");
				$.each(data.operacoes, function(i, items){
					var op = items[0];
					var val = items[1];
			        $("tbody").prepend("<tr><td>" + op + "</td><td>" + val + "</td></tr>");
	    		});
	    	}
		});
		ev.preventDefault();
		return false;
	});
});