# calc evaluation using argparse
import argparse

parser = argparse.ArgumentParser(description="Simple Calculator")
parser.add_argument('--x', type=int, required=True, help="First number")
parser.add_argument('--y', type=int, required=True, help="Second number")
parser.add_argument('--opt', type=str, required=True, choices=['add', 'sub', 'mul', 'div'], help="Operation")
args = parser.parse_args()

if args.opt == 'add':
    result = args.x + args.y
elif args.opt == 'sub':
    result = args.x - args.y
elif args.opt == 'mul':
    result = args.x * args.y  # fixed multiplication
elif args.opt == 'div':
    if args.y == 0:
        print("Error: Division by zero")
        exit(1)
    result = args.x / args.y

print("Result is", result)
