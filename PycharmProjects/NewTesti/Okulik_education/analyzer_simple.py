import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("logs", help="file name")
parser.add_argument("--date", help="date for search")
parser.add_argument("--full", help="date for search", action="store_true")
args = parser.parse_args()
print(args.logs, args.date, args.full)

