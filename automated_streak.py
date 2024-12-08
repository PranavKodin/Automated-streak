import os
import subprocess
from datetime import datetime

def run_cmd(command):
    """Execute a shell command and print the result or error."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
        print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}")
        print(f"Error: {e.stderr.strip()}")
        print(f"Output: {e.stdout.strip()}")

def make_changes(file_path="auto_update.txt"):
    """Make changes to the specified file."""
    try:
        with open(file_path, "w") as f:
            f.write(f"Updated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print(f"Changes saved to {file_path}.")
    except IOError as e:
        print(f"Failed to write changes: {e}")

def push_to_github(repo_path):
    """Push changes to GitHub."""
    if not os.path.isdir(repo_path):
        print(f"Invalid repository path: {repo_path}")
        return

    os.chdir(repo_path)
    run_cmd("git add .")
    commit_message = f"Automated update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    run_cmd(f'git commit -m "{commit_message}"')
    run_cmd("git push origin main")

def main():
    """Main function to make changes and push to GitHub."""
    repo_path = r"E:/automated streak/Automated-streak"  # Adjust the repository path as needed
    make_changes()
    push_to_github(repo_path)

if __name__ == "__main__":
    while True:
        main()
