import charts
import pandas as pa


def run():
  continent = input('Continent ==> ')
  df = pa.read_csv('data.csv')
  df = df[df['Continent'] == continent]

  countries = df['Country'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)  

if __name__ == '__main__':
  run()