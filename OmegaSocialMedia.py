from collections import defaultdict, deque
import heapq

Class OmegaSocialMedia;
    def __init__(self);
    self.users = {}
    self.friendships = defaultdict(set)
    self.feed =  []
    self.max_feed_size = 1000