from oop import *

def test_speak():
    miles = JackRussellTerrier("Miles", 4)
    danny =  Dachshund("Danny", 5)

    assert(miles.speak() == "Arf")
    assert(miles.speak("Grrr") == "Miles says Grrr")
    assert(miles.age == 4)
    assert(danny.speak("Danny says bark"))
    assert(print(danny) == "Danny is 5 years old") 