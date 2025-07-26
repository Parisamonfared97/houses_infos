houses=[]

for i in range (5):
    city=input("enter city name:")
    area=input("enter Area(متراژ:)")
    elevator=input("Does this house have elevator?(y/n):")
    parking=input("Does this house have parking?(y/n):")
    year=input("enter year of build:")
    print("-"*30)

    house={
        "city":city,
           "area":area,
           "elevator":elevator,
           "parking":parking,
            "year":year
    }
    houses.append(house)

print("Houses List:")
print("=" * 30)

for house in houses:
    print("Houses List: ")
    print("city: ", house["city"])
    print("area: ", house["area"])
    print("elevator: ", house["elevator"])
    print("parking: ", house["parking"])
    print("year: ", house["year"])
    print("-" * 30)
