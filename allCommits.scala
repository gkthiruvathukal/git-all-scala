
      %%("git", "remote", "add", "upstream", sourcePath)(currentPath)
      %%("git", "fetch", "upstream")(currentPath)
      %%("git", "checkout", currentHash)(currentPath)
