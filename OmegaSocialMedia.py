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
            print(f"User '{username}' registered succesfully.")
        pass
    
    def add_friendship(self, username, email, phone_number):
        # (not implemented yet)
        pass

    def remove_friendship(self, user1, user2):
        # (not implemented yet)
        pass

    def add_post(self,user,content):
        # (not implemented yet)
        pass

    def get_user_posts(self, user):
        # (not implemented yet)
        pass

    def recommend_friends(self, user):
        # (not implemented yet)
        pass

