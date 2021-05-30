class Food:
    """
    This is a class that mostly just contains data members relating to products at the store. The only thing it is
    capable of doing besides storing data members is being able to decrease the quantity of that product.
    """
    def __init__(self, title, description, protein, carbs, fat):
        """
        initialization method that initializes attributes of the product such as the id code, the name, a description,
        price and quantity available
        """
        self._title = title
        self._description = description
        self._protein = protein
        self._carbs = carbs
        self._fat = fat

    def get_title(self):
        """
        get method that returns the title of the product
        """
        return self._title

    def get_description(self):
        return self._description

    def get_protein(self):
        """
        get method for the description of the product
        """
        return self._protein

    def get_carbs(self):
        """
        get method for the price of the product
        """

        return self._carbs

    def get_fat(self):
        """
        get method for how much of the product is available
        """
        return self._fat


class Person:
    """
    This is a class that stores information about the customer. Stuff like membership status, name, and what is in
    their cart
    """
    def __init__(self, name, daily_protein, daily_carbs, daily_fat, daily_cals):
        """
        Change this to have parameters of all the daily macros.
        """
        self._name = name
        self._intake = []
        self._daily_protein = daily_protein
        self._daily_carbs = daily_carbs
        self._daily_fat = daily_fat
        self._daily_cals = daily_cals
        self._protein_consumed = 0.0
        self._carbs_consumed = 0.0
        self._fats_consumed = 0.0
        self._cals_consumed = 0.0

    def get_name(self):
        """
        get method that returns the person's name
        """
        return self._name

    def add(self, food):
        """
        function that adds food to the person's intake
        """
        self._intake.append(food)

    def empty_intake(self):
        """
        function used to empty customer's cart
        """
        self._intake = []

    def get_intake(self):
        """
        get method that returns the customer's cart. Technically wasn't required but it made the assignment much easier
        """
        return self._intake

    def get_daily_protein(self):
        return self._daily_protein

    def get_daily_carbs(self):
        return self._daily_carbs

    def get_daily_fat(self):
        return self._daily_fat

    def get_daily_cals(self):
        return self._daily_cals

    def get_protein_consumed(self):
        return self._protein_consumed

    def get_carbs_consumed(self):
        return self._carbs_consumed

    def get_fat_consumed(self):
        return self._fats_consumed

    def get_cals_consumed(self):
        return self._cals_consumed

    def macros_consumed(self):

        for food in self.get_intake():
            #self._protein_consumed += float(food.get_protein()) * float(food.get_servings())
            #self._carbs_consumed += float(food.get_carbs()) * float(food.get_servings())
            #self._fats_consumed += float(food.get_fat()) * float(food.get_servings())
            self._protein_consumed += float(food.get_protein())
            self._carbs_consumed += float(food.get_carbs())
            self._fats_consumed += float(food.get_fat())
        p = self.get_protein_consumed()
        c = self.get_carbs_consumed()
        f = self.get_fat_consumed()
        self._cals_consumed = float((p * 4.0) + (c * 4.0) + (f * 9.0))

        #print("Protein consumed:", p)
        #print("Carbohydrates consumed:", c)
        #print("Fats consumed:", f)
        return "Total calories consumed: "+str(self.get_cals_consumed())


class Library:

    def __init__(self):
        """
        initialization method that has private data members store_inventory and membership_list. These private data
        members are both lists that hold inventory information and a membership list.
        """
        self._inventory = []
        self._person_list = []

    def get_inventory(self):
        return self._inventory

    def add_food(self, food):
        """
        function that adds products to the stores inventory
        """
        self._inventory.append(food)

    def add_person(self, person):
        """
        function that adds members to the stores membership list
        """
        self._person_list.append(person)

    def get_product_from_title(self, product_title):
        """
        function that gets a product from the store's inventory if the product exists.
        """

        for food in self.get_inventory():
            if food.get_title() == product_title:
                return food
        return None

    def get_person_from_name(self, person_name):
        """
        function that returns a member's information (object) if the id can be verified in the membership list
        """
        for person in self._person_list:
            if person.get_name() == person_name:
                return person
        return None

    def product_search(self, search_str):
        """
        This is a keyword search that takes in a one word string and uses the one word string to search for food
        titles and descriptions. Then returns the foods that match.
        :return: a list of product titles(s)
        """
        matches = []
        for food in self._inventory:
            if search_str.lower() in food.get_title().lower() or search_str.lower() in food.get_description().lower():
                matches.append(food.get_title())
        matches.sort()
        return matches

    def add_to_intake(self, food_title, servings, person_name='Treven'):
        """
        Adds a product object to the customer cart data member if it exists.
        """
        product_check = self.get_product_from_title(food_title)
        person_check = self.get_person_from_name(person_name)

        if product_check is None:
            return "product not found"
        elif person_check is None:
            return "Person does not exist"
        else:
            if servings % 1 != 0:
                for i in range(int(servings // 1)):
                    person_check.add(product_check)
                rdr = servings % 1
                descrip = "This adds calories from foods where a non-integer amount of servings where taken in"
                temp_food = Food("temporary food", descrip, product_check.get_protein() * rdr, product_check.get_carbs() * rdr, product_check.get_fat() * rdr)
                person_check.add(temp_food)
                return "added to intake"
            else:
                for i in range(servings):
                    person_check.add(product_check)
                return "added to intake"

