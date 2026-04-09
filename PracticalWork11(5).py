from abc import ABC, abstractmethod
from enum import Enum


class Stat(Enum):
    intelligence = "Intelligence"
    strength = "Strength"
    dexterity = "Dexterity"
    mana = "Mana"
    defense = "Defense"


class Character(ABC):
    def __init__(
        self,
        name: str,
        max_hp: int,
        hp: int,
        level: int,
        intelligence: int,
        strength: int,
        dexterity: int,
        mana: int,
        defense: int,
    ):
        self._name = name
        self._max_hp = max_hp
        self._hp = hp
        self._level = level
        self._intelligence = intelligence
        self._strength = strength
        self._dexterity = dexterity
        self._mana = mana
        self._defense = defense

    @abstractmethod
    def attack(self):
        pass

    def take_damage(self, damage: int):
        actual_damage = max(0, damage - self._defense)
        self._hp -= actual_damage

        if self._hp < 0:
            self._hp = 0

    def level_up(self):
        if self._level < 20:
            self._level += 1

    def increase_stat(self, stat: Stat):
        if stat == Stat.intelligence:
            self._intelligence += 1

        elif stat == Stat.strength:
            self._strength += 1

        elif stat == Stat.dexterity:
            self._dexterity += 1

        elif stat == Stat.mana:
            self._mana += 1

        elif stat == Stat.defense:
            self._defense += 1

        else:
            print("Invalid stat")

    def rest(self):
        self._hp = self._max_hp

    def heal(self, heal_hp: int):
        self._hp += heal_hp

        if self._hp > self._max_hp:
            self._hp = self._max_hp


class Paladin(Character):
    def attack(self) -> int:
        if self._mana >= 5:
            self._mana -= 5
            return 4 * self._strength

        return 1 * self._strength

    def shield(self):
        self._defense += 4 + self._level

    def unshield(self):
        self._defense -= 4 + self._level

    def heal_ally(self, ally: Character):
        heal_hp = int(5 + 2 * self._level + 0.5 * self._mana)
        ally.heal(heal_hp)


class Mage(Character):
    def attack(self) -> int:
        if self._mana >= 3:
            self._mana -= 3
            return 3 * self._intelligence + 4

        return 1 * self._intelligence

    def fireball(self) -> int:
        if self._mana >= 5:
            self._mana -= 5
            return 2 * self._intelligence + 3

        return 1 * self._intelligence

    def heal_ally(self, ally: Character):
        heal_hp = 3 + self._level + 3 * self._intelligence
        ally.heal(heal_hp)
