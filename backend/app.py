from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://dbuser:wxDuSTuQRuNvAYMb @to-do-list.oqi8izk.mongodb.net/?retryWrites=true&w=majority&appName=to-do-list")
db = client['todoDB']
collection = db['todoItems']

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    if not item_name or not item_description:
        return "Missing required fields", 400

    data = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    collection.insert_one(data)
    return "To-Do item submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)