'''5. City Population & Development Dashboard 
Problem Statement 
The government wants to analyze city data. 
Store details of at least 30 cities. 
Example Structure 
cities = { 
    "Delhi": { 
        "population": 32000000, 
        "area": 1484, 
        "literacy": 89 
    } 
} 
Requirements 
1. Display all city details.  
2. Find the most populated city.  
3. Find the least populated city.  
4. Calculate average population.  
5. Display cities with literacy rate above 90%.  
6. Display cities with literacy below average.  
7. Calculate population density.  
8. Find city with highest density.  
9. Categorize cities:  
o Small  
o Medium  
o Large  
10. Create a development-priority list.  
11. Generate separate dictionaries for:  
o High Literacy Cities  
o Low Literacy Cities  
12. Generate a national summary report.  
Challenge 
Rank all cities based on population density.'''

# City Population & Development Dashboard

cities = {
    "Delhi": {"population": 32000000, "area": 1484, "literacy": 89},
    "Mumbai": {"population": 21000000, "area": 603, "literacy": 91},
    "Kolkata": {"population": 15000000, "area": 206, "literacy": 88},
    "Chennai": {"population": 11000000, "area": 426, "literacy": 90},
    "Bengaluru": {"population": 13000000, "area": 741, "literacy": 92},
    "Hyderabad": {"population": 10500000, "area": 650, "literacy": 87},
    "Pune": {"population": 7500000, "area": 516, "literacy": 89},
    "Ahmedabad": {"population": 8500000, "area": 505, "literacy": 86},
    "Jaipur": {"population": 4200000, "area": 467, "literacy": 84},
    "Lucknow": {"population": 3800000, "area": 631, "literacy": 82}
}

while True:

    print("\n===== CITY DEVELOPMENT DASHBOARD =====")
    print("1. Display All Cities")
    print("2. Most Populated City")
    print("3. Least Populated City")
    print("4. Average Population")
    print("5. Literacy Above 90")
    print("6. Literacy Below Average")
    print("7. Population Density")
    print("8. Highest Density City")
    print("9. Categorize Cities")
    print("10. Development Priority List")
    print("11. Literacy Dictionaries")
    print("12. National Summary Report")
    print("13. Rank Cities By Density")
    print("14. Exit")

    choice = int(input("Enter Choice : "))

    # --------------------------------------------------
    # Display all cities

    if choice == 1:

        dict_items = list(cities.items())

        for item in dict_items:
            print(item[0], ":", item[1])

    # --------------------------------------------------
    # Most populated city

    elif choice == 2:

        dict_items = list(cities.items())

        max_city = dict_items[0][0]
        max_population = dict_items[0][1]["population"]

        for item in dict_items:

            if item[1]["population"] > max_population:

                max_population = item[1]["population"]
                max_city = item[0]

        print("\nMost Populated City")
        print(max_city, "-", max_population)

    # --------------------------------------------------
    # Least populated city

    elif choice == 3:

        dict_items = list(cities.items())

        min_city = dict_items[0][0]
        min_population = dict_items[0][1]["population"]

        for item in dict_items:

            if item[1]["population"] < min_population:

                min_population = item[1]["population"]
                min_city = item[0]

        print("\nLeast Populated City")
        print(min_city, "-", min_population)

    # --------------------------------------------------
    # Average population

    elif choice == 4:

        total_population = 0

        dict_items = list(cities.items())

        for item in dict_items:
            total_population += item[1]["population"]

        average_population = total_population / len(cities)

        print("Average Population :", average_population)

    # --------------------------------------------------
    # Literacy above 90

    elif choice == 5:

        print("\nCities With Literacy Above 90")

        dict_items = list(cities.items())

        for item in dict_items:

            if item[1]["literacy"] > 90:
                print(item[0])

    # --------------------------------------------------
    # Literacy below average

    elif choice == 6:

        total_literacy = 0

        dict_items = list(cities.items())

        for item in dict_items:
            total_literacy += item[1]["literacy"]

        average_literacy = total_literacy / len(cities)

        print("\nCities Below Average Literacy")

        for item in dict_items:

            if item[1]["literacy"] < average_literacy:
                print(item[0])

    # --------------------------------------------------
    # Population density

    elif choice == 7:

        print("\nPopulation Density")

        dict_items = list(cities.items())

        for item in dict_items:

            density = item[1]["population"] / item[1]["area"]

            print(item[0], ":", density)

    # --------------------------------------------------
    # Highest density city

    elif choice == 8:

        highest_density = 0
        density_city = ""

        dict_items = list(cities.items())

        for item in dict_items:

            density = item[1]["population"] / item[1]["area"]

            if density > highest_density:

                highest_density = density
                density_city = item[0]

        print("\nHighest Density City")
        print(density_city)

    # --------------------------------------------------
    # Categorize cities

    elif choice == 9:

        small = []
        medium = []
        large = []

        dict_items = list(cities.items())

        for item in dict_items:

            population = item[1]["population"]

            if population < 5000000:
                small.append(item[0])

            elif population < 15000000:
                medium.append(item[0])

            else:
                large.append(item[0])

        print("\nSmall Cities :", small)
        print("Medium Cities :", medium)
        print("Large Cities :", large)

    # --------------------------------------------------
    # Development priority list

    elif choice == 10:

        priority = []

        dict_items = list(cities.items())

        for item in dict_items:

            if item[1]["literacy"] < 85:
                priority.append(item[0])

        print("\nDevelopment Priority Cities")
        print(priority)

    # --------------------------------------------------
    # Literacy dictionaries

    elif choice == 11:

        high_literacy = {}
        low_literacy = {}

        dict_items = list(cities.items())

        for item in dict_items:

            if item[1]["literacy"] >= 90:
                high_literacy[item[0]] = item[1]

            else:
                low_literacy[item[0]] = item[1]

        print("\nHigh Literacy Cities")
        print(high_literacy)

        print("\nLow Literacy Cities")
        print(low_literacy)

    # --------------------------------------------------
    # National summary report

    elif choice == 12:

        total_population = 0

        dict_items = list(cities.items())

        for item in dict_items:
            total_population += item[1]["population"]

        average_population = total_population / len(cities)

        print("\n===== NATIONAL SUMMARY REPORT =====")
        print("Total Cities :", len(cities))
        print("Total Population :", total_population)
        print("Average Population :", average_population)

    # --------------------------------------------------
    # Rank cities by density

    elif choice == 13:

        print("\nCity Ranking By Density")

        temp = cities.copy()

        while len(temp) > 0:

            dict_items = list(temp.items())

            density_city = dict_items[0][0]
            highest_density = dict_items[0][1]["population"] / dict_items[0][1]["area"]

            for item in dict_items:

                density = item[1]["population"] / item[1]["area"]

                if density > highest_density:

                    highest_density = density
                    density_city = item[0]

            print(density_city, "-", highest_density)

            del temp[density_city]

    # --------------------------------------------------
    # Exit

    elif choice == 14:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")