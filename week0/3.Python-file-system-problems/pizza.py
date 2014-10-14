from collections import defaultdict
from time import time
from datetime import datetime

current_bill = defaultdict(int)
order_files = {}


def pizza():
    full_command = input('Enter command>')
    command = full_command.split(' ')[0]
    COMMANDS = {'take': take, 'status': status,
                'save': save, 'list': list_orders}
    COMMANDS[command](full_command, current_bill)
    pizza()


def take(command, current_bill):
    command = command.split(' ')
    client_name = command[1]
    price = float(command[2])
    current_bill[client_name] += price
    print('Taking order from {0} for {1:.2f}'.format(client_name, price))


def status(command, current_bill):
    for client in current_bill:
        print(client + ' - ' + str(current_bill[client]))


def save(command, current_bill):
    ts = time()
    filename = 'orders_' + \
        datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    bill_file = open(filename + '.txt', 'a')
    for client in current_bill:
        bill_file.write(client + ' - ' + str(current_bill[client]) + '\n')
    print('Saved the current order to ' + filename)
    order_files[filename] = bill_file
    bill_file.close()


def list_orders(command, current_bill):
    for i, filename in enumerate(order_files):
        print('[' + str(i + 1) + '] - ' + filename)


def main():
    pizza()


if __name__ == '__main__':
    main()
