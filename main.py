import discord
client = discord.Client()
print('If some kid decided to just spam add you to bunch of group chats in discord just use this tool. \n\n(Please know that this tool makes you leave ALL of your group chats.)\n\nIf you want to not leave all your group then contact sigma#4268, I will try to make one \nPlease Read Instructions Below.\n')

print("How to Get Your Discord Token: https://www.youtube.com/watch?v=YEgFvgg7ZPI\n\nInstructions\n-------------\n1. Get Your Discord Token\n2. Execute Script\n3. Paste Your Discord Token In Without The Quotation Marks & Press Enter.\n4. Go on Your Discord Account and Type 'start' in Any Place & Enter\n5. It Will Start to Leave Group Chats For You.\nDiscord for Help: sigma#4268 \n")

token = input("Enter Discord Token: ")
@client.event
async def on_ready():
	print('Ready')

@client.event
async def on_message(message):
	if message.author == client.user:
		starting = str(message.content)
		if starting == 'start':
			await message.delete()
			groups_left = 0
			for i in client.private_channels:
				if isinstance(i, discord.GroupChannel):
					await i.leave()
					groups_left += 1
					print(f'You Left {groups_left} groups.')
			await client.close()


client.run(token, bot = False)
#made this cuz a kid spammed added me with groups on discord
