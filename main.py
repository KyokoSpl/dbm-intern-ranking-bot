import discord
from discord import app_commands
import settings

from mappings import char_map
from AcceptDeclineView import AcceptDeclineView
import api_handlers as api

MY_GUILD = discord.Object(id=GUILDID)  # replace with your guild id
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
    charp1="Enter your character",
    charp2="Enter the enemies character",
)
async def result(
    interaction: discord.Interaction,
    score: str = "0",
    enemy: discord.Member = None,
    charp1: str = "None",
    charp2: str = "None",
):
    """Enter a result of your set"""

    member = interaction.user  # The user executing the command

    if not await char_validation(charp1, is_enemy=False, interaction=interaction):
        return
    if not await char_validation(charp2, is_enemy=True, interaction=interaction):
        return

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
        interaction.guild.roles,
        id=BOTROLE,  # Bot role ID replace with your bot role id
    )  # Bot role ID
    if bot_role in enemy.roles:
        botreport = discord.Embed(
            title=":stop_sign: ERROR",
            description="Seriously? You wanna play against one of the all mighty?",
            color=discord.Color.red(),
        )
        await interaction.response.send_message(embed=botreport, ephemeral=True)
        return

    view = AcceptDeclineView(member, score, enemy, charp1, charp2)
    prompt_embed = discord.Embed(
        title="Do you accept the result?",
        description=f"**{member.mention}** scored **{score}** against **{enemy.mention}**\n **{member.mention}** played **{charp1}** and **{enemy.mention}** played **{charp2}**",
        color=discord.Color.blue(),
    )
    #
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


@client.tree.command()
@app_commands.describe()
@app_commands.default_permissions(administrator=True)
async def getplayerlist(interaction: discord.Interaction):
    """Get the list of all players"""
    playerlist = api.get_player_list()
    if playerlist is None or len(playerlist) == 0:
        await interaction.response.send_message(f"No players found!", ephemeral=True)
        return
    else:
        player = discord.Embed(
            title=":white_check_mark: PLAYERS",
            description=f"Players in the database:\n {playerlist}",
            color=discord.Color.green(),
        )
        await interaction.response.send_message(embed=player, ephemeral=False)


@client.tree.command()
@app_commands.describe(
    player="Select Member to get his stats",
)
async def getstats(interaction: discord.Interaction, player: discord.Member = None):
    """Get the stats of a player from all time"""
    if player == None:
        player = interaction.user

    stats = api.get_stats(player.id)

    if stats is None or len(stats) == 0:
        await interaction.response.send_message(
            f"No stats found for {player.mention}", ephemeral=True
        )
        return
    wins = stats[0]["wins"]
    loses = stats[0]["loses"]
    winrate = wins / (loses + wins)
    winrate = round(winrate * 100, 2)
    match_count = wins + loses
    match_count = round(match_count, 2)
    stats_embed = discord.Embed(
        title=":white_check_mark: STATS",
        description=f"Stats of **{player.mention}\n **Matches played: **{match_count}**\n Wins: **{wins}**\n Loses: **{loses}**\n Winrate: **{winrate}%**",
        color=discord.Color.green(),
    )
    await interaction.response.send_message(embed=stats_embed, ephemeral=False)


# validate char selection
async def char_validation(
    char: str, is_enemy: bool = False, interaction: discord.Interaction = None
) -> bool:
    if char.lower() not in [char.lower() for char in char_map.keys()]:
        if is_enemy is False:
            message = "Tipfehler in your character!"

        else:
            message = "Tipfehler in enemy character!"

        no_char_report = discord.Embed(
            title=":stop_sign: ERROR",
            description=message,
            color=discord.Color.red(),
        )
        await interaction.response.send_message(embed=no_char_report, ephemeral=True)
        return False

    return True


client.run(token)
