
import pandas as pd

df = pd.read_csv('PRODUTOS.csv')

products = df['Produto'].tolist()
barcode = df['CodigoDeBarras'].tolist()

product_barcode_pairs = list(zip(products, barcode))

### PRINTA AS INFORMAÇÕES JUNTAS ###
for product, code in product_barcode_pairs:
    print(f"Product: {product} | Barcode: {code}")

### GERA UMA NOVA ARRAY ###
new_csv = []

for item in product_barcode_pairs:
    modified_item = item
    new_csv.append(modified_item)

print(new_csv)





