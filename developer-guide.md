# Developer's Guide  

There are two main documented guidelines for developing the
SeisUP Project Creator application:  
> follow PEP8
> use the GitFlow workflow process.

Naming Conventions and Style Guide:
-----------------------------------

We should follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide, but here are some key things to be aware of.

First of all, keep your code readable, so that someone new coming
into the project can read your code and know exactly what it does.

**Module level**  
Modules should be named using all lowercase letters, be simple, easy to read, and descriptive.  For example:  

	simplyread.py  

Functions defined in modules should have similar tasks, for instance
a module containing various functions to copy files, link files, create
files, etc., could be put into a module called `fileutil.py`

**Function level**  
Functions should be all lowercase, word separated by underscores, and be descriptive. For example:  

	tool_to_copy_files()

Each function should have a docstring immediately following the function definition as follows:

```
def tool_to_copy_files():
	"""
	A short one-line description of function.

	input:
		None
		stringvar	- (str) path to a directory
		intvar		- (int) how many licks it takes to get to the center of a lolipop.

	output:
		None (if its not returning anything)
		returns forty_two - the answer to the meaning of life
	"""
	now start
	writing your function
	# with appropriate comments in places
	if nothing_more:
		print 'finished'
```

Don't name variables the same as Python's builtin types or keywords.
For instance,  

	`int = 'something'`

is not good.  `int` is a Python keyword for integer. Just don't do this, come up with a different name.  


Workflow with Git:
------------------

The source code is hosted in a private repository on <bitbucket.org>

We will be following a well documented workflow known as [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).

There is a production code we call the `master`.  This code is working code
that endusers should be able to use. Developers should not touch the `master` branch unless they are merging other branches to fix bugs or to roll out a new release.

A branch of the `master` we will call `develop` will be used for developing
new features and enhancements. Each new feature or enhancement being worked
on should be a branch off of `develop` called somethin descriptive like 
`cool_new_feature`. Once these features are completed they will be merged with `develop`, and when we have enough new features and enhancements, 
`develop` will be merged with `master` as a release version.

The `master` and `develop` branches have already been created in the 
production code repository located [here](https://bitbucket.org/cory_robinson/supprojectcreator/overview). Each developer should clone this repository 
into their own local `develop` repository located on their local machine, 
say in your home directory. In your home directory, execute:  

```
git clone ssh://user@host/path/to/repo.git
git checkout -b develop origin/develop
```

To work on a new feature on the `develop` branch, execute:

```
git checkout -b new_feature develop
```
The `-b` tells git to create a new branch called `new_feature` based off of the `develop` branch.  With this command, you are automatically switched over to the `new_feature` branch. You can execute

```
git branch -a
```
to see a list of branches you have and which one you are currently on.

Now develop your new feature. Either place it in an existing module, or create a new module for it.  When you think you have something working, 
execute

```
git add new_feature.py
```
To see the status of your repo, execute `git status -s`. The files with an `A` are the ones you just added. 
Files with an `M` are one that you have modified, and might need to add.

Once you `add`ed the files, execute
```
git commit -m "write a short message emphasing your new feature or bug fix"
```
You may want to edit some more code before you're ready to move on, and so 
whichever files you edit, you will need to `git add` them, then do another `git commit -m "message"`

Now, if you're through making changes for the time being, you will need to push those changes to the repository you branched off of. So if you created a branch `new_feature` based off of the `develop` branch, you will need to

```
git pull origin develop 	# this bring in any code that someone else may have updated
git push origin develop 	# puts your new code into the main develop branch
```

As a side note, it is probably a good idea to `git pull` from whatever branch you are working off of, whenever you begin working, so that your branch will contain the most up-to-date code from everyone. If someone else has pushed code into `develop` and you haven't pulled before you `push` your changes, then your branch will be 'behind' and you may have to do a `rebase` with that branch. This may happen occasionally, and you can find some instructions on how to handle it [here](https://www.atlassian.com/git/tutorials/comparing-workflows/centralized-workflow).

If your new feature is done, you've `pulled` and `pushed` and you're ready to merge it with the `develop` code, then you should submit a `pull request` by clicking the 
'pull request' link on your bitbucket.org repository website. The box on the left should be whatever `new_feature` branch you have, and you want that to go into whatever origin branch `master` or `develop` which you choose from the box on the right. Then your code will be reviewed, and tested by another developer, before we make the final merge.

Reviewing Pull Requests
-----------------------

blah blah blah!