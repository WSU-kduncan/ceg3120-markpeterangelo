Command Line Git;

1.) status: -Shows status of the local repository. This status includes: ~number of local commits that have not been synced with remote (GitHub) ~list of files in local folder than are NOT being tracked by git ~list of files in local folder that have changes that need to be committed [git status]

2.) clone: -creates a clone/copy of an existing repository into a new directory. ~It is also used to create remote-tracking branches for each branch in the cloned repository. ~It is the most common command which allows users to obtain a development copy of an existing central repository. [git clone]

3.) add: -adds all modified and new (untracked) files in the current directory and all subdirectories to the staging area (a.k.a. the index) thus preparing them to be included in the next git commit. [git add]

4.) rm:

used to remove files from a Git repository. ~It can be thought of as the inverse of the git add command. ~The git rm command can be used to remove individual files or a collection of files. ~The primary function of git rm is to remove tracked files from the Git index. [git rm]
5.) commit: -term used for saving changes. ~Git does not add changes to a commit automatically. ~You need to indicate which file and changes need to be saved before running the Git commit command. [git commit]

6.) push: -used to upload local repository content to a remote repository. ~Pushing is how you transfer commits from your local repository to a remote repo ~pushing exports commits to remote branches [git push]

7.) fetch: -used to download commits, files and references from a remote repository into the local repository. ~It is used to see what other members of the team have been working on. ~fetching imports commits to local branches [git fetch]

8.) merge: -lets you take the independent lines of development created by git branch and integrate them into a single branch. [git merge]

9.) pull: -a GIT command that downloads the latest changes from the remote repository and automatically merges those changes in the local repository. [git pull]

10.) branch: -used to work with different versions of a repository at the same time. ~By default a repository has a master branch (a production branch). ~Any other branch is a copy of the master branch (as it was at a point in time). ~New Branches are for bug fixes and feature work separate from the master branch. ~A command which helps in creating, deleting and listing branches of the main code. [git branch] 11.) checkout: -the act of switching between different versions of a target entity. ~The git checkout command operates upon three distinct entities: files, commits, and branches. ~In addition to the definition of "checkout" the phrase "checking out" is commonly used to imply the act of executing the git checkout command. [git checkout]

init(don't do yet)

remote(don't do yet)

Git Files & Folders;

1.) .git folder: -the directory which is created when you do git init (in the case of a new project) or you do git clone (in the case of pulling a project from somewhere else). ~This is the "thing" which makes your project a "git" repository. ~Contains all the information that is necessary for your project in version control and all the information about commits, remote repository address, etc How To Use It: -Create a new folder, and add a file in it. -Now go to your terminal and add it like you add the normal files in Git. -Push them into the repository, and check the status to make sure you have created a directory.

2.) .gitignore file: -Specifies intentionally untracked files to ignore ~Files already tracked by Git are not affected ~The purpose of gitignore files is to ensure that certain files not tracked by Git remain untracked. How To Use It: -Create .gitignore File inside the project folder. -Write the name of the files you want to ignore in the .gitignore text file. -Each file name should be written in a new line.

.git/hooks(don't do yet)

GitHub;

1.) Pull requests: -Pull requests let you tell others about changes you've pushed to a branch in a repository on GitHub. ~Once a pull request is opened, you can discuss and review the potential changes with collaborators and add follow-up commits before your changes are merged into the base branch. How To Use It: -Click the Pull Requests tab. -Click New pull request. -In the base: dropdown, select master. In the compare: dropdown, select the branch you recently pushed to the repository. -Click Create pull request.

2.) SSH authentication to repositories: -SSH public key authentication works with a pair of generated encryption keys. The public key is shared and used to encrypt messages. The private key is kept safe and secure on your system and is used to read messages encrypted with the public key. How To Use It: -go to your GitHub dashboard -then click on Settings from the dropdown menu for your account -then go to SSH and GPG keys: -Select the New SSH key button: -Lastly, copy your public SSH key which is stored in a file with a .pub file extension in your .ssh folder

Actions(don't do yet)

Resources;

Pro Git Book
