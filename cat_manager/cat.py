class Cat:
    """
    A class representing a cat with attributes for its name, age, color, energy level, and hunger level.

    The Cat class allows you to simulate common cat behaviors such as meowing, eating, playing, and sleeping.
    The cat's energy and hunger levels are dynamically adjusted based on its actions.

    Attributes:
        name (str): The name of the cat.
        age (int): The age of the cat in years.
        color (str): The color of the cat's fur.
        energy (int): The cat's energy level (0 to 100, default is 100).
        hunger (int): The cat's hunger level (0 to 100, default is 0).

    Methods:
        meow(): Prints a meowing sound based on the cat's hunger level.
        eat(food: int): Feeds the cat and adjusts hunger and energy levels.
        play(time: int): Allows the cat to play, reducing energy and increasing hunger.
        sleep(time: int): Makes the cat sleep, increasing energy.

    Behavior Rules:
        - The cat's energy and hunger levels are always kept within 0 to 100.
        - Eating decreases hunger and increases energy.
        - Playing decreases energy and increases hunger, with penalties if the cat is too tired or hungry.
        - Sleeping increases energy but only if the cat isn't already at full energy.
        - The cat's meow changes based on its hunger level."""

    def __init__(self, name: str, age: int, color: str, energy=100, hunger=0):
        """
        Initialize a Cat object with the given attributes.
        Args:
            name (str): The name of the cat.
            age (int): The age of the cat.
            color (str): The color of the cat.
            energy (int, optional): The energy level of the cat, ranging from 0 to 100. Defaults to 100.
            hunger (int, optional): The hunger level of the cat, ranging from 0 to 100. Defaults to 0.
        Attributes:
            name (str): The name of the cat.
            age (int): The age of the cat.
            color (str): The color of the cat.
            energy (int): The energy level of the cat, clamped between 0 and 100.
            hunger (int): The hunger level of the cat, clamped between 0 and 100.
        """
        self.name = name
        self.age = age
        self.color = color
        self.energy = max(0, min(energy, 100))
        self.hunger = max(0, min(hunger, 100))

    def meow(self):
        """
        Simulates the cat's meowing behavior based on its hunger level.
        The method prints different meowing sounds and corresponding emoji
        depending on the cat's hunger level:
        - Hunger < 20: Not hungry, purring and happy.
        - Hunger < 50: Satisfied, normal meow.
        - Hunger < 80: Hungry, slightly sad meow.
        - Hunger >= 80: Very hungry and irritated, loud meow.
        Attributes:
            hunger (int): The current hunger level of the cat.
        """
        if self.hunger < 20:  # Not hungry
            print("Purr... Meow! \U0001f63b")
        elif self.hunger < 50:  # Satisfied
            print("Meow! \U0001f63a")
        elif self.hunger < 80:  # Hungry
            print("Meow... \U0001f63f")
        else:
            print("MEOOOOOW!! \U0001f63e")  # Very hungry and irritated

    def eat(self, food: int):
        """
        Feeds the cat with a specified amount of food, adjusting its hunger and energy levels.
        Args:
            food (int): The amount of food to feed the cat. Must be between 0 and 100 inclusive.
        Raises:
            ValueError: If the food level is not within the valid range (0 to 100).
        Effects:
            - Decreases the cat's hunger level by the food amount, but not below 0.
            - Increases the cat's energy level by the food amount, but not above 100.
        """
        if 0 <= food <= 100:
            self.hunger = max(self.hunger - food, 0)
            self.energy = min(self.energy + food, 100)
        else:
            raise ValueError(
                f"Invalid food level: {food}. The level should be between 0 and 100."
            )

    def play(self, time: int):
        """
        Simulates the cat playing for a specified amount of time, adjusting its energy
        and hunger levels accordingly.
        Parameters:
            time (int): The duration of playtime in minutes. Must be between 0 and 100.
        Raises:
            ValueError: If the provided time is not within the range of 0 to 100.
        Behavior:
            - If the cat's energy is 30 or below, energy depletes faster (1.5x the time).
              A message is printed indicating the cat is too tired to play much.
            - Otherwise, energy decreases by the amount of time spent playing.
            - If the cat's hunger is 70 or above, hunger increases faster (1.2x the time).
              A message is printed indicating the cat is very hungry while playing.
            - Otherwise, hunger increases by the amount of time spent playing.
            - Energy and hunger levels are clamped between 0 and 100.
        """
        if 0 <= time <= 100:
            if self.energy <= 30:
                print(
                    f"{self.name.title()} is too tired to play much, energy depletes faster."
                )
                self.energy = max(self.energy - (time * 1.5), 0)
            else:
                self.energy = max(self.energy - time, 0)

            if self.hunger >= 70:
                print(f"{self.name.title()} is playing but is very hungry!")
                self.hunger = min(self.hunger + (time * 1.2), 100)
            else:
                self.hunger = min(self.hunger + time, 100)

        else:
            raise ValueError(
                "Invalid time level. The time should be between 0 and 100 minutes."
            )

    def sleep(self, time: int):
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


class DomesticCat(Cat):
    """
    DomesticCat is a subclass of Cat that represents a domesticated cat with specific behaviors.
    Attributes:
        energy (int): The energy level of the cat. Defaults to 100.
        hunger (int): The hunger level of the cat. Defaults to 0.
    Methods:
        __init__(name: str, age: int, color: str, energy=100, hunger=0):
            Initializes a DomesticCat instance with the given attributes.
        ask_for_affection():
            Displays a message indicating that the cat is seeking affection by rubbing
            against the user's leg and purring.
    """

    def __init__(self, name: str, age: int, color: str, energy=100, hunger=0):
        """
        Initialize the Cat parent class with the given attributes.
        Args:
            name (str): The name of the cat.
            age (int): The age of the cat in years.
            color (str): The color of the cat's fur.
            energy (int, optional): The energy level of the cat. Defaults to 100.
            hunger (int, optional): The hunger level of the cat. Defaults to 0.
        """
        super().__init__(name, age, color, energy, hunger)

    def ask_for_affection(self):
        """
        Displays a message indicating that the cat is seeking affection.
        This method prints a message describing the cat's behavior of rubbing
        against the user's leg and purring to request attention and affection.
        """
        print(f"{self.name} rubs against your leg and purrs, asking for affection.")
