from django.test import TestCase
from random import randrange
from apps.users.models import User


class ModelUnitTestCase(TestCase):
    def setUp(self):
        User.objects.create(id=1, email="user1@example.com", password="Pa$$w0rd", first_name="John", last_name="Doe")
        User.objects.create(id=2, email="user2@example.com", password="Pa$$w0rd", first_name="Jane", last_name="Smith")
        User.objects.create(id=3, email="user3@example.com", password="Pa$$w0rd", first_name="Michael",
                            last_name="Johnson"),
        User.objects.create(id=4, email="user4@example.com", password="Pa$$w0rd", first_name="Emily",
                            last_name="Williams"),
        User.objects.create(id=5, email="user5@example.com", password="Pa$$w0rd", first_name="William",
                            last_name="Jones"),
        User.objects.create(id=6, email="user6@example.com", password="Pa$$w0rd", first_name="Olivia",
                            last_name="Brown"),
        User.objects.create(id=7, email="user7@example.com", password="Pa$$w0rd", first_name="John", last_name="Davis"),
        User.objects.create(id=8, email="user8@example.com", password="Pa$$w0rd", first_name="Jane",
                            last_name="Miller"),
        User.objects.create(id=9, email="user9@example.com", password="Pa$$w0rd", first_name="Liam",
                            last_name="Wilson"),
        User.objects.create(id=10, email="user10@example.com", password="Pa$$w0rd", first_name="Jane",
                            last_name="Moore")
        return User.objects.all()

    def full_names(self):
        """Return list of "full names" from the provided `users` list."""
        return [str(user) for user in User.objects.all()]

    def test_full_names(self):
        assert self.full_names() == [
            "John Doe",
            "Jane Smith",
            "Michael Johnson",
            "Emily Williams",
            "William Jones",
            "Olivia Brown",
            "John Davis",
            "Jane Miller",
            "Liam Wilson",
            "Jane Moore",
        ]
        arr = self.full_names()
        assert arr[:2] == [
            "John Doe",
            "Jane Smith",
        ]

    def unique_first_names(self):
        """Return list of unique first names from the provided `users` list."""
        arr = [user.first_name for user in User.objects.all()]
        return list(set(arr))

    def test_unique_first_names(self):
        answer = self.unique_first_names()
        answer.sort()
        assert answer == ['Emily', 'Jane', 'John', 'Liam', 'Michael', 'Olivia', 'William']

    def find_by_id(self, id):
        """Return user dictionary from the provided `users` list matching the provided `id`."""
        user = User.objects.get(id=id)
        return {
            "id": user.id,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name
        }

    def test_find_by_id(self):
        assert self.find_by_id(9) == {
            "id": 9,
            "email": "user9@example.com",
            "first_name": "Liam",
            "last_name": "Wilson"
        }

        assert self.find_by_id(2) == {
            "id": 2,
            "email": "user2@example.com",
            "first_name": "Jane",
            "last_name": "Smith"
        }


first_names = ["John", "Jane", "Michael", "Emily", "William", "Olivia", "James", "Sophia", "Liam", "Ava"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
domains = ["yahoo.com", "hotmail.com", "example.com", "gmail.com", "aol.com"]


def user_list_factory(length=10):
    """Generate a list of fake user dictionaries."""
    users = list()
    for x in range(length):
        f, l, m = randrange(10), randrange(10), randrange(5)
        user = User()
        user.id = x
        user.first_name = first_names[f]
        user.last_name = last_names[l]
        user.email = first_names[f].lower() + last_names[f].lower() + str(x) + '@' + domains[m]
        users.append(user)
    return users


user_list = user_list_factory(length=10)
print(user_list)
