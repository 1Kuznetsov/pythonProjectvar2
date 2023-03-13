import ru_local as ru
print(ru.WRITE_THE_VOLUME_OF_PETROL_IN_GALLON)
volume_of_petrol_in_gallon = float(input())
barrel_to_gallons = 19.5
gallons_of_petrol_to_pounds_of_carbon_dioxide = 20
gallons_of_petrol_to_BTU = 115000
gallon_of_ethanol_to_BTU = 75700
cost_of_one_gallon_of_petrol = 3
volume_of_petrol_in_liters = volume_of_petrol_in_gallon * 3.78
volume_of_barrel = volume_of_petrol_in_gallon / barrel_to_gallons
volume_of_carbon_dioxide = volume_of_petrol_in_gallon * gallons_of_petrol_to_pounds_of_carbon_dioxide
volume_of_ethanol = gallon_of_ethanol_to_BTU * volume_of_petrol_in_gallon / gallon_of_ethanol_to_BTU
cost = cost_of_one_gallon_of_petrol * volume_of_petrol_in_gallon
print(ru.VOLUME_OF_PETROL_IN_LITERS, volume_of_petrol_in_liters)
print(ru.VOLUME_OF_BARREL, volume_of_barrel)
print(ru.VOLUME_OF_CARBON_DIOXIDE, volume_of_carbon_dioxide)
print(ru.VOLUME_OF_ETHANOL, volume_of_ethanol)
print(ru.COST, cost)
