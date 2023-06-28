# Day 17 <--> Quiz Project with OOP

class User:
    # pass
    def __init__(self,user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Michelle")
user_2 = User("002", "Sarah")


user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


# attribute --> variable associated with an object

# PascalCase, camelCase, and snake_case are common class naming conventions
# print(user_1.username)

# constructor --> used to initialize attributes in a class

# methods can also be created for an object