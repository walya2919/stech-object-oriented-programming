from lib.game import Game, MONEY
from lib.player import Seojin24102406


def main():
    players = [Seojin24102406(MONEY["SEED"])]
    game = Game(players, rounds=100000)
    game.play()

if __name__ == '__main__':
    main()
