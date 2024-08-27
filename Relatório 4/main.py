from database import Database
from helper.writeAJson import writeAJson
from product_analyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
db.resetDatabase()
analyzer = ProductAnalyzer(db)

result = analyzer.total_vendas()
writeAJson(result, "Total de vendas por dia")

result = analyzer.produto_mais_vendido()
writeAJson(result, "Produto mais vendido")

result = analyzer.cliente_mais_gasta()
writeAJson(result, "Cliente que mais gastou em uma única compra")

result = analyzer.produtos_venda_maior_um()
writeAJson(result, "Produtos com vendas acima de 1 unidade")