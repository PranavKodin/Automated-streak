import os
import subprocess
import time
from datetime import datetime

def run_cmd(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        print(f"Command: {command}")
        print(f"Error: {result.stderr.strip()}")
        print(f"Output: {result.stdout.strip()}")
    else:
        print(result.stdout.strip())

def make_changes():
    print("Making changes to the code...")
    with open("auto_update.txt", "w") as f:
        f.write(f"Updated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    print("Changes made.")

def push_to_github():
    repo_path = r'E:/automated streak'  
    try:
        os.chdir(repo_path)
    except Exception as e:
        print(f"Failed to change directory: {e}")
        return

    run_cmd("git add .")
    commit_message = f"Added a new feature to pvt project on {datetime.now()}"
    run_cmd(f'git commit -m "{commit_message}"')
    run_cmd("git push origin main")

def main_loop():
    make_changes()  
    push_to_github()  
        
if __name__ == "__main__":
    main_loop()

