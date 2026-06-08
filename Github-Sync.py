import os
import shutil
import subprocess

# ================= CONFIG =================
GITLAB_REPO = os.environ["GITLAB_REPO"]
GITLAB_TOKEN = os.environ["GITLAB_TOKEN"]

GITHUB_REPO = os.environ["GITHUB_REPO"]

LOCAL_DIR = "./repo-sync"
BRANCH = "main"

# Inject token into GitLab URL
# Convert: https://gitlab.com/user/repo.git
# To:      https://oauth2:TOKEN@gitlab.com/user/repo.git
AUTH_GITLAB_REPO = GITLAB_REPO.replace(
    "https://", f"https://oauth2:{GITLAB_TOKEN}@"
)

# Use SSH key for GitHub
os.environ["GIT_SSH_COMMAND"] = "ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no"


# =============== UTIL FUNCTION ===============
def run_command(cmd, cwd=None):
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd)
    if result.returncode != 0:
        raise Exception(f"Command failed: {' '.join(cmd)}")


# =============== CLEAN OLD REPO ===============
if os.path.exists(LOCAL_DIR):
    print("Removing existing directory...")
    shutil.rmtree(LOCAL_DIR)


# =============== CLONE FROM GITLAB ===============
print("Cloning from GitLab...")
run_command(["git", "clone", AUTH_GITLAB_REPO, LOCAL_DIR])


# =============== ENTER DIRECTORY ===============
os.chdir(LOCAL_DIR)


# =============== CHECKOUT BRANCH ===============
print("Checking out branch...")
subprocess.run(["git", "checkout", BRANCH], stderr=subprocess.DEVNULL) or run_command(
    ["git", "checkout", "-b", BRANCH]
)


# =============== PULL LATEST ===============
print("Pulling latest changes...")
run_command(["git", "pull", "origin", BRANCH])


# =============== ADD GITHUB REMOTE ===============
print("Configuring GitHub remote...")
subprocess.run(["git", "remote", "remove", "github"], stderr=subprocess.DEVNULL)
GITHUB_REPO = "git@github.com:kalindalapreethiyadav/system_desgin.git"

run_command(["git", "remote", "add", "github", GITHUB_REPO])

print("\n🔍 DEBUG: Checking Git remotes...")
run_command(["git", "remote", "-v"])

print("\n🔍 DEBUG: Testing SSH connection...")
run_command(["ssh", "-vT", "git@github.com"])

# =============== DEBUG ===============
run_command(["git", "remote", "-v"])


# =============== PUSH TO GITHUB ===============
print("Pushing to GitHub...")
run_command(["git", "push", "github", BRANCH, "--force"])


print("✅ Sync completed successfully!")
