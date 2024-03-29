from event import Event

class SpecialEvent(Event):
    def __init__(self, name, start_date, end_date, location, special_attribute):
        super().__init__(name, start_date, end_date, location)
        self.special_attribute = special_attribute

    # Getter and setter methods for special attribute
    def get_special_attribute(self):
        return self.special_attribute

    def set_special_attribute(self, special_attribute):
        self.special_attribute = special_attribute




