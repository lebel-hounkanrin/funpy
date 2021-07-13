import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-a', '--add', help="Addiction", nargs='+', type=int)
parser.add_argument('-m', '--multiply', help="multiplication", nargs='+', type=int)
parser.add_argument('-s', '--sustraction', help="soustraction", nargs='+', type=int)
parser.add_argument('-d', '--division', help="division", nargs='+', type=int)

args = parser.parse_args()

if args.add :
    print(sum(args.add))


if args.multiply:
    total = 1
    for nb in args.multiply:
        total *= nb
    print(total)


if args.sustraction:
    total = args.sustraction[0]
    if len(args.sustraction) == 1:
        total = 0 - args.sustraction[0]
    else:
        for nb in args.sustraction:
            total -= nb
        total += args.sustraction[0]
    print(total)


