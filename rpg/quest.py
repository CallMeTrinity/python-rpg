from abc import ABC, abstractmethod

from rpg.player import Player


class Quest(ABC):
    def __init__(self, title: str, description: str, victory_message: str):
        self.title = title
        self.description = description
        self.victory_message = victory_message
        self.completed = False

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def reward(self, player: Player, xp: int, gold: int):
        pass

    def mark_completed(self):
        self.completed = True
        print(self.victory_message)

class DialogQuest(Quest):
    def __init__(self, title, description, victory_message,question: str, choices: list, correct_choice: int):
        super().__init__(title, description, victory_message)
        self.question = question
        self.choices = choices
        self.correct_choice = correct_choice

    def start(self):
        print(f"{self.title} : {self.description}")
        print(f"{self.question}")

        for idx, choice in enumerate(self.choices, 1):
            print(f"[{idx}] : {choice}")
        try:
            answer = int(input("Votre réponse : "))
            if str(answer) == str(self.correct_choice):
                self.mark_completed()
            else:
                print("Perdu !")

        except (ValueError, IndexError):
            print("Entrée Invalid")

    def reward(self, player, xp, gold):
        print(f"+{xp}xp")
        print(f"+{gold} gold")
        player.add_xp(xp)
        player.gold += gold
# Maybe Class ActionQuest in the future