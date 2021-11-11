from csvreader import CsvReader

if __name__ == "__main__":
        with CsvReader('good.csv') as file:
            print("\n******* GET DATA ********")
            data = file.getdata()
            print(data)
            print("\n******* GET HEADER ********")
            header = file.getheader()
            print(header)

            file.header = True
            file.skip_top = 2
            file.skip_bottom = 5
            print("\n******* GET DATA ********")
            data = file.getdata()
            print(data)
            print("\n******* GET HEADER ********")
            header = file.getheader()
            print(header)

if __name__ == "__main__":
    with CsvReader('bad.csv') as file:
        print("\n******* DEUXIEME TEST ********")

        if file == None:
            print("File is corrupted")
 

