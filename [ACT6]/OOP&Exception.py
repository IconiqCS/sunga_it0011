class Item:
    """Class to represent an item."""
    
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"


class ItemManagement:
    """Class to manage items."""
    
    def __init__(self):
        self.items = []  # List to store items

    def add_item(self, item):
        """Add an item to the list."""
        self.items.append(item)
        print("Item added successfully!")

    def view_items(self):
        """View all items."""
        if not self.items:
            print("No items found.")
            return
        print("\nItems:")
        for item in self.items:
            print(item)

    def update_item(self, item_id, name=None, description=None, price=None):
        """Update an existing item."""
        for item in self.items:
            if item.item_id == item_id:
                if name is not None:
                    item.name = name
                if description is not None:
                    item.description = description
                if price is not None:
                    item.price = price
                print("Item updated successfully!")
                return
        print("Item not found!")

    def delete_item(self, item_id):
        """Delete an item by ID."""
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                print("Item deleted successfully!")
                return
        print("Item not found!")


def main():
    """Main function to run the item management application."""
    manager = ItemManagement()  # Create an instance of ItemManagement

    while True:
        print("=====================================")
        print("Item Management Application")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        print("=====================================")

        choice = input("Enter your choice: ")

        if choice == '1':  # Add Item
            try:
                item_id = input("Enter item ID: ")
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                price = float(input("Enter item price: "))  # Convert to float
                if price < 0:  # Validate price
                    raise ValueError("Price cannot be negative.")
                new_item = Item(item_id, name, description, price)
                manager.add_item(new_item)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':  # View Items
            manager.view_items()

        elif choice == '3':  # Update Item
            item_id = input("Enter item ID to update: ")
            name = input("Enter new item name (leave blank to keep current): ")
            description = input("Enter new item description (leave blank to keep current): ")
            price_input = input("Enter new item price (leave blank to keep current): ")
            price = float(price_input) if price_input else None  # Convert to float if not empty
            manager.update_item(item_id, name if name else None, description if description else None, price)

        elif choice == '4':  # Delete Item
            item_id = input("Enter item ID to delete: ")
            manager.delete_item(item_id)

        elif choice == '5':  # Exit
            print("Exiting the application.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()  # Start the application