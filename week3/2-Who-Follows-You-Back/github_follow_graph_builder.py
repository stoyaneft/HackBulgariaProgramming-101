import requests
from directed_graph import DirectedGraph


class GithubFollowGraph:

    FOLLOWING_URL = 'https://api.github.com/users/{}/following'
    with open('token.txt', 'r') as token_file:
        content = token_file.readline()[:-1]
        token = (content, '')

    def __init__(self, username, depth):
        self.graph = DirectedGraph()
        self.main_user = username
        self.depth = depth
        followers = [self.main_user]
        current_depth = 0
        while current_depth < depth:
            new_followers = []
            for follower in followers:
                followings = GithubFollowGraph._get_following(follower)
                new_followers.extend(followings)
                for following in followings:
                    self.graph.add_edge(follower, following)
            followers = new_followers
            current_depth += 1

    @staticmethod
    def _get_following(username):
        url = GithubFollowGraph.FOLLOWING_URL.format(username)
        request = requests.get(url, auth=GithubFollowGraph.token)
        request.raise_for_status()
        following = [person['login'] for person in request.json()]
        return following

    def following(self):
        return list(self.graph.get_neighbours_for(self.main_user))

    def is_following(self, username):
        return username in self.following()

    def steps_to(self, username):
        last_level = [self.main_user]
        counter = 0
        while counter <= self.depth:
            next_level = set()
            if username in last_level:
                return counter
            for person in last_level:
                next_level = next_level.union(
                    self.graph.get_neighbours_for(person))
            last_level = next_level
            counter += 1
        return 0
