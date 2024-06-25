from astrapy import DataAPIClient

# Initialize the client
client = DataAPIClient("AstraCS:iwarwQAxLISzoemuBKgNAlws:dc48f5f0250dda8699c584a40cd7c2d58a4c2a2227891c1667964118775d1731")
db = client.get_database_by_api_endpoint(
  "https://a13163e2-82f4-4996-8969-1beb3348cab5-us-east-2.apps.astra.datastax.com"
)

print(f"Connected to Astra DB: {db.list_collection_names()}")