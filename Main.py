import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="שמך")
args: Namespace = parser.parse_args()
if args.name:
    print(f"שלום {args.name}!")