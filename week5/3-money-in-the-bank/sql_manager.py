import sqlite3
import hashlib
from datetime import datetime

from Client import Client

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''CREATE TABLE IF NOT EXISTS
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                email TEXT,
                reset_pass_hash TEXT)'''

    cursor.execute(create_query)
    conn.commit()


def create_failed_logins_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS
        failed_logins(
            id INTEGER PRIMARY KEY,
            username TEXT,
            last_login TEXT)
        ''')
    conn.commit()


def create_tans_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS
        tans(
            id INTEGER PRIMARY KEY,
            tan TEXT,
            username TEXT,
            is_used BOOLEAN)
        ''')
    conn.commit()


def change_message(new_message, logged_user):
    cursor.execute("UPDATE clients SET message = ? WHERE id = ?",
                   (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    check_password_strong(logged_user.get_username, new_pass)
    cursor.execute("UPDATE clients SET password = ? WHERE id = ?",
                   (hashed(new_pass), logged_user.get_id()))
    conn.commit()


def reset_password(new_pass, username):
    check_password_strong(username, new_pass)
    cursor.execute("UPDATE clients SET password = ? WHERE username = ?",
                   (hashed(new_pass), username))
    conn.commit()


def hashed(password):
    encoded_password = password.encode('utf-8')
    hashed_password = hashlib.sha1(encoded_password).hexdigest()
    return hashed_password


def generate_random_hash():
    import uuid
    return uuid.uuid4().hex


def check_password_strong(username, password):
    if len(list(password)) <= 8:
        print('Your password must be longer than 8 symbols!')
        return False
    if not any([s.isupper for s in password]):
        print('Your password must contain capital letters!')
        return False
    if not any([s.isdigit() for s in password]):
        print('Your password must contain digits!')
        return False
    SPECIAL_CHARS = set('''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~´''')
    if not (set(password) & SPECIAL_CHARS):
        print('Your password must contain a special character')
        return False
    if username in password:
        print('Your password should not contain your username!')
        return False


def is_password_correct(username, password):
    cursor.execute('''SELECT COUNT (*)
        FROM clients
        WHERE username = ? AND password = ?''', (username, hashed(password)))
    password = cursor.fetchone()
    return bool(password)


def register(username, password, email):
    check_password_strong(username, password)
    rand_hash = generate_random_hash()
    cursor.execute(
        '''INSERT INTO clients(username, password, email, reset_pass_hash)
        VALUES(?,?,?,?)''',
        (username, hashed(password), email, rand_hash))
    conn.commit()
    return True


def login(username, password):
    cursor.execute('''SELECT id, username, balance, message
        FROM clients
        WHERE username = ? AND password = ?
        LIMIT 1''', (username, hashed(password)))
    user = cursor.fetchone()
    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False


def register_failed_login(username, time):
    cursor.execute('''INSERT INTO failed_logins(username, last_login)
        VALUES(?, ?)''', (username, time))
    conn.commit()


def clear_failures_history(username):
    cursor.execute(
        '''DELETE FROM failed_logins WHERE username = ?''', (username, ))
    conn.commit()


def get_login_tries(username):
    cursor.execute('SELECT COUNT (*) FROM failed_logins WHERE username = ?',
                   (username, ))
    failed_logins_count = cursor.fetchone()
    if not failed_logins_count:
        return 0
    return failed_logins_count[0]


def get_last_failed_login(username):
    cursor.execute('''SELECT last_login FROM failed_logins
        WHERE username = ? ORDER BY last_login DESC''', (username, ))
    last_login = cursor.fetchone()
    if last_login:
        return datetime.strptime(last_login[0], '%Y-%m-%d %H:%M:%S.%f')
    else:
        return None


def get_user_email(username):
    cursor.execute('''SELECT email
        FROM clients
        WHERE username = ?''', (username,))
    email = cursor.fetchone()[0]
    return email


def get_user_reset_pass_hash(username):
    cursor.execute('''SELECT reset_pass_hash
        FROM clients
        WHERE username = ?''', (username,))
    rand_hash = cursor.fetchone()[0]
    return rand_hash


def get_user_unused_tans(username):
    cursor.execute('''SELECT tan
        FROM tans
        WHERE username = ? AND is_used = ?''', (username, False))
    tans = cursor.fetchall()
    return [tan[0] for tan in tans]


def get_all_tans():
    cursor.execute('''SELECT tan
        FROM tans''')
    tans = cursor.fetchall()
    return [tan[0] for tan in tans]


def generate_tans(username):
    tans = []
    all_tans = get_all_tans()
    for i in range(0, 10):
        tan = generate_random_hash()
        while tan in all_tans or tan in tans:
            tan = generate_random_hash()
        tans.append((tan, username, False))
    cursor.executemany(
        '''INSERT INTO tans(tan, username, is_used) VALUES(?, ?, ?)''', tans)
    conn.commit()
    return [tan[0] for tan in tans]


def mark_tan_as_used(tan):
    cursor.execute('''UPDATE tans SET is_used=? WHERE tan = ?''', (True, tan))
    conn.commit()


def deposit(username, money):
    cursor.execute(
        '''UPDATE clients SET balance=balance+?
        WHERE username = ?''', (money, username))
    conn.commit()


def withdraw(username, money):
    cursor.execute(
        '''UPDATE clients SET balance=balance-?
        WHERE username = ?''', (money, username))
    conn.commit()
