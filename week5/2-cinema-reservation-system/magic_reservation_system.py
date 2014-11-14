import sqlite3


db = sqlite3.connect('cinema.db')
db.row_factory = sqlite3.Row
cursor = db.cursor()
HALL_SIZE = 100


def get_command():
    return input('Enter command>').split(' ')


def show_movies():
    cursor.execute('''SELECT id, name, rating FROM movies ORDER BY rating
        ''')
    movies = cursor.fetchall()
    print('Current movies:')
    for movie in movies:
        print(
            "[{}] - {} ({})".format(
                movie['id'], movie['name'], movie['rating'])
        )


def print_projection_info(projection_info, tickets):
    free_seats = find_seats_available(projection_info[0])
    free_seats_info = '{} spots available'.format(free_seats)
    projection_info.append(free_seats_info)
    print(
        '[{}] - {} {} ({}) - {}'.format(*(tuple(projection_info))), end=' ')
    if tickets and tickets > free_seats:
        print('- NOT ENOUGH!')
    else:
        print()


def show_movie_projections(movie_id, date=None, tickets=None):
    if date:
        cursor.execute('''SELECT movies.name, projections.id,
        projections.time, projections.type
        FROM movies
        INNER JOIN projections
        ON movies.id = projections.movie_id
        WHERE movies.id = ? AND projections.date = ?
        ORDER BY date, time
            ''', (movie_id, date))
        projections = cursor.fetchall()
        print("Projections for movie '{}' on {}:".format(
            projections[0]['name'], date))
        for projection in projections:
            projection_info = [
                projection['id'], '', projection['time'], projection['type']]
            print_projection_info(projection_info, tickets)

    else:
        cursor.execute('''SELECT movies.name, projections.id, projections.date,
            projections.time, projections.type
            FROM movies
            INNER JOIN projections
            ON movies.id = projections.movie_id
            WHERE movies.id = ?
            ORDER BY date, time
            ''', (movie_id,))
        projections = cursor.fetchall()
        print("Projections for movie '{}':".format(projections[0]['name']))
        for projection in projections:
            projection_info = [
                projection['id'], projection['date'],
                projection['time'], projection['type']]
            print_projection_info(projection_info, tickets)



def find_seats_available(projection_id):
    seats_occupied = find_ocupied_seats(projection_id)
    return HALL_SIZE - len(seats_occupied)


def find_ocupied_seats(projection_id):
    cursor.execute('''SELECT row, col
        FROM reservations
        WHERE projection_id = ?
        ''', (projection_id,))
    occupied_seats = []
    reserved_seats = cursor.fetchall()
    for reserved_seat in reserved_seats:
        occupied_seats.append((reserved_seat['row'], reserved_seat['col']))
    return occupied_seats


def show_hall(projection_id):
    occupied_seats = find_ocupied_seats(projection_id)
    print(end='   ')
    for row in range(1, 11):
        print(str(row), end=' ')
    print()
    for row in range(1, 11):
        print(str(row), end=' ')
        if row != 10:
            print(end=' ')
        for col in range(1, 11):
            if (row, col) in occupied_seats:
                print('X', end=' ')
            else:
                print('.', end=' ')
        print()


def reserve(name, projection_id, row, col):
    cursor.execute('''
        INSERT INTO reservations(username, projection_id, row, col)
        VALUES(?, ?, ?, ?)''', (name, projection_id, row, col))
    db.commit()


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
    show_movie_projections(movie_id, False, number_of_tickets)
    projection_id = input("Step 3 (Projection): Choose a projections>")
    if projection_id == 'give_up':
        return
    print('Available seats (marked with a dot):')
    show_hall(projection_id)
    occupied_seats = find_ocupied_seats(projection_id)
    chosen_seats = []
    for ticket in range(number_of_tickets):
        seat_free = False
        while not seat_free:
            seat_chosen = input("Step 4 (Seats): Choose seat {}>".format(ticket + 1))
            if seat_chosen == 'give_up':
                return
            seat_chosen = tuple(int(x.strip()) for x in seat_chosen.split(','))
            if seat_chosen in occupied_seats:
                print('This seat is already taken!')
            elif seat_chosen[0] > 10 or seat_chosen[1] > 10:
                print('Lol! Cinema is 10x10.')
            else:
                seat_free = True
                occupied_seats.append(seat_chosen)
                chosen_seats.append(seat_chosen)
    cursor.execute('''SELECT movies.name, movies.rating, projections.date,
        projections.time, projections.type
        FROM movies
        INNER JOIN projections
        ON movies.id = projections.movie_id
        WHERE movies.id = ? AND projections.id = ?
            ''', (movie_id, projection_id))
    reservation = cursor.fetchone()
    print('This is your reservation:')
    print('Movie: {} {}'.format(reservation['name'],
                                reservation['rating']))
    print('Date and Time: {}  {} ({})'.format(
        reservation['date'], reservation['time'], reservation['type']))
    print('Seats:', end=" ")
    for seat in chosen_seats[:-1]:
        print(str(seat), end=", ")
    print(str(chosen_seats[-1]))
    confirm = input('Step 5 (Confirm - type "finalize") >')
    if confirm == 'give_up':
        return
    if confirm == 'finalize':
        for seat in chosen_seats:
            reserve(name, projection_id, seat[0], seat[1])
        print('Thanks!')


def cancel_reservation(name):
    cursor.execute('''DELETE FROM reservations WHERE username = ?
        ''', (name, ))
    db.commit()


def print_commands_available():
    print('The following commands are available:')
    print('- "show_movies" - prints all movies ordered by rating')
    print('- "show_movie_projections <movie_id> [<date>]" prints all \
projections of a given movie for the given date (date is optional).')
    print('- "make_reservation" - choose a movie and reserve your seats')
    print('- "cancel_reservation <name>" disintegrates given person''s reservation')
    print('- "exit" - Leaves program')


def main():
    while True:
        full_command = get_command()
        command = full_command[0]

        if command == 'exit':
            print('Goodbye')
            return

        elif command == 'show_movies':
            show_movies()

        elif command == 'show_movie_projections':
            movie_id = full_command[1]
            if len(full_command) == 2:
                show_movie_projections(movie_id)
            else:
                date = full_command[2]
                show_movie_projections(movie_id, date)

        elif command == 'make_reservation':
            make_reservation()

        elif command == 'cancel_reservation':
            name = full_command[1]
            cancel_reservation(name)

        elif command == 'help':
            print_commands_available()

        else:
            print('Wrong command!')
            print('Type "help" to see list of available commands.')


if __name__ == '__main__':
    find_seats_available(5)
    main()
