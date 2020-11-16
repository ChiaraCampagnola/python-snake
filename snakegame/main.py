#!/usr/bin/env python3

''' Main file, controls game flow '''

import argparse

from snakegame.play import play
from snakegame.utils import get_high_score, save_high_score


def main():
    ''' Parse arguments '''

    parser = argparse.ArgumentParser(description='A simple game of snake.')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-s', '--score', help='Show the current high score', 
                    action='store_const', const=True)
    group.add_argument('-r', '--reset', help='Reset the current high score', 
                    action='store_const', const=True)
    args = parser.parse_args()

    if args.score:
        highscore = get_high_score()
        print(f"Current high score: {highscore}")
    elif args.reset:
        old_highscore = get_high_score()
        save_high_score(0)
        print(f'The highscore has been reset. It was previously {old_highscore}.')
    else:
        play()

if __name__ == "__main__":
    main()
