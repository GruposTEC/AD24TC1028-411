import sys
from pathlib import Path

def main():
    pass
    print(sys.argv)
    #print(sys.argv[1])
    #print(sys.argv[2])

    print(Path.cwd())
    print(Path.cwd().parent)

    padre = Path.cwd().parent
    folder = Path("5-Strings")
    small = padre / folder / sys.argv[1]
    secuencia = padre /folder / sys.argv[2]

    print(small)
    print(secuencia)

    f = open(small)
    for linea in f:
        linea = linea.strip()
        linea = linea.split(",")
        print(linea)



if __name__ == "__main__":
    main()