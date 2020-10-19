# get top posts in a subreddit
import praw # pip install this

reddit = praw.Reddit(   # my application
    client_id='UctJAJCE-8-nvA',
    client_secret='1FsIcCXLLrKqxcAU3bRISfzuUrI',
    user_agent = 'my user agent'

)
sb = input("Enter subreddit to go to")
n = int(input("Enter the number of titles needed"))
for submission in reddit.subreddit(sb).hot(limit=n):
    print(submission.title)
    print('=========================')
