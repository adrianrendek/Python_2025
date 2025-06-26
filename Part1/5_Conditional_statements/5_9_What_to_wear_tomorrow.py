print("What is the weather forecast for tomorrow?")
temperature = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")

if temperature > 20:
    print("Wear jeans and a T-shirt")

if temperature <= 20 and temperature > 10:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")

if temperature <= 10 and temperature > 5:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")