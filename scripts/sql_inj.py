"""
In this program, the vulnerable_query() function constructs 
an SQL query string by directly concatenating the username 
input from the user. This makes it vulnerable to SQL injection 
attacks, where an attacker can manipulate the username input 
to inject malicious SQL code, potentially leading to unauthorized 
access, data leakage, or data manipulation.
""" 

import sqlite3

def vulnerable_query(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username='" + username + "'"
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    username = input("Enter username: ")
    result = vulnerable_query(username)
    print(result)

