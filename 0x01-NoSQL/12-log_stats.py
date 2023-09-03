#!/usr/bin/env python3
"""Log stats
    """
from pymongo import MongoClient


def log_stats(logs: MongoClient):
    """Python script that provides some stats
        about Nginx logs stored in MongoDB
        """
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("{} logs\nMethods:".format(logs.count_documents({})))
    for method in method:
        print("\tmethod {}: {}".format
              (method, logs.count_documents({"method": method})))
    print("{} status check".format
          (logs.count_documents({"method": "GET", "path": "/status"})))


if __name__ == "__main__":
    """Main function
        """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    log_stats(logs)
