class Exhibition:
    def __init__(self, start_date, end_date, location):
        self._start_date = start_date
        self._end_date = end_date
        self._location = location
        self._artworks = []  # Aggregation relationship

    # Getter methods
    def get_start_date(self):
        return self._start_date

    def get_end_date(self):
        return self._end_date

    def get_location(self):
        return self._location

    def get_artworks(self):
        return self._artworks

    # Setter methods
    def set_start_date(self, start_date):
        self._start_date = start_date

    def set_end_date(self, end_date):
        self._end_date = end_date

    def set_location(self, location):
        self._location = location

    def set_artworks(self, artworks):
        self._artworks = artworks

    # Methods to add and remove artworks
    def add_artwork(self, artwork):
        self._artworks.append(artwork)

    def remove_artwork(self, artwork):
        self._artworks.remove(artwork)


