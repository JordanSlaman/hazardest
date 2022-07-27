from django.db import models


class CardSuits(models.TextChoices):
    DIAMONDS = 'D', 'Diamonds'
    CLUBS = 'C', 'Clubs'
    HEARTS = 'H', 'Hearts'
    SPADES = 'S', 'Spades'

    @classmethod
    def is_red(cls, suit):
        return suit in (cls.DIAMONDS, cls.HEARTS)

    @classmethod
    def is_black(cls, suit):
        return not cls.is_red(suit)


class CardValues(models.IntegerChoices):
    ACE = 1, 'Ace'
    KING = 2, 'King'
    QUEEN = 3, 'Queen'
    JACK = 4, 'Jack'
    TEN = 5, 'Ten'
    NINE = 6, 'Nine'


class GameStates(models.TextChoices):
    WAITING = 'WT', 'Waiting to Start'
    IN_PROGRESS = 'IP', 'In Progress'
    ABANDONED = 'AB', 'Abandoned'
    OVER = 'OV', 'Over'


class PlayerPositions(models.TextChoices):
    NORTH = 'N', 'North',
    EAST = 'E', 'East',
    SOUTH = 'S', 'South',
    WEST = 'W', 'West'

    @classmethod
    def valid_position(cls, team, position):
        valid_team_positions = {
            PlayerTeams.RED: (cls.NORTH, cls.SOUTH),
            PlayerTeams.BLACK: (cls.EAST, cls.WEST)
        }
        return position in valid_team_positions[team]

    @classmethod
    def left_of(cls, position):
        return {
            cls.NORTH: cls.EAST,
            cls.EAST: cls.SOUTH,
            cls.SOUTH: cls.WEST,
            cls.WEST: cls.NORTH
        }[position]


class PlayerTeams(models.TextChoices):
    RED = 'RED', 'Red'
    BLACK = 'BLK', 'Black'

