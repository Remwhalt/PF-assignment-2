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

