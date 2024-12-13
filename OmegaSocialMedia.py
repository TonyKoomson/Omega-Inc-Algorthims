from collections import defaultdict, deque
import heapq

class OmegaSocialMedia:
    def __init__(self):
        self.users = []
        self.friendships = {}  
        self.posts = []  
        self.live_feed = []

    def register_user(self, username, email, phone_number):
        # Registering a new user
        for user in self.users:
            if user['username'] == username:
                print(f"Error: User with username '{username}' already exists.")
                return
        new_user = {
            'username': username,
            'email': email,
            'phone_number': phone_number
        }
        self.users.append(new_user)
        self.friendships[username] = []  # Store friends list for the user
        print(f"User '{username}' registered successfully.")

    def add_friendship(self, user1, user2):
        # Adds a friendship between two users
        if user1 not in self.friendships or user2 not in self.friendships:
            print("Error: One or both users do not exist.")
            return
        
        if user2 not in self.friendships[user1]:
            self.friendships[user1].append(user2)
            self.friendships[user2].append(user1)
            print(f"Users '{user1}' and '{user2}' are now friends.")
        else:
            print(f"Error: Users '{user1}' and '{user2}' are already friends.")

    def remove_friendship(self, user1, user2):
        # Removes a friendship between two users
        if user1 not in self.friendships or user2 not in self.friendships:
            print("Error: One or both users do not exist.")
            return

        if user2 in self.friendships[user1]:
            self.friendships[user1].remove(user2)
            self.friendships[user2].remove(user1)
            print(f"Users '{user1}' and '{user2}' are no longer friends.")
        else:
            print(f"Error: Users '{user1}' and '{user2}' are not friends.")

    def add_post(self, user, content):
        # Adds a post to the user's post list
        if user not in self.friendships:
            print(f"Error: User '{user}' does not exist.")
            return
        
        if not content.strip():
            print("Error: Post content cannot be empty or just spaces.")
            return

        new_post = {
            'user': user,
            'content': content,
            'timestamp': len(self.posts)  # Simple timestamp using the current length of posts
        }
        self.posts.append(new_post)
        print(f"Post added by {user}: {content}")

    def get_user_posts(self, user):
        # Retrieves posts for a specific user
        user_posts = [post for post in self.posts if post['user'] == user]
        
        if not user_posts:
            print(f"No posts found for user '{user}'.")
            return
        
        for post in user_posts:
            print(f"{post['user']}: {post['content']}")

    def recommend_friends(self, user):
        # Recommends friends based on mutual friends (using BFS)
        if user not in self.friendships:
            print(f"Error: User '{user}' does not exist.")
            return
        
        mutual_friends_count = defaultdict(int)
        visited = set()
        queue = deque([user])

        while queue:
            current_user = queue.popleft()
            visited.add(current_user)
            for friend in self.friendships[current_user]:
                if friend != user and friend not in visited:
                    queue.append(friend)
                for mutual_friend in self.friendships[friend]:
                    if mutual_friend != user and mutual_friend not in self.friendships[user]:
                        mutual_friends_count[mutual_friend] += 1
        
        recommended_friends = sorted(mutual_friends_count.items(), key=lambda x: x[1], reverse=True)
        
        if not recommended_friends:
            print(f"No friends recommended for '{user}'.")
        else:
            print(f"Friend recommendations for '{user}':")
            for friend, count in recommended_friends:
                print(f"{friend} with {count} mutual friends.")

    def remove_post(self, user, content):
        # Removes a specific post by a user
        if user not in self.friendships:
            print(f"Error: User '{user}' does not exist.")
            return
        
        post_to_remove = None
        for post in self.posts:
            if post['user'] == user and post['content'] == content:
                post_to_remove = post
                break
        
        if post_to_remove:
            self.posts.remove(post_to_remove)
            print(f"Post removed by {user}: {content}")
        else:
            print(f"Error: Post not found for user '{user}' with content '{content}'.")

    def merge_sort(self, posts):
        # Merge Sort to sort posts by timestamp (recency)
        if len(posts) <= 1:
            return posts
        mid = len(posts) // 2
        left = self.merge_sort(posts[:mid])
        right = self.merge_sort(posts[mid:])
        
        return self.merge(left, right)

    def merge(self, left, right):
        # Merging function for merge sort
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i]['timestamp'] > right[j]['timestamp']:  # Sorting by recency (timestamp)
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def get_sorted_posts(self):
        # Retrieves the sorted posts using merge sort
        sorted_posts = self.merge_sort(self.posts)
        return sorted_posts
    
    def add_post_to_live_feed(self, post):
        # Adds posts to live feed (using Priority Queue)
        heapq.heappush(self.live_feed, (-post['timestamp'], post))  # Max-heap by negating the timestamp

    def get_live_feed(self):
        # Retrieves live feed (most recent posts first)
        live_feed_posts = []
        while self.live_feed:
            _, post = heapq.heappop(self.live_feed)
            live_feed_posts.append(post)
        return live_feed_posts
        