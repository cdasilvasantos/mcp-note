#!/usr/bin/env python3
import os
import sys
import argparse
from datetime import datetime
import re

# Constants
NOTES_DIR = "notes"
NOTES_FILE = "notes.txt"

def find_project_root():
    """
    Find the current project root directory.
    
    Returns:
        The absolute path to the current project root directory.
    """
    # Simply return the current working directory
    # In a more advanced implementation, this could look for specific markers
    # like .git, package.json, etc. to find the actual project root
    return os.getcwd()


def ensure_notes_directory(project_root):
    """
    Ensure the notes directory exists in the project.
    
    Args:
        project_root: The root directory of the project.
        
    Returns:
        The path to the notes directory.
    """
    notes_dir = os.path.join(project_root, NOTES_DIR)
    
    # Create the notes directory if it doesn't exist
    if not os.path.exists(notes_dir):
        os.makedirs(notes_dir)
        print(f"Created notes directory: {notes_dir}")
    
    return notes_dir


def ensure_notes_file(notes_dir):
    """
    Ensure the notes file exists in the notes directory.
    
    Args:
        notes_dir: The path to the notes directory.
        
    Returns:
        The path to the notes file.
    """
    notes_file = os.path.join(notes_dir, NOTES_FILE)
    
    # Create the notes file if it doesn't exist
    if not os.path.exists(notes_file):
        with open(notes_file, 'w') as f:
            pass  # Create an empty file
        print(f"Created notes file: {notes_file}")
    
    return notes_file


def add_note(note_text):
    """
    Add a new note to the project's notes file.
    
    Args:
        note_text: The text of the note to add.
        
    Returns:
        True if successful, False otherwise.
    """
    try:
        project_root = find_project_root()
        notes_dir = ensure_notes_directory(project_root)
        notes_file = ensure_notes_file(notes_dir)
        
        # Get the current timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # Read existing notes to determine the next ID
        with open(notes_file, 'r') as f:
            lines = f.readlines()
        
        # Find the highest ID
        highest_id = 0
        for line in lines:
            id_match = re.match(r'\[([0-9]+)\]', line)
            if id_match:
                note_id = int(id_match.group(1))
                highest_id = max(highest_id, note_id)
        
        # Next ID is one more than the highest
        next_id = highest_id + 1
        
        # Format the new note
        new_note = f"[{next_id}] ({timestamp}) {note_text}\n"
        
        # Append the note to the file
        with open(notes_file, 'a') as f:
            f.write(new_note)
        
        print(f"Added note #{next_id}: {note_text}")
        return True
    except Exception as e:
        print(f"Error adding note: {str(e)}")
        return False


def list_notes():
    """
    List all notes in the project's notes file.
    
    Returns:
        True if successful, False otherwise.
    """
    try:
        project_root = find_project_root()
        notes_dir = ensure_notes_directory(project_root)
        notes_file = ensure_notes_file(notes_dir)
        
        # Read and display notes
        with open(notes_file, 'r') as f:
            notes = f.readlines()
        
        if not notes:
            print("No notes found.")
        else:
            print(f"Notes for project at {project_root}:")
            print("-" * 50)
            for note in notes:
                print(note.strip())
            print("-" * 50)
            print(f"Total notes: {len(notes)}")
        
        return True
    except Exception as e:
        print(f"Error listing notes: {str(e)}")
        return False


def remove_note(note_id):
    """
    Remove a note by its ID.
    
    Args:
        note_id: The ID of the note to remove.
        
    Returns:
        True if successful, False otherwise.
    """
    try:
        project_root = find_project_root()
        notes_dir = ensure_notes_directory(project_root)
        notes_file = ensure_notes_file(notes_dir)
        
        # Read existing notes
        with open(notes_file, 'r') as f:
            notes = f.readlines()
        
        # Find the note with the specified ID
        removed = False
        new_notes = []
        for note in notes:
            id_match = re.match(r'\[([0-9]+)\]', note)
            if id_match and int(id_match.group(1)) == int(note_id):
                removed = True
                print(f"Removed note: {note.strip()}")
            else:
                new_notes.append(note)
        
        if not removed:
            print(f"Note with ID {note_id} not found.")
            return False
        
        # Write back the remaining notes
        with open(notes_file, 'w') as f:
            f.writelines(new_notes)
        
        return True
    except Exception as e:
        print(f"Error removing note: {str(e)}")
        return False


def main():
    """
    Main entry point for the CLI tool.
    """
    parser = argparse.ArgumentParser(description="Universal Project Notes Tool")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Add note command
    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("text", help="Note text")
    
    # List notes command
    subparsers.add_parser("list", help="List all notes")
    
    # Remove note command
    remove_parser = subparsers.add_parser("remove", help="Remove a note by ID")
    remove_parser.add_argument("id", type=int, help="Note ID to remove")
    
    args = parser.parse_args()
    
    if args.command == "add":
        add_note(args.text)
    elif args.command == "list":
        list_notes()
    elif args.command == "remove":
        remove_note(args.id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
