from argparse import ArgumentParser
import time
import pandas as pd
import os


def _parse_arguments():
    parser = ArgumentParser(description='hami')
    parser.add_argument('--mode', help='the mode you want to call')
    args, unknown = parser.parse_known_args()

    return args


if __name__ == '__main__':
    print('This is main')
    df = pd.read_csv(os.path.join("data", "addresses.csv"))
    print(df.head())
    print(df.shape)
    df = pd.concat([df, df])
    print(df.shape)
    df.to_csv(os.path.join("data", "addresses_new.csv"))



