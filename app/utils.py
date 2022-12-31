def get_population():
  keys = ['col', 'bol']
  values = [300, 40]
  return keys, values


def get_population_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result


def get_population_by_year(data):
  result = {}
  result['2022'] = int(data['2022 Population'])
  result['2020'] = int(data['2020 Population'])
  result['2015'] = int(data['2015 Population'])
  result['2010'] = int(data['2010 Population'])
  result['2000'] = int(data['2000 Population'])
  result['1990'] = int(data['1990 Population'])
  result['1980'] = int(data['1980 Population'])
  result['1970'] = int(data['1970 Population'])

  return result.keys(), result.values()


def get_world_population_percentage(data, continent):
  data = list(filter(lambda item: item['Continent'] == continent, data))
  countries = list(map(lambda item: item['Country'], data))
  percentages = list(
    map(lambda item: float(item['World Population Percentage']), data))
  return countries, percentages


message = 'Hola Python'
