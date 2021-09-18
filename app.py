from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
import numpy as np
from config import username, password, port, db_name
import pandas as pd

# Flask Setup
app = Flask(__name__)
# Database Setup using SQLAlchmy ORM
URI = f"postgresql://{username}:{password}@localhost:{port}/{db_name}"
Engine = create_engine(URI)
Base = automap_mapbase()
Base.prepare(engine, reflect=True)
# Map table

@app.route('/')
def home():
    return render_template("index.html")
@app.route("/everything")
def everything():
	df = pd.read_sql("""SELECT * FROM app_record;""", engine)
	results = df.to_dict(orient = "records")

	return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)