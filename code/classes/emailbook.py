#  сделать список емэйлов

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __repr__(self):
        return f"{self.name}: {self.phone_number}, {self.email}"

class Contacts:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        for cur_contact in self.contacts:
            if cur_contact.name == contact.name:
                return False
        self.contacts.append(contact)
        return True

    def rm_contact(self, contact):
        for cur_contact in self.contacts:
            if cur_contact.name == contact.name:
                self.contacts.remove(contact)
                return True
        return False

    # Ar -> Artemiy, Arina, ...
    def find_by_mask(self, mask):
        return [contact for contact in self.contacts if contact.name.startswith(mask)]



artemiy = Contact("Artemiy", "89139267132", "artfly94@gmail.com")
my_contacts = Contacts()
my_contacts.add_contact(artemiy)
also_artemiy = Contact("Artemiy", "89139267132", "artfly94@gmail.com")
my_contacts.add_contact(also_artemiy)
print(my_contacts.contacts)

# # abcd = Contact("Abcd", "89139464444", "1@example.com")
# print(abcd)
# my_contacts = Contacts()
# my_contacts.add_contact(artemiy)
# artemiy = Contact("Artemiy", "89139267132", "artfly94@gmail.com")
# my_contacts.add_contact(artemiy)
# print(my_contacts.contacts)
# abcd = Contact("Abcd", "89139464444", "1@example.com")
# if not contacts.add_contact(abcd):
#     print(f"Already existed: {abcd.name}")
# contacts.find_by_mask("A")

