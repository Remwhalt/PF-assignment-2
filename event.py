class Event:
    def __init__(self, name, start_date, end_date, location):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location

    # Getter methods
    def get_name(self):
        return self.name

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_location(self):
        return self.location

    # Setter methods
    def set_name(self, name):
        self.name = name

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_location(self, location):
        self.location = location





