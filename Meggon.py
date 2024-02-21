# Replace 'CHANNEL_ID_RESPOND' with the ID of the channel where you want the bot to respond
CHANNEL_ID_RESPOND = 1210006762162356325
CHANNEL_ID_LISTEN = 974077965686165514

# Create an instance of the bot
bot = commands.Bot(command_prefix='&!?')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    # Check if the message starts with the command prefix and is not from the bot itself
    if message.content.startswith('&!?') and message.author != bot.user:
        # Check if the message is in the specified channel to listen
        if message.channel.id == CHANNEL_ID_LISTEN:
            # Extract the command and check for specific commands
            command = message.content[3:].lower().strip()
            if command == 'fuf':
                # Replace 'CHANNEL_ID_RESPOND' with the ID of the channel where you want to respond
                respond_channel = bot.get_channel(CHANNEL_ID_RESPOND)
                await respond_channel.send(f"Please, tell me again, young Padawan, how chatGPT will not work?")

    # Let the bot process commands as well
    await bot.process_commands(message)

# Run the bot with the token
bot.run(TOKEN)