import discord
from discord.ext import tasks
import asyncio

TOKEN = 'ODEzMjE2ODk1NzYyMTY5ODc2.G-P4O9.ix4yU6SlB_TAECqKj3OKPPUJDf-oJR2eILR8vI'  # 유저 토큰
COMMAND_PREFIX = '!'
TARGET_CHANNEL_ID = None

with open("g.txt", "r", encoding="utf-8") as f:
    AD_TEXT = f.read()

client = discord.Client(self_bot=True)

@client.event
async def on_ready():
    print(f"{client.user} 로그인 완료")

@client.event
async def on_message(message):
    global TARGET_CHANNEL_ID

    if message.author.id != client.user.id:
        return

    if message.content.startswith("!홍보"):
        try:
            parts = message.content.split()
            if len(parts) != 2:
                await message.channel.send("사용법: `!홍보 <채널ID>`")
                return

            channel_id = int(parts[1])
            channel = client.get_channel(channel_id)
            if not channel:
                await message.channel.send("유효하지 않은 채널 ID입니다.")
                return

            TARGET_CHANNEL_ID = channel_id
            await message.channel.send(f"이제 {channel.mention} 채널에 6시간마다 홍보를 시작합니다.")
            if not auto_advertise.is_running():
                auto_advertise.start()

        except Exception as e:
            await message.channel.send(f"오류 발생: {e}")

@tasks.loop(hours=6)
async def auto_advertise():
    if TARGET_CHANNEL_ID:
        channel = client.get_channel(TARGET_CHANNEL_ID)
        if channel:
            try:
                await channel.send(AD_TEXT)
            except Exception as e:
                print(f"홍보 실패: {e}")

client.run(TOKEN)
