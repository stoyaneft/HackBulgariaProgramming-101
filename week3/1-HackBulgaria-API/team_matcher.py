from hackbg_team_matcher import HackBgTeamMatcher


def get_command():
    return input().split(' ')


def main():
    print('Hello, you can use one the the following commands:\n'
          'list_courses - this lists all the courses that are available now.\n'
          'match_teams <course_id>, <team_size>, <group_time>\n')
    team_matcher = HackBgTeamMatcher()
    full_command = get_command()
    command = full_command[0]
    if command == 'list_courses':
        print('Here are the courses:')
        team_matcher.list_courses()
        full_command = get_command()
        command = full_command[0]
        if command == 'match_teams':
            course_id = int(full_command[1])
            team_size = int(full_command[2])
            group_time = int(full_command[3])
            team_matcher.match_command(course_id, team_size, group_time)


if __name__ == '__main__':
    main()
