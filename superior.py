import praw
import os

sub = "linuxmasterrace"

client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')
password = os.environ.get('pass')

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=password,
                     user_agent='You better be using Arch',
                     username='iusearchbtwbot')

for submission in reddit.subreddit(sub).new(limit=None):
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        if (not comment.saved):
          if ( "arch" in comment.body and "btw" in comment.body ):
            comment.reply("I use Arch btw. \n^Beep ^Boop")
            comment.save()
