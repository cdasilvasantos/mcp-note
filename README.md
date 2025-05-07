# Universal Project Notes Tool (mcp-note CLI)

## Overview

The Universal Project Notes Tool (`mcp-note`) is a CLI tool that allows developers to add, list, and remove project-scoped notes directly inside each project's repository. Notes are stored in a `notes/` folder inside the project, ensuring that:

* Notes are portable with the project (in version control)
* No background server is required → CLI works on-demand
* Users and AI tools can easily add/view/remove notes while working on the project

## Features

- **Project-scoped notes**: Notes live inside each project's directory
- **No background server**: CLI works on-demand from any terminal
- **Globally callable**: Use `mcp-note` command from anywhere
- **Portable**: Notes follow the project when copied or moved
- **AI/Autocoder Friendly**: AI can call CLI command or read `notes.txt` directly
- **Simple storage format**: Plain text file with timestamps and IDs

## Commands

The `mcp-note` CLI provides the following commands:

### Add a Note
```bash
mcp-note add "Your note text here"
```
Adds a new note to the current project's notes file with a timestamp and ID.

### List Notes
```bash
mcp-note list
```
Displays all notes for the current project.

### Remove a Note
```bash
mcp-note remove <id>
```
Removes the note with the specified ID from the project's notes file.

## Installation

### Prerequisites

- Python 3.8 or higher

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/cd58/mcp-note.git
   cd mcp-note
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the package in development mode:
   ```bash
   pip install -e .
   ```

This will make the `mcp-note` command available globally while in the virtual environment.

## Usage

The `mcp-note` CLI tool is designed to be used within any project directory. It automatically creates a `notes/` directory and `notes.txt` file if they don't exist.

### Example Workflow

1. Navigate to your project:
   ```bash
   cd ~/projects/my-project
   ```

2. Add a note:
   ```bash
   mcp-note add "Fix the footer alignment issue later"
   ```

3. Add another note:
   ```bash
   mcp-note add "Improve mobile menu spacing"
   ```

4. List all notes:
   ```bash
   mcp-note list
   ```
   Output:
   ```
   Notes for project at /home/user/projects/my-project:
   --------------------------------------------------
   [1] (2025-05-07 14:50) Fix the footer alignment issue later
   [2] (2025-05-07 15:02) Improve mobile menu spacing
   --------------------------------------------------
   Total notes: 2
   ```

5. Remove a note:
   ```bash
   mcp-note remove 1
   ```

6. List notes again:
   ```bash
   mcp-note list
   ```
   Output:
   ```
   Notes for project at /home/user/projects/my-project:
   --------------------------------------------------
   [2] (2025-05-07 15:02) Improve mobile menu spacing
   --------------------------------------------------
   Total notes: 1
   ```

## Storage Format

Notes are stored in a simple text file format at:

```
/your-project/
├── ...
├── notes/
│   └── notes.txt
```

Each note is stored with an ID, timestamp, and the note text:

```
[1] (2025-05-07 14:50) Fix the footer alignment issue later
[2] (2025-05-07 15:02) Improve mobile menu spacing
```

## Benefits

- **Project-scoped**: Notes are stored within each project, making them contextually relevant
- **Version control friendly**: Notes can be committed to git along with code changes
- **No external dependencies**: Works without any external services or databases
- **Simple format**: Easy to read and parse by both humans and machines
- **AI-friendly**: Easily integrated into AI workflows and automation

## License

MIT