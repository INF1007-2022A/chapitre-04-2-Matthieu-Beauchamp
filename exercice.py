#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def get_first_part_of_name(name: str) -> str:
    premierPrenom = name.split("-")[0]
    return f"Bonjour {premierPrenom.capitalize()}"


def get_random_sentence(animals, adjectives, fruits):
    animal = random.randrange(0, len(animals))
    adjective = random.randrange(0, len(adjectives))
    fruit = random.randrange(0, len(fruits))

    phrase = f"Aujourd’hui, j’ai vu un {animals[animal]} "\
    + f"s’emparer d’un panier {adjectives[adjective]} plein "\
    + f"de {fruits[fruit]}."

    return phrase


def encrypt(text, shift):
    nLetters = ord("Z") - ord("A") + 1 # ngl I don't even know
    minLetter = ord("A")

    shift = shift % nLetters

    encrypted = ""
    for letter in text:
        letterValue = ord(letter.upper()) - minLetter

        if (letter.isalpha()):
            letterValue = (letterValue + shift) % nLetters
        
        encrypted += chr(letterValue + minLetter)

    return encrypted


def decrypt(encrypted_text, shift):
    nLetters = ord("Z") - ord("A") + 1 # "A" to "A" is one letter, not 0
    minLetter = ord("A")

    shift = shift % nLetters

    decrypted = ""
    for letter in encrypted_text:
        letterValue = ord(letter) - minLetter
        
        if (letter.isalpha()):
            letterValue = (letterValue - shift) % nLetters

        decrypted += chr(letterValue + minLetter)

    return decrypted


def testEncryption():
    txt = ""
    for _ in range(random.randrange(10, 15)):
        txt += chr(random.randrange(ord("A"), ord("z")))

    key =  random.randrange(1, 1024)

    print(txt)
    txt = encrypt(txt, key)
    print(txt)
    print(decrypt(txt, key))


if __name__ == "__main__":
    parrot = "jEaN-MARC"
    print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

    animals = ("chevreuil", "chien", "pigeon")
    adjectives = ("rouge", "officiel", "lourd")
    fruits = ("pommes", "kiwis", "mangue")
    print(get_random_sentence(animals, adjectives, fruits))

    print(encrypt("ABC", 1))
    print(encrypt("abc 123 XYZ", 50))
    print(decrypt("DEF 123 ABC", 50))
    testEncryption()
