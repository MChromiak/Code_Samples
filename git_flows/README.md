### Syncing the fork repository
This library is hosted at GitHub thus any change requires forking. WHile 
forking the original source repo can be modified by its creator thus the fork
 will stay behind new changes from the original author.
 
To keep you for updated with the original repo one has to do the update 
manually and locally with the following steps:

1. Add the remote, call it "upstream":

`git remote add upstream https://github.com/whoever/whatever.git`

2. Fetch all the branches of that remote into remote-tracking branches, such 
as  upstream/master:

`git fetch upstream`

3. Make sure that you're on your local's forked `master` branch:

`git checkout master`

4. There are two ways now:


* Rewrite your master branch so that any commits of  yours that aren't 
already in `upstream/master` are replayed on top of that other branch:<br/> 
`git rebase upstream/master`

* Alternatively: If you don't want to rewrite the history of your master 
branch, (for example because other people may have cloned it). Merge the 
changes from `upstream/master` into your local master branch. This brings 
your fork's master branch into sync with the upstream repository, without 
losing your local changes:<br/>
`git merge upstream/master` <br/> 
However, for making further pull requests that are as clean as possible, it's
probably better to rebase.<br/> 
**Note:** If your local branch didn't have any unique commits, Git will 
instead perform a "fast-forward":

Now simply:

`git push origin/master`

However, if you've chose to rebase your branch onto `upstream/master` you may 
need to force the push in order to push it to your own forked repository on GitHub.  
You'd do that with:

`git push -f origin master`

You only need to use the `-f` the first time after you've rebased.

**NOTE** note that rather than having to rebase your own master branch to 
ensure you are starting with clean state, you should probably work on a 
separate branch and make a pull request from that. This keeps your master 
clean for any future merges and it stops you from having to rewrite history with
`-f` which messes up everyone that could have cloned your version.