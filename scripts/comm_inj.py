"""
In this example, the vulnerable_function() takes user input 
and directly concatenates it into a shell command without 
proper sanitization or validation. If an attacker provides 
a malicious input containing special characters or commands, 
they can execute arbitrary commands on the system, leading to 
command injection vulnerabilities.
"""


import subprocess

def vulnerable_function(user_input):
    subprocess.call("ping " + user_input, shell=True)

if __name__ == "__main__":
    user_input = input("Enter IP address to ping: ")
    vulnerable_function(user_input)