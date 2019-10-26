from collections import Counter
from collections import OrderedDict


class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def player_rank(self, rank):
        return None


table = LeagueTable(['Mike', 'Chris', 'Arnold'])
table.record_result('Mike', 2)
table.record_result('Mike', 3)
table.record_result('Arnold', 5)
table.record_result('Chris', 5)
print(table.player_rank(1))


# 11. PathPYTHON  DATA STRUCTURES  STRINGS  PUBLIC
# Write a function that provides change directory (cd) function for an abstract file system.
#
# Notes:
#
# Root path is '/'.
# Path separator is '/'.
# Parent directory is addressable as '..'.
# Directory names consist only of English alphabet letters (A-Z and a-z).
# The function should support both relative and absolute paths.
# The function will not be passed any invalid paths.
# Do not use built-in path-related functions.

class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        pass

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)