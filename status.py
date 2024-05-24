import docker
import discord
import os
import asyncio

from discord.ui import Modal, TextInput, Select



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


CLIENT_VARIABLE = os.environ.get("CLIENT_VARIABLE")



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

class FeedbackModal(Modal):
  title = " Doggo Feedback"

  feedback_input = TextInput(label="Tell us what you think about Doggo!", style=TextInput.style.short)

  async def on_submit(self, interaction: discord.Interaction):
    feedback = self.feedback_input.value
    await interaction.response.send_message(content=f"Thanks for your feedback, {interaction.user.display_name}!")
    # Send feedback to a designated channel (explained later)
    await client.get_channel(feedback_channel_id).send(f"{interaction.user.display_name}: {feedback}")

client = discord.Client(intents=discord.Intents.default().message_content)

feedback_channel_id = os.environ.get("CHANNEL_ID")



@discord.client.event
async def on_message(message):
  if message.author == discord.client.user:
    return

  if message.content.startswith('#doggo'):
    # Open feedback modal
    modal = FeedbackModal()
    await modal.present(view=message.channel)


discord.client.run("CLIENT_VARIABLE")
