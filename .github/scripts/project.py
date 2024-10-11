from github import Github
import os

# Variables to configure
repo_name = os.getenv("REPO")
board_name = os.getenv("BOARD_NAME")
phase_columns = os.getenv("PHASE_COLUMNS").split(", ")

def create_board():
    g = Github(os.getenv("GH_TOKEN"))
    repo = g.get_repo(repo_name)
    
    # Create the project board
    project = repo.create_project(name=board_name, body="Auto-generated project board for phases.")
    for column_name in phase_columns:
        project.create_column(column_name)
    
    print(f"Project board '{board_name}' created with columns: {', '.join(phase_columns)}")

if __name__ == "__main__":
    create_board()
