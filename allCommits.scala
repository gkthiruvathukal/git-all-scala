
    val sourcePath = root / sourceFolder
    val destinationPath = root / destinationFolder

    //Checks whether these two folders already exist and if so exits the program and alerts the user
    if (exists ! sourcePath) {
      println("Source folder already exists cannot execute program")
      System.exit(0)
    }
    if (exists ! destinationPath) {
      println("Destination folder already exists cannot execute program")
      System.exit(0)
    }

    //Gets the hashs for each commit and prepares them as an iterator
    val logForList = hashCodes(sourceFolder).toList
    val currentNodeHashes = for (i <- (startHash to logForList.size - 1 by stride).toList) yield logForList(i)
    val logIterator = currentNodeHashes.toIterator

    //Creates folder where all commits will be placed as subfolders
    mkdir ! root / destinationFolder

    //This loop creates a new folder for each commit and fills it with the files that were current as of that commit
    for (currentHash <- logIterator) {
      mkdir ! destinationPath / currentHash
      var currentPath = destinationPath / currentHash
      %.git('init)(currentPath)
      %%("git", "remote", "add", "upstream", sourcePath)(currentPath)
      %%("git", "fetch", "upstream")(currentPath)
      %%("git", "checkout", currentHash)(currentPath)
      var lines = %%("cloc", currentPath)(destinationPath)
      println(lines)
    }
  }
