from collections import defaultdict, deque
import heapq

class OmegaSocialMedia:
    def __init__(self):
        self.users = []:
        self.frendships = {}:
        self.post = []:
    
    def register_user(self,username,email,phone_number):
        for user in self.users:
            if user['username'] == username:
                print(f"Error: User with username '{username}' already exsits.")
                return
            new_user = {
                'username': username,
                'email': email,
                'phone_number': phone_number
            }
            self.users.append(new_user)
            self.frendships[username] = username
            print(f"User '{username}' registered succesfully.")
        
    
    def add_friendship(self, username, email, phone_number):
        if user1 not in self.friendships or user2 not in self.friendships:
            print("Error: one or both users do not exist.")
        return
    
        if user2 not in self.friendships or user2 not in self.friendships:
            print("Error: One or both users do not exist.")
            return
        
        if user2 not in self.frendships[user1]:
            self.frendships[user1].append(user2)
            self.add_friendships[user2].append(user1)
            print(f"Users '{user1} and {user2} are now friends.")
        else:
            print(f"Error: Users '{user1}' and '{user2}are already friends.")

    def remove_friendship(self, user1, user2):
        if user1 not in self.friendship or user2 not in self.friendships:
            print("Error: One or Both users does not exist")
        return

        if user2 in self.frendships[user1]:
            self.frendships[user1].remove(user2)
            self.frendships[user2].remove(user1)
            print(f"Users '{user1}' and ' {user2}' are no longer friends")
        else:
            print(f"Error: Users '{user1}' and '{user2}' are not friends")

    def add_post(self,user,content):
        # (not implemented yet)
        pass

    def get_user_posts(self, user):
        # (not implemented yet)
        pass

    def recommend_friends(self, user):
        # (not implemented yet)
        pass

