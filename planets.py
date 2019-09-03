planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")
planet_list.append("Pluto")

rocky_planets = planet_list[slice(0, 4, 1)]

del(planet_list[8])

spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
   ("Apollo", "Moon"),
   ("Mariner", "Mercury"),
   ("Venera", "Venus"),
   ("Mars 2", "Mars"),
   ("Curiosity", "Mars"),
   ("New Horizons", "Pluto")
]

for planets in planet_list:
    final = ""
    ship_list = f"\n {planets} has been visited by:"
    for ships in spacecraft:
        if planets == ships[1]:
            ship_list += f"\n *{ships[0]}"
    final += f"{ship_list}"
    print(final)
