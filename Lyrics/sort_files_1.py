import os

def main():
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        print("{}".format(filename))
        os.rename(filename, "{}".format(filename))

main()
