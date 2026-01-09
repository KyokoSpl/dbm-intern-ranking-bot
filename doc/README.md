# DBM Ranking Bot - Documentation

This folder contains UML diagrams documenting the architecture and behavior of the DBM Ranking Discord Bot.

## Diagrams Overview

### 1. Use Case Diagram (`use_case_diagram.puml`)
Shows the interactions between different actors (Player, Administrator, Moderator) and the system's functionality.

**Key Actors:**
- **Player**: Regular users who can report match results, view stats, and accept/decline results
- **Administrator**: Users with admin permissions who can manage players and games
- **Moderator**: Users who can accept/decline match results on behalf of players
- **Ranking API**: External backend system that stores all game data

**Main Use Cases:**
- Report Match Result
- Accept/Decline Match Result
- View Player Stats
- Add/Delete Players (Admin only)
- Delete Game Records (Admin only)
- Get Player List (Admin only)

### 2. Activity Diagram (`activity_diagram.puml`)
Illustrates the complete flow of reporting a match result, from initial command to final API call.

**Main Flow:**
1. Player initiates `/result` command
2. System validates all inputs (score format, character selection, opponent)
3. System creates interactive Accept/Decline prompt
4. Opponent or Moderator accepts or declines
5. On acceptance: Game data is sent to the Ranking API
6. On decline: Moderators are notified

**Key Decision Points:**
- Score format validation
- Self-match prevention
- Bot-match prevention
- Character validation
- Authorization checks for Accept/Decline actions

### 3. Sequence Diagram (`sequence_diagram.puml`)
Shows the detailed message flow and interactions between components over time.

**Main Scenarios:**
1. **Match Result Submission**: Complete flow from command input through validation
2. **Accept Scenario**: What happens when opponent accepts the result
3. **Decline Scenario**: What happens when opponent declines the result
4. **Get Stats Scenario**: How player statistics are retrieved and displayed

**Key Interactions:**
- Player → Discord → Bot → Command Handler
- Validation checks with character mappings
- AcceptDeclineView button handling
- API communication for game data persistence
- Notification flows for all parties involved

### 4. Component Diagram (`component_diagram.puml`)
Shows the high-level system architecture, component dependencies, and deployment view.

**Main Components:**

- **MyClient**: Core Discord bot client
  - Manages event handling and command tree
  
- **Command Handlers**: Slash command implementations
  - Handles all user interactions
  
- **AcceptDeclineView**: Interactive UI component
  - Manages Accept/Decline buttons and workflows
  
- **API Handlers**: REST client for backend communication
  - Encapsulates all HTTP operations
  
- **Validation Logic**: Input validation
  - Character, score, and permission validators
  
- **Configuration**: Settings and mappings
  - Bot configuration and character-to-ID mapping

**External Dependencies:**
- Discord.py library (Discord API wrapper)
- Requests library (HTTP client)
- Discord Platform (Gateway and API)
- Ranking API backend (REST service)
- PostgreSQL database (via API)

**Data Flow:**
User → Discord → Bot Client → Command Handler → API Handler → Ranking API → Database

### 5. Class Diagram (`class_diagram.puml`)
Displays the system's architecture, showing all major components and their relationships.

**Main Components:**

- **MyClient**: Discord bot client that extends `discord.Client`
  - Manages command tree and bot lifecycle

- **AcceptDeclineView**: Interactive UI component
  - Handles Accept/Decline buttons
  - Validates user permissions
  - Triggers API calls on acceptance

- **CommandHandlers**: Module containing all slash command implementations
  - `/result`: Report match results
  - `/addplayer`: Add player to database
  - `/deleteplayer`: Remove player
  - `/deletegame`: Remove game record
  - `/getplayerlist`: List all players
  - `/getstats`: Get player statistics

- **APIHandlers**: Module for external API communication
  - HTTP REST client for Ranking API
  - Handles all CRUD operations

- **Mappings**: Configuration for character-to-ID mapping
  - Maps Super Smash Bros. character names to database IDs

- **Settings**: Bot configuration
  - Discord token, role IDs, guild ID

## Diagram Files

- `use_case_diagram.puml` - User interactions and system capabilities
- `activity_diagram.puml` - Match result reporting workflow
- `sequence_diagram.puml` - Detailed message flows and interactions
- `component_diagram.puml` - High-level architecture and dependencies
- `class_diagram.puml` - Detailed class structure and relationships

## How to View the Diagrams

### Option 1: PlantUML Online Server
1. Visit http://www.plantuml.com/plantuml/uml/
2. Copy the content of any `.puml` file
3. Paste into the text area
4. View the rendered diagram

### Option 2: VS Code with PlantUML Extension
1. Install the "PlantUML" extension in VS Code
2. Open any `.puml` file
3. Press `Alt+D` to preview the diagram

### Option 3: Command Line (requires PlantUML installed)
```bash
# Install PlantUML (requires Java)
# On Ubuntu/Debian:
sudo apt-get install plantuml

# Generate PNG images
plantuml doc/*.puml

# Or generate SVG
plantuml -tsvg doc/*.puml
```

### Option 4: IntelliJ IDEA / PyCharm
1. Install the "PlantUML Integration" plugin
2. Open any `.puml` file
3. The diagram will render automatically in the editor

## System Architecture Summary

The bot follows a layered architecture:

1. **Presentation Layer**: Discord UI (commands, embeds, interactive buttons)
2. **Application Layer**: Command handlers and business logic
3. **Integration Layer**: API handlers for external communication
4. **Configuration Layer**: Settings and mappings

**Key Design Patterns:**
- **Command Pattern**: Slash commands are registered and handled independently
- **View Pattern**: AcceptDeclineView encapsulates interactive UI logic
- **Separation of Concerns**: Clear separation between Discord logic and API communication
- **Configuration Management**: Centralized settings and mappings

## Important Notes

- The bot requires a separate Ranking API backend (see main README.md)
- All game data is stored externally via REST API
- Authorization is role-based (Player, Moderator, Administrator)
- Match results require opponent confirmation to prevent false reporting
- Character mappings must match the database fighter IDs

## Updating the Diagrams

When making changes to the codebase:

1. Update the relevant `.puml` file(s)
2. Regenerate the diagram to verify correctness
3. Keep the diagrams in sync with the actual implementation

## References

- PlantUML Documentation: https://plantuml.com/
- Discord.py Documentation: https://discordpy.readthedocs.io/
- Project Repository: https://github.com/kyoko-git/dbm-ranking-api