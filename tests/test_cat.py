import pytest
from cat_manager.cat import Cat
from cat_manager.cat import WildCat


def test_meow_not_hungry(capfd):
    """
    Test that the cat meows with a happy face emoji when not hungry.
    """
    cat = Cat(name="TestCat", age=3, color="Gray")
    cat.hunger = 10
    cat.meow()
    out, err = capfd.readouterr()
    assert out.strip() == "Purr... Meow! \U0001f63b"


def test_meow_satisfied(capfd):
    """
    Test that the Cat's meow method outputs the correct satisfied meow sound.
    """
    cat = Cat(name="TestCat", age=3, color="Gray")
    cat.hunger = 30
    cat.meow()
    out, err = capfd.readouterr()
    assert out.strip() == "Meow! \U0001f63a"


def test_meow_hungry(capfd):
    """
    Test the meow method of the Cat class when the cat is hungry.
    """
    cat = Cat(name="TestCat", age=3, color="Gray")
    cat.hunger = 60
    cat.meow()
    out, err = capfd.readouterr()
    assert out.strip() == "Meow... \U0001f63f"


def test_meow_very_hungry(capfd):
    """
    Test the meow method of the Cat class when the cat is very hungry.
    """
    cat = Cat(name="TestCat", age=3, color="Gray")
    cat.hunger = 90
    cat.meow()
    out, err = capfd.readouterr()
    assert out.strip() == "MEOOOOOW!! \U0001f63e"


def test_eat_valid_food():
    """
    Test that the cat's hunger decreases and energy increases when fed with valid food amount.
    """
    cat = Cat(name="TestCat", age=3, color="Gray")
    cat.hunger = 50
    cat.energy = 50
    cat.eat(30)
    assert cat.hunger == 20
    assert cat.energy == 80


def test_eat_invalid_food_amount():
    """
    Test that the eat method raises a ValueError when an invalid food amount is provided.
    """
    cat = Cat(name="TestCat", age=3, color="Gray")
    with pytest.raises(ValueError):
        cat.eat(150)


def test_eat_max_energy():
    """
    Test that the cat's energy does not exceed 100 when fed.
    """
    cat = Cat(name="TestCat", age=3, color="Gray")
    cat.hunger = 50
    cat.energy = 90
    cat.eat(20)
    assert cat.energy == 100


def test_play_valid_time():
    """
    Test that the cat's energy decreases and hunger increases when it plays for a valid amount of time.
    """
    cat = Cat(name="TestCat", age=3, color="Gray")
    cat.energy = 80
    cat.hunger = 40
    cat.play(30)
    assert cat.energy == 50
    assert cat.hunger == 70


def test_play_low_energy():
    """
    Test that when the cat has 30 or less energy, it depletes faster (1.5x).
    """
    cat = Cat(name="TestCat", age=3, color="Gray")
    cat.energy = 30
    cat.hunger = 40
    cat.play(20)
    assert cat.energy == 0  # 1.5x depletion
    assert cat.hunger == 60  # 1.2x increase


def test_play_invalid_time():
    """
    Test that the play method raises a ValueError when an invalid time is provided.
    """
    cat = Cat(name="TestCat", age=3, color="Gray")
    with pytest.raises(ValueError):
        cat.play(150)


def test_sleep_valid_time():
    """
    Test that the cat's energy increases when it sleeps for a valid amount of time.
    """
    cat = Cat(name="TestCat", age=3, color="Gray")
    cat.energy = 50
    cat.sleep(30)
    assert cat.energy == 80


def test_sleep_invalid_time():
    """
    Test that the sleep method raises a ValueError when an invalid time is provided.
    """
    cat = Cat(name="TestCat", age=3, color="Gray")
    with pytest.raises(ValueError):
        cat.sleep(150)


def test_sleep_max_energy():
    """
    Test that the sleep method raises a ValueError when the cat's energy is already at maximum.
    """
    cat = Cat(name="TestCat", age=3, color="Gray")
    cat.energy = 100
    with pytest.raises(ValueError):
        cat.sleep(20)


def test_wildcat_rest_increases_energy(monkeypatch):
    """
    Test that the WildCat's rest method increases energy by a random amount.
    """
    cat = WildCat(name="WildTestCat", age=4, color="Brown")
    cat.energy = 0

    # Mock randint to control the random energy increase
    monkeypatch.setattr("cat_manager.cat.randint", lambda a, b: 30)
    cat.rest()
    assert cat.energy == 30


