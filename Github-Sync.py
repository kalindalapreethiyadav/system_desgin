import os
import shutil
import subprocess

# ================= CONFIG =================
CI_JOB_TOKEN = os.environ["CI_JOB_TOKEN"]

GITLAB_REPO = f"https://gitlab-ci-token:{CI_JOB_TOKEN}@gitlab.com/kalindalapreethiyadav/system_desgin.git"
GITHUB_REPO = "git@github.com:kalindalapreethiyadav/system_desgin.git"

LOCAL_DIR = "./repo-sync"
BRANCH = "main"

# Use SSH key
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
subprocess.run(["git", "remote", "remove", "github"], stderr=subprocess.DEVNULL)
run_command(["git", "remote", "add", "github", GITHUB_REPO])

# =============== CHECKOUT BRANCH ===============
print("Checking out branch...")
subprocess.run(["git", "checkout", BRANCH], stderr=subprocess.DEVNULL) or run_command(["git", "checkout", "-b", BRANCH])

# =============== PULL ===============
print("Pulling latest changes...")
run_command(["git", "pull", "origin", BRANCH])

# =============== DEBUG ===============
run_command(["git", "remote", "-v"])

# =============== PUSH ===============
print("Pushing to GitHub...")
run_command(["git", "push", "github", BRANCH, "--force"])

print("✅ Sync completed successfully!")