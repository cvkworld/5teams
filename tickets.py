from datetime import datetime

class Ticket:
    def __init__(self, date, title, amount):
        self.date = date
        self.title = title
        self.amount = amount


class CashRegister:
    def __init__(self):
        self.tickets = []

    def create_ticket(self, date, title, amount):
        for ticket in self.tickets:
            if ticket.date == date:
                return "A ticket with the same date already exists."

        new_ticket = Ticket(date, title, amount)
        self.tickets.append(new_ticket)
        return "Ticket created successfully."

    def modify_ticket(self, date, new_title, new_amount):
        for ticket in self.tickets:
            if ticket.date == date:
                ticket.title = new_title
                ticket.amount = new_amount
                return "Ticket modified successfully."

        return "No ticket found with the given date."

    def delete_ticket(self, date):
        for ticket in self.tickets:
            if ticket.date == date:
                self.tickets.remove(ticket)
                return "Ticket deleted successfully."

        return "No ticket found with the given date."

    def get_total_per_month(self, month):
        total_amount = 0
        for ticket in self.tickets:
            if ticket.date.month == month:
                total_amount += ticket.amount

        return total_amount

    def get_grand_total(self):
        total_amount = 0
        for ticket in self.tickets:
            total_amount += ticket.amount

        return total_amount


# Example usage
cash_register = CashRegister()

date_format = "%Y-%m-%d"
print(cash_register.create_ticket(datetime.strptime("2023-05-01", date_format), "Ticket 1", 100))
print(cash_register.create_ticket(datetime.strptime("2023-05-02", date_format), "Ticket 2", 200))
print(cash_register.create_ticket(datetime.strptime("2023-05-02", date_format), "Ticket 3", 300))  # Duplicate date, should return an error
print(cash_register.create_ticket(datetime.strptime("2023-06-01", date_format), "Ticket 4", 400))

print(cash_register.modify_ticket(datetime.strptime("2023-05-02", date_format), "Updated Ticket", 250))
print(cash_register.modify_ticket(datetime.strptime("2023-05-03", date_format), "Ticket 5", 500))  # Non-existent date, should return an error

cash_register.delete_ticket(datetime.strptime("2023-05-01", date_format))
cash_register.delete_ticket(datetime.strptime("2023-05-03", date_format))  # Non-existent date, should return an error

print(cash_register.get_total_per_month(5))  # Get total amount for May
print(cash_register.get_grand_total())  # Get grand total
