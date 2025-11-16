# Travis Delcambre
from classes import Store

# Create ONE store object for the whole program
# We keep this single instance because categories + items belong to this store
store = Store("Walmart")

while True:
    try:
        # Main menu for category-level operations
        user_cat_choice = int(input("(1. Add Category / 2. Remove Category / 3. Access Category / 4. View Categories / 5. Store Value / 6. Search Item / 7. Stop)\n> "))
    except ValueError:
        # Input validation to keep your program from crashing
        print("Must be integer (1, 2, 3, 4, 5, 6, or 7)")
        continue

    # match-case makes it easy to read and maintain
    match user_cat_choice:
        case 1:
            # ----- ADD CATEGORY -----
            category_name = input("Category name: ").strip().lower()
            new_category = store.add_category(category_name)
            if new_category:
                print(f"Added {new_category}")

        case 2:
            # ----- REMOVE CATEGORY -----
            category_name = input("Category name: ").strip().lower()
            del_category = store.remove_category(category_name)
            if del_category:
                print(f"Removed {del_category}")

        case 3:
            # ----- ACCESS CATEGORY (GO INTO SUB-MENU) -----
            store.view_categories()
            category_name = input("Category name: ").strip().lower()

            # We now get a specific Category object
            access_category = store.find_category(category_name)

            # Only if the category exists do we enter the sub-menu
            if access_category:
                while True:
                    try:
                        # Item-level menu (inside a category)
                        user_item_choice = int(input("\n(1. Add Item / 2. Remove Item / 3. View Items / 4. Sort Items / 5. Filter by Stock / 6. Update Item / 7. Stop)\n> "))
                    except ValueError:
                        print("Must be integer (1, 2, 3, 4, 5, or 6)")
                        continue

                    match user_item_choice:
                        case 1:
                            # ----- ADD ITEM -----
                            item_name = input("Item name: ").strip().lower()

                            # Input validation for numeric values
                            while True:
                                try:
                                    item_price = float(input("Item price: "))
                                    item_stock = int(input("Item stock: "))
                                    break
                                except ValueError:
                                    print("Must be a number!")

                            add_item = access_category.add_item(item_name, item_price, item_stock)
                            if add_item:
                                print(f"Added {add_item}")

                        case 2:
                            # ----- REMOVE ITEM -----
                            item_name = input("Item name: ").strip().lower()
                            del_item = access_category.remove_item(item_name)
                            if del_item:
                                print(f"Removed {del_item}")

                        case 3:
                            # ----- VIEW ITEMS -----
                            access_category.view_items()

                        case 4:
                            # ----- SORT ITEMS -----
                            # Sorting by name, price, or stock helps the user quickly organize data
                            sort_value = input("Sort by (name, price, stock): ").lower().strip()
                            access_category.sort_items(sort_value)

                        case 5:
                            # ----- FILTER BY STOCK -----
                            # Allow user to find items between two stock values
                            while True:
                                try:
                                    min_amount = int(input("Minimum Stock: "))
                                    max_amount = int(input("Maximum Stock: "))

                                    # Swap values if reversed
                                    if min_amount > max_amount:
                                        min_amount, max_amount = max_amount, min_amount
                                    break
                                except ValueError:
                                    print("Must be an integer!")

                            access_category.filter_by_stock(min_amount, max_amount)

                        case 6:
                            # ----- UPDATE ITEM -----
                            item_name = input("Item name: ").strip().lower()
                            item = access_category.find_item(item_name)

                            if item:
                                while True:
                                    try:
                                        update_choice = int(input("(1. Update Price / 2. Update Stock / 3. Stop)\n> "))
                                    except ValueError:
                                        print("Must be integer (1, 2, or 3)")
                                        continue

                                    match update_choice:
                                        case 1:
                                            # Update item price
                                            new_price = float(input("New price: "))
                                            item.update_price(new_price)

                                        case 2:
                                            # Update stock count
                                            new_stock = int(input("New stock: "))
                                            item.update_stock(new_stock)

                                        case _:
                                            break

                        case _:
                            # Breaks out of the item sub-menu
                            break

        case 4:
            # ----- VIEW ALL CATEGORIES -----
            store.view_categories()

        case 5:
            # ----- TOTAL STORE VALUE -----
            # Adds all (price * stock) for every item in every category
            total_value_stock = store.total_store_value()
            print(f"${total_value_stock}")

        case 6:
            # ----- SEARCH ANY ITEM ACROSS ALL CATEGORIES -----
            item_name = input("Item name: ").strip().lower()
            item = store.search_item(item_name)
            if item:
                print(f"Found {item.name}")
                print(item)

        case _:
            # Exit the main menu loop
            break
