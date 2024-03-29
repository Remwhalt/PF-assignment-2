class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, exhibition_location):
        self._title = title
        self._artist = artist
        self._date_of_creation = date_of_creation
        self._historical_significance = historical_significance
        self._exhibition_location = exhibition_location

    # Getter methods
    def get_title(self):
        return self._title

    def get_artist(self):
        return self._artist

    def get_date_of_creation(self):
        return self._date_of_creation

    def get_historical_significance(self):
        return self._historical_significance

    def get_exhibition_location(self):
        return self._exhibition_location

    # Setter methods
    def set_title(self, title):
        self._title = title

    def set_artist(self, artist):
        self._artist = artist

    def set_date_of_creation(self, date_of_creation):
        self._date_of_creation = date_of_creation

    def set_historical_significance(self, historical_significance):
        self._historical_significance = historical_significance

    def set_exhibition_location(self, exhibition_location):
        self._exhibition_location = exhibition_location


