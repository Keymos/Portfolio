# Lists accounts that are not following back and gives the option
# to unfollow them.
from InstagramAPI import InstagramAPI


class MyInstagramAPI:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.api = InstagramAPI(self.username, self.password)
        self.api.login()
        self.user_id = self.api.username_id
        print(self.user_id)


    def __getFollwxs(self, api_function):
        following = []
        next_max_id = True
        while next_max_id:
            # first iteration hack
            if next_max_id == True: next_max_id = ''
            _ = api_function(self.user_id, maxid=next_max_id)
            following.extend(self.api.LastJson.get('users', []))
            next_max_id = self.api.LastJson.get('next_max_id', '')
        return following


    def getFollowings(self):
        return self.__getFollwxs(self.api.getUserFollowings)


    def getFollowers(self):
        return self.__getFollwxs(self.api.getUserFollowers)

    def Unfollow(self, idOfEheUser):
        self.api.unfollow(idOfEheUser)



userName = input("Username: ")
Password = input("Password: ")
Account = MyInstagramAPI(userName, Password)
i = 0
List_Followers = []
List_Followings = []
FullList_Followers = Account.getFollowers()
FullList_Followings = Account.getFollowings()
while i < len(FullList_Followers):
    List_Followers.append(FullList_Followers[i]['username'])
    #print(List_Followers[i])
    i = i + 1

i = 0
while i < len(FullList_Followings):
    List_Followings.append(FullList_Followings[i]['username'])
    #print(List_Followings[i])
    i = i + 1

# Shows the usernames of those who are not following back.
print("Users that are not follwing you back are:")
Ungrats = []
for z in List_Followings:
    if z not in List_Followers:
        Ungrats.append(z)
        print(z)

CurrentInput = False
while CurrentInput == False:
    Input = input("would you like to unfollow some of them? (y/n): ")
    if Input == 'y' or Input == 'n':
        break

if Input == 'y':
    i = 0
    j = 0
    while j < len(Ungrats):
        Input = ''
       	CurrentInput = False
        while CurrentInput == False:
            Input = input("Unfollow %s? (y/n): " % Ungrats[j])
            if Input == 'y' or Input == 'n':
                break
        if Input == 'y':
            while i < len(List_Followings):
                # print(i)
                if Ungrats[j] in FullList_Followings[i]['username']:
                    Account.Unfollow(FullList_Followings[i]['pk'])
                    break
                else:
                    i = i +1
        #print('-----%i' % j)
        j = j + 1
    print("Done.")
