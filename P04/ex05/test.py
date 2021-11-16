from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../athlete_events.csv')
from HowManyMedalsByCountry import howManyMedalsByCountry
print("\n********** Medals for France **********")
print(howManyMedalsByCountry(data, 'France'))
print("\n********** Medals for Serbia **********")
print(howManyMedalsByCountry(data, 'Serbia'))
