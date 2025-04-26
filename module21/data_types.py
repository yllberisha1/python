class DataTypes:
    def __init__(self):
        self.data = {
            "string": "Hello, Python!",
            "int": 100,
            "float": 9.99,
            "bool": False,
            "list": [1, 2, 3, "apple", 4.5],
            "tuple": (1, 2, 3, "apple", 4.5),
            "set": {1, 2, 3, 4, 5},
            "dict": {"name": "John", "age": 30, "city": "New York"},
            "none": None,
            "bytes": b"Hello",
            "bytearray": bytearray([65, 66, 67]),
            "complex": 1 + 2j
        }

    def display(self):
        for key, value in self.data.items():
            print(f"{key.capitalize()}: {value}")

    def update(self, key, value):
        if key in self.data:
            self.data[key] = value

    def get_type(self, key):
        return type(self.data.get(key, None))
