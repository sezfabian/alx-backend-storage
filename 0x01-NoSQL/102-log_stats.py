#!/usr/bin/env python3
"""Log stats
    """
from pymongo import MongoClient


def log_ips(logs: MongoClient):
    """ Returns a list of top 10 of the most present IPs
        in the collection nginx of the database logs
        """
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    return list(logs.aggregate(pipeline))


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

    ip_counts = log_ips(logs)
    print("IPs:")
    for i in range(10):
        print("\t{}: {}".format(ip_counts[i].get('_id'),
                                ip_counts[i].get('count')))


if __name__ == "__main__":
    """Main function
        """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs.nginx
    log_stats(logs)
