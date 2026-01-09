# Documentation Index

Welcome to the DBM Ranking Discord Bot documentation!

## 📑 Documentation Files

### Overview Documents
1. **[README.md](README.md)** - Main documentation guide
   - Comprehensive overview of all diagrams
   - How to view and use the diagrams
   - System architecture summary
   - Installation instructions for diagram viewers

2. **[ARCHITECTURE_OVERVIEW.txt](ARCHITECTURE_OVERVIEW.txt)** - ASCII architecture visualization
   - Text-based system architecture diagram
   - Can be viewed directly in terminal
   - Shows component relationships and data flow
   - Deployment architecture
   - Technology stack overview

3. **[DIAGRAM_QUICK_REFERENCE.md](DIAGRAM_QUICK_REFERENCE.md)** - Quick reference guide
   - Cheat sheet for all diagrams
   - Which diagram to use when
   - UML symbol reference
   - Quick view commands
   - Troubleshooting tips

### UML Diagrams (PlantUML Format)

4. **[use_case_diagram.puml](use_case_diagram.puml)** - Use Case Diagram
   - **What it shows:** User interactions and system capabilities
   - **Best for:** Understanding what users can do
   - **Actors:** Player, Administrator, Moderator, Ranking API
   - **Key use cases:** Report results, manage players, view statistics

5. **[activity_diagram.puml](activity_diagram.puml)** - Activity Diagram
   - **What it shows:** Step-by-step workflow for match result reporting
   - **Best for:** Understanding business process flow
   - **Contains:** Validation logic, decision points, error handling
   - **Focus:** Complete flow from command input to API storage

6. **[sequence_diagram.puml](sequence_diagram.puml)** - Sequence Diagram
   - **What it shows:** Detailed message exchanges over time
   - **Best for:** Debugging and understanding component interactions
   - **Scenarios:** Submit result, Accept, Decline, Get stats
   - **Contains:** Lifelines, activation boxes, message flows

7. **[component_diagram.puml](component_diagram.puml)** - Component Diagram
   - **What it shows:** High-level system architecture
   - **Best for:** Understanding system structure and dependencies
   - **Components:** Bot client, handlers, API layer, configuration
   - **Shows:** External dependencies, data flow, deployment view

8. **[class_diagram.puml](class_diagram.puml)** - Class Diagram
   - **What it shows:** Detailed code structure
   - **Best for:** Understanding implementation details
   - **Contains:** Classes, methods, attributes, relationships
   - **Shows:** Inheritance, composition, dependencies

## 🚀 Quick Start

### First Time Here?
1. Start with [ARCHITECTURE_OVERVIEW.txt](ARCHITECTURE_OVERVIEW.txt) for a high-level view
2. Read [README.md](README.md) for detailed explanations
3. View the diagrams in this order:
   - Use Case Diagram (what the system does)
   - Component Diagram (system architecture)
   - Activity Diagram (how workflows work)
   - Sequence Diagram (detailed interactions)
   - Class Diagram (code structure)

### Need Something Specific?
- **Understanding user roles?** → Use Case Diagram
- **How does match reporting work?** → Activity Diagram
- **What components exist?** → Component Diagram
- **Message flow details?** → Sequence Diagram
- **Code structure?** → Class Diagram
- **Quick reference?** → [DIAGRAM_QUICK_REFERENCE.md](DIAGRAM_QUICK_REFERENCE.md)

## 🛠️ Viewing the Diagrams

### Option 1: Online (Easiest)
```
1. Visit http://www.plantuml.com/plantuml/uml/
2. Open any .puml file
3. Copy and paste the content
4. View the rendered diagram
```

### Option 2: VS Code
```bash
# Install PlantUML extension
code --install-extension jebbs.plantuml

# Open .puml file and press Alt+D (Windows/Linux)
```

### Option 3: Command Line
```bash
# Generate all diagrams as PNG
plantuml doc/*.puml

# Generate as SVG (recommended for scaling)
plantuml -tsvg doc/*.puml
```

### Option 4: IntelliJ/PyCharm
```
1. Install "PlantUML Integration" plugin
2. Open any .puml file
3. Diagram renders automatically
```

## 📊 Diagram Summary Table

| Diagram | File | Purpose | Complexity |
|---------|------|---------|------------|
| Use Case | `use_case_diagram.puml` | User interactions | ⭐ Easy |
| Activity | `activity_diagram.puml` | Business workflow | ⭐⭐ Medium |
| Sequence | `sequence_diagram.puml` | Message flow | ⭐⭐⭐ Advanced |
| Component | `component_diagram.puml` | System architecture | ⭐⭐ Medium |
| Class | `class_diagram.puml` | Code structure | ⭐⭐⭐ Advanced |

## 🎯 Use Case Scenarios

### Scenario: New Developer Onboarding
1. Read [ARCHITECTURE_OVERVIEW.txt](ARCHITECTURE_OVERVIEW.txt)
2. Review [Component Diagram](component_diagram.puml)
3. Study [Class Diagram](class_diagram.puml)
4. Read main [README.md](README.md) in project root

### Scenario: Understanding User Features
1. Review [Use Case Diagram](use_case_diagram.puml)
2. Read [README.md](README.md) documentation
3. Check [Activity Diagram](activity_diagram.puml) for workflows

### Scenario: Debugging an Issue
1. Check [Sequence Diagram](sequence_diagram.puml) for message flow
2. Review [Activity Diagram](activity_diagram.puml) for logic flow
3. Refer to [Class Diagram](class_diagram.puml) for implementation

### Scenario: System Architecture Review
1. Start with [Component Diagram](component_diagram.puml)
2. Review [ARCHITECTURE_OVERVIEW.txt](ARCHITECTURE_OVERVIEW.txt)
3. Read architecture section in [README.md](README.md)

## 📚 Related Documentation

- **Project README:** `../README.md` - Setup and installation
- **API Documentation:** See [dbm-ranking-api](https://github.com/kyoko-git/dbm-ranking-api)
- **Discord.py Docs:** https://discordpy.readthedocs.io/
- **PlantUML Reference:** https://plantuml.com/

## 🔄 Keeping Documentation Updated

When making code changes, update the relevant diagrams:

- **New command added?** → Update Use Case, Activity, Sequence, Class diagrams
- **Architecture change?** → Update Component and Class diagrams
- **Workflow change?** → Update Activity and Sequence diagrams
- **New component?** → Update all relevant diagrams

## 💡 Tips

- **ASCII diagram** ([ARCHITECTURE_OVERVIEW.txt](ARCHITECTURE_OVERVIEW.txt)) is great for quick terminal viewing
- **PlantUML diagrams** are source-controlled and easy to maintain
- **Quick Reference** ([DIAGRAM_QUICK_REFERENCE.md](DIAGRAM_QUICK_REFERENCE.md)) has symbol explanations
- **README** has the most detailed narrative explanations

## 🆘 Need Help?

1. Check [DIAGRAM_QUICK_REFERENCE.md](DIAGRAM_QUICK_REFERENCE.md) for common issues
2. Read the detailed [README.md](README.md)
3. Review [ARCHITECTURE_OVERVIEW.txt](ARCHITECTURE_OVERVIEW.txt) for system understanding
4. Refer to the main project README in parent directory

---

**Documentation Version:** 1.0  
**Last Updated:** 2024  
**Maintained by:** DBM Ranking Bot Development Team