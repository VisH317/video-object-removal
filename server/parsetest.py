import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--x')
parser.add_argument('--y')
args = parser.parse_args(['--x', 'x', '--y', 'y'])

