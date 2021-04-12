from os import popen, system
from os.path import exists


class Git:
    def __init__(self) -> None:
        self.gitFolderName = ".git"
        self.gitPath = "/usr/bin/git"

    def checkIfGitInstalled(self) -> bool:
        return exists(self.gitPath)

    def checkIfGitRepository(self) -> bool:
        return exists(self.gitFolderName)

    def gitClone(self, repoURL: str, dst: str) -> int:
        return system("git clone {} {}-q".format(repoURL, dst))

    def gitCommitHashCodes(self, sourceFolder: str) -> list:
        output = []

        log: str = popen(cmd="cd {} && git log".format(sourceFolder)).read()
        logList: list = log.split("\n")

        message: str
        for message in logList:
            if message.find("commit") != -1:
                output.append(message.split(" ")[1])
        return output
