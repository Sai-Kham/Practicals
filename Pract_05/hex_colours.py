COLOUR_CODES = {"Canary": "##ffff99", "Canary Yellow": "#ffef00",
                "Candy Apple Red": "#ff0800", "Candy Pink": "#e4717a",
                "Caput Mortuum": "#592720", "Cardinal": "#c41e3a",
                "Caribbean Green": "#00cc99", "Carmine": "#960018",
                "Carmine Pink": "#eb4c42", "Carnation Pink": "#ffa6c9",
                "Carnelian": "#b31b1b", "Carolina Blue": "#56a0d3"}

colour_name = input("Enter a colour name: ").capitalize()
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name, COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ").capitalize()
