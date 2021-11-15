from FileLoader import FileLoader

loader = FileLoader()
data = loader.load('../athlete_events.csv')

from YoungestFellah import youngfellah
print(youngfellah(data, 2004))
print(youngfellah(data, 1991))
