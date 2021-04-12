from os import popen, system, chdir, getcwd
from os.path import exists


class Git:
    def __init__(self) -> None:
        self.gitFolderName = ".git"
        self.gitPath = "/usr/bin/git"

    def checkIfGitInstalled(self) -> bool:
        return exists(self.gitPath)

    def checkIfGitRepository(self, src: str) -> bool:
        cwd = getcwd()
        chdir(src)

        val = exists(self.gitFolderName)

        chdir(cwd)
        return val

    def gitClone(self, repoURL: str, dst: str) -> int:
        return system(
            "git clone {} {} -q && cd {} && for remote in `git branch -r | grep -v /HEAD`; do git checkout --track $remote -f -q; done".format(
                repoURL, dst, dst
            )
        )

    def gitCommitHashCodes(self, sourceFolder: str) -> list:
        output = []

        cwd = getcwd()
        chdir(sourceFolder)

        branches: list = (
            popen("git branch").read().replace(" ", "").replace("*", "").split("\n")
        )

        branch: str
        for branch in branches:
            system("git checkout {} -q".format(branch))

            log: str = popen(cmd="git log").read()
            logList: list = log.split("\n")

            message: str
            for message in logList:
                if message.find("commit") != -1:
                    output.append(message.split(" ")[1])
        chdir(cwd)

        return output
