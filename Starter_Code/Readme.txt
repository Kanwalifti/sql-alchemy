Climate analysis and data exploration were conducted on an SQLite file using SQLAlchemy ORM Queries, Pandas, and Matplotlib. The database was connected to using the "create_engine" command, and "automap_base()" was used to reflect tables into classes.

Precipitation data was obtained by designing a query and loading the results into a DataFrame. The data was then plotted and summarized statistically.

In addition, three queries were used to determine the total number of weather stations, identify the most active stations, and retrieve temperature observation data (TOBS) for the last 12 months.

Below, you can see the two plots:

![Fig1](C:\Users\kanwal\Documents\UT Austin Projects\WEEK 10\10-Advanced-SQL\challenge\PrecipitationTemps.png)
![Fig2](C:\Users\kanwal\Documents\UT Austin Projects\WEEK 10\10-Advanced-SQL\challenge\StationTemps.png)

A Flask API was developed based on the queries. The API has several routes, including a home page, which serves as the default landing page. 
The other routes provide data in JSON format.
The first route returns a dictionary containing the results of the percipitation queries. 
The second and third routes return JSON lists of weather stations and temperature observation data (TOBS), respectively. 
The fourth and fifth route returns a JSON list containing the minimum, maximum, and average temperature for a given start date, and fifth with start and end date range.