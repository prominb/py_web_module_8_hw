from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://romalearn:S13o1ebSZ63pTcsV@prominb0.3pd0e3e.mongodb.net/?retryWrites=true&w=majority&appName=Prominb0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
