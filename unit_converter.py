# This is a project developed by devhorla a.k.a Horlalaycon @ Github
def help_option():
    print("""help
                ==============================================================================
                This a unit converter for calculating length, weight, and temperature
                ==============================================================================
                    *_* LENGTH CONVERSION enter either (l/length) 
                ------------------------------------------------------------------------------
                        * meter to kilometer enter either (m-km/meter-kilometer)
                ------------------------------------------------------------------------------
                        * meter to centimeter enter either (m-cm/meter-centimeter)
                ------------------------------------------------------------------------------
                        * meter to kilometer enter either (m-mm/meter-millimeter)
                ------------------------------------------------------------------------------
                        * kilometer to meter enter either (km-m/kilometer-meter)
                ------------------------------------------------------------------------------
                        * centimeter to meter enter either (cm-m/centimeter-meter)
                ------------------------------------------------------------------------------
                        * millimeter to meter enter either (mm-m/millimeter-meter)
                ------------------------------------------------------------------------------
                        * foot to inch enter either (ft-inch/foot-inch)
                ------------------------------------------------------------------------------
                        * inch to foot enter either (inch-ft/inch-foot)
                ------------------------------------------------------------------------------
                        * yard to mile enter either (ft-inch/foot-inch)
                ------------------------------------------------------------------------------
                        * mile to yard enter either (ft-inch/foot-inch)
                ------------------------------------------------------------------------------
                ==============================================================================
                ------------------------------------------------------------------------------
                    *_* WEIGHT CONVERSION enter either (w/weight)
                ------------------------------------------------------------------------------
                        * for kilogram to gram enter either (kg-lb/kilogram-pound) 
                ------------------------------------------------------------------------------
                        * for gram to kilogram enter either (lb-kg/pound-kilogram)
                ------------------------------------------------------------------------------
                        * ounce to gram enter either (oz-g/ounce-gram)
                ------------------------------------------------------------------------------
                        * gram to ounce enter either (g-oz/gram-ounce)
                ------------------------------------------------------------------------------
                ==============================================================================
                ------------------------------------------------------------------------------
                    *_* TEMPERATURE CONVERSION enter either (t/temperature)
                ------------------------------------------------------------------------------
                        * celsius to fahrenheit enter either (c-f/celsius-fahrenheit)
                ------------------------------------------------------------------------------
                        * fahrenheit to celsius enter either (f-c/fahrenheit-celsius)
                ------------------------------------------------------------------------------
                        * celsius to kelvin enter either (c-k/celsius-kelvin)
                ------------------------------------------------------------------------------
                        * fahrenheit to celsius enter either (k-c/kelvin-celsius)
                ------------------------------------------------------------------------------

                """)


purpose = ""
while purpose != "l" or purpose != "w" or purpose != "t" or purpose != "h" or purpose != "length" or purpose != "weight" or purpose != "temperature" or purpose != "help":
    purpose = input("What do you want to convert? \n")
#
# Length Operations
    if purpose == "l" or purpose == "length":
        length_operation = input("What operation do you want to perform in length:\n")
#
    # meter to kilometer
        if length_operation == "m-km" or length_operation == "meter-kilometer":
            meters = int(input("Enter the meters value: "))
            kilometers = str(meters / 1000)
            print("-" * 40)
            print(f'{meters} meter is: {kilometers} kilometer')
            print("-" * 40)
            break
    # meter to centimeter
        elif length_operation == "m-cm" or length_operation == "meter-centimeter":
            meters = int(input("Enter the meter value: "))
            centimeters = str(meters * 100)
            print("-" * 40)
            print(f'{meters} meter is: {centimeters} centimeter')
            print("-" * 40)
            break
    # meter to millimeter
        elif length_operation == "m-mm" or length_operation == "meter-millimeter":
            meters = int(input("Enter the meters value: "))
            millimeters = str(meters * 1000)
            print("-" * 40)
            print(f'{meters} meter is: {millimeters} millimeter')
            print("-" * 40)
            break
    # kilometer to meter
        elif length_operation == "km-m" or length_operation == "kilometer-meter":
            kilometers = int(input("Enter the kilometer value: "))
            meters = str(kilometers * 1000)
            print("-" * 40)
            print(f'{kilometers} kilometer is: {meters} meter')
            print("-" * 40)
            break
    # centimeter to meter
        elif length_operation == "cm-m" or length_operation == "centimeter-meter":
            centimeters = int(input("Enter the centimeter value: "))
            meters = str(centimeters / 100)
            print("-" * 40)
            print(f'{centimeters} centimeter is: {meters} meter')
            print("-" * 40)
            break
    # millimeter to meter
        elif length_operation == "mm-m" or length_operation == "millimeter-meter":
            millimeters = int(input("Enter the millimeter value: "))
            meters = str(millimeters / 100)
            print("-" * 40)
            print(f'{millimeters} millimeter is: {meters} meter')
            print("-" * 40)
            break
    # feet to inches
        elif length_operation == "ft-inch" or length_operation == "foot-inch":
            feet = int(input("Enter the feet value: "))
            inches = str(feet * 12)
            print("-" * 40)
            print(f'{feet} feet is: {inches} inches')
            print("-" * 40)
            break
    # inches to feet
        elif length_operation == "inch-ft" or length_operation == "inch-foot":
            inches = int(input("Enter the inches value: "))
            feet = str(inches / 12)
            print("-" * 40)
            print(f'{inches} inches is: {feet} feet')
            print("-" * 40)
            break
    # yards to miles
        elif length_operation == "yd-ml" or length_operation == "yard-mile":
            yards = int(input("Enter the yard value: "))
            miles = str(yards / 1760)
            print("-" * 40)
            print(f'{yards} yards is: {miles} miles')
            print("-" * 40)
            break
    # yards to miles
        elif length_operation == "yd-ml" or length_operation == "yard-mile":
            miles = int(input("Enter the mile value: "))
            yards = str(miles * 1760)
            print("-" * 40)
            print(f'{miles} miles is: {yards} yards')
            print("-" * 40)
            break
    # help
        elif length_operation == "h" or length_operation == "help":
            help_option()
    # error
        else:
            print("Invalid Operation, enter (h/help) for help menu")
