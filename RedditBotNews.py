import praw # pip install this

reddit = praw.Reddit(
    client_id='UctJAJCE-8-nvA',
    client_secret='1FsIcCXLLrKqxcAU3bRISfzuUrI',
    user_agent = 'my user agent'

)
for submission in reddit.subreddit('news').hot(limit=5):
    print(submission.title)
    print('=========================')
