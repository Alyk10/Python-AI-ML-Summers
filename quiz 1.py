import pandas as pd

weather_data = {
    'day': ['1/1/2026', '1/2/2026', '1/3/2026', '1/4/2017'],
    'temperature': [32, 35, 28, 24],
    'windspeed': [6, 7, 2, 7],
    'event': ['Rain', 'Sunny', 'Snow', 'Sunny']
}

df = pd.DataFrame(weather_data)
print("Shape:", df.shape,"\n")      
print("First 3 rows:", df.head(3) "\n")
print("Last 2 rows:", df.tail(2)"\n")