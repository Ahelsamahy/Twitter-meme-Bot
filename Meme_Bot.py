import tweepy  # the main library
import time  # for the interval
import os
import shutil
import schedule
from pathlib import Path


CONSUMER_KEY = 'Your Own Credentials'
CONSUMER_SECRET = 'Your Own Credentials'
ACCESS_KEY = 'Your Own Credentials'
ACCESS_SECRET = 'Your Own Credentials'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def release_the_meme():
    imagePath = 'Memes'
    script_dir = os.path.dirname(os.path.realpath(
        __file__))
    # absolute dir the script is in
    images = os.path.join(script_dir, imagePath)

    # sort by data of modification
    imagesScanned = sorted(Path(images).iterdir(), key=os.path.getmtime)

    for i in imagesScanned:

        filename = os.path.join(imagePath, i)

        # this one is used instead of the old one to remove the string from the end with [:num]
        i = i.name
        pureName = i.replace("-", " ")

        api.update_status_with_media(pureName[:-4], filename)

        # Moving the file
        source = images + "/" + i
        destination = '_Done'
        MoveTo = os.path.join(script_dir, destination)
        shutil.move(source, MoveTo)
        print("the file \"" + i + "\" is moved")

        # will send message to my account everytime the bot uploads with the
        # time of upload and the number of tweet so i know that the bot is still working

        id = "Change it to yours"

        # fetching the user (that is the bot account) to get the number of tweets
        user = api.get_user(user_id=id)
        # fetching the statuses_count attribute
        statuses_count = user.statuses_count
        # to get time of upload in 12 hour format
        date_time = time.strftime('%Y-%m-%d %I:%M:%S %p')
        print("and uploaded to twitter at " + date_time +
              " tweet num is " + str(statuses_count))

        # send me DM to tell me that all uploading is done
        text = "I successfully uploaded meme at " + date_time + \
            " , tweet num is " + str(statuses_count)

        api.send_direct_message(
            "you should write the ID of your account", text)
        break


"""
to deal with the file location,
the code was working when I gave the absolute path
but when i move it to server, I don't know really the location for it,
so i need to get the location for the script first and then add the location of the folder of
images then work with it
"""
# RUN THE CODE AS ADMIN #
"""
tmus is used to make the code work on the background of server even when 
you close the window/session

tmux a -t 0 ==> to join the session
tmux kill-session -t #num

"""

schedule.every(10800).seconds.do(release_the_meme)


while True:
    schedule.run_pending()
