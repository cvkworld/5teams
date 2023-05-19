class Desktop:
    def __init__(self, nb_network_outlets, nb_power_outlets, nb_phone_sockets, nb_chairs, nb_tables, nb_people):
        self.nb_network_outlets = nb_network_outlets
        self.nb_power_outlets = nb_power_outlets
        self.nb_phone_sockets = nb_phone_sockets
        self.nb_chairs = nb_chairs
        self.nb_tables = nb_tables
        self.nb_people = nb_people
    
    def tauxespacedispo(self):
        occupied_space = self.nb_network_outlets + self.nb_power_outlets + self.nb_phone_sockets + self.nb_chairs + self.nb_tables
        total_space = self.nb_people
        available_space = total_space - occupied_space
        return (available_space / total_space) * 100


class OfficeDeveloper(Desktop):
    def __init__(self, nb_network_outlets, nb_power_outlets, nb_phone_sockets, nb_chairs, nb_tables, nb_people):
        super().__init__(nb_network_outlets, nb_power_outlets, nb_phone_sockets, nb_chairs, nb_tables, nb_people)
    
    def tauxespacedispo(self):
        occupied_space = (3 * self.nb_network_outlets) + (3 * self.nb_power_outlets) + self.nb_phone_sockets + (1.5 * self.nb_chairs) + self.nb_tables
        total_space = self.nb_people
        available_space = total_space - occupied_space
        return (available_space / total_space) * 100


class OfficeCommercial(Desktop):
    def __init__(self, nb_network_outlets, nb_power_outlets, nb_phone_sockets, nb_chairs, nb_tables, nb_people):
        super().__init__(nb_network_outlets, nb_power_outlets, nb_phone_sockets, nb_chairs, nb_tables, nb_people)
    
    def tauxespacedispo(self):
        occupied_space = self.nb_network_outlets + self.nb_power_outlets + (2 * self.nb_phone_sockets) + (2 * self.nb_chairs) + self.nb_tables
        total_space = self.nb_people
        available_space = total_space - occupied_space
        return (available_space / total_space) * 100


# Create an instance of OfficeDeveloper
office_dev = OfficeDeveloper(4, 6, 2, 10, 5, 20)

# Calculate available space percentage for OfficeDeveloper
available_space_percentage_dev = office_dev.tauxespacedispo()
print("Available space percentage for OfficeDeveloper:", available_space_percentage_dev)

# Create an instance of OfficeCommercial
office_com = OfficeCommercial(4, 6, 2, 10, 5, 20)

# Calculate available space percentage for OfficeCommercial
available_space_percentage_com = office_com.tauxespacedispo()
print("Available space percentage for OfficeCommercial:", available_space_percentage_com)
