import sql_manager
import getpass
import datetime


def main_menu():
    print(
        "Welcome to our bank service. You are not logged in. \n \
You can register, login, send-reset-password or reset-password")
    while True:
        full_command = input("$$$>").split(" ")
        command = full_command[0]

        if command == 'register':
            register()

        elif command == 'login':
            login()

        elif command == 'send-reset-password':
            username = full_command[1]
            subject = 'Reset password'
            reset_hash = sql_manager.get_user_reset_pass_hash(username)
            message = 'Enter this hash to reset your password {}'.format(
                reset_hash)
            send_email(username, subject, message)

        elif command == 'reset-password':
            username = full_command[1]
            reset_password(username)

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def register():
    username = input("Enter your username: ")
    password = getpass.getpass()
    email = input("Enter your email address: ")

    registration_succesfull = sql_manager.register(
        username, password, email)
    if registration_succesfull:
        print("Registration Successfull")
    else:
        print("Registration failed")


def login():
    username = input("Enter your username: ")
    time = datetime.datetime.now()
    last_failed_login_time = sql_manager.get_last_failed_login(
        username)
    if last_failed_login_time is not None:
        time_passed_after_last_login = abs(
            time - last_failed_login_time)
    login_tries = sql_manager.get_login_tries(username)
    is_bruforcing = login_tries >= 5
    if is_bruforcing:
        if time_passed_after_last_login.seconds < 300:
            print('You are blocked for {} seconds'.format(
                300 - time_passed_after_last_login.seconds))
        else:
            sql_manager.clear_failures_history(username)
            print('Login failed')
    else:
        password = getpass.getpass()
        logged_user = sql_manager.login(username, password)
        if logged_user:
            logged_menu(logged_user)
            sql_manager.clear_failures_history(username)
        else:
            sql_manager.register_failed_login(username, time)
            print("Login failed")


def reset_password(username):
    entered_hash = input('Enter the send hash to reset your password: ')
    user_hash = sql_manager.get_user_reset_pass_hash(username)
    if entered_hash == user_hash:
        print('You can now change your password:')
        new_pass = getpass.getpass()
        sql_manager.reset_password(new_pass, username)
    else:
        print('Wrong hash!')


def send_email(username, subject, msg):
    import smtplib
    import json

    sender = 'stoyaneft@gmail.com'
    with open('password.json', 'r') as password_file:
        load_data = json.load(password_file)
    password = load_data['password']
    receiver = sql_manager.get_user_email(username)
    message = "\r\n".join([
        "From: {}",
        "To: {}",
        "Subject: {}",
        "",
        "{}"
    ]).format(sender, receiver, subject, msg)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        server.close()
        print ('Successfully sent the mail')
    except:
        print ("Failed to send mail")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")
        #command = 'get-tan'
        username = logged_user.get_username()

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = input("Enter your new password: ")
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'deposit':
            money = int(input('Enter amount:'))
            tan = input('Enter TAN code:')
            if tan in sql_manager.get_user_unused_tans(username):
                sql_manager.deposit(username, money)
                print('Transaction successful!')
                print('{} were deposited to the bank'.format(money))
                sql_manager.mark_tan_as_used(tan)
            else:
                print('Wrong TAN code!')

        elif command == 'withdraw':
            money = int(input('Enter amount:'))
            tan = input('Enter TAN code:')
            if tan in sql_manager.get_user_unused_tans(username):
                if sql_manager.withdraw(username, money):
                    print('Transaction successful!')
                    print('{} were withdrawed from the bank'.format(money))
                else:
                    print('Withdraw failed. Not enough money!')
                sql_manager.mark_tan_as_used(tan)
            else:
                print('Wrong TAN code!')

        elif command == 'display_balance':
            print('You have {} $ in your account'.format(
                logged_user.get_balance()))

        elif command == 'get-tan':
            unused_tans = sql_manager.get_user_unused_tans(username)
            if unused_tans:
                print(
                    'You have {} remaining TAN codes to use!'.format(
                        len(unused_tans)))
            else:
                password_correct = False
                while not password_correct:
                    password = getpass.getpass()
                    password_correct = sql_manager.is_password_correct(
                        username, password)
                    if not password_correct:
                        print('Incorrect password!')
                tans = sql_manager.generate_tans(username)
                desc_msg = 'You can use these 10 TANS in order to perform a transaction:'
                tans.insert(0, desc_msg)
                message = '\n'.join(tans)
                subject = 'TAN codes'
                send_email(username, subject, message)

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")


def main():
    sql_manager.create_clients_table()
    sql_manager.create_failed_logins_table()
    sql_manager.create_tans_table()
    main_menu()

if __name__ == '__main__':
    main()
