import os

class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        if filename is None:
            raise ValueError("No filename")
        self.filename = filename
        if not os.path.isfile(filename):
            raise ValueError("File not found")
        if sep == '':
            raise ValueError("Need a sep")
        self.sep = sep
        self.header = header
        if skip_bottom < 0 or skip_top < 0 or skip_top > skip_bottom:
            raise ValueError("Skip bottom and top need to be >= 0 and top > bottom")
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        try:
            self.file = open(self.filename, "r")
        except OSError as e:
            print(e.errno)
        print(self.file)
        line = self.file.readline()
        new_line = line.replace(" ", "")
        new_line = new_line.replace("\"", "")
        new_line = new_line.replace("\n", "")
        ref_list = new_line.split(self.sep)
        ref_size = len(ref_list)
        while line:
            new_line = line.replace(" ", "")
            new_line = new_line.replace("\"", "")
            new_line = new_line.replace("\n", "")
            tmp_list = new_line.split(self.sep)
            tmp_list = list(filter(None, tmp_list))
            if (len(tmp_list) != ref_size):
                return None
            line = self.file.readline()
        return self
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom. 
        Returns:
            nested list (list(list, list, ...)) representing the data.
        """
        self.file.seek(0)
        main_list = []
        line = self.file.readline()
        index = 1
        while line:
            if self.skip_top > 0 and index < self.skip_top:
                line = self.file.readline()
            elif self.skip_bottom > 0 and index > self.skip_bottom:
                break
            else:
                new_line = line.replace(" ", "")
                new_line = new_line.replace("\"", "")
                new_line = new_line.replace("\n", "")
                sublist = new_line.split(self.sep)
                main_list.append(sublist)
                line = self.file.readline()
            index += 1
        return main_list

    
    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
            list: representing the data (when self.header is True).
            None: (when self.header is False).
        """
        self.file.seek(0)
        if self.header is True:
            line = self.file.readline()
            new_line = line.replace(" ", "")
            new_line = new_line.replace("\"", "")
            new_line = new_line.replace("\n", "")
            header_list = new_line.split(',')
            return header_list
        else:
            return None
