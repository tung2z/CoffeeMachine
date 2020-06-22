# put your python code here
days = int(input())
foodForDay = int(input())
flightCost = int(input())
hotelCost = int(input())

print(days * foodForDay +(days - 1) * hotelCost + flightCost * 2)
