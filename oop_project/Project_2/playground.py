from data_models.AquaPokemon import AquaPokemon

squirtle = AquaPokemon("Squirtle", "002",10,50.10,20,50,[("tackle", 40)])
print(squirtle.name)
print(squirtle.pokedexId)
print(squirtle.__dict__)