from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../athlete_events.csv')

from HowManyMedals import howManyMedals

print(howManyMedals(data, 'Kjetil Andr Aamodt'))
