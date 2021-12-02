import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources\hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement

#flask setup
app = Flask(__name__)
#Flask routes
@app.route("/")
def Hawaii():
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session= Session(engine)
    
    first_query_dt= dt.date(2017,8,23)
    data = [Measurement.date, Measurement.prcp]
    q_result= session.query(*data).filter(Measurement.date >=first_query_dt).all()
    
    session.close()
    
    precipit = list(np.ravel(q_result))
    
    return jsonify(precipit)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    
    act_st= session.query(Measurement.station, func.count(Measurement.id)).\
    group_by(Measurement.station).\
    order_by(func.count(Measurement.id).desc()).all()
    
    session.close()
    
    station = list(np.ravel(act_st))
    
    return jsonify(station)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    
    most_act = "USC00519281" 
    first_query_dt= dt.date(2017,8,23)
    
    act_st_temp= session.query(Measurement.tobs).\
    filter(Measurement.date >=first_query_dt).\
    filter(Measurement.station == most_act).all()
    
    session.close()
    
    tob = list(np.ravel(act_st_temp))
    
    return jsonify(tob)
    
@app.route("/api/v1.0/<start>")
def start(start_date):
    session = Session(engine)
    
    beg_date= start_date
    q_results= session.query(func.min(Measurement.tobs), func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.date >=beg_date).all()
    
    session.close()
    
    date = list(np.ravel(q_results))
    
    return jsonify(date)

@app.route("/api/v1.0/<start>/<end>")
def dates (date_1, date_2):
    session = Session (engine)
        
    start = date_1
    end = date_2
    q_results= session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >=start).filter(Measurement.date <=end).all()
    
    session.close()
    
    dates = list(np.ravel(q_results))
    
    return jsonify (dates)

if __name__ == '__main__':
    app.run(debug=True)
