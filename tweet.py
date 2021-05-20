import tweepy

auth = tweepy.OAuthHandler("QjUyaELZLcFCNB4iSCGmmerIL", "YyJedvRuL223Lc3qpJ7oLy7o5JZdCI7iNqpJRQ3OijhjBQvHpS")
auth.set_access_token("942898015068594176-VysBmrclmAdoghThUQNNLbuze9pttPb", "DQ5zLaup9zZH9Vy6t6Km7irdGCk1xIfqQwKJRu7QUKsvq")

api = tweepy.API(auth)

