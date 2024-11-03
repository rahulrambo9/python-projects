class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.user = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

u1 = User("01", "Rajesh")
u2 = User("02", "rahul")

u1.follow(u2)

print(u1.followers)
print(u2.followers)
print(u1.following)
print(u2.following)
