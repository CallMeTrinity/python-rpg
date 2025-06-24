from abc import ABC, abstractmethod

from rpg.player import Player


class Quest(ABC):
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        self.completed = False

    @abstractmethod
    def start(self):
        pass

    def mark_completed(self):
        self.completed = True
        print(f"✅ Quête '{self.title}' complétée !")

class DialogQuest(Quest):
    def __init__(self, title, description, question, choices, correct_choice):
        super().__init__(title, description)
        self.question = question
        self.choices = choices
        self.correct_choice = correct_choice

    def start(self):
        print(f"{self.title} : {self.description}")
        print(f"{self.question}")

        for idx, choice in enumerate(self.choices, 1):
            print(f"{idx} : {choice}")
        try:
            answer = int(input("Votre réponse : "))
            if self.choices[answer - 1] == self.correct_choice:
                self.mark_completed()
            else:
                print("Perdu !")

        except (ValueError, IndexError):
            print("Entrée Invalid")

# Maybe Class ActionQuest in the future