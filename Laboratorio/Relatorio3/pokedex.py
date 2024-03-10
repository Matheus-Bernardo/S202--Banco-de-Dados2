from database import Database

class Pokedex:
    def __init__(self, database: Database):
        self.database = database
        self.pokemon_collection = database.collection

    def informacoes_pokemon_por_nome(self, name: str):#Informações pelo nome
        return self.pokemon_collection.find_one({"name": name})

    def buscar_todos_pokemons(self):#retorna todos pokemons
        return list(self.pokemon_collection.find())
    
    def pokemons_fraqueza_unica(self):
        return self.pokemon_collection.find({"$where": "this.weaknesses.length == 1"})
         

    def pokemons_renascer_03_06(self):
         return self.pokemon_collection.find({"spawn_chance": {"$gt": 0.3, "$lt": 0.6}})
         

    def pokemons_tipo_fogo(self):
        return self.pokemon_collection.find({"type":"Fire"})