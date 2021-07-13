import math
import argparse
parser = argparse.ArgumentParser()
#Tout les entiers de 1 à 9 sont narcissiques.
#153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93034 sont des nombres narcissiques.
parser.add_argument('integers', help="entier naturel non nul", type=int)
args = parser.parse_args()
def narcissistic( value ):
    value = str(value)
    i = 0
    for val in value:
        i += math.pow(int(val), len(value))
    if int(value) == i:
        print("True")
        #return True
    else:
        print("False")
        #return False


narcissistic(args.integers)
