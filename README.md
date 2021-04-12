# Git Commit Exploder

> Program which checkouts all previous versions of a Git repository and stores them in a `../temp/` directory

## Table of Contents

- [Git Commit Exploder](#git-commit-exploder)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [How to Execute](#how-to-execute)
    - [Command Line Arguements](#command-line-arguements)
  - [TODO](#todo)

## About

## How to Execute

### Command Line Arguements
- `-u / --url`: This argument is where the url for the desired git repo is provided.  If not provided then the program will fail
- `-s / --src`: This argument should be the name of the repo you wish to analyze.  It should also include all folders after root that specify the desired location of the folder.  It must match the name on GitHub otherwise the program will fail
- ~~`-d / --dst`: This argument is the user’s desired name for the result of the program.  It can be any name that is not already in use~~
- `--start`: This argument allows for the downloading of hash codes to start with a hash code later than the first one.  If left unspecified it is automatically set to 1 and every hash code is included
- `--stride`: This argument allows you to skip every n hash codes.  When used in conjunction with the start command it allows for the downloading of each hash to be spread more easily between compute nodes
## TODO
