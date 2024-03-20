/* 
In this code, the displayMessage function retrieves 
the value of an input field with the id "message" and 
sets it as the inner HTML content of an element with 
the id "output". This code is vulnerable to XSS because 
it directly injects the user-supplied input into the HTML 
without proper sanitization.
*/

function displayMessage() {
    var message = document.getElementById("message").value;
    document.getElementById("output").innerHTML = "Message: " + message;
}
