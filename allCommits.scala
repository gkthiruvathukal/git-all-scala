
      %.git('init)(currentPath)
      %%("git", "remote", "add", "upstream", sourcePath)(currentPath)
      %%("git", "fetch", "upstream")(currentPath)
      %%("git", "checkout", currentHash)(currentPath)
      var lines = %%("cloc", currentPath)(destinationPath)
      println(lines)
