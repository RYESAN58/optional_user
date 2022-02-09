# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Users:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.lastname = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query)
        # Create an empty list to append our instances of friends
        arr = []
        # Iterate over the db results and create instances of friends with cls.
        for user in results:
            arr.append( cls(user) )
        return arr
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO user ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('users').query_db( query, data)
    @classmethod
    def remove(cls, num ):
        query = f"DELETE FROM `users`.`user` WHERE (`id` = {num});"
        return connectToMySQL('users').query_db( query)
    @classmethod
    def update(cls, data):
        query= "UPDATE `users`.`user` SET `first_name` = %(fname)s, `last_name` = %(lname)s, `email` = %(email)s WHERE (`id` =  %(id)s);"
        return connectToMySQL('users').query_db( query,data)