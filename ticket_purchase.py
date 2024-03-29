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


