from lib.scoreboard import Scoreboard
from lib.database import Database
from lib.async_wrapper import AsyncWrapper
from lib.db_attributes import ATTRIBUTES


class User:
    def __init__(self, username=None):
        self.score = 0
        self.username = username

    @AsyncWrapper.background
    def initialize_database(self):
        try:
            Database.initialize(database=ATTRIBUTES["database"],
                                host=ATTRIBUTES["host"],
                                user=ATTRIBUTES["user"],
                                password=ATTRIBUTES["password"])
        except:
            pass

    def save_score_to_db(self):
        try:
            Scoreboard.save_record(self.username, self.score)
        except:
            pass

    def add_score(self):
        self.score += 1

    @staticmethod
    def view_record_table():
        try:
            return Scoreboard.view_record()
        except:
            return None
