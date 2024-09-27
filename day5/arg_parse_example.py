from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("path", type=str)
parser.add_argument("count", type=int)

args = parser.parse_args()
print(f"{args.path=}, {args.count=}")