import pymongo 
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://harshalnir99:harshalnir99@harshal1.dx009wo.mongodb.net/")
db = client.test

DATA_FILE_PATH = (r"D:\Insurance Project\Insurance_ML_Project\insurance.csv")
DATABASE_NAME = "Insurance"
COLLECTION_NAME = "Insurance Predication dataset"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")


    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)