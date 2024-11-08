from datetime import datetime

def mysql_to_bra(dta):
   return datetime.strftime(dta, '%d/%m/%Y')