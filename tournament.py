__author__ = 'Oswald A Smith'
__title__ = 'Tournament'
__version__ = '1.0'
__license__ = 'MIT'
__copyright__ = '2014 Oswald A Smith'

class Tournament(object):
    """Implements the Tournament class.
    """
    def __init__(self, name, tourn_format, sport, city, country, start_date,
                 end_date):
        self._name = name
        self._tourn_format = tourn_format
        self._sport = sport
        self._city = city
        self._country = country
        self._start_date = start_date
        self._end_date = end_date

        self.fixtures = []  # Contains fixture object with matches to be played
        self._tourn_complete = True  # Set to true at completion to disallow
        # editing
        self._winner = None

#region Accessors / Mutators / Predicates

    @property
    def name(self):
        """Returns the name of the tournament."""
        return self._name

    @name.setter
    def name(self, value):
        """Sets the tournament name to 'value'."""
        self._name = value

    @property
    def tourn_format(self):
        """Returns the format (Single or Double Elimination) of tournament."""
        return self._tourn_format

    @tourn_format.setter
    def tourn_format(self, value):
        """Sets the tournament format to 'value'."""
        self._tourn_format = value

    @property
    def sport(self):
        """Returns the sport of the tournament."""
        return self._sport

    @sport.setter
    def sport(self, value):
        """Sets the tournament sport to 'value'.'"""
        self._sport = value

    @property
    def city(self):
        """Returns the city hosting the tournament."""
        return self._city

    @city.setter
    def city(self, value):
        """Sets the tournament city to 'value'."""
        self._city = value

    @property
    def country(self):
        """Returns the country hosting the tournament."""
        return self._country

    @country.setter
    def country(self, value):
        """Sets the tournament country to 'value'."""
        self._country = value

    @property
    def start_date(self):
        """Returns the date the tournament started / is starting."""
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        """Sets the tournament starting date to 'value'."""
        self._start_date = value

    @property
    def end_date(self):
        """Returns the date the tournament ended / is ending."""
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        """Sets the tournament end date to 'value'."""
        self._end_date = value

    @property
    def winner(self):
        """Returns the tournament winner."""
        return self._winner

    @winner.setter
    def winner(self, value):
        """Sets the tournament winner to 'value'."""
        self._winner = value
#endregion

