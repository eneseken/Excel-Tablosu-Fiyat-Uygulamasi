import pandas as pd
import requests
from bs4 import BeautifulSoup
import locale

# Load the data
df = pd.read_excel('veriler.xlsx')

# Get the unique driving styles
driving_styles = df['KULLANIM TARZI'].unique()

# Ask the user to select a driving style
print("KULLANIM TARZI")
for i, style in enumerate(driving_styles):
    print(f"{i+1}. {style}")
choice = int(input()) - 1
selected_driving_style = driving_styles[choice]

# Filter the data by the selected driving style
selected_rows = df[df['KULLANIM TARZI'] == selected_driving_style]



# Get the unique brands for the selected driving style and model year
brands = selected_rows['MARKA'].unique()

# Ask the user to select a brand
print("MARKA")
for i, brand in enumerate(brands):
    print(f"{i+1}. {brand}")
choice = int(input()) - 1
selected_brand = brands[choice]

# Filter the data by the selected brand
selected_rows = selected_rows[selected_rows['MARKA'] == selected_brand]


# Get the unique brand types for the selected driving style, model year, and brand
brand_types = selected_rows['MARKA MODEL TİPİ'].unique()

# Ask the user to select a brand type
print("MARKA MODEL TİPİ")
for i, brand_type in enumerate(brand_types):
    print(f"{i+1}. {brand_type}")
choice = int(input()) - 1
selected_brand_type = brand_types[choice]

# Filter the data by the selected brand type
selected_rows = selected_rows[selected_rows['MARKA MODEL TİPİ'] == selected_brand_type]



# Get the unique model years for the selected driving style
model_years = selected_rows['MODEL YILI'].unique()

# Ask the user to select a model year
print("MODEL YILI")
for i, year in enumerate(model_years):
    print(f"{i+1}. {year}")
choice = int(input()) - 1
selected_model_year = model_years[choice]

# Filter the data by the selected model year
selected_rows = selected_rows[selected_rows['MODEL YILI'] == selected_model_year]




# Get the unique fuel types for the selected driving style, model year, brand
fuel_types = selected_rows['YAKIT'].unique()

# Ask the user to select a fuel type
print("YAKIT")
for i, fuel_type in enumerate(fuel_types):
    print(f"{i+1}. {fuel_type}")
choice = int(input()) - 1
selected_fuel_type = fuel_types[choice]


#Get the unique brand types for the selected driving style, model year, and brand
brand_types_specific = selected_rows['MARKA TİPİ'].unique()

# Ask the user to select a brand type
print("MARKA TİPİ")
for i, brand_type_scpecific in enumerate(brand_types_specific):
    print(f"{i+1}. {brand_type_scpecific}")
choice = int(input()) - 1
selected_brand_type_specific = brand_types_specific[choice]

# Modify the URL to include the selected model year and brand type
url = f'https://www.tasit.com/otomobil?q={selected_model_year}+{selected_brand}' #if you want a specific result, you must add more detail in link

# Send a request to the URL and extract the page content using BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

prices = soup.find_all('div', class_='custom-highlight-real-price')
prices_float = []
for price in prices:
    price_str = price.text.replace('.', '').replace(',', '.').replace(' TL', '')
    prices_float.append(locale.atof(price_str))

# High 
max_price = max(prices_float)
max_price_str = f"{max_price:,.0f}₺".replace(',', '.')

# Low
min_price = min(prices_float)
min_price_str = f"{min_price:,.0f}₺".replace(',', '.')

# Average
avg_price = sum(prices_float) / len(prices_float)
avg_price_str = f"{avg_price:,.0f}₺".replace(',', '.')

print(f"En düşük fiyat: {min_price_str}")
print(f"Ortalama fiyat: {avg_price_str}")
print(f"En yüksek fiyat: {max_price_str}")