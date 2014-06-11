
$(document).ready(function(){
	$("#signup").submit(function(e){

      $.post("./adduser",
        $("#signup").serialize(),
        function(data){
            console.log('signup');
            console.log(data);
         
      
          return false;
        }
      )
		alert('test');
      return false
  })




});
function signup(){
	// alert('test2');
	return false
}