def test_wildcat_hunt_success(monkeypatch):
    """
    Test that the WildCat successfully hunts prey and adjusts energy and hunger levels.
    """
    cat = WildCat(name="WildTestCat", age=4, color="Brown")
    cat.energy = 50
    cat.hunger = 50

    # Mock methods to control behavior
    monkeypatch.setattr(cat, "determine_prey_size", lambda: "medium")
    monkeypatch.setattr(
        cat, "calculate_success", lambda prey_size: 100
    )  # Always succeed
    monkeypatch.setattr(
        "cat_manager.cat.randint", lambda a, b: 30
    )  # Fixed random values

    cat.hunt()
    assert cat.energy == 80  # +30 energy
    assert cat.hunger == 20  # -30 hunger


def test_wildcat_hunt_failure(monkeypatch):
    """
    Test that the WildCat fails to hunt prey and loses energy.
    """
    cat = WildCat(name="WildTestCat", age=4, color="Brown")
    cat.energy = 50
    cat.hunger = 50

    # Mock methods to control behavior
    monkeypatch.setattr(cat, "determine_prey_size", lambda: "medium")
    monkeypatch.setattr(cat, "calculate_success", lambda prey_size: 0)  # Always fail

    cat.hunt()
    assert cat.energy == 40  # -10 energy
    assert cat.hunger == 50  # Hunger remains unchanged


def test_wildcat_can_hunt(monkeypatch):
    """
    Test the can_hunt method for different conditions.
    """
    cat = WildCat(name="WildTestCat", age=4, color="Brown")

    # Case: Too hungry and exhausted
    cat.energy = 0
    cat.hunger = 100
    assert not cat.can_hunt()

    # Case: Not hungry
    cat.energy = 50
    cat.hunger = 0
    assert not cat.can_hunt()

    # Case: Can hunt
    cat.hunger = 50
    assert cat.can_hunt()


def test_wildcat_determine_prey_size():
    """
    Test the determine_prey_size method for different energy and hunger levels.
    """
    cat = WildCat(name="WildTestCat", age=4, color="Brown")

    # Case: Large prey
    cat.energy = 90
    cat.hunger = 10
    assert cat.determine_prey_size() == "large"

    # Case: Medium prey
    cat.energy = 50
    cat.hunger = 50
    assert cat.determine_prey_size() == "medium"

    # Case: Small prey
    cat.energy = 20
    cat.hunger = 80
    assert cat.determine_prey_size() == "small"


def test_wildcat_calculate_success():
    """
    Test the calculate_success method for different prey sizes and conditions.
    """
    cat = WildCat(name="WildTestCat", age=4, color="Brown")

    # Case: Large prey with low energy and high hunger
    cat.energy = 20
    cat.hunger = 90
    assert cat.calculate_success("large") == 30  # Adjusted for new logic

    # Case: Medium prey with balanced energy and hunger
    cat.energy = 50
    cat.hunger = 50
    assert cat.calculate_success("medium") == 50

    # Case: Small prey with high energy and low hunger
    cat.energy = 90
    cat.hunger = 10
    assert cat.calculate_success("small") == 60  # +10 for small prey

    # Case: Large prey with high energy and low hunger
    cat.energy = 90
    cat.hunger = 10
    assert cat.calculate_success("large") == 40  # -10 for large prey


def test_wildcat_process_hunt_result_success(monkeypatch):
    """
    Test the process_hunt_result method when the hunt is successful.
    """
    cat = WildCat(name="WildTestCat", age=4, color="Brown")
    cat.energy = 50
    cat.hunger = 50

    # Mock random values
    monkeypatch.setattr("cat_manager.cat.randint", lambda a, b: 20)

    cat.process_hunt_result("medium", success=True)
    assert cat.energy == 70  # +20 energy
    assert cat.hunger == 30  # -20 hunger


def test_wildcat_process_hunt_result_failure():
    """
    Test the process_hunt_result method when the hunt fails.
    """
    cat = WildCat(name="WildTestCat", age=4, color="Brown")
    cat.energy = 50
    cat.hunger = 50

    cat.process_hunt_result("medium", success=False)
    assert cat.energy == 40  # -10 energy
    assert cat.hunger == 50  # Hunger remains unchanged
