class ProductAnalyzer:
    def __init__(self, db):
        self.db = db

    def total_vendas(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"_id": 1}}
        ]
        return list(self.db.collection.aggregate(pipeline))

    def produto_mais_vendido(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ]
        return list(self.db.collection.aggregate(pipeline))

    def cliente_mais_gasta(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ]
        return list(self.db.collection.aggregate(pipeline))

    def produtos_venda_maior_um(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"total": {"$gt": 1}}}
        ]
        return list(self.db.collection.aggregate(pipeline))
