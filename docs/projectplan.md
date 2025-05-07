# 📘 PROJECT PLAN: Universal Project Notes Tool (MCP CLI Version)

## 📌 Project Overview

**Goal:**
Create a universal `mcp-note` CLI tool that allows users to add, list, and remove project-scoped notes directly inside each project's repository without needing a constantly running MCP server.

Notes will be stored per project in a `notes/` folder inside the repository, ensuring that:

* Notes are portable with the project (in version control)
* No background server is required → CLI works on-demand
* Users and AI tools can easily add/view/remove notes while working on the project

---

## 🎯 Use Case Example

While working in any project (ex: `mindmenu` project):

```bash
cd ~/projects/mindmenu
mcp-note add "Fix footer later on."
```

→ Creates (if not exists):

```
mindmenu/notes/notes.txt
```

→ Adds entry:

```
[2025-05-07 14:50] Fix footer later on.
```

---

Later:

```bash
mcp-note list
```

→ Outputs all notes from `mindmenu/notes/notes.txt`

---

## 🧱 Components

### ✅ Global CLI Tool (`mcp-note`)

**Responsibilities:**

* Detect the current working directory as the project root
* Ensure `notes/notes.txt` exists (auto-create if needed)
* Append new notes to `notes.txt`
* Read and display notes on request
* Remove notes by line number (optional feature)

**Example commands:**

```bash
mcp-note add "Fix CSS hover effect."
mcp-note list
mcp-note remove 2
```

---

## 📦 Notes Storage Format (per-project)

Example `notes.txt` entry:

```
[1] (2025-05-07 14:50) Fix footer later on.
[2] (2025-05-07 15:02) Improve mobile menu spacing.
```

**File location:**

```
/my-project/
├── index.html
├── styles.css
├── notes/
│   └── notes.txt
```

✅ Keeps notes with the project
✅ Easy to commit to git if desired
✅ Portable and decentralized

---

## 🧠 Benefits

| Benefit               | Description                                          |
| --------------------- | ---------------------------------------------------- |
| Project-scoped notes  | Notes live inside each project's directory           |
| No background server  | CLI works on-demand from any terminal                |
| Globally callable     | Use `mcp-note` command from anywhere                 |
| Portable              | Notes follow the project when copied or moved        |
| AI/Autocoder Friendly | AI can call CLI command or read `notes.txt` directly |

---

## 🚀 Bonus (Optional Extensions)

| Feature              | Description                                           |
| -------------------- | ----------------------------------------------------- |
| Delete notes         | `/note remove <id>`                                   |
| Add tags             | `/note add [bug] Fix button alignment`                |
| AI summary           | `mcp-note summarize` → auto-generate summary of notes |
| Git hook integration | Auto-summarize notes on git commit (future)           |

---

## 🛠️ Technical Architecture

```
[ User Terminal (anywhere) ]
        ↓
[ mcp-note CLI (global) ]
        ↓
[ Project Directory ]
        ↓
[ notes/notes.txt ]
```

✅ No server needed
✅ Local + portable
✅ AI/Autocoder-ready CLI interface

---

## 📅 Milestones

| Milestone                                   | Description           | Target |
| ------------------------------------------- | --------------------- | ------ |
| ✅ CLI with `add` and `list`                 | Core functionality    | Day 1  |
| ✅ Auto-create `notes/` directory if missing | Usability             | Day 1  |
| ✅ Store notes in timestamped format         | Persistent storage    | Day 1  |
| 🚧 CLI remove note by ID                    | (Optional but useful) | Day 2  |
| 🚧 Bonus AI / summary commands              | Future ideas          | Day 3+ |

---

## ✅ Summary

This version of the Universal Notes Tool will be:

✅ **Decentralized → No server needed**
✅ **Project-scoped → Notes live in each project repo**
✅ **Globally callable → Simple CLI command from anywhere**
✅ **Developer-first → For fast, interrupt-free note taking while working**
✅ **AI-friendly → Easily integrated into automation, autocoder flows, or manual use**

Perfect for:

* Developers
* Teams
* AI agents
* Version control environments
