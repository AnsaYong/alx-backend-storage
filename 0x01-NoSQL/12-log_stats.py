#!/usr/bin/env python3
"""
This module provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


# Connect to MongoDB
client = MongoClient()
db = client.logs
collection = db.nginx

# Count total logs
total_logs = collection.count_documents({})

# Count logs by method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in methods}

# Count logs with method=GET and path=/status
status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

# Display stats
print(f"{total_logs} logs")
print("Methods:")
for method, count in method_counts.items():
    print(f"\tmethod {method}: {count}")
print(f"{status_check_count} status check")
