from flask import Flask, render_template, redirect
import scrape_mars
from flask_pymongo import PyMongo


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/db_mars"
mongo = PyMongo(app)

@app.route("/")
def index():

    # Find one record of data from the mongo database
    mars = mongo.db.mars.find_one()

    return render_template("index.html", mars = mars)

@app.route('/scrape')
def scrape():
    mars_data = scrape_mars.scrape()
    
    # Update the Mongo database using update and upsert=True
    mongo.db.mars.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)