from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@client.event
async def on_ready():
	#ココに記述
#任意のチャンネルIDを記述
ch_id = 677346242426044449
#入力されたチャンネルIDからチャンネル情報を取得してchannelに格納する。
channel = client.get_channel(ch_id)
#channelに指定されたワードをポストする。
await channel.send("起動完了！")

bot.run(token)
