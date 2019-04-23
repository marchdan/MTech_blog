<?php
if($_POST["emotion"]){
	mail("ackerd2@rpi.edu", "Survey response", $_POST["message"], "From: script@gmail.com");
}
?>