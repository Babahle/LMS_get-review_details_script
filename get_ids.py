import sys


def main():
    ids = []
    for i in sys.argv:
        uuid = ""
        if i.find("(") > -1 and i.find(")") > -1:
            for char in i:
                if char != "(" and char != ")":
                    uuid += char
        print(uuid)            

if __name__ == '__main__':
    main()
