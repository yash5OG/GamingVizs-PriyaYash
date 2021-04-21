from flask import Flask, jsonify
import pandas as pd
import datetime as dt
import json
import numpy as np

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Create engine to hawaii.sqlite
# engine = create_engine("sqlite:///{FILES}.sqlite")

# Reflect an existing database into a new model
# Base = automap_base()

# Reflect the tables
# Base.prepare(engine, reflect=True)

# Save references to each table
# Measurement = Base.classes.measurement
# Station = Base.classes.station

# Create our session (link) from Python to the DB
# session = Session(engine)

# Flask Setup
app = Flask(__name__)

@app.route("/")
def home():
    # return render_template("index.html")
    return (
        "<h1>Welcome to the Twitch Dashboard Homepage!</h1><br/>"
        "Available Routes:<br/>"
        "/top_games<br/>"
        "/platforms<br/>"
        "/timeline<br/>"
        "/hours<br/>"
        "/growth<br/>"
        "/growth/games<br/>"
        "/growth/streamers<br/>"
        
    )


# @app.route("/top_games")
# def precipitation():
#     # Retrieve the last 12 months of precipitation data
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
#     # Perform a query to retrieve the data and precipitation scores
#     date_prcp = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()
    
#     session.close()
    
#     precipitation = {date: prcp for date, prcp in date_prcp}
#     print(precipitation)
#     return jsonify(precipitation)


# @app.route("/platforms")
# def stations():
#     # List the stations
#     results = session.query(Station.station).all()
    
#     session.close()
#     stations = list(np.ravel(results))
    
#     return jsonify(stations)


# @app.route("/timeline")
# def tobs():
#     # Query the dates and temperature observations of the most active station for the last year of data
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281')\
#                 .filter(Measurement.date >= prev_year).all()
        
#     session.close()    
#     temps = {date: tobs for date, tobs in results}

#     # Return a JSON list of temperature observations (TOBS) for the previous year.
#     date_temp = list(np.ravel(temps))
#     return jsonify(date_temp)

# @app.route("/hours")
# def tobs():
#     # Query the dates and temperature observations of the most active station for the last year of data
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281')\
#                 .filter(Measurement.date >= prev_year).all()
        
#     session.close()    
#     temps = {date: tobs for date, tobs in results}

#     # Return a JSON list of temperature observations (TOBS) for the previous year.
#     date_temp = list(np.ravel(temps))
#     return jsonify(date_temp)

# @app.route("/growth")
# def tobs():
#     # Query the dates and temperature observations of the most active station for the last year of data
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281')\
#                 .filter(Measurement.date >= prev_year).all()
        
#     session.close()    
#     temps = {date: tobs for date, tobs in results}

#     # Return a JSON list of temperature observations (TOBS) for the previous year.
#     date_temp = list(np.ravel(temps))
#     return jsonify(date_temp)

# @app.route("/growth/games")
# def tobs():
#     # Query the dates and temperature observations of the most active station for the last year of data
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281')\
#                 .filter(Measurement.date >= prev_year).all()
        
#     session.close()    
#     temps = {date: tobs for date, tobs in results}

#     # Return a JSON list of temperature observations (TOBS) for the previous year.
#     date_temp = list(np.ravel(temps))
#     return jsonify(date_temp)

# @app.route("/growth/streamers")
# def tobs():
#     # Query the dates and temperature observations of the most active station for the last year of data
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#     results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281')\
#                 .filter(Measurement.date >= prev_year).all()
        
#     session.close()    
#     temps = {date: tobs for date, tobs in results}

#     # Return a JSON list of temperature observations (TOBS) for the previous year.
#     date_temp = list(np.ravel(temps))
#     return jsonify(date_temp)



if __name__ == "__main__":
    app.run(debug=True)