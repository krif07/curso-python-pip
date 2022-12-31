import utils

data = [{
  'Country': 'Colombia',
  'Population': 350
}, {
  'Country': 'Perú',
  'Population': 250
}, {
  'Country': 'Bolivia',
  'Population': 200
}]


def run():
  keys, values = utils.get_population()
  print(keys, values)
  print(utils.message) 

  country = input('Type country: ')

  result = utils.get_population_by_country(data, country)
  print(result)


if __name__ == '__main__':
  run()