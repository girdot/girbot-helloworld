from girbot import client

@client.command( "helloworld" )
async def helloworld(ctx):
    await ctx.send( "Oho heya" )
