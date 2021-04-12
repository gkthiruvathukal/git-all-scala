from os import mkdir
from os.path import exists
from shutil import rmtree

from progress.bar import Bar
from progress.spinner import MoonSpinner

from libs.cmdLineParser import cmdLineParser
from libs.git import Git


class GitCommitExploder:
    def __init__(self) -> None:
        args = cmdLineParser()
        self.repoURL: str = args.url[0]
        self.src: str = args.src[0]
        self.start: int = args.start
        self.stride: int = args.stride

    def checkSourcePathAvailibility(self) -> bool:
        return exists(self.src)

    def checkDestinationPathAvailibility(self) -> bool:
        return exists("output")

    def makeDesitinationPath(self, dst: str) -> bool:
        try:
            mkdir(dst)
        except FileExistsError:
            return False
        return True

    def deleteRepo(self) -> bool:
        return rmtree(self.src)


if __name__ == "__main__":
    gce = GitCommitExploder()
    git = Git()

    with MoonSpinner(message="Starting program... ") as spinner:
        # Check to see if git is installed
        if not git.checkIfGitInstalled():
            print("git is not installed. Exiting program...")
            exit(1)
        else:
            spinner.next()
        # Check to see if the Source folder already exists
        if gce.checkSourcePathAvailibility():
            print("{} already exists. Exiting program...".format(gce.src))
            exit(2)
        else:
            spinner.next()
        # Check to see if the Output folder already exists
        if type(gce.checkDestinationPathAvailibility()) is str:
            print("Output folder has already been created. Exiting program...")
            exit(3)
        else:
            spinner.next()
        # Create the Output folder
        if not gce.makeDesitinationPath(dst="output"):
            print("Unable to create output folder. Exiting program...")
            exit(4)
        else:
            spinner.next()

    # Clone the git repository
    print("Cloning git repository {} to local machine... ".format(gce.repoURL))
    git.gitClone(repoURL=gce.repoURL, dst=gce.src)

    # Check to make sure that the cloned repo is a git repository
    if not git.checkIfGitRepository(src=gce.src):
        print(
            "{} is not a valid git repository. Exiting program...".format(gce.repoURL)
        )
        exit(5)

    # Get the commit hash codes
    chc = git.gitCommitHashCodes(sourceFolder=gce.src)

    # Iterate through the hash codes
    with Bar(message="Exploding commits from {}".format(gce.src), max=len(chc)) as bar:
        for commit in chc:
            # Create a folder for that specific hash code
            gce.makeDesitinationPath(dst="output/" + commit)

            # Create git repo that tracks the changes for a specific commit
            git.gitRepoCreate(src=gce.src, dst="output/" + commit, chc=commit)
            bar.next()

    # Delete git repository
    gce.deleteRepo()
