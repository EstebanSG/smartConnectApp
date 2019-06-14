<?php

require_once('../../../include/phpmailer/class.phpmailer.php');

$mail = new PHPMailer();

if( $_SERVER['REQUEST_METHOD'] == 'POST' ) {

	$name = $_POST['template-medical-name'];
	$phone = $_POST['template-medical-phone'];
	$email = $_POST['template-medical-email'];
	$dob = $_POST['template-medical-dob'];
	$date = $_POST['template-medical-appoint-date'];
	$second_booking = $_POST['template-medical-second-booking'];
	$message = $_POST['template-medical-message'];

	$subject = 'New Appointment';

	$botcheck = $_POST['template-medical-botcheck'];

	$toemail = 'user@email.com'; // Your Email Address
	$toname = 'Name'; // Your Name

	if( $botcheck == '' ) {

		$mail->SetFrom( $email , $name );
		$mail->AddReplyTo( $email , $name );
		$mail->AddAddress( $toemail , $toname );
		$mail->Subject = $subject;

		$name = isset($name) ? "Name: $name<br><br>" : '';
		$phone = isset($phone) ? "Phone: $phone<br><br>" : '';
		$email = isset($email) ? "Email: $email<br><br>" : '';
		$dob = isset($dob) ? "Date of Birth: $dob<br><br>" : '';
		$date = isset($date) ? "Appointment Date: $date<br><br>" : '';
		$second_booking = isset($second_booking) ? "Second Booking: $second_booking<br><br>" : '';
		$message = isset($message) ? "Message: $message<br><br>" : '';

		$referrer = $_SERVER['HTTP_REFERER'] ? '<br><br><br>This Form was submitted from: ' . $_SERVER['HTTP_REFERER'] : '';

		$body = "$name $phone $email $dob $date $second_booking $message $referrer";

		$mail->MsgHTML( $body );
		$sendEmail = $mail->Send();

		if( $sendEmail == true ):
			echo 'We have <strong>successfully</strong> received your Appointment Request and will get Back with a Confirmation as soon as possible.';
		else:
			echo 'Email <strong>could not</strong> be sent due to some Unexpected Error. Please Try Again later.<br /><br /><strong>Reason:</strong><br />' . $mail->ErrorInfo . '';
		endif;
	} else {
		echo 'Bot <strong>Detected</strong>.! Clean yourself Botster.!';
	}
} else {
	echo 'An <strong>unexpected error</strong> occured. Please Try Again later.';
}

?>