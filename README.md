# Genshin Impact Check-In Helper

A personal port from https://github.com/am-steph/wayscript-login-helper that I made to work on a raspberry pi.

Installation:
```
git clone git@github.com:Toinehaaijer/genshin-daily-check-in-bot.git
pip install -r requirements.txt
chmod a+x main.py
cp .env.example .env
```

Get your cookie(s) and fill it in the .env file (or your environment) as explained in: https://am-steph.github.io/wayscript-login-helper/

Then run it with: `./main.py`

Of course, you'd want it to run every day, so you can set up a cronjob for this via `crontab -e` similar to this:
```
5 5 * * * /home/pi/Software/genshin-daily-check-in-bot/main.py >> /home/pi/Software/genshin-daily-check-in-bot/var/check-in.log 2>&1
```

Haven't tested the discord webhook after porting, but added a very basic telegram notification.

To add telegram notifications:
1. Create a bot via the BotFather (/newbot) as explained in https://core.telegram.org/bots
2. Store the bot access token
3. Message the bot at least once
4. Add the token to the `.env` file (filling chat id is not neccessary, as it will retrieve it from the first message)



Guide 
https://am-steph.github.io/wayscript-login-helper/
