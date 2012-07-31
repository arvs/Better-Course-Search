$(function(){
	$(profs).each(function(k,v){
		$.getJSON('search_for_prof?name=' + v, function(data){
			$('#professors').append("<tr><td>" + data.name + "</td><td>" + data.result + "</td></tr>");
		});
	});
});