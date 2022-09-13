from Pract_08.taxi import Taxi


def main():
    new_texi = Taxi("Prius 1", 100)
    new_texi.drive(40)
    print(new_texi)
    new_texi.start_fare()
    new_texi.drive(100)
    print(new_texi)


main()
