from os.path import exists


class Git:
    def __init__(
        self, gitFolderName: str = ".git", gitPath: str = "/usr/bin/git"
    ) -> None:
        self.gitFolderName = ".git"
        self.gitPath = "/usr/bin/git"

    def checkIfInstalled(self) -> bool:
        return exists(self.gitPath)

    def checkIfGitRepository(self) -> bool:
        return exists(self.gitFolderName)
