#!/usr/bin/env amm

import $ivy.`com.chuusai::shapeless:2.4.0-M1`
import $ivy.`org.log4s::log4s:1.9.0`
import $ivy.`org.slf4j::slf4j-simple:1.7.30`

import ammonite.ops._
import ammonite.ops.ImplicitWd._
import scala.collection.mutable.ListBuffer
import scala.io.StdIn.readLine

@main
def hello(person: String): Unit = {
    println(f"Hello ${person}")
}

@main
def commits(url: String, src: String, dst: String, start: Int, stride: Int): Unit = {
    val repoURL = url
    val sourceFolder = src
    val destinationFolder = dst
    val startHash = start

    val logger = org.log4s.getLogger

    logger.info("I'm logging, Baby")

    //Establishes path for source folder where clone occurs and destination folder which will recieve every commit
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

    //Clones repo into source folder
    %.git("clone", repoURL)( root / sourceFolder)

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

def hashCodes(args: String): Array[String] = {
    val source = root / args
    val log = %%("git", "log")(source)
    val logString = log.toString
    val logArray = logString.split("\n")
    val justHashCodes = logArray filter { line => line.startsWith("commit") } map { line => line.split(" ")(1) }

    return justHashCodes
}
