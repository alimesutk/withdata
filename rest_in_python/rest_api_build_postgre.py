from flask_sqlalchemy import sqlalchemy
import pandas as pd

baglan = sqlalchemy.create_engine('postgresql://admin:secret@localhost:5432/postgres')
baglanti = baglan.connect()

sorgu1 = baglanti.execute('SELECT * FROM typicode.albums LIMIT 10')
sonuc_tablo = pd.DataFrame(sorgu1.fetchall())
print(sonuc_tablo)


@app.route('/api/v1/resources/users', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for user in users:
        if user['id'] == id:
            results.append(user)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


app.run()


sorgu1.close()