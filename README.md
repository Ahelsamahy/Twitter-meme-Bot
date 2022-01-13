
<h3 align="center">I did it for memes</h3>

<p align="center">
  <a href="#Why">Why</a> •
  <a href="#How-it-works">How it Works</a> •
  <a href="#Installation">Installation</a> •
  <a href="#emailware">Emailware</a> •
  <a href="#license">License</a>
</p>

<p align="center">
<img src="https://github.com/Ahelsamahy/Twitter-meme-Bot/blob/main/Header%20image.png?raw=true" >
</p>



# Why
I had folder on my phone since 2013 with 5K+ image of memes inside of it and didn't want for it all to go for nothing as it made me laugh a lot when internet was out, so i decided to share this knowledge with the world as it would make it a better place

(it was also a proof to tell my teacher that I can code better in python)

# How-it-works
From the main method `release_the_meme()` first it gets the absolute directory of the ` .py` file then it sorts the images in the folder `Memes` according to their modification time then in the for loop, it uploads the first image in the for loop with its name (after replacing every {-} with space ) as a caption, then it moves it to `_Done` folder to not upload it again and shows in the terminal that it is moved with the number of tweet.

After the image is uploaded, the bot will send a message to the main account (that is defined in  `api.send_direct_message()`) with the date of uploading the tweet and the number of it, it is used to keep you updated with the recent ones and keep an eye that the bot is still working.

# Installation
> ⚠️ Best to run the bot on a VPS to make sure it is running 24/7. For now i'm using [vultr][1].

You will need to have [Tweepy][2] , [Schedule][3] and [Tmux][4] with Python3



1. Clone this repository `git clone https://github.com/Ahelsamahy/Twitter-meme-Bot.git`
2. Install all requirements `pip install -r requirements.txt`
3. Create an app account on [Twitter][5]

    3.1. Sign in with your Twitter account.
    
    3.2. Create a new app account.
    
    3.3. Modify the settings for that app account to allow read & write.

    3.4. Generate a new OAuth token with those permissions.

Following these steps will create 4 tokens that you will need to place in the configuration file discussed below.

3. Edit and update the main file with your `CONSUMER_KEY` `CONSUMER_SECRET` `ACCESS_KEY` `ACCESS_SECRET`

4. Change  `id` with the bot's twitter account id in addition to `api.send_direct_message()` with your account ID to get message from the bot

[1]: https://www.vultr.com/ "VPS"
[2]: https://docs.tweepy.org/en/stable/install.html "Tweepy library"
[3]: https://pypi.org/project/schedule/ "Schedule"
[4]: https://linuxize.com/post/getting-started-with-tmux/ "Tmux"
[5]: https://dev.twitter.com/apps "create app"

# Emailware
Twitter-meme-Bot is an [emailware](https://en.wiktionary.org/wiki/emailware). Meaning, if you liked using this app or it has helped you in any way, I'd like you send me an email at <ahmelsamahy@gmail.com> about anything you'd want to say about this software. I'd really appreciate it!

# License
If you have project similar to this which you will use this instead in it or you may use this project, don't forget to mention me or send me email about it.