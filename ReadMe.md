# 📘 Git & GitHub Notes (Practical + Explained)
## 1️⃣ Basic Setup (One-time)
Check Git installation
git --version


What it does: Confirms Git is installed and shows the version.

Set username and email
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"


What it does:
Identifies you as the author of commits (important for GitHub & teams).

Set default branch to main
git config --global init.defaultBranch main


What it does:
Ensures all new repos use main instead of master.

2️⃣ Creating a New Repository (Local → GitHub)
Initialize Git
git init


What it does:
Creates a .git folder → turns a normal folder into a Git repository.

Check repository status
git status


What it does:
Shows:

modified files

staged files

untracked files

This is your most-used command.

3️⃣ Staging & Committing
Stage all files
git add .


What it does:
Moves changes from working directory → staging area.

Stage a specific file
git add filename.ext


What it does:
Stages only the selected file.

Commit changes
git commit -m "Meaningful commit message"


What it does:
Creates a snapshot of staged changes with a message.

❗ No commit = nothing to push.

4️⃣ Connecting to GitHub (Remote Repo)
Add remote repository
git remote add origin https://github.com/USERNAME/REPO_NAME.git


What it does:
Connects local repo to GitHub.

Check remote
git remote -v


What it does:
Shows fetch & push URLs of the remote.

5️⃣ Pushing & Pulling
Push to GitHub (first time)
git push -u origin main


What it does:

Pushes code to GitHub

Links local main with remote main

Push changes (after first time)
git push


What it does:
Uploads new commits to GitHub.

Pull latest changes
git pull


What it does:
Fetches + merges changes from remote to local.

6️⃣ Branch Management
Show branches
git branch


What it does:
Lists local branches.

Show remote branches
git branch -r


What it does:
Lists branches on GitHub.

Create new branch
git branch feature-name


What it does:
Creates a new branch (does not switch).

Switch branch
git checkout branch-name


What it does:
Moves HEAD to another branch.

Create + switch branch
git checkout -b branch-name


What it does:
Creates and switches in one step.

Delete local branch
git branch -d branch-name


What it does:
Deletes branch safely (only if merged).

Delete remote branch
git push origin --delete branch-name


What it does:
Removes branch from GitHub.

7️⃣ Undo & Fix Mistakes
Unstage a file
git restore --staged filename


What it does:
Removes file from staging area.

Discard local changes
git restore filename


What it does:
Reverts file to last committed state.

⚠️ Permanent loss of changes.

Amend last commit
git commit --amend


What it does:
Edits last commit message or adds forgotten files.

8️⃣ Removing Git (If Needed)
Remove Git from project
Remove-Item -Recurse -Force .git


(PowerShell)

What it does:
Completely removes Git history from folder.

9️⃣ Best Practices (Important)

One project = one repo

Commit small, logical changes

Write clear commit messages

Pull before pushing

Avoid submodules unless required

🔁 Daily Workflow (Remember This)
git status
git add .
git commit -m "message"
git push


That’s 80% of Git usage.

📌 Final Advice (Straight Talk)

You don’t need advanced Git now.
Master status → add → commit → push.
Everything else builds on that.


This structure is:
- Simple
- Interview-safe
- Easy to extend later

---

# 2️⃣ GIT COMMANDS — INTERVIEW LANGUAGE EXPLANATION

Use these answers **word-for-word** if needed.

---

### 🔹 What is `git init`?
> `git init` initializes a new Git repository by creating a `.git` directory that tracks project history.

---

### 🔹 What is `git status`?
> `git status` shows the current state of the working directory and staging area, including modified, staged, and untracked files.

---

### 🔹 What does `git add` do?
> `git add` moves changes from the working directory to the staging area so they can be included in the next commit.

---

### 🔹 What is a commit?
> A commit is a snapshot of the project at a specific point in time, stored with a unique hash and a message.

---

### 🔹 What does `git commit -m` do?
> It permanently records staged changes into the Git history with a descriptive message.

---

### 🔹 What is a branch in Git?
> A branch is an independent line of development that allows changes without affecting the main codebase.

---

### 🔹 Difference between `main` and `master`?
> There is no technical difference; `main` is the modern default branch name, while `master` is legacy.

---

### 🔹 What is `origin`?
> `origin` is the default alias for the remote repository URL.

---

### 🔹 What does `git push` do?
> `git push` uploads local commits to a remote repository such as GitHub.

---

### 🔹 What does `git pull` do?
> `git pull` fetches changes from the remote repository and merges them into the current branch.

---

### 🔹 What is `.git`?
> `.git` is a hidden directory that stores the entire version history, configuration, and metadata of the repository.

---

### 🔹 What is a merge conflict?
> A merge conflict occurs when Git cannot automatically combine changes from different branches.

---

### 🔹 What is HEAD in Git?
> HEAD is a pointer that represents the current branch and commit you are working on.

---

## 🔥 Final Honest Advice
- Maintain **one README per repo**
- Write **short but structured notes**
- Git knowledge like this already puts you **above average candidates**

Next things I can give you (very useful):
- A **commit message style guide**
- A **DSA folder structure that scales**
- Common **Git interview trick questions**

Say what you want next.