#
#
# Weight Operation
    elif purpose == "w" or purpose == "weight":
        weight_operation = input("what operation do you want to perform in weight\n")
    # kilogram to pounds
        if weight_operation == "kg-lb" or weight_operation == "kilogram-pound":
            kilograms = int(input("Enter the kilogram value: "))
            pounds = kilograms * 2.2046226218
            pounds = round(pounds, 3)
            print("-" * 40)
            print(f'{kilograms} kilograms is: {pounds} pounds')
            print("-" * 40)
            break
    # pound to kilogram
        elif weight_operation == "lb-kg" or weight_operation == "pound-kilogram":
            pounds = int(input("Enter the pound value: "))
            kilograms = pounds * 0.45359237
            kilograms = round(kilograms, 3)
            print("-" * 40)
            print(f'{pounds} pounds is: {kilograms} kilograms')
            print("-" * 40)
            break
    # gram to ounce
        elif weight_operation == "g-oz" or weight_operation == "gram-ounce":
            grams = int(input("Enter the gram value: "))
            ounces = grams * 0.03527407
            ounces = round(ounces, 3)
            print("-" * 40)
            print(f'{grams} grams is: {ounces} ounces')
            print("-" * 40)
            break
    # ounce to gram
        elif weight_operation == "oz-g" or weight_operation == "ounce-gram":
            ounces = int(input("Enter the ounce value: "))
            grams = ounces * 28.3495231
            grams = round(grams, 3)
            print("-" * 40)
            print(f'{ounces} ounces is: {grams} grams')
            print("-" * 40)
            break
    # help
        elif weight_operation == "h" or weight_operation == "help":
            help_option()
    # error
        else:
            print("Invalid Operation, enter (h/help) for help menu")
#
#
# Temperature Operation
    elif purpose == "t" or purpose == "temperature":
        temperature_operation = input("what operation do you want to perform in Temperature:\n")
#
    # celsius to fahrenheit
        if temperature_operation == "c-f" or temperature_operation == "celsius-fahrenheit":
            celsius = int(input("Enter the celsius value: "))
            fahrenheit = celsius * 1.8 + 32
            print("-" * 40)
            print(f'{celsius} celsius is: {fahrenheit} fahrenheit')
            print("-" * 40)
            break
    # fahrenheit to celsius
        elif temperature_operation == "f-c" or temperature_operation == "fahrenheit-celsius":
            fahrenheit = int(input("Enter the celsius value: "))
            celsius = (fahrenheit - 32) / 1.8
            print("-" * 40)
            print(f'{fahrenheit} fahrenheit is: {celsius} celsius')
            print("-" * 40)
            break
    # celsius to kelvin
        elif temperature_operation == "c-k" or temperature_operation == "celsius-kelvin":
            celsius = int(input("Enter the celsius value: "))
            kelvin = celsius + 273.15
            print("-" * 40)
            print(f'{celsius} celsius is: {kelvin} kelvin')
            print("-" * 40)
            break
    # kelvin to celsius
        elif temperature_operation == "k-c" or temperature_operation == "kelvin-celsius":
            kelvin = int(input("Enter the kelvin value: "))
            celsius = kelvin + 273.15
            print("-" * 40)
            print(f'{kelvin} kelvin is: {celsius} celsius')
            print("-" * 40)
            break
    # help
        elif temperature_operation == "h" or temperature_operation == "help":
            help_option()
    # error
        else:
            print("Invalid Operation, enter (h/help) for help menu")
# help
    elif purpose == "h" or purpose == "help":
        help_option()
# error
    else:
        print("Sorry, Operation not Recognized!!, enter (h/help) for help menu")
