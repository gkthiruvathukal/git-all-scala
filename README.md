# Git Commit Exploder

> Program which checkouts all previous versions of a Git repository and stores them in a `temp` directory

## Table of Contents

- [Git Commit Exploder](#git-commit-exploder)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [How to Execute](#how-to-execute)
    - [Prerequisites](#prerequisites)
    - [Steps to Execute](#steps-to-execute)
    - [Command Line Arguements](#command-line-arguements)
  - [TODO](#todo)

## About

This program is meant to take a git repository, go through **EVERY** commit on **EVERY** branch in that repository and create a git repository initalized at that specific commit.

As you can imagine, this program results in a considerable amount of computer storage being used up.

## How to Execute

### Prerequisites

1. You must have `Python 3.9.x` installed
2. You must have `pip` installed for your version of `Python 3.9.x`

### Steps to Execute

1. In your terminal, run `python -m pip install progress` **or** `python -m pip install -r requirements.txt`
2. In your terminal, run `python gitCommitExploder.py -u GIT_REPO_URL` where `GIT_REPO_URL` is the repository that you are cloning to your local machine

### Command Line Arguements

- `-u / --url`: This argument is where the url for the desired git repo is provided.  If not provided then the program will fail
- `-s / --src`: This argument should be the name of the repo you wish to analyze.  It should also include all folders after root that specify the desired location of the folder.  It must match the name on GitHub otherwise the program will fail
- ~~`--start`: This argument allows for the downloading of hash codes to start with a hash code later than the first one.  If left unspecified it is automatically set to 1 and every hash code is included~~
- ~~`--stride`: This argument allows you to skip every n hash codes.  When used in conjunction with the start command it allows for the downloading of each hash to be spread more easily between compute nodes~~

## TODO

1. Implement `--start` arguement
2. Implement `--stride` arguement
3. Dockerize project
