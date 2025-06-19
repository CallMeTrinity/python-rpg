from rpg.game import Game


def main():

    n = input("Combien de joueurs sont présents ? ")
    Game(int(n))

if __name__ == "__main__":
    main()