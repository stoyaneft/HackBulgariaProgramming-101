import requests
import random
from collections import defaultdict


class HackBgTeamMatcher:

    HACK_BG_API_URL = 'https://hackbulgaria.com/api/students/'

    def __init__(self):
        request = requests.get(HackBgTeamMatcher.HACK_BG_API_URL, verify=False)
        if request.status_code != requests.codes.ok:
            request.raise_for_status()
        self.api_data = request.json()
        self.available_courses = defaultdict(list)
        self.id_to_name = []

    def list_courses(self):
        for person in self.api_data:
            for course in person['courses']:
                self.available_courses[course['name']].append((
                    person['name'], course['group'], person['available']))
        for i, course in enumerate(self.available_courses):
            print('[' + str(i + 1) + '] ' + course)
            self.id_to_name.append(course)

    def match_command(self, course_id, team_size, group_time):
        courses = self.available_courses[self.id_to_name[course_id - 1]]
        people_available = [course[0] for course in courses if (
            (group_time == course[1]) and course[2])]
        print(people_available)
        random.shuffle(people_available)
        print('==================')
        for index in range(0, len(people_available), team_size):
            for person in people_available[index: index + team_size]:
                print(person)
            print('==================')
