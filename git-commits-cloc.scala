#!/usr/bin/env amm

import $ivy.`com.chuusai::shapeless:2.4.0-M1`
import $ivy.`org.log4s::log4s:1.9.0`
import $ivy.`org.slf4j:slf4j-simple:1.7.30`

import ammonite.ops._
import ammonite.ops.ImplicitWd._
import scala.collection.mutable.ListBuffer
import scala.io.StdIn.readLine

@main
def hello(
       @arg(doc = "person to greet")
       person: String,
       @arg(doc = "number of greetings to extend to person (default = 1)")
       count: Int = 1,
       @arg(doc = "flag (default = True)")
       flag : Boolean = true): Unit = {

   val logger = org.log4s.getLogger
   logger.debug(f"person = ${person}, count = ${count}")
   (1 to count) map { i => logger.info(f"Hello ${person} ${i}") } 
}

@main
def commits(
  @arg(doc = "URL of repo (must be able to clone from this URL)") url: String,
  @arg(doc = "source folder for cloning") src: String,
  @arg(doc = "dstination folder for exploding commits") dst: String,
  @arg(doc = "start at commit (e.g. 0 is the first commit in branch)") start: Int,
  @arg(doc = "skip commmits (e.g. go from 0 to 0 + stride value") stride: Int): Unit = {

    val logger = org.log4s.getLogger

    logger.info("I'm logging, Baby")

    //Establishes path for source folder where clone occurs and destination folder which will recieve every commit
    val sourcePath = root / src
    val destinationPath = root / dst

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
    %.git("clone", url)( root / src)

    //Gets the hashs for each commit and prepares them as an iterator
    val logForList = hashCodes(src).toList
    val currentNodeHashes = for (i <- (start to logForList.size - 1 by stride).toList) yield logForList(i)
        val logIterator = currentNodeHashes.toIterator

        //Creates folder where all commits will be placed as subfolders
        mkdir ! root / dst

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
