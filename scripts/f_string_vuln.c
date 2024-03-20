/*
In this program, the vulnerable_function() directly uses 
printf() with the user-supplied input input as the format 
string. This makes it vulnerable to a format string attack, 
where an attacker can input format specifiers (%s, %x, %n, etc.) 
to read from or write to arbitrary memory locations, potentially 
leading to information disclosure or arbitrary code execution.
*/

#include <stdio.h>

void vulnerable_function(char *input) {
    printf(input); // Vulnerable to format string attack
}

int main() {
    char input[20];
    printf("Enter input: ");
    fgets(input, sizeof(input), stdin);
    vulnerable_function(input);
    return 0;
}