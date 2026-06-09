import os
import shutil
import subprocess

# ================= CONFIG =================
GITLAB_REPO = os.environ["GITLAB_REPO"]
GITLAB_TOKEN = os.environ["GITLAB_TOKEN"]

GITHUB_REPO = "git@github.com:kalindalapreethiyadav/system_desgin.git"

LOCAL_DIR = "./repo-sync"
BRANCH = "main"

# Inject token into GitLab repo
AUTH_GITLAB_REPO = GITLAB_REPO.replace(
    "https://", f"https://oauth2:{GITLAB_TOKEN}@"
)

# Use SSH key
os.environ["GIT_SSH_COMMAND"] = "ssh -i ~/.ssh/id_ed25519 -o StrictHostKeyChecking=no"


# =============== UTIL FUNCTION ===============
def run_command(cmd, cwd=None, ignore_error=False):
    print(f"\nRunning: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)

    print(result.stdout)
    print(result.stderr)

    if result.returncode != 0 and not ignore_error:
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
subprocess.run(["git", "checkout", BRANCH], stderr=subprocess.DEVNULL) or \
run_command(["git", "checkout", "-b", BRANCH])


# =============== PULL LATEST ===============
print("Pulling latest changes...")
run_command(["git", "pull", "origin", BRANCH])


# =============== SET GITHUB REMOTE ===============
print("Configuring GitHub remote...")

# Remove old if exists
subprocess.run(["git", "remote", "remove", "github"], stderr=subprocess.DEVNULL)

# ✅ ADD IT BACK (CRITICAL FIX)
run_command(["git", "remote", "add", "github", GITHUB_REPO])

# Debug remotes
run_command(["git", "remote", "-v"])


# =============== SSH DEBUG (optional) ===============
run_command(["ssh", "-T", "git@github.com"], ignore_error=True)


# =============== PUSH TO GITHUB ===============
print("Pushing to GitHub...")

run_command(["git", "push", "-u", "github", f"{BRANCH}:main", "--force"])


print("✅ Sync completed successfully!")

