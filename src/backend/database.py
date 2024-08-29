import sqlite3

def create_table():
    conn = sqlite3.connect('ava.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS conversations
                 (id INTEGER PRIMARY KEY, user_input TEXT, ava_response TEXT)''')
    conn.commit()
    conn.close()

def insert_conversation(user_input, ava_response):
    conn = sqlite3.connect('ava.db')
    c = conn.cursor()
    c.execute("INSERT INTO conversations (user_input, ava_response) VALUES (?, ?)", (user_input, ava_response))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
    insert_conversation('Hello', 'Hi there!')
