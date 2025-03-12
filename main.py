# Part of case-study #2: Fuel cost from Novosibirsk to different cities
# Developer: Gaberman A, Garchenko V.
#

import ru_local as ru


def main():
    '''
    Main function.
    :return: None
    '''

    average_fuel_consumption = float(input(ru.NUMBER_AVERAGE_CONSUMPTION))
    fuel_number = int(input(ru.FUEL_NUMBER))
    distance_to_Moscow = 3306
    distance_to_Saint_Petersburg = 3994
    distance_to_Tomsk = 258
    price_fuel_92 = 56.30
    price_fuel_95 = 60.25
    price_fuel_98 = 70.29

    total_fuel_consumption_to_Moscow = (
        distance_to_Moscow / average_fuel_consumption)
    total_fuel_consumption_to_Saint_Petersburg = (
        distance_to_Saint_Petersburg / average_fuel_consumption)
    total_fuel_consumption_to_Tomsk = (
        distance_to_Tomsk / average_fuel_consumption)

    if fuel_number == 92:
        cost_fuel_to_Moscow = (
            total_fuel_consumption_to_Moscow * price_fuel_92)
        cost_fuel_to_Saint_Petersburg = (
            total_fuel_consumption_to_Saint_Petersburg * price_fuel_92)
        cost_fuel_to_Tomsk = (
            total_fuel_consumption_to_Tomsk * price_fuel_92)

        print(f'{ru.COST_FUEL} {ru.DESTINATION_MOSCOW} - '
              f'{round(cost_fuel_to_Moscow, 2)} {ru.CURRENCY}')
        print(f'{ru.COST_FUEL} {ru.DESTINATION_SAINT_PETERSBURG} - '
              f'{round(cost_fuel_to_Saint_Petersburg, 2)} {ru.CURRENCY}')
        print(f'{ru.COST_FUEL} {ru.DESTINATION_TOMSK} - '
              f'{round(cost_fuel_to_Tomsk, 2)} {ru.CURRENCY}')

    elif fuel_number == 95:
        cost_fuel_to_Moscow = (
            total_fuel_consumption_to_Moscow * price_fuel_95)
        cost_fuel_to_Saint_Petersburg = (
            total_fuel_consumption_to_Saint_Petersburg * price_fuel_95)
        cost_fuel_to_Tomsk = (
            total_fuel_consumption_to_Tomsk * price_fuel_95)

        print(f'{ru.COST_FUEL} {ru.DESTINATION_MOSCOW} - '
              f'{round(cost_fuel_to_Moscow, 2)} {ru.CURRENCY}')
        print(f'{ru.COST_FUEL} {ru.DESTINATION_SAINT_PETERSBURG}- '
              f'{round(cost_fuel_to_Saint_Petersburg, 2)} {ru.CURRENCY}')
        print(f'{ru.COST_FUEL} {ru.DESTINATION_TOMSK} - '
              f'{round(cost_fuel_to_Tomsk, 2)} {ru.CURRENCY}')

    elif fuel_number == 98:
        cost_fuel_to_Moscow = (
            total_fuel_consumption_to_Moscow * price_fuel_98)
        cost_fuel_to_Saint_Petersburg = (
            total_fuel_consumption_to_Saint_Petersburg * price_fuel_98)
        cost_fuel_to_Tomsk = (
            total_fuel_consumption_to_Tomsk * price_fuel_98)

        print(f'{ru.COST_FUEL} {ru.DESTINATION_MOSCOW} - '
              f'{round(cost_fuel_to_Moscow, 2)} {ru.CURRENCY}')
        print(f'{ru.COST_FUEL} {ru.DESTINATION_SAINT_PETERSBURG} - '
              f'{round(cost_fuel_to_Saint_Petersburg, 2)} {ru.CURRENCY}')
        print(f'{ru.COST_FUEL} {ru.DESTINATION_TOMSK} - '
              f'{round(cost_fuel_to_Tomsk, 2)} {ru.CURRENCY}')

    else:
        print(f'{ru.ERROR_MESSAGE}')


if __name__ == '__main__':
    main()
