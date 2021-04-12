from os import mkdir
from os.path import exists
from shutil import rmtree


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

    # Check to see if git is installed

    if not git.checkIfGitInstalled():
        print("git is not installed. Exiting program...")
        exit(1)

    # Check to see if the Source folder already exists
    if gce.checkSourcePathAvailibility():
        print("{} already exists. Exiting program...".format(gce.src))
        exit(2)

    # Check to see if the Output folder already exists
    if type(gce.checkDestinationPathAvailibility()) is str:
        print("Output folder has already been created. Exiting program...")
        exit(3)

    # Create the Output folder
    if not gce.makeDesitinationPath(dst="output"):
        print("Unable to create output folder. Exiting program...")
        exit(4)

    # Clone the git repository
    git.gitClone(repoURL=gce.repoURL, dst=gce.src)

    # Get the commit hash codes
    chc = git.gitCommitHashCodes(sourceFolder=gce.src)

    # Create the folders from the hash codes
    for commit in chc:
        gce.makeDesitinationPath(dst="output/" + commit)

    # Delete git repository
    gce.deleteRepo()
