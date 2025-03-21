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

    def meow(self, hunger_level):
        """
        Simulates the cat's meow based on its hunger level.
        Parameters:
            hunger_level (int): An integer representing the cat's hunger level,
                            which should be between 0 and 100 inclusive.
        Raises:
            ValueError: If the hunger_level is not within the range of 0 to 100.
        The cat's meow varies depending on its hunger level:
        - If hunger_level > 70, the cat is not hungry and meows happily.
        - If 50 < hunger_level <= 70, the cat is satisfied and meows contentedly.
        - If hunger_level <= 50, the cat is very hungry and meows sadly.
        """
        if 0 <= hunger_level <= 100:
            if hunger_level > 70:  # Not hungry
                print("Meow!\U0001f63b")
            elif hunger_level > 50:  # Satisfied
                print("Meow\U0001f63a")
            else:  # Very hungry
                print("Meow...\U0001f63f")
        else:
            raise ValueError(
                f"Invalid hunger level: {hunger_level}. The cat's hunger should be between 0 and 100."
            )  # Tratar erro depois

    def eat(self, food):

        if 0 <= self.hunger < 100 and 0 <= self.energy < 100:
            if 0 <= food <= 100:
                self.hunger = max(self.hunger - food, 0)
                self.energy = min(self.energy + food, 100)
            else:
                raise ValueError(
                    f"Invalid food level: {food}. The level should be between 0 and 100."
                )
        else:
            raise ValueError(
                f"Invalid food level: {food}. The level should be between 0 and 100."
            )


my_cat = Cat(name="Marceline", age=2, color="Black and White")
my_cat.meow(0)
my_cat.eat(20)
