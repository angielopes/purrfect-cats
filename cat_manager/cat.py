class Cat:

    def __init__(self, name, age, color):
        """
        Initializes a new instance of the Cat class.
        Args:
            name (str): The name of the cat.
            age (int): The age of the cat.
            color (str): The color of the cat.
            energy (int, default=100): The initial energy of the cat (default is 100).
            hunger (int, default=0): The initial hunger level of the cat (default is 0).
        """
        self.name = name
        self.age = age
        self.color = color
        self.energy = 100
        self.hunger = 0

    def meow(self):
        """
        Makes the cat meow based on its hunger level.
        The method prints different meow sounds and corresponding cat face emojis
        depending on the cat's hunger level:
        - If hunger > 70: prints "Meow!" with a happy cat face emoji.
        - If hunger > 50: prints "Meow" with a smiling cat face emoji.
        - Otherwise: prints "Meow..." with a crying cat face emoji.
        """
        if self.hunger > 70:  # Not hungry
            print("Meow!\U0001f63b")
        elif self.hunger > 50:  # Satisfied
            print("Meow\U0001f63a")
        else:  # Very hungry
            print("Meow...\U0001f63f")

    def eat(self, food):
        """
        Feeds the cat with a specified amount of food.
        Parameters:
            food (int): The amount of food to feed the cat. Must be between 0 and 100.
        Raises:
            ValueError: If the food level is not between 0 and 100.
            ValueError: If the cat's hunger level is already 0.
        """
        if self.hunger != 0:
            if 0 <= food <= 100:
                self.hunger = max(self.hunger - food, 0)
                self.energy = min(self.energy + food, 100)
            else:
                raise ValueError(
                    f"Invalid food level: {food}. The level should be between 0 and 100."
                )
        else:
            raise ValueError(f"The cat can't eat because its hunger level is 0.")


# my_cat = Cat(name="Marceline", age=2, color="Black and White")
# my_cat.hunger = 50
# my_cat.energy = 45
# my_cat.eat(20)
# print(f"Fome após comer: {my_cat.hunger}, Energia após comer: {my_cat.energy}")
