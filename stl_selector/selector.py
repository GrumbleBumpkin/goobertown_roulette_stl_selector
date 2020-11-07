import glob
import os
import random
import time


def get_input():
    file_path = input('Specify your target STL folder (blank to quit):')
    if file_path and not os.path.isdir(file_path):
        raise FileNotFoundError(f'{file_path} is not a valid directory.')
    return file_path


def run_selector(file_path):
    start = time.time()
    files = glob.glob(f'{file_path}/**/*.stl', recursive=True)
    selection = random.choice(files)
    elapsed_time = time.time() - start

    print(f'Scan time: {elapsed_time} seconds over {len(files)} files\n')
    print(f'Your Goobertown Roulette model is:\n\n{selection}\n\nGood luck and paint bravely!')


if __name__ == "__main__":
    while True:
        try:
            file_path = get_input()
            if not file_path:
                break
            run_selector(file_path)
        except FileNotFoundError as e:
            print(f'\n{e.args[0]}\n')
