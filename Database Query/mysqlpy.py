#MySQL/MariaDB compatible query using PyMySQL on Python 3.6
#World example database found at https://dev.mysql.com/doc/index-other.html
#By John Knowles

import pymysql
#access pymysql library


hostname = 'localhost'
username = 'root'
password = 'mysql'
database = 'world'
#global variables


def queryCountryNamePopulation( conn ) :
#function to print out Country Name and Population

    currentConnection = conn.cursor()
    #cursor object used to manage interactions witht he SQL Database

    currentConnection.execute( "SELECT Name, Population FROM country" )
    #run SQL code to select the Name and Population rows from country table

    for name, population in currentConnection.fetchall() :
    #for loop that goes through all rows of name and population
        print (name, population)
        #print current row
#end function


#begin code
print ("Country and Population Query")

myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )
#establish connection to the database using pymysql.connect and global variables

queryCountryNamePopulation( myConnection )
#run queryCountryNamePopulation passing in the new established database connection myConnection

myConnection.close()
#close the database connection when finished
#end code