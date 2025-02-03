import discord
from discord import app_commands
import settings

# from mapppings import char_map
from AcceptDeclineView import AcceptDeclineView
import api_handlers as api

MY_GUILD = discord.Object(id=962463337394876436)  # replace with your guild id
token = settings.TOKEN


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = app_commands.CommandTree(self)

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as: {client.user} (ID: {client.user.id})")


@client.tree.command()
@app_commands.describe(
    score="Enter the score e.g., 4:3 (First your score)",
    enemy="Enter the opponent",
    # charp1="Enter your character",
    # charp2="Enter the enemies character",
)
async def result(
    interaction: discord.Interaction,
    score: str = "0",
    enemy: discord.Member = None,
    # charp1: str = "None",
    # charp2: str = "None",
):
    """Enter a result of your set"""

    member = interaction.user  # The user executing the command

    # validate char selection
    # if charp1 not in char_map:
    #     no_char_report = discord.Embed(
    #         title=":stop_sign: ERROR",
    #         description="Tipfehler in your character!",
    #         color=discord.Color.red(),
    #     )
    #     await interaction.response.send_message(embed=no_char_report, ephemeral=True)
    #     return
    # if charp2 not in char_map:
    #     no_char_report = discord.Embed(
    #         title=":stop_sign: ERROR",
    #         description="Tipfehler in enemy character!",
    #         color=discord.Color.red(),
    #     )
    #     await interaction.response.send_message(embed=no_char_report, ephemeral=True)
    #     return

    # Validate the score format
    if not score.count(":") == 1 or not all(
        part.isdigit() for part in score.split(":")
    ):
        scoreinvalid = discord.Embed(
            title=":stop_sign: ERROR",
            description="Invalid score format! Please use X:X where X is a number.",
            color=discord.Color.red(),
        )
        await interaction.response.send_message(embed=scoreinvalid, ephemeral=True)
        return

    if member == enemy:
        enemyequalsmember = discord.Embed(
            title=":stop_sign: ERROR",
            description="You cannot report a match against yourself!",
            color=discord.Color.red(),
        )
        await interaction.response.send_message(embed=enemyequalsmember, ephemeral=True)
        return

    bot_role = discord.utils.get(
        interaction.guild.roles, id=962486170384752680
    )  # Bot role ID
    if bot_role in enemy.roles:
        botreport = discord.Embed(
            title=":stop_sign: ERROR",
            description="Seriously? You wanna play against one of the all mighty?",
            color=discord.Color.red(),
        )
        await interaction.response.send_message(embed=botreport, ephemeral=True)
        return

    # view = AcceptDeclineView(member, score, enemy, charp1, charp2)
    view = AcceptDeclineView(member, score, enemy)
    prompt_embed = discord.Embed(
        title="Do you accept the result?",
        description=f"**{member.mention}** scored **{score}** against **{enemy.mention}** \n",
        color=discord.Color.blue(),
    )
    # **{member.mention}** played **{charp1}** and **{enemy.mention}** played **{charp2}**"
    view.message = await interaction.response.send_message(
        f"{enemy.mention}", embed=prompt_embed, view=view
    )


@client.tree.command()
@app_commands.describe(
    player="Select Member",
    displayname="Enter the display name",
)
@app_commands.default_permissions(administrator=True)
async def addplayer(
    interaction: discord.Interaction,
    player: discord.Member = None,
    displayname: str = "None",
):
    """Add a player to the database"""

    if player == None:
        no_player = discord.Embed(
            title=":stop_sign: ERROR",
            description="You need to select a player!",
            color=discord.Color.red(),
        )
        await interaction.response.send_message(embed=no_player, ephemeral=True)
        return
    if displayname == "None":
        no_displayname = discord.Embed(
            title=":stop_sign: ERROR",
            description="You need to enter a display name!",
            color=discord.Color.red(),
        )
        await interaction.response.send_message(embed=no_displayname, ephemeral=True)
        return
    else:
        # send the player to the api
        api.add_player(player.id, displayname)
        added_player = discord.Embed(
            title=":white_check_mark: ADDED",
            description=f"Added {player.mention} to the database!",
            color=discord.Color.green(),
        )
        await interaction.response.send_message(embed=added_player, ephemeral=True)


@client.tree.command()
@app_commands.describe(
    player="Select Member",
)
@app_commands.default_permissions(administrator=True)
async def deleteplayer(
    interaction: discord.Interaction,
    player: discord.Member = None,
):
    # moderator_role_id = 962745818023092326
    # moderator_role = discord.utils.get(interaction.guild.roles, id=moderator_role_id)

    # if interaction.user == player or (
    #     moderator_role and moderator_role in interaction.user.roles
    # ):
    #     no_permission = discord.Embed(
    #         title=":no_entry_sign: NOT ALLOWED!",
    #         description="You're not allowed to do that!",
    #         color=discord.Color.red(),
    #     )
    #     await interaction.response.send_message(embed=no_permission, ephemeral=True)
    #     return

    if player == None:
        no_player = discord.Embed(
            title=":stop_sign: ERROR",
            description="You need to select a player!",
            color=discord.Color.red(),
        )
        await interaction.response.send_message(embed=no_player, ephemeral=True)
        return
    else:
        # send the player to the api
        api.delete_player(player.id)
        deleted_player = discord.Embed(
            title=":white_check_mark: DELETED",
            description=f"Deleted {player.mention} from the database!",
            color=discord.Color.green(),
        )
        await interaction.response.send_message(embed=deleted_player, ephemeral=True)


@client.tree.command()
@app_commands.describe(
    score1="Enter the id of the first result",
    score2="Enter the id of the second result",
)
@app_commands.default_permissions(administrator=True)
async def deletegame(
    interaction: discord.Interaction,
    score1: int = None,
    score2: int = None,
):
    """Delete a game from the database"""
    if score1 == None or score2 == None:
        no_game = discord.Embed(
            title=":stop_sign: ERROR",
            description="You need to select a game!",
            color=discord.Color.red(),
        )
        await interaction.response.send_message(embed=no_game, ephemeral=True)
        return
    else:
        # send the player to the api
        api.del_game(score1)
        api.del_game(score2)
        deleted_game = discord.Embed(
            title=":white_check_mark: DELETED",
            description=f"Deleted {score1} and {score2} from the database!",
            color=discord.Color.green(),
        )
        await interaction.response.send_message(embed=deleted_game, ephemeral=True)


client.run(token)
