# DBM Ranking Discord Bot

This is a discord bot that allows you to track results manage player and create own rankings.

## 📚 Documentation

**Comprehensive UML diagrams and architecture documentation are available in the [`doc/`](doc/) folder!**

- 🎨 **Use Case Diagram** - User interactions and system capabilities
- 📊 **Activity Diagram** - Match result reporting workflow
- 🔄 **Sequence Diagram** - Detailed message flows and interactions
- 🏗️ **Component Diagram** - System architecture and dependencies
- 📦 **Class Diagram** - Code structure and relationships

**Quick Links:**
- [Documentation Index](doc/INDEX.md) - Start here for navigation
- [Architecture Overview](doc/ARCHITECTURE_OVERVIEW.txt) - ASCII art system overview
- [Quick Reference](doc/DIAGRAM_QUICK_REFERENCE.md) - Diagram cheat sheet

## ! IMPORTANT !
**set up the api found here first: [dbm ranking api](https://github.com/kyoko-git/dbm-ranking-api)**

## Dependencies:
- python 3.8+
- pip


## Setup:
1. craete a discord bot and invite it to your server [discord docs](https://discord.com/developers/docs/intro)
2. create a role for the bot and give it the permission to ping users and send embeds (or if u want to keep it simple giv the role all permissions discord offers for roles)
3. follow the how to use section below
4. add your players to the database with the `/add_player` command
5. use a Database Managment tool to add fighters to the database table `fighters` and edit the mappings.py file to match your fighters table


### how to use
- clone the repo
- chnage the token in the `settings.py` to your discord bot token
- change Guild id to your guild id in `main.py`
- change Bot id to your bot_role id in `main.py`
- change moderator role id to your moderator role id in `AcceptDeclineView.py`
- execute the following commands in the cloned repo
- ``` bash
  python -m venv venv
  pip install -r requirements.txt
  source ./venv/activate #choose the correct one for your shell
  python main.py
  ```
