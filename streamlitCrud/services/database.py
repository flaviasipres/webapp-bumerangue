import pyodbc

server = 'DESKTOP-DS47K04\SQLEXPRESS' 
database = 'BumerangueWebApp' 
username = 'bumeranguereatop' 
password = '1234' 
cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()