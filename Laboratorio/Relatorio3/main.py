from database import Database
from helper.writeAJson import writeAJson
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
pokedex = Pokedex(db)

#salvando as 5 queries
writeAJson(pokedex.pokemons_fraqueza_unica(),"PokemonFraquezaUnica")
writeAJson(pokedex.buscar_todos_pokemons(),"TodosPokemons")
writeAJson(pokedex.informacoes_pokemon_por_nome("Bulbasaur"),"InformaçãoUnica")
writeAJson(pokedex.pokemons_renascer_03_06(),"Spwan03_06")
writeAJson(pokedex.pokemons_tipo_fogo(),"PokemonsDeFogo")

