import subprocess

def check_for_deletions():
    # Get the list of deleted files/folders in the pull request branch
    deleted_items = subprocess.check_output(["git", "diff", "--name-only", "origin/main...HEAD"]).decode("utf-8").splitlines()

    if deleted_items:
        print("Deletions detected:")
        for item in deleted_items:
            print(item)
        return False

    return True

if __name__ == "__main__":
    if not check_for_deletions():
        exit(1)