<?php
// Sample PHP file

// Define a simple function to welcome users
function welcomeUser($name) {
    return "Welcome, " . htmlspecialchars($name) . "!";
}

// Use the function
echo welcomeUser("Visitor");

?>