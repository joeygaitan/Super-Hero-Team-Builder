import pytest
import superheroes
import random
import io
import sys

# checks the length of attacks
def test_case_for_hero_length():
    team_one = superheroes.Team("One")
    team_two = superheroes.Team("Two")
    
    assert team_one.attack(team_two) == "There isn't any heroes in the opposing team"