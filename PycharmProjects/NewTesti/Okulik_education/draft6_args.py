import argparse

parser = argparse.ArgumentParser()


parser.add_argument('name', help='just a name')
args = parser.parse_args()
print(args.name)
