import glob
import os
import random


def run_selector():
    file_path = input('Specify your target STL folder (q to quit):')
    if file_path.lower() == 'q':
        return False
    if not os.path.isdir(file_path):
        raise FileNotFoundError(f'{file_path} is not a valid directory.')
    selection = random.choice(glob.glob(f'{file_path}/**/*.stl', recursive=True))
    print(f'Your Goobertown Roulette model is:\n\n"{selection}"!\n\nGood luck!')


if __name__ == "__main__":
    while True:
        try:
            will_continue = run_selector()
            if not will_continue:
                break
        except FileNotFoundError as e:
            print(f'\n{e.args[0]}\n')
