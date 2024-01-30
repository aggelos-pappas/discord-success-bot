# Discord Succes Bot with Leaderboard

This Discord bot is designed to award points to members who post images in a specified channel, and it maintains a leaderboard to track members' points.

## Features

- Automatically awards points to members who post images in the designated success channel.
- Generates a leaderboard showing members with the most points.
- Uses Discord.py library for Discord bot integration.

## Setup

### Prerequisites

- Python 3.6 or higher
- Discord account
- Bot token (obtained from the Discord Developer Portal)

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/aggelos-pappas/discord-succes-bot.git
    ```

2. Navigate to the project directory:

    ```bash
    cd discord-bot-leaderboard
    ```

3. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. Create a `config.json` file in the project directory with the following structure:

    ```json
    {
        "token": "YOUR_DISCORD_BOT_TOKEN",
        "prefix": "!",
        "success_channel": "success"
        "bot_channel" : "bot"
    }
    ```

    Replace `"YOUR_DISCORD_BOT_TOKEN"` with your actual bot token obtained from the Discord Developer Portal.

2. Customize the `"prefix"` and `"success_channel"` values in the `config.json` file as needed.

### Running the Bot

Run the bot by executing the main Python script:

```bash
python bot.py



The bot should now be online and operational on your Discord server.

Usage
Members can earn points by posting images in the designated success channel.
Use the !leaderboard command to display the leaderboard showing members with the most points.

License
This project is licensed under the MIT License .

Acknowledgments
This project is built using the Discord.py library.
