# artwork.py
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




# exhibition.py
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


# ticket.py
class Ticket:
    def __init__(self, ticket_type, availability, purchase_date, redemption_status, purchase_method):
        self._ticket_type = ticket_type
        self._availability = availability
        self._purchase_date = purchase_date
        self._redemption_status = redemption_status
        self._purchase_method = purchase_method

    # Getter methods
    def get_ticket_type(self):
        return self._ticket_type

    def get_availability(self):
        return self._availability

    def get_purchase_date(self):
        return self._purchase_date

    def get_redemption_status(self):
        return self._redemption_status

    def get_purchase_method(self):
        return self._purchase_method

    # Setter methods
    def set_ticket_type(self, ticket_type):
        self._ticket_type = ticket_type

    def set_availability(self, availability):
        self._availability = availability

    def set_purchase_date(self, purchase_date):
        self._purchase_date = purchase_date

    def set_redemption_status(self, redemption_status):
        self._redemption_status = redemption_status

    def set_purchase_method(self, purchase_method):
        self._purchase_method = purchase_method

    # Methods to mark ticket as redeemed and update availability
    def mark_as_redeemed(self):
        self._redemption_status = True

    def update_availability(self, status):
        self._availability = status


# visitor.py
class Visitor:
    def __init__(self, visitor_id, membership_status, preferences, contact_information, age):
        self._visitor_id = visitor_id
        self._membership_status = membership_status
        self._preferences = preferences
        self._contact_information = contact_information
        self.age = age

    # Getter methods
    def get_visitor_id(self):
        return self._visitor_id

    def get_membership_status(self):
        return self._membership_status

    def get_preferences(self):
        return self._preferences

    def get_contact_information(self):
        return self._contact_information

    def get_age(self):
        return self.age

    # Setter methods
    def set_visitor_id(self, visitor_id):
        self._visitor_id = visitor_id

    def set_membership_status(self, membership_status):
        self._membership_status = membership_status

    def set_preferences(self, preferences):
        self._preferences = preferences

    def set_contact_information(self, contact_information):
        self._contact_information = contact_information

    def set_age(self, age):
        self.age = age

    # Method to update contact information
    def update_contact_information(self, contact_info):
        self._contact_information = contact_info

    # Method to purchase ticket
    def purchase_ticket(self, ticket):
        return TicketPurchase(self, ticket)


# ticket_purchase.py
class TicketPurchase:
    def __init__(self, visitor, ticket_type, ticket):
        self.visitor = visitor
        self.ticket_type = ticket_type
        self.ticket = ticket

    def calculate_total_price(self):
        """
        Calculate the total price of the ticket purchase based on visitor's age, membership status, and ticket type.
        """
        if self.ticket_type == "Special Event":
            return self.ticket.price
        else:
            base_price = self.ticket.price
            if self.visitor.age < 18 or self.visitor.age >= 60 or self.visitor.membership_status == "Student" or self.visitor.membership_status == "Teacher":
                return 0  # Free ticket for children, seniors, students, and teachers
            elif self.visitor.membership_status == "Group":
                return base_price * 0.5  # 50% discount for groups
            else:
                total_price = base_price * 1.05  # Add 5% VAT
                return total_price

    # Getter and setter methods
    def get_visitor(self):
        return self.visitor

    def set_visitor(self, visitor):
        self.visitor = visitor

    def get_ticket_type(self):
        return self.ticket_type

    def set_ticket_type(self, ticket_type):
        self.ticket_type = ticket_type

    def get_ticket(self):
        return self.ticket

    def set_ticket(self, ticket):
        self.ticket = ticket


# event.py
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





# special_event.py
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

# Test cases for Artwork class
print("--- Test Cases for Artwork ---")
artwork1 = Artwork("Creativeness", "Reem", "1896", "Renaissance painting", "Gallery 111")
print("Artwork 1 Title:", artwork1.get_title())
print("Artwork 1 Artist:", artwork1.get_artist())
print("Artwork 1 Date of Creation:", artwork1.get_date_of_creation())
print("Artwork 1 Historical Significance:", artwork1.get_historical_significance())
print("Artwork 1 Exhibition Location:", artwork1.get_exhibition_location())

# Test cases for Exhibition class
print("\n--- Test Cases for Exhibition ---")
exhibition1 = Exhibition("2024-04-01", "2024-06-30", "ADNEC")
print("Exhibition 1 Start Date:", exhibition1.get_start_date())
print("Exhibition 1 End Date:", exhibition1.get_end_date())
print("Exhibition 1 Location:", exhibition1.get_location())

# Test cases for Ticket class
print("\n--- Test Cases for Ticket ---")
ticket1 = Ticket("Regular", True, "2024-04-01", False, "Online")
print("Ticket 1 Type:", ticket1.get_ticket_type())
print("Ticket 1 Availability:", ticket1.get_availability())
print("Ticket 1 Purchase Date:", ticket1.get_purchase_date())
print("Ticket 1 Redemption Status:", ticket1.get_redemption_status())
print("Ticket 1 Purchase Method:", ticket1.get_purchase_method())

# Creating an instance of the Visitor class with age attribute
visitor1 = Visitor("12345", "Regular", "Art enthusiast", "example@example.com", 25)
# Test case to verify the age attribute
print("Visitor 1 Age:", visitor1.get_age())  # Expected output: 25

# Test cases for TicketPurchase class
print("\n--- Test Cases for TicketPurchase ---")
ticket_purchase1 = TicketPurchase(visitor1, "Regular", ticket1)
print("Ticket Purchase 1 Visitor:", ticket_purchase1.get_visitor().get_visitor_id())
print("Ticket Purchase 1 Ticket Type:", ticket_purchase1.get_ticket_type())
print("Ticket Purchase 1 Ticket Availability:", ticket_purchase1.get_ticket().get_availability())