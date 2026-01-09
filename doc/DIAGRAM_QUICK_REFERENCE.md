# UML Diagrams Quick Reference

This document provides a quick overview of all UML diagrams available for the DBM Ranking Discord Bot.

## 📊 Available Diagrams

### 1️⃣ Use Case Diagram
**File:** `use_case_diagram.puml`

**Purpose:** Shows what different users can do with the system

**Key Elements:**
- 👤 **Actors:** Player, Administrator, Moderator, Ranking API
- 🎯 **Use Cases:** Report results, manage players, view stats
- 🔗 **Relationships:** Include, extend, and associations

**When to use:** Understanding system functionality from user perspective

---

### 2️⃣ Activity Diagram
**File:** `activity_diagram.puml`

**Purpose:** Shows the step-by-step workflow for reporting match results

**Key Elements:**
- ▶️ **Start/End points:** User action to completion
- ◇ **Decision points:** Validation checks (score format, character validity)
- 📦 **Activities:** Validation, API calls, notifications
- 🔀 **Branches:** Accept/Decline/Timeout scenarios

**When to use:** Understanding business logic flow and validation sequence

---

### 3️⃣ Sequence Diagram
**File:** `sequence_diagram.puml`

**Purpose:** Shows detailed message exchanges between components over time

**Key Elements:**
- 🎭 **Actors:** Player, Opponent
- 📦 **Components:** Discord, Bot, Handlers, API
- ➡️ **Messages:** Function calls, API requests, responses
- ⏱️ **Lifelines:** Component activation and deactivation
- 🔄 **Scenarios:** Submit, Accept, Decline, Get Stats

**When to use:** Debugging interactions or understanding timing and message flow

---

### 4️⃣ Component Diagram
**File:** `component_diagram.puml`

**Purpose:** Shows high-level system architecture and component relationships

**Key Elements:**
- 🧩 **Components:** MyClient, Handlers, View, API Handlers
- 🔌 **Ports:** Command endpoints, buttons
- 📚 **Dependencies:** discord.py, requests libraries
- ☁️ **External Systems:** Discord Platform, Ranking API, Database
- 🔗 **Connections:** Component dependencies and data flow

**When to use:** Understanding system architecture and deployment

---

### 5️⃣ Class Diagram
**File:** `class_diagram.puml`

**Purpose:** Shows detailed class structure, attributes, methods, and relationships

**Key Elements:**
- 📦 **Packages:** Discord Bot Client, UI Components, Command Handlers, etc.
- 🏛️ **Classes:** MyClient, AcceptDeclineView, APIHandlers
- 🔧 **Methods:** Functions and their signatures
- 📊 **Attributes:** Data members
- 🔗 **Relationships:** Inheritance, associations, dependencies

**When to use:** Understanding code structure and implementation details

---

## 🔍 Which Diagram Should I Use?

| Question | Diagram |
|----------|---------|
| What can users do? | Use Case |
| How does a feature work step-by-step? | Activity |
| What messages are exchanged between components? | Sequence |
| What are the main system components? | Component |
| How is the code structured? | Class |
| How do components depend on each other? | Component |
| What's the validation flow? | Activity |
| Who can perform which actions? | Use Case |
| What APIs are called and when? | Sequence |

---

## 🚀 Quick View Commands

### Online (No Installation)
```bash
# Visit PlantUML web server
# Copy paste .puml file content
http://www.plantuml.com/plantuml/uml/
```

### VS Code
```bash
# Install extension
code --install-extension jebbs.plantuml

# Preview: Alt+D (Windows/Linux) or Option+D (Mac)
```

### Command Line
```bash
# Generate all diagrams as PNG
plantuml doc/*.puml

# Generate as SVG (scalable)
plantuml -tsvg doc/*.puml

# Generate specific diagram
plantuml doc/use_case_diagram.puml
```

---

## 📝 Diagram Symbols Cheat Sheet

### Use Case Diagram
- `()` = Use case (oval)
- `actor` = Actor (stick figure)
- `-->` = Association
- `..>` = Include/Extend relationship
- `<<include>>`, `<<extend>>` = Stereotypes

### Activity Diagram
- `start`, `stop` = Start/end points (filled circles)
- `:Activity;` = Activity box
- `if (condition) then (yes)` = Decision diamond
- `|Swimlane|` = Actor swimlane

### Sequence Diagram
- `->` = Synchronous message (solid line)
- `-->` = Return message (dashed line)
- `activate/deactivate` = Lifeline activation
- `alt/else/end` = Alternative paths
- `note` = Annotations

### Component Diagram
- `component []` = Component
- `port` = Interface point
- `package {}` = Group of components
- `->` = Dependency
- `..>` = Usage relationship

### Class Diagram
- `class` = Class definition
- `+` = Public
- `-` = Private
- `--|>` = Inheritance (extends)
- `..>` = Dependency
- `-->` = Association

---

## 🎓 Learning Path

**Beginner:** Start here ⬇️
1. Use Case Diagram - Understand what the system does
2. Component Diagram - See the big picture
3. Activity Diagram - Follow a workflow

**Intermediate:**
4. Sequence Diagram - See detailed interactions
5. Class Diagram - Understand implementation

---

## 🔧 Common Issues

### Diagram not rendering?
- Check for syntax errors
- Ensure PlantUML is properly installed
- Try online server first for validation

### Missing connections?
- All relationships are explicitly defined
- Check the legend/notes for clarification

### Too complex?
- Each diagram focuses on a specific aspect
- Read the README.md for narrative explanations

---

## 📚 Further Reading

- **PlantUML Docs:** https://plantuml.com/
- **UML Basics:** https://www.uml-diagrams.org/
- **Discord.py:** https://discordpy.readthedocs.io/
- **Project README:** `../README.md`
- **Detailed Docs:** `README.md` (this folder)

---

## 🆘 Need Help?

1. Read the main `README.md` in this folder
2. Check the notes embedded in each diagram
3. Refer to the source code in `../`
4. Review the project's main README

---

**Last Updated:** 2024
**Maintained by:** DBM Ranking Bot Development Team