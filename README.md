# sql-alchemy

# Introduction:

The Hawaiian Islands offer a captivating blend of stunning landscapes, ranging from serene sandy beaches with emerald-blue waters and palm trees to the awe-inspiring rugged terrain of volcanic mountains shaping the earth. The islands boast a rich tapestry of biodiversity, featuring a diverse array of plants, animals, and a vibrant mix of people from various races and ethnicities. This cultural melting pot epitomizes the essence of the U.S. experience, showcasing immigration, collaboration, and harmonious living.

The purpose of this repository is to conduct a climate analysis on Honolulu, Hawaii. The analysis aims to assist clients in their trip planning by providing valuable insights into the weather conditions and outlining the best activities and experiences they can look forward to during their vacation.

# Libraries:
- ORM queries,
- Pandas, 
- Matplotlib
- SQL Tolkit: SQLAlchemy

# Step 1 - Climate Analysis and Exploration:

This project utilized Python and SQLAlchemy to conduct climate analysis and data exploration of the climate database. The analysis involved using SQLAlchemy ORM queries, Pandas, and Matplotlib for data manipulation and visualization. The complete climate analysis and data exploration can be found in the Python pandas notebook file available in the "starter notebook" link.
Additionally, the "hawaii.sqlite" file contains the required data for the analysis.
- To establish a connection with the SQLite database, SQLAlchemy's create_engine was used with the code: engine = create_engine("sqlite:///Resources/hawaii.sqlite").
- The tables were reflected into classes using SQLAlchemy's automap_base() and saved as "Station" and "Measurement" for further data manipulation.
- To connect Python with the database, a SQLAlchemy session was created. It is essential to close the session at the end of the notebook to manage database connections effectively.

# Precipitation Analysis:

For this analysis, a query was designed to retrieve the last 12 months of precipitation data, specifically selecting the date and precipitation (prcp) values.

The query results were then loaded into a Pandas DataFrame, and the index was set to the date column. The DataFrame values were sorted by date to ensure chronological order.

To visualize the results, the DataFrame plot method was used, generating a plot that illustrates the precipitation trends over the past 12 months.

![]()

# Station Analysis:

To start the station analysis, a query was formulated to calculate the total number of stations, resulting in the discovery of 9 stations.

Next, the most active station list was determined by sorting the stations based on their observation counts in descending order. The station with the code USC00519281 was identified as the most active station, having the highest number of observations.

Another query was created to retrieve the last 12 months of temperature observation data (TOBS) specifically for the station with the highest observation count (USC00519281).

To visualize the temperature observation data, a histogram was plotted with 12 bins, presenting a clear representation of the temperature distribution over the past 12 months for the most active station.

![]()

# Step 2 - Climate App:

After completing the initial analysis, a Flask API was designed based on the previously developed queries.

The following routes were created using Flask:

1. / : This is the home page of the app.

2. /api/v1.0/precipitation : Converts the query results to a dictionary with date as the key and prcp as the value. It then returns the JSON representation of this dictionary.

3. /api/v1.0/stations : Returns a JSON list of stations from the dataset.

4. /api/v1.0/tobs : Queries the dates and temperature observations of the most active station for the last year of data. It returns a JSON list of temperature observations (TOBS) for the previous year.

5. /api/v1.0/<start> and /api/v1.0/<start>/<end> : Returns a JSON list of the minimum temperature (TMIN), the average temperature (TAVG), and the maximum temperature (TMAX) for a given start date or start-end date range.

   - When given the start date only, it calculates TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
   
   - When given both the start and end dates, it calculates TMIN, TAVG, and TMAX for dates between the start and end dates (inclusive).

The app provides an interface to access the climate data using these routes, making it convenient for users to retrieve specific information from the dataset.

