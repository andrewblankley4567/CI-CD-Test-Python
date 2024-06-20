from oop import *
import pytest

@pytest.fixture
def getJackRussell():
    return JackRussellTerrier("Miles", 4)

@pytest.fixture
def getDachshund():
    return Dachshund("Danny", 5)

def test_speak(getJackRussell, getDachshund):
    miles = getJackRussell
    danny =  getDachshund
    assert(miles.speak() == "Miles says Arf")
    assert(miles.speak("Grrr") == "Miles says Grrr")
    assert(miles.age != 2)
    assert(danny.speak("Danny says bark"))
    assert(danny.__str__() == "Danny is 5 years old") 
