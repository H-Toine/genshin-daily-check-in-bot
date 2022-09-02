# Genshin Impact Check-In Helper

A personal port from https://github.com/am-steph/wayscript-login-helper that I made to work on a raspberry pi.

## Notes for Windows

You may want to install [Git Bash](https://gitforwindows.org) to clone the repository  and to run below commands.

If you can't see the dot files (.env), make sure you have "show hidden files" enabled

## Installation

```
git clone git@github.com:Toinehaaijer/genshin-daily-check-in-bot.git
pip install -r requirements.txt
chmod a+x main.py
cp .env.example .env
```

## Cookies

1. Go to the Daily Check-In event website https://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=en-us
2. Log in with your MiHoYo/Genshin Impact account.
3. If you have never checked in before, manually check in once to ensure that your cookies are set properly.
4. Open the developer tools on your web browser (F12 on firefox/chrome)
5. Click on the “Console” tab
6. Type in document.cookie in the console
7. Copy the text output from the console
8. fill it in the .env file (or your environment).

### Multiple Accounts
Add a # immediately after the first cookie and paste the second cookie, no quotations and no spaces.

Do not log out of any account to grab another cookie, just open incognito and get cookie and close browser.

- Remove any quotation marks “” at the front or end of the text
- Go back to the MiHoYo event website. You may close the tab but do not click the “Log Out” button because it may cause your cookie to expire.
- IF YOU WANT TO CHECK-IN MULTIPLE GENSHIN ACCOUNTS:
- Paste your first cookie into the Value box on Wayscript.
- Open a new private browsing / Incognito window
- Go to the MiHoYo event website on your new browser instance, and log in with your second account
- Copy the document.cookie as before
- Go back to the Wayscript page, and type a hash # at the end of your first cookie
- Paste your second cookie immediately after the # and remove the quotation marks “” if needed

## Running the bot

Run it with: `./main.py`

### Scheduling

Schedule a task, preferably setting the time after the daily reset.

#### Linux

Of course, you'd want it to run every day, so you can set up a cronjob for this via `crontab -e` similar to this:
```
5 5 * * * /home/pi/Software/genshin-daily-check-in-bot/main.py >> /home/pi/Software/genshin-daily-check-in-bot/var/check-in.log 2>&1
```

#### Windows

Or if you're on Windows, you can use the Task Scheduler

Create a basic task:
  - Trigger: Daily
  - Actions (Start a program):
    - Browse to script
    - Start in: location of the script

## Telegram/Discord webhooks

Haven't tested the discord webhook after porting, but added a very basic telegram notification.

### Telegram

To add telegram notifications:
1. Create a bot via the BotFather (/newbot) as explained in https://core.telegram.org/bots
2. Store the bot access token
3. Message the bot at least once
4. Add the token to the `.env` file (filling chat id is not neccessary, as it will retrieve it from the first message)

### Discord

Follow the first 3 steps provided here: https://am-steph.github.io/wayscript-login-helper/#discord-webhooks

Then fill in the discord webhook in the .env file

Guide 
https://am-steph.github.io/wayscript-login-helper/
