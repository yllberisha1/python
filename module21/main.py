from data_types import DataTypes

def main():
    data = DataTypes()

    # Display initial values
    data.display()

    # Modify some values
    data.update("list", ["banana", 2, 3, "apple", 4.5])
    data.update("dict", {"name": "John", "age": 35, "city": "New York"})
    data.update("set", {1, 2, 3, 4, 5, 6})

    # Display updated values
    print("\nUpdated data:")
    data.display()

    # Check types of variables
    print("\nTypes of variables:")
    for key in ["string", "int", "bool"]:
        print(f"{key.capitalize()} type: {data.get_type(key)}")

if __name__ == "__main__":
    main()
