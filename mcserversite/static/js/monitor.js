$( document ).ready(function() {

	$('#button_encender').click(function()
	{
		console.log("tramito el jquery");		
		$.get('/monitor/api/encender/', function(data)
		{
			console.log("llego dentro del get del javascript");			
			$('#progressPC').css("visibility", "visible");
			$('#button_encender').prop("disabled",true);
			move();
		});
	});
	$('#button_encender_minecraft').click(function()
	{
		console.log("tramito el jquery");		
		$.get('/monitor/api/encenderminecraft/', function(data)
		{
			console.log("llego dentro del get del javascript");
			$('#progressMC').css("visibility", "visible");			
			$('#button_encender_minecraft').prop("disabled",true);
			move_mc();
		});
		/* Para las pruebas con un servidor de prueba
		console.log("llego dentro del get del javascript");
		$('#progressMC').css("visibility", "visible");			
		$('#button_encender_minecraft').prop("disabled",true);
		move_mc();
		*/
    });
});

function move() {
    var elem = document.getElementById("varPC"); 
	var width = 0;
	var incremento = 0.1
    var id = setInterval(frame, 200);
    function frame() {
        if (width >= 100) {
			clearInterval(id);
			$('#button_encender').prop("disabled",false);
        } else {
			width = width + incremento; 
			//console.log(width);
            elem.style.width = width + '%'; 
        }
    }
}

function move_mc() {
    var elem = document.getElementById("varMC"); 
	var width = 0;
	var incremento = 1
    var id = setInterval(frame, 100);
    function frame() {
        if (width >= 100) {
			clearInterval(id);			
        } else {
			width = width + incremento; 
			//console.log(width);
            elem.style.width = width + '%'; 
        }
    }
}