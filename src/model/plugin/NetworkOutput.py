import sys
import ast


def main():

    with open("script.py", "w") as fd:
        fd.write("import socket" + "\n")
        for i in sys.argv[1:]:
            res = ast.literal_eval(i)
            if res["out"] is not None:
                fd.write(res["out"] + "\n")
            else:
                fd.write('"' + res["name"] + '"' + "\n")
    fd.close()


if __name__ == "__main__":
    main()
