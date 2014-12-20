__author__ = 'Oswald A Smith'
__title__ = 'Player'
__version__ = '1.0'
__license__ = 'MIT'



class Player(object):
    """ Implements the Player class.

    """

    def __init__(self, id, first_name, last_name, age, affiliation,
                 starter,
                 position):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._affiliation = affiliation
        self._starting_status = starter
        self._position = position

        self._display_name = self._first_name + " " + self._last_name

    @property
    def id(self):
        """Returns the player's ID number."""
        return self._id

    @id.setter
    def id(self, value):
        """Sets the player's ID to 'value'."""
        self._id = value

    @property
    def first_name(self):
        """Returns the player's first name."""
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        """Returns player's last name."""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def display_name(self):
        """Returns the player's name formatted for display."""
        return self._display_name

    @property
    def age(self):
        """Returns the player's age."""
        return self._age

    @age.setter
    def age(self, value):
        """Sets the player's age to 'value'."""
        self._age = value

    @property
    def affiliation(self):
        """Returns the player's affiliation."""
        return self._affiliation

    @affiliation.setter
    def affiliation(self, value):
        """Sets the player's affiliation to 'value'."""
        self._affiliation = value

    @property
    def starter(self):
        """Returns starting status as a boolean value."""
        return self._starting_status

    @starter.setter
    def starter(self, value):
        """Sets the player's starting status to 'value'."""
        self._starting_status = value

    @property
    def position(self):
        """Returns the player's position"""
        return self._position

    @position.setter
    def position(self, value):
        """Sets the player's position to 'value'."""
        self._position = value

    def __eq__(self, other_player):
        """Checks if two players are the same person.
        :param other_player - other player object
        :return True if equal, otherwise False
        """
        return self._id == other_player.id

    def __str__(self):
        return "Name:     {}\n".format(self._display_name) + \
                "Age:      {}\n".format(self._age)          + \
                "Team:     {}\n".format(self._affiliation)  + \
                "Position: {}\n".format(self._position)



oz = Player(1234, 'Oswald', 'Smith', 28, 'Jamaica', True, 'Striker')
ak = Player(4321, 'Anna-Kaye', 'Smith', 32, 'Jamaica', True, 'Centre')