from collections import defaultdict
from time import time
from datetime import datetime
from glob import glob
import os
import re


current_order = defaultdict(int)
order_filenames = []
list_called = False
is_saved = True
discard_enabled = False
finish_prompted = False
is_finished = False


def pizza():
    full_command = input('Enter command>')
    command = full_command.split(' ')[0]
    COMMANDS = {'take': take, 'status': status, 'save': save,
                'list': list_orders, 'load': load, 'finish': finish}
    if command in COMMANDS:
        COMMANDS[command](full_command)
    else:
        print('Unknown command!\n' \
              'Try one of the following:\n'
              'take <name> <price>\n'
              'status\n'
              'save\n'
              'list\n'
              'load <number>\n'
              'finish')
    global is_finished
    if not is_finished:
        pizza()


def take(command):
    command = command.split(' ')
    client_name = command[1]
    price = float(command[2])
    current_order[client_name] += price
    global is_saved
    is_saved = False
    print('Taking order from {0} for {1:.2f}'.format(client_name, price))
    global list_called
    list_called = False


def status(command):
    for client in current_order:
        print(client + ' - ' + str(current_order[client]))
    global list_called
    list_called = False


def save(command):
    ts = time()
    filename = 'orders_' + \
        datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    order_file = open(filename + '.txt', 'a')
    for client in current_order:
        order_file.write(client + ' - ' + str(current_order[client]) + '\n')
    print('Saved the current order to ' + filename)
    order_file.close()
    global is_saved
    is_saved = True
    global list_called
    list_called = False


def list_orders(command):
    full_order_filenames = glob('*.txt')
    global order_filenames
    order_filenames = [os.path.splitext(filename)[0] for filename in full_order_filenames]
    for i, filename in enumerate(order_filenames):
        print('[' + str(i + 1) + '] - ' + filename)
    global list_called
    list_called = True


def load(command):
    global discard_enabled
    if not list_called:
        print('Use list command before loading.')
        return
    if not is_saved and not discard_enabled:
        print('You have not saved the current order.\n' \
              'If you wish to discard it, type load <number> again.')
        discard_enabled = True
        return
    command = command.split(' ')
    load_file_num = int(command[1])
    print('Loading ' + order_filenames[load_file_num - 1])
    load_file = open(order_filenames[load_file_num - 1] + '.txt', 'r')
    lines = load_file.readlines()
    global current_order
    current_order = defaultdict(int)
    for line in lines:
        client_order = re.findall('[\w.]+', line)
        current_order[client_order[0]] = float(client_order[1])
    load_file.close()
    discard_enabled = False
    global list_called
    list_called = False


def finish(command):
    global finish_prompted
    if not is_saved and not finish_prompted:
        print('You have not saved your order.\n' \
            'If you wish to continue, type finish again.\n' \
            'If you want to save your order, type save')
        finish_prompted = True
        return
    print('Finishing order. Goodbye!')
    global is_finished
    is_finished = True
    global list_called
    list_called = False


def main():
    pizza()


if __name__ == '__main__':
    main()
