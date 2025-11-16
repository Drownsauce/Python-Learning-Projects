class Item:
    def __init__(self, name, price, stock):
        # I store the basic information for each item.
        # Every item MUST have a name, a price, and a stock count,
        # so I save them as instance attributes.
        self.name = name
        self.price = price
        self.stock = stock

    def update_price(self, new_price):
        # I created this method, so I can easily update an item's price
        # without replacing the entire object.
        self.price = new_price

    def update_stock(self, new_stock):
        # This lets me change only the stock amount for the item.
        # I added this because stock changes more often than anything else.
        self.stock = new_stock

    def __str__(self):
        # I return a clean string so whenever I print an Item object,
        # I immediately see the important information.
        return f"[{self.name.lower()}] Price: {self.price} Stock: {self.stock}"


class Category:
    def __init__(self, name, items=None):
        # A category groups many items together (like "electronics", "clothing", etc.),
        # so I store a name and a list of Item objects.
        # If no list is passed in, I create an empty one.
        self.name = name
        self.items = items if items else []

    def find_item(self, name):
        # I added this helper method, so I can quickly look up
        # an Item object by its name. It's used by multiple other methods.
        for item in self.items:
            if item.name == name:
                return item
        return None

    def add_item(self, name, price, stock):
        # When adding an item, I first check that an item with the same name
        # does not already exist in this category.
        if not self.find_item(name):
            self.items.append(Item(name, price, stock))
            return name
        return None

    def remove_item(self, name):
        # I remove the item only if it exists. This helps prevent errors.
        del_item = self.find_item(name)
        if del_item:
            self.items.remove(del_item)
            return del_item.name
        return None

    def view_items(self):
        # I display every item in the category.
        for item in self.items:
            print(item)

    def sort_items(self, sort_value):
        # I added sorting because it's useful to organize items.
        # Depending on what the user chooses, I sort by that attribute.
        match sort_value:
            case 'name':
                self.items.sort(key=lambda item: item.name)
            case 'price':
                self.items.sort(key=lambda item: item.price)
            case 'stock':
                self.items.sort(key=lambda item: item.stock)
        # After sorting, I show the result.
        self.view_items()

    def filter_by_stock(self, min_amount, max_amount):
        # I added this so the user can view items based on stock ranges.
        # This is useful for checking low-stock or high-stock items.
        for item in self.items:
            if min_amount <= item.stock <= max_amount:
                print(item)

    def __str__(self):
        # I return a readable representation of the category
        # with all its items listed.
        return f"({self.name}) {[item.__str__() for item in self.items]} "


class Store:
    def __init__(self, name, categories=None):
        # This class represents the entire store.
        # It contains multiple categories, so I store them in a list.
        self.name = name
        self.categories = categories if categories else []

    def find_category(self, name):
        # I use this helper method to quickly get a Category object by name.
        # It keeps the code in add/remove methods clean.
        for cat in self.categories:
            if cat.name == name:
                return cat
        return None

    def add_category(self, name):
        # I add a category only if one with the same name does not already exist.
        if not self.find_category(name):
            self.categories.append(Category(name))
            return name
        return None

    def remove_category(self, name):
        # To remove a category, I find it first.
        # If found, I remove it and return the name.
        remove_category = self.find_category(name)
        if remove_category:
            self.categories.remove(remove_category)
            return remove_category.name
        return None

    def view_categories(self):
        # I display all categories in the store.
        for cat in self.categories:
            print(cat)

    def total_store_value(self):
        # I calculate the total value of every item in every category.
        # This is useful for inventory valuation.
        total = 0
        for cat in self.categories:
            for item in cat.items:
                total += item.price * item.stock
        return total

    def search_item(self, name):
        # This searches through EVERY category to find an item by name.
        # I added this so users don’t need to know where the item is stored.
        for cat in self.categories:
            for item in cat.items:
                if item.name == name:
                    return item
        return None
