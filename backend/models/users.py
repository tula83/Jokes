from db_connection.connection import user_collection

class User:
    def __init__(self, email=None,username=None):
        self.email=email
        self.username=username


    def get_user_data(self):
        # Simple function to retrieve user preferences or history (for now, returns a static response)
        user_data=user_collection.find()
        users=[]
        for item in user_data:
            item['_id']=str(item['_id'])
            users.append(item)

        return users

    def save_user_data(self):
        try:
            user_collection.insert_one({"email":self.email,"username":self.username})
            return "inserted successfully",201

        except Exception as e:
            print('excepton occurred',e)
            return "excetioon occurred",400



