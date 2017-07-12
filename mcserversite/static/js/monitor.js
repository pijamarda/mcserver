$( document ).ready(function() {

	$('#button_encender').click(function()
	{
		console.log("tramito el jquery");		
		$.get('/monitor/api/encender/', function(data)
		{
			console.log("llego dentro del get del javascript");
			$('#suma_puntos').html(data);			
		});
    });
});