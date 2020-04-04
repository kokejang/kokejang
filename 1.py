import discord
import datetime
client=discord.Client()
token='Njk1NjUxOTE5NDA2MDM5MDcy.XofALA.DirFQqjK4a4L1C6SGw-z8Jd_UFM'
@client.event
async def on_ready():
    print('----------------------------------------------------------------------------')
    print(f'| Client ID: {client.user.id}                                             |')
    print(f'| Client Name: {client.user.name}                                                    |')
    print(f'| Client Token: {str(token)} |')
    print('----------------------------------------------------------------------------\n\n=========================================\n\n')
@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content.startswith('고게장'):
        try:
            if message.content=='고게장 방송':
                await message.author.send('https://www.twitch.tv/kkj2020%27)
                await message.channel.send('DM을 확인해주세요!')
        except:
            print('에러가 발생하였습니다')
client.run(token)

