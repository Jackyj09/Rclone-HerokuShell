# HerokuShell-Rclone
 Interface Heroku's shell through Telegram, plus Rclone support
 
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://gitlab.com/PavithranR/rcloneheroku-shell/tree/master)

## Installation
- First get the following prepared:
  - A @BotFather bot token. [Tutorial](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token)
  - Your Telegram user ID. Talk with [this](https://t.me/userinfobot) bot
  - [OPTIONAL] Your Rclone config, you need to encode it to [Base64](https://www.base64encode.org)
- Next click the Deploy button above, make sure you have a Heroku account
- Fill in the text fields with the information you prepared
- Press the `Deploy` button
- Wait for the app to finish deploying
- Go to the app's dashboard and go onto the 'Resources' tab
- On the `web npm start` worker, click the pencil icon and toggle it off
- On the `worker source setup.sh && bash start.sh` worker, click the the pencil icon and toggle it on
- Now open telegram and use the commands below to interact with your bot

## Commands
- To use rclone commands do `/run rclone [param]...`
```
run - Execute command
enter - Send input lines to command
type - Type keys into command
control - Type Control+Letter
meta - Send the next typed key with Alt
keypad - Toggle keypad for special keys
redraw - Force the command to repaint
end - Send EOF to command
cancel - Interrupt command
kill - Send signal to process
status - View status and current settings
cd - Change directory
env - Manipulate the environment
shell - Change shell used to run commands
resize - Change the terminal size
setsilent - Enable / disable silent output
setlinkpreviews - Enable / disable link expansion
setinteractive - Enable / disable shell interactive flag
help - Get help
file - View and edit small text files
upload - Upload and overwrite raw files
r - Alias for /run or /enter
```

### Required Variables

* `BOT_TOKEN`: The bot token provided by @BotFather
* `OWNER_ID`: Your Telegram user ID, get it from @userinfobot
* `RCLONE_CONFIG_BASE64`: Your Rclone config encoded using [Base64](https://www.base64encode.org)