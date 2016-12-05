from flask import Flask, render_template
import urllib2, json, os
import quandl 


app = Flask(__name__)

quandl.ApiConfig.api_key = 'RVXSJLquh4yaDva-T4TB'


@app.route("/")
def root():

    data = quandl.get_table("ZACKS/FC", ticker="MSFT")
    print data
    return render_template("index.html", pic=data)
"""
    u = urllib2.urlopen("http://finance.yahoo.com/d/quotes.csv?s=GOOGL&f=abo")
    response = u.read()
    data = json.loads( response )
    return render_template("index.html", pic = data['url'] )
"""

if __name__ == "__main__":
    app.debug = True
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
