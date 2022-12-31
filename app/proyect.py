import charts
import utils
import read_csv


def generate_population_chart_by_country(country):
  data = read_csv.read_csv('data.csv')
  country_list = utils.get_population_by_country(data, country)

  if len(country_list) > 0:
    country = country_list[0]
    labels, values = utils.get_population_by_year(country)
    charts.generate_bar_chart(country['Country'], labels, values)


def generate_world_population_percentage(continent):
  data = read_csv.read_csv('data.csv')
  countries, percentages = utils.get_world_population_percentage(data, continent)
  charts.generate_pie_chart(countries, percentages)


if __name__ == '__main__':
  country = input('Type country => ')
  generate_population_chart_by_country(country)
  generate_world_population_percentage('America')
