import pytest
from cat_manager.cat import Cat


def test_meow_not_hungry(capfd):
    """
    Test that the cat meows with a happy face emoji when not hungry.
    """
    cat = Cat(name="TestCat", age=3, color="Gray")
    cat.meow(80)
    out, err = capfd.readouterr()
    assert out.strip() == "Meow!\U0001f63b"


def test_meow_satisfied(capfd):
    """
    Test that the Cat's meow method outputs the correct satisfied meow sound.
    """
    cat = Cat(name="TestCat", age=3, color="Gray")
    cat.meow(60)
    out, err = capfd.readouterr()
    assert out.strip() == "Meow\U0001f63a"


def test_meow_very_hungry(capfd):
    """
    Test the meow method of the Cat class when the cat is very hungry.
    """
    cat = Cat(name="TestCat", age=3, color="Gray")
    cat.meow(30)
    out, err = capfd.readouterr()
    assert out.strip() == "Meow...\U0001f63f"


def test_meow_invalid_hunger_level():
    """
    Test that the Cat.meow method raises a ValueError when an invalid hunger level is provided.
    """
    cat = Cat(name="TestCat", age=3, color="Gray")
    with pytest.raises(ValueError):
        cat.meow(150)
