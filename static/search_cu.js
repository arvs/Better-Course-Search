$(function(){
	$(profs).each(function(k,v){
		$.getJSON('search_for_prof?name=' + v, function(data){
			if (data.classes.length != 0)
				$('#professors').append("<tr><td>" + data.name + "</td><td>" + wrap_a(data.classes) + "</td></tr>");
		});
		var wrap_a = function(arr){
			s = ""
			$(arr).each(function(k,v){
				s+='<a href="'+ v + '">Class ' + (k+1)  + ', </a>';
			});
			return s
		}
	});
});