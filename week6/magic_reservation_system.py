from cinema import Cinema
from command_parser import CommandParser
from connections import *


cinema = Cinema(10, 10)


def create_command_parser():
    command_parser = CommandParser()
    command_parser.add_command('show_movies', show_movies)
    command_parser.add_command(
        'show_movie_projections', show_movie_projections)
    command_parser.add_command('make_reservation', make_reservation)
    command_parser.add_command('cancel_reservation', cancel_reservation)
    command_parser.add_command('exit', exit)
    command_parser.add_command('help', show_help)
    return command_parser


def show_movies():
    print('Current movies:')
    print(cinema.show_movies())


def show_movie_projections(movie_id, date=None):
    projections_info = cinema.show_movie_projections(movie_id, date)
    if date:
        print('Projections for movie {} on {}:'.format(
            projections_info['movie_name'], date))
    else:
        print('Projections for movie {}:'.format(
            projections_info['movie_name']))
    print(projections_info['projections_details'])


def show_hall(projection_id):
    occupied_seats = cinema.get_occupied_seats(projection_id)
    rows = cinema.get_rows()
    cols = cinema.get_cols()
    print(end='   ')
    for row in range(1, rows + 1):
        print(str(row), end=' ')
    print()
    for row in range(1, rows + 1):
        print(str(row), end=' ')
        if row != rows:
            print(end=' ')
        for col in range(1, cols + 1):
            if (row, col) in occupied_seats:
                print('X', end=' ')
            else:
                print('.', end=' ')
        print()


def make_reservation():
    name = input("Step 1 (User): Choose name>")
    if name == 'give_up':
        return
    number_of_tickets = input("Step 1 (User): Choose number of tickets>")
    if number_of_tickets == 'give_up':
        return
    number_of_tickets = int(number_of_tickets)
    show_movies()
    movie_id = input("Step 2 (Movie): Choose a movie>")
    if movie_id == 'give_up':
        return
    show_movie_projections(movie_id)
    projection_id = input("Step 3 (Projection): Choose a projections>")
    if projection_id == 'give_up':
        return
    print('Available seats (marked with a dot):')
    show_hall(projection_id)
    occupied_seats = cinema.get_occupied_seats(projection_id)
    chosen_seats = []
    for ticket in range(number_of_tickets):
        seat_free = False
        while not seat_free:
            seat_chosen = input(
                "Step 4 (Seats): Choose seat {}>".format(ticket + 1))
            if seat_chosen == 'give_up':
                return
            seat_chosen = tuple(int(x.strip()) for x in seat_chosen.split(','))
            if seat_chosen in occupied_seats:
                print('This seat is already taken!')
            elif seat_chosen[0] > 10 or seat_chosen[0] < 1 \
                    or seat_chosen[1] > 10 or seat_chosen[1] < 1:
                print('Lol! Cinema is 10x10.')
            else:
                seat_free = True
                occupied_seats.append(seat_chosen)
                chosen_seats.append(seat_chosen)
    print_reservation(movie_id, projection_id, chosen_seats)
    confirm = input('Step 5 (Confirm - type "finalize") >')
    if confirm == 'give_up':
        return
    if confirm == 'finalize':
        for seat in chosen_seats:
            cinema.add_reservation(name, projection_id, seat[0], seat[1])
        print('Thanks! Enjoy the movie!')


def print_reservation(movie_id, projection_id, chosen_seats):
    reservation = cinema.get_reservation(movie_id, projection_id)
    print('This is your reservation:')
    print('Movie: {} ({})'.format(reservation['movie_name'],
                                  reservation['rating']))
    print('Date and Time: {}  {} ({})'.format(
        reservation['date'], reservation['time'], reservation['type']))
    print('Seats: {}'.format(
        ', '.join([str(seat) for seat in chosen_seats])))


def cancel_reservation(name):
    cinema.cancel_reservation(name)
    print('Reservation on the name of {} was canceled.'.format(name))


def main():
    command_parser = create_command_parser()
    while True:
        command = input('>')
        command_parser.execute(command)


def exit():
    import sys
    print('Goodbye!')
    sys.exit()


def show_help():
    print('The following commands are available:')
    print('- "show_movies" - prints all movies ordered by rating')
    print('- "show_movie_projections <movie_id> [<date>]" prints all \
projections of a given movie for the given date (date is optional).')
    print('- "make_reservation" - choose a movie and reserve your seats')
    print('- "cancel_reservation <name>" disintegrates \
given person''s reservation')
    print('- "exit" - Leaves program')

if __name__ == '__main__':
    main()
