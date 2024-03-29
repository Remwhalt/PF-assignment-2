class Visitor:
    def __init__(self, visitor_id, membership_status, preferences, contact_information, age):
        self._visitor_id = visitor_id
        self._membership_status = membership_status
        self._preferences = preferences
        self._contact_information = contact_information
        self.age= age

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
        return self._age


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
        self._age = age


    # Method to update contact information
    def update_contact_information(self, contact_info):
        self._contact_information = contact_info

    # Method to purchase ticket
    def purchase_ticket(self, ticket):
        return TicketPurchase(self, ticket)


