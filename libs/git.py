from os import popen, removexattr, system, chdir, getcwd
from os.path import exists


class Git:
    def __init__(self) -> None:
        self.gitFolderName = ".git"
        self.gitPath = "/usr/bin/git"
        self.cwd = getcwd()

    def checkIfGitInstalled(self) -> bool:
        return exists(self.gitPath)

    def checkIfGitRepository(self, src: str) -> bool:
        chdir(src)

        val = exists(self.gitFolderName)

        chdir(self.cwd)
        return val

    def gitClone(self, repoURL: str, dst: str) -> int:
        return system(
            "git clone {} {} -q && cd {} && for remote in `git branch -r | grep -v /HEAD`; do git checkout --track $remote -f -q; done".format(
                repoURL, dst, dst
            )
        )

    def gitCommitHashCodes(self, sourceFolder: str) -> set:
        output = []

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
        chdir(self.cwd)

        commit: str
        for commit in output:
            if commit == "":
                output.pop(output.index(commit))

        return set(output)

    def gitRepoCreate(self, src: str, dst: str, chc) -> None:
        src: str = self.cwd + "/" + src

        chdir(dst)

        system("git init -q")
        system("git remote add upstream {}".format(src))

        chdir(self.cwd)
