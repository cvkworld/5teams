import random

from desktop import OfficeCommercial, OfficeDeveloper

class Company:
    def __init__(self):
        self.sales_offices = [
            OfficeCommercial(nb_network_outlets=4, nb_power_outlets=6, nb_phone_sockets=2, nb_chairs=10, nb_tables=5, nb_people=20),
            OfficeCommercial(nb_network_outlets=4, nb_power_outlets=6, nb_phone_sockets=2, nb_chairs=10, nb_tables=5, nb_people=20),
            OfficeCommercial(nb_network_outlets=4, nb_power_outlets=6, nb_phone_sockets=2, nb_chairs=10, nb_tables=5, nb_people=20)
        ]
        self.dev_offices = [
            OfficeDeveloper(nb_network_outlets=4, nb_power_outlets=6, nb_phone_sockets=2, nb_chairs=10, nb_tables=5, nb_people=20),
            OfficeDeveloper(nb_network_outlets=4, nb_power_outlets=6, nb_phone_sockets=2, nb_chairs=10, nb_tables=5, nb_people=20)
        ]

    def add_staff(self):
        sales_count = 0
        dev_count = 0

        while True:
            office_type = random.choice(["sales", "developer"])
            if office_type == "sales":
                office = random.choice(self.sales_offices)
                if office.tauxespacedispo() > 0:
                    office.nb_people += 1
                    sales_count += 1
            else:
                office = random.choice(self.dev_offices)
                if office.tauxespacedispo() > 0:
                    office.nb_people += 1
                    dev_count += 1

            company_space_rate = self.calculate_company_space_rate()
            print("Salespeople:", sales_count)
            print("Developers:", dev_count)
            print("Sales Office Space Rate:", self.sales_offices[0].tauxespacedispo())
            print("Developer Office Space Rate:", self.dev_offices[0].tauxespacedispo())
            print("Company Space Rate:", company_space_rate)
            print("------------------------")

            if company_space_rate == 0:
                break

    def calculate_company_space_rate(self):
        total_people = 0
        total_space = 0

        for office in self.sales_offices + self.dev_offices:
            total_people += office.nb_people
            total_space += office.nb_network_outlets + office.nb_power_outlets + office.nb_phone_sockets + office.nb_chairs + office.nb_tables

        if total_people == 0:
            return 0

        return ((total_people - total_space) / total_people) * 100


# Create an instance of the Company class
company = Company()

# Add staff to the offices
company.add_staff()
