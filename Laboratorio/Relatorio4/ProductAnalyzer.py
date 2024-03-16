from database import Database
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
#db.resetDatabase()

#1- Total de vendas por dia
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$data_compra", "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}
])
writeAJson(result, "Total de vendas por dia")

# 2- produto mais vendido em todas as compras.
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
     {"$group": {"_id": "$produtos.descricao","quantidade_total_vendida": {"$sum": "$produtos.quantidade"}}},
     {"$sort": {"quantidade_total_vendida": -1}},
     {"$limit": 1}
])
#
writeAJson(result, "produto mais vendido em todas as compras")

# 3- Cliente que mais gastou:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$sort": {"total_gasto": -1}},
    {"$limit": 1}
])
writeAJson(result, "Cliente que mais gastou")

# 3- Mais de uma quatidade Vendida
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$match": {"produtos.quantidade": {"$gt": 1}}},
    {"$group": {"_id": "$produtos.descricao", "quantidade_total_vendida": {"$sum": "$produtos.quantidade"}}}
])

writeAJson(result, "Vendidos mais que 1")