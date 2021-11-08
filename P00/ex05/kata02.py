from datetime import datetime
import time

t = (3,30,2019,9,25)

date_objet = datetime(t[2], t[3], t[4], t[0], t[1], 0)
date_str = date_objet.strftime("%d/%m/%Y %H:%M")
print(date_str)
        
