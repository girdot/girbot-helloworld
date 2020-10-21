from bot import client

@client.command( "helloworld" )
async def helloworld(ctx):
    await ctx.send( "Oh heya" )
