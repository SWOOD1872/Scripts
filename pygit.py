#!/usr/bin/env python3

import os
import sys
from argparse import ArgumentParser

parser = ArgumentParser(description="%(prog)s: A Python interface to common Git commands using the argparse\
                                                    module of the Python standard library")
parser.add_argument("-d", "--delete_repo", help="Delete a git repository")
parser.add_argument("-c", "--create_repo", help="Create a new git repository")
parser.add_argument("-l", "--list_repos", help="List a directory if it contains a git repository (Checks all sub-directories)")
args = parser.parse_args()

# Delete a git repository
def delete_git_repo(repo):
    repo_path = os.path.join(repo, ".git")
    try:
        if not os.path.isdir(repo_path):
            raise FileNotFoundError
        sys.stdout.write(f"Deleting git repository {repo_path}\n")
        os.system(f"rm -rf {repo_path}")
    except FileNotFoundError:
        sys.stderr.write(f"No git repository found in {repo}\n")

# Create a git repository
def create_git_repo(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError
        if os.path.isdir(os.path.join(directory, ".git")):
            raise FileExistsError
        curdir = os.getcwd()
        os.chdir(directory)
        sys.stdout.write(f"Creating git repository {os.path.join(os.getcwd(), '.git')}\n")
        os.system("git init > /dev/null 2>&1")
        os.chdir(curdir) # Required?
    except FileNotFoundError:
        sys.stderr.write(f"Specified directory '{directory}' does not exist\n")
    except FileExistsError:
        sys.stdout.write(f"A Git repository already exists in {directory}\n")

# List a directory (and all sub-directories) if it has a git repository
def list_git_repos(directory):
    dirs_with_repos = list()
    repos_found = 0
    for dp, dn, _ in os.walk(directory):
        if ".git" in dn:
            repos_found += 1
            sys.stdout.write(f"Git repository found in {dp}\n")
    if repos_found == 0:
        sys.stdout.write(f"No git repository found in {directory} or in any sub-directory\n")

if args.delete_repo:
    delete_git_repo(args.delete_repo)

if args.create_repo:
    create_git_repo(args.create_repo)

if args.list_repos:
    list_git_repos(args.list_repos)