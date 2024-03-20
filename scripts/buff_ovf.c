/*
In this program, vulnerable_function() copies 
the input string input into a fixed-size buffer 
buffer using strcpy() without checking the length 
of the input. If the input is longer than the size 
of the buffer (in this case, 10 characters), it will 
overflow the buffer, leading to undefined behavior 
and potentially allowing an attacker to execute arbitrary 
code or manipulate program behavior.
*/

#include <stdio.h>
#include <string.h>

void vulnerable_function(char *input) {
    char buffer[10];
    strcpy(buffer, input); // Vulnerable to buffer overflow
    printf("Buffer content: %s\n", buffer);
}

int main() {
    char input[20];
    printf("Enter input: ");
    fgets(input, sizeof(input), stdin);
    vulnerable_function(input);
    return 0;
}