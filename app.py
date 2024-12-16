import typer
from rich.console import Console
from rich.prompt import Prompt
import subprocess

app = typer.Typer()
console = Console()

def execute_git_command(command: str):
    """Execute a git command and print the output."""
    try:
        result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
        console.print(result.stdout)
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Error:[/red] {e.stderr}")

@app.command()
def menu():
    """Interactive Git shell menu."""
    while True:
        console.print("\n[bold cyan]Git Shell Menu[/bold cyan]")
        console.print("1. Status")
        console.print("2. Add")
        console.print("3. Commit")
        console.print("4. Push")
        console.print("5. Pull")
        console.print("6. Exec (Advanced Command)")
        console.print("7. Exit")

        choice = Prompt.ask("Select an option", choices=["1", "2", "3", "4", "5", "6", "7"])

        if choice == "1":
            execute_git_command("git status")
        elif choice == "2":
            file_to_add = Prompt.ask("Enter file to add (or '.' for all)")
            execute_git_command(f"git add {file_to_add}")
        elif choice == "3":
            commit_message = Prompt.ask("Enter commit message")
            execute_git_command(f"git commit -m \"{commit_message}\"")
        elif choice == "4":
            execute_git_command("git push")
        elif choice == "5":
            execute_git_command("git pull")
        elif choice == "6":
            advanced_command = Prompt.ask("Enter advanced git command")
            execute_git_command(f"git {advanced_command}")
        elif choice == "7":
            console.print("Exiting Git Shell. Goodbye!")
            break

if __name__ == "__main__":
    app()
