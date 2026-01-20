import pymongo
from pymongo.errors import ConnectionFailure, ConfigurationError, InvalidURI
import os

def check_mongodb_url(url):
    try:
        client = pymongo.MongoClient(url, serverSelectionTimeoutMS=3000)
        client.server_info()
        print("[✓] MongoDB URL is valid and connected successfully!")
    except (ConnectionFailure, ConfigurationError, InvalidURI) as e:
        print("[✗] Invalid MongoDB URL or connection failed!")
        print("Error:", e)
    finally:
        try:
            client.close()
        except:
            pass

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("🔍 MongoDB URL Validator")
    print("🎨 Made by Z3eem | 🌐 Full-Stack Dev")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    # 👉 Paste your MongoDB URL here instead of using input()
    mongo_url = input("Enter your MongoDB URL to check: ")
    check_mongodb_url(mongo_url)
url(mongo_url)
