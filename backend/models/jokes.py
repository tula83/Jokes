from db_connection.connection import jokes_collection

class Jokes:
    def __init__(self, category=None,message=None):
        self.category=category
        self.message=message

    def get_joke(self):
        data=jokes_collection.find()
        result=[]
        for item in data:
            item['_id']=str(item['_id'])
            result.append(item)

        return result

    def save_joke(self):
        try:
            jokes_collection.insert_one({"category":self.category,"message":self.message})
            return "inserted successfully"

        except Exception as e:
            print('exception occurred',e)
            return "error occurred while inserting data",404


