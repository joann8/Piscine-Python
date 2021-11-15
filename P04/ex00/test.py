from FileLoader import FileLoader

print("**** Right Test ******")
loader = FileLoader()
data = loader.load("./athlete_events.csv")
loader.display(data,12)

print("\n**** Wrong Test ******")

loader.display(data,-1)
data = loader.load("./athlete_even.csv")
loader.display(data,12)