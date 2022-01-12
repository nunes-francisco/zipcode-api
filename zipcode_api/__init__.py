import git

repo = git.Repo(search_parent_directories=True)
version = repo.tags[-1]
__version__ = version