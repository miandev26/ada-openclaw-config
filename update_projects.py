import os
from datetime import datetime

PROJECTS_FILE = "PROJECTS.md"

def update_status(project_name, status, agent="Dev-Ada"):
    if not os.path.exists(PROJECTS_FILE):
        return "PROJECTS.md not found."
    
    with open(PROJECTS_FILE, 'r') as f:
        lines = f.readlines()
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_lines = []
    updated = False
    
    for line in lines:
        if f"**{project_name}**" in line:
            # Simple table row update (expects the table structure to remain consistent)
            parts = line.split("|")
            if len(parts) >= 5:
                parts[3] = f" {status} "
                parts[4] = f" {now} "
                line = "|".join(parts)
                updated = True
        new_lines.append(line)
    
    if updated:
        with open(PROJECTS_FILE, 'w') as f:
            f.writelines(new_lines)
        return f"Status for '{project_name}' updated to '{status}'."
    else:
        return f"Project '{project_name}' not found in PROJECTS.md."

if __name__ == "__main__":
    # This script can be called by agents to report their progress
    import sys
    if len(sys.argv) > 2:
        print(update_status(sys.argv[1], sys.argv[2]))
