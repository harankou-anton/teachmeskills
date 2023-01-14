data = {
     'Belarus': ['Minsk', 'Gomel', 'Vitebsk', 'Brest'],
     'Russia': ['Moscow', 'Saint-Petersburg', 'Novosibirsk'],
     'Ukraine': ['Kiev', 'Odessa', 'Kharkov'],
     'Poland': ['Warsaw', 'Cracow', 'Gdansk'],
     'France': ['Paris', 'Marseille', 'Brest']
     }


def get_country(city):
    for data_countries, data_cities in data.items():
        if city in data_cities:
            print(data_countries)


if __name__ == '__main__':
    get_country(input('Type name of a city: '))
