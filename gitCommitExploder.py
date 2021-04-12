from os import mkdir
from os.path import exists

from libs.cmdLineParser import cmdLineParser
from libs.git import Git


class GitCommitExploder:
    def __init__(self, destinationFolder: str = "ouput") -> None:
        args = cmdLineParser()
        self.dst: str = destinationFolder
        self.repoURL: str = args.url[0]
        self.src: str = args.src[0]
        self.start: int = args.start[0]
        self.stride: int = args.stride[0]

    def checkSourcePathAvailibility(self) -> bool:
        return exists(self.src)

    def checkDestinationPathAvailibility(self) -> bool:
        return exists(self.dst)

    def makeDesitinationPath(self) -> bool:
        mkdir(self.dst)


if __name__ == "__main__":
    gce = GitCommitExploder()
    git = Git()

    # Check to see if git is installed

    # Check to see if the Source folder already exists

    # Check to see if the Output folder already exists

    # Create the Output folder

    # Clone the git repository

    # Get the commit hash codes

    # Create the folders from the hash codes
