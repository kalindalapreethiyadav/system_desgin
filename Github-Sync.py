import os
import shutil
import subprocess

# ================= CONFIG =================
GITLAB_REPO = "https://gitlab.com/kalindalapreethiyadav/system_desgin.git"
GITHUB_REPO = "git@github.com:kalindalapreethiyadav/system_desgin.git"

LOCAL_DIR = "./repo-sync"
BRANCH = "main"

# Ensure SSH key is used
os.environ["GIT_SSH_COMMAND"] = "ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no"


# =============== UTIL FUNCTION ===============
def run_command(cmd, cwd=None):
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, text=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {' '.join(cmd)}")


# =============== CLEAN OLD REPO ===============
if os.path.exists(LOCAL_DIR):
    print("Removing old repo directory...")
    shutil.rmtree(LOCAL_DIR)


# =============== CLONE GITLAB ===============
print("Cloning GitLab repo...")
run_command(["git", "clone", GITLAB_REPO, LOCAL_DIR])


# =============== CHANGE DIR ===============
os.chdir(LOCAL_DIR)


# =============== SET REMOTE ===============
print("Setting up GitHub remote...")

# Remove existing remote if exists
subprocess.run(["git", "remote", "remove", "github"], stderr=subprocess.DEVNULL)

# Add GitHub remote
run_command(["git", "remote", "add", "github", GITHUB_REPO])


# =============== FETCH + CHECKOUT ===============
print("Checking out branch...")
run_command(["git", "checkout", BRANCH])


# =============== PULL LATEST (SAFE) ===============
print("Pulling latest changes from GitLab...")
run_command(["git", "pull", "origin", BRANCH])


# =============== PUSH TO GITHUB ===============
print("Pushing to GitHub...")
run_command(["git", "push", "github", BRANCH])


print("✅ Sync completed successfully!")