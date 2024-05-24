import docker
import discord
import os
import asyncio



print('imported docker')

client = docker.DockerClient(base_url='unix://var/run/docker.sock')
containers = client.containers.list(all=True)
print('established client')

containernum = 0
containerList = []

for container in containers:
        containerInfo = {}
        containerInfo["Name"] = container.name
        containerInfo["Status"] = container.status
        containerInfo["Short_Id"] = container.short_id
        containerInfo["image"] = container.image
        containernum += 1
        print(f'retrieved container {containernum} info')

        containerList.append(containerInfo)


for item in containerList:
        print(item)





from discord.ui import Modal



intents = discord.Intents.default()
intents.message_content = True

discord.client = discord.Client(intents=intents)




@discord.client.event
async def on_ready():
    print(f'We have logged in as {discord.client.user}')

@discord.client.event
async def on_message(message):
    if message.author == discord.client.user:
        return

    if message.content.startswith('#doggo'):
        globaluser = message.author
        nickname = globaluser.display_name
        await message.channel.send(f'## Hello {globaluser.display_name}! \r\r Here are your currently running containers - ')
        for item in containerList:
            await message.channel.send(f'\r\r {item}')


discord.client.run("CLIENT_VARIABLE")
