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
        if self.hunger < 30:  # Not hungry
            print("Meow!\U0001f63b")
        elif self.hunger < 60:  # Satisfied
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

    def play(self, time):
        """
        Allows the cat to play for a specified amount of time, adjusting its energy and hunger levels accordingly.

        Parameters:
            time (int): The amount of time the cat plays, in minutes. Must be between 0 and 100 inclusive.
        Raises:
            ValueError: If the time is not within the valid range (0 to 100 minutes).
            ValueError: If the cat's energy is 30 or less, or if its hunger is 70 or more.
        """
        if self.energy > 30 and self.hunger < 70:
            if 0 <= time <= 100:
                self.energy = max(self.energy - time, 0)
                self.hunger = min(self.hunger + time, 100)
            else:
                raise ValueError(
                    f"Invalid time level: {time}. The time should be between 0 and 100 minutes."
                )
        else:
            raise ValueError(
                "The cat cannot play right now. Check if he is hungry or has low energy."
            )

    def sleep(self, time):
        """
        Makes the cat sleep for a specified amount of time, increasing its energy level.
        Args:
            time (int): The amount of time (in minutes) the cat sleeps. Must be between 0 and 100.
        Raises:
            ValueError: If the time is not within the range of 0 to 100 minutes.
            ValueError: If the cat's energy level is already at 100 or above, indicating it is too energetic to sleep.
        Notes:
            The cat's energy level will not exceed 100, even if the time provided would result in a higher value.
        """
        if self.energy < 100:
            if 0 <= time <= 100:
                self.energy = min(self.energy + time, 100)
            else:
                raise ValueError(
                    f"Invalid time level: {time}. The time should be between 0 and 100 minutes."
                )
        else:
            raise ValueError("The cat is too energetic to sleep now.")


# <==== Quick tests ====>

my_cat = Cat(name="Marceline", age=2, color="Black and White")
my_cat.hunger = 0
my_cat.energy = 100
# my_cat.eat(20)
my_cat.play(50)
my_cat.sleep(30)
print(f"Fome: {my_cat.hunger}, Energia: {my_cat.energy}")
