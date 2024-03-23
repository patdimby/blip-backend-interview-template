users = [
  {
    "id": 1,
    "email": "user1@example.com",
    "first_name": "John",
    "last_name": "Doe"
  },
  {
    "id": 2,
    "email": "user2@example.com",
    "first_name": "Jane",
    "last_name": "Smith"
  },
  {
    "id": 3,
    "email": "user3@example.com",
    "first_name": "Michael",
    "last_name": "Johnson"
  },
  {
    "id": 4,
    "email": "user4@example.com",
    "first_name": "Emily",
    "last_name": "Williams"
  },
  {
    "id": 5,
    "email": "user5@example.com",
    "first_name": "William",
    "last_name": "Jones"
  },
  {
    "id": 6,
    "email": "user6@example.com",
    "first_name": "Olivia",
    "last_name": "Brown"
  },
  {
    "id": 7,
    "email": "user7@example.com",
    "first_name": "John",
    "last_name": "Davis"
  },
  {
    "id": 8,
    "email": "user8@example.com",
    "first_name": "Jane",
    "last_name": "Miller"
  },
  {
    "id": 9,
    "email": "user9@example.com",
    "first_name": "Liam",
    "last_name": "Wilson"
  },
  {
    "id": 10,
    "email": "user10@example.com",
    "first_name": "Jane",
    "last_name": "Moore"
  }
]

def full_names(users):
    """Return list of "full names" from the provided `users` list."""
    return users

def test_full_names():
    assert full_names(users) == [
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

    assert full_names(users[:2]) == [
        "John Doe",
        "Jane Smith",
    ]


def unique_first_names(users):
    """Return list of unique first names from the provided `users` list."""
    return users

def test_unique_first_names():
    answer = unique_first_names(users)
    answer.sort()
    assert answer  == ['Emily', 'Jane', 'John', 'Liam', 'Michael', 'Olivia', 'William']


def find_by_id(users, id):
    """Return user dictionary from the provided `users` list matching the provided `id`."""
    return {}

def test_find_by_id():
    assert find_by_id(users, 9) == {
        "id": 9,
        "email": "user9@example.com",
        "first_name": "Liam",
        "last_name": "Wilson"
    }

    assert find_by_id(users, 2) == {
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
    return users