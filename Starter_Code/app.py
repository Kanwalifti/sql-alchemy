# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# reflect an existing database into a new model
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect the tables
Base = automap_base()
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>" 
        f"/api/v1.0/<start>/<end><br/>"
    )

#Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    result = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= "2016-08-23").\
    order_by(Measurement.date).distinct().all()

    session.close

# Create a dictionary from the row data and append to a list of dates & prcp
    precipitation_analysis = []
    for date, prcp in result:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["precipitation"] = prcp
        precipitation_analysis.append(prcp_dict)

    return jsonify(precipitation_analysis)

#Query the dates and temperature observations of the most-active station for the previous year of data.
# Return a JSON list of temperature observations for the previous year.

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    #result = session.query(Measurement.station, func.count(Measurement.id))\
    #.group_by(Measurement.station)\
    #.order_by(func.count(Measurement.id).desc()).all()

    #session.query(Measurement.date, Measurement.station ,Measurement.tobs).filter(Measurement.date >= "2016-08-23").\
    #order_by(Measurement.date).distinct().all()

    #result = session.query(Measurement.station).filter(Measurement.station, Measurement.tobs ,Measurement.date <= "2016-08-23").\
     #   order_by(Measurement.date).distinct().all()
    result = session.query(Station.station).all()
    session.close

# Convert list of tuples into normal list
    active_stations = list(np.ravel(result))

    return jsonify(active_stations)

#Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.


@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date.between('2016-08-23', '2017-08-23')).\
        filter(Measurement.station == 'USC00519281').all()
    
   # session.query(Measurement.date, Measurement.station ,Measurement.tobs).\
    #    filter(Measurement.date <="2017, 8, 23" >= "2016-08-23").filter(Measurement.station == 'USC00519281').\
    #order_by(Measurement.date).distinct().all()

    session.close
    
    # Convert list of tuples into normal list
    tobs = list(np.ravel(result))
    
    return jsonify(tobs)
    

#dynamic route f"/api/v1.0/<start>" 
# For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
#start= []

@app.route("/api/v1.0/<start_date>")
def start(start_date):
    session = Session(engine)
    result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()

# Convert list of tuples into normal list
    tobs = list(np.ravel(result))
    
    session.close  
    
    return jsonify(tobs)


# For a specified start date and end date, 
# calculate TMIN, TAVG, and TMAX for the dates from the start date to the  end date, inclusive.

@app.route("/api/v1.0/<start_date>/<end_date>")
def start_end(start_date, end_date):
    session = Session(engine)
   
    result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date.between(start_date, end_date)).all()

# Convert list of tuples into normal list
    tobs = list(np.ravel(result))
    
    session.close

    return jsonify(tobs)






if __name__ == '__main__':
    app.run(debug=True)