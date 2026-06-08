import os
import subprocess

# CONFIG
GITLAB_REPO = "https://gitlab.com/kpreethiyadav579/system_desgin.git"
GITHUB_REPO = "https://kalindalapreethiyadav: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@github.com/kalindalapreethiyadav/system_desgin.git"

LOCAL_DIR = "./repo-sync"
BRANCH = "main"


def run(cmd, cwd=None):
    """Execute shell command."""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            shell=True,
            text=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)


def clone_if_needed():
    if not os.path.exists(LOCAL_DIR):
        print("Cloning GitLab repo...")
        run(f"git clone {GITLAB_REPO} {LOCAL_DIR}")
    else:
        print("Repo already exists")

def setup_github_remote():
    print("Setting up GitHub remote...")

    # Check if remote already exists
    remotes = subprocess.run(
        "git remote",
        cwd=LOCAL_DIR,
        shell=True,
        text=True,
        stdout=subprocess.PIPE
    ).stdout

    if "github" not in remotes:
        run(f"git remote add github {GITHUB_REPO}", cwd=LOCAL_DIR)
    else:
        print("GitHub remote already configured")


def pull_from_gitlab():
    print("Pulling latest from GitLab...")
    run(f"git pull origin {BRANCH}", cwd=LOCAL_DIR)


def push_to_github():
    print("Pushing to GitHub...")
    run(f"git push github {BRANCH}", cwd=LOCAL_DIR)


def main():
    clone_if_needed()
    setup_github_remote()
    pull_from_gitlab()
    push_to_github()


if __name__ == "__main__":
    main()
