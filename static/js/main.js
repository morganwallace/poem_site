$("#signup").submit(function(){

	$.post("./adduser",
		$("#signup").serialize(),
		function(data){
		    console.log('signup');
		    console.log(data);
		    if (data.success==true){
		    	//load profile page
		    	window.open('/','_self');
		    }
		    else{
		    	alert('email is not unique!');
		    }
		}
	)
	console.log('testing blerg');
	// e.preventDefault();
	return false
  })

//   Add poem
$("#add-poem").submit(function(){

	$.post("./addpoem",
		$("#add-poem").serialize(),
		function(data){
		    console.log('addpoem');
		    console.log(data);
		    if (data.success==true){
		    	//load profile page
		    	console.log('opening: '+'/poem/'+data.title)
		    	window.open('/poem/'+data.title,'_self');
		    }
		    else{
		    }
		}
	)
	console.log('testing blerg');
	// e.preventDefault();
	return false
  })



//sign-in
$("#sign-in").submit(function(){

	// $.post("./signin",
	// 	$("#sign-in").serialize(),
	// 	function(data){
	// 	    console.log('sign-in');
	// 	    console.log(data);
	// 	    if (data.success==true){
	// 	    	console.log('sign in success');
	// 	    }
	// 	    else{
	// 	    	console.log('sign in failure');
	// 	    }
	// 	}
	// )
	console.log('testing sign-in');
	// e.preventDefault();
	return false
  })

$(document).ready(function(){
    $('.navbar-nav [data-toggle="tooltip"]').tooltip();
    $('.navbar-twitch-toggle').on('click', function(event) {
        event.preventDefault();
        $('.navbar-twitch').toggleClass('open');
    });
    
    $('.nav-style-toggle').on('click', function(event) {
        event.preventDefault();
        var $current = $('.nav-style-toggle.disabled');
        $(this).addClass('disabled');
        $current.removeClass('disabled');
        $('.navbar-twitch').removeClass('navbar-'+$current.data('type'));
        $('.navbar-twitch').addClass('navbar-'+$(this).data('type'));
    });
    $("#sign-in").hide();
    $("#login-btn").click(function(){
    	$("#login-btn").hide();
    	$("#sign-in").fadeIn(200);

    });


});