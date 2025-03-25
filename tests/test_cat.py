import pytest
from cat_manager.cat import Cat


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
    assert cat.energy == 35  # Adjusted for 1.5x depletion
    assert cat.hunger == 76  # Adjusted for 1.2x increase


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
