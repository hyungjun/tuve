TUVE Documentation
==================

Transportation of Underground with Visualization Enhancement, starting with Tokyo Metro (東京メトロ) API

(All the parts are not supposed to be here, README.md, but I keep it this way until I see a better document structure. Configuration for read-the-docs is already setup [here](https://tuve.readthedocs.org/en/latest/). **This is a documentation for developers. This does not explain how to use TUVE's  front-end for public users. The users guide will be shipped in front-end.**)

# Installation
## For Service

If you want to contribute to TUVE, please also refer [For Contribution](#for-contribution) part.

* Clone TUVE

```
git clone https://github.com/dinerk/tuve.git
```

* Have your Python environment ready

```
cd tuve
virtuelenv env
source env/script/activate
pip install -r requirements.txt
# or just sudo pip without having virtual env.
```

* Initialize front-end

```
git submodule update --init # and check if `frontend` directory has `dist` subdirectory.
```

* Prepare a proper `API_KEY` if nessacery. (optional)

```
# If you are using bash it might look like...
export TUVE_API_KEY=0123456789abcdef

# or if you are on fish shell...
set -gx TUVE_API_KEY 0123456789abcdef
```

For your convenience, add `API_KEY` to you environment variables by `TUVE_API_KEY` and you will be fine without specifying API_KEY at CLI every time you run TUVE. To get Tokyo Metro API key, visit [here](https://developer.tokyometroapp.jp/info).

* And all set. Let's serve !

```
# default context is "develop"
python tuve serve

# "production" is also available.
python tuve serve production 

# to provide API_KEY manually,
python tuve serve --API_KEY=0123456789abcdef

# to see available options for `serve` command,
$ python tuve serve -h

usage: python tuve serve [-h] [--HOST] [--PORT] [--DEBUG] [--API_KEY]
                         [--LOG_LEVEL]
                         [CONTEXT]

positional arguments:
  CONTEXT       TUVE's running context. You have `production` and
                `develop(default)` context.

optional arguments:
  -h, --help    show this help message and exit
  --HOST        Host name for serving
  --PORT        Port number for serving
  --DEBUG       Related to mp forking and auto-reload in Tornado
  --API_KEY     API KEY if necessary
  --LOG_LEVEL   5=VERBOSE...50=CRITICAL, [5, 10, 20, 30, 40, 50]

When DEBUG flag is off, Tornado tries to fork processes by a number of
processors. And if API_KEY is missing, TUVE will looks up OS environment
variables if `TUVE_API_KEY` is defined.

```
And then you should be able to access the front-end through your browser locally.

## For contribution

There is a lot of good resourses to read how to contribute with Git and Github.

* [Github guide - contributing](https://guides.github.com/activities/contributing-to-open-source/)
* [Github guide - forking](https://guides.github.com/activities/forking/)
* [Git the  simple guide](http://rogerdudler.github.io/git-guide/)
* [From Stack Overflow](http://stackoverflow.com/questions/315911/git-for-beginners-the-definitive-practical-guide)
* [Atlassian Git tutorial](https://www.atlassian.com/git/tutorials/)
* [Learn Git branching](http://pcottle.github.io/learnGitBranching/)

### Development Environment

To start preparing your development environment, first you need to fork [TUVE](https://github.com/dinerk/tuve) Git repository before cloning. Once you have forked the repo, you can clone yours.

```
# note the renamed URL and destination.
git clone https://github.com/your-name/tuve.git tuve-your-name

# In order to make your local repo up-to-date with main repository,
cd tuve-your-name
git remote add upstream git://github.com/dinerk/tuve.git
```

Then you can procced the rest refering [For Service](#for-service). Now you should have two remote repos and one local.

* `local`
  * your new branches made here.
  * your commits are done here on some branches you made.
* `origin`
  * your branches are pushed here.
  * your PRs (pull request) are made here. (conventionally)
* `upstream`
  * your PRs from `origin` are sent here.
  * your friend's PR is also sent here.
  * Other people do the same thing.
  * So `local` should be updated frequently as `upstream` grows to keep it tracked.
  * It's always not enough to type `git fetch upstream` at your `local` unless a project is in low activity. It does not make you confused.

Basically you can do anything under this environment. You can create a PR that introduces many cool features, you can fix many bugs that you have found. Or you can even make your repo complelety "forked" and keep walking with that. But there's a few more things to read to have better open-sourced life.

### Community

#### Checking issues

You can easily get the general idea about needs of the project by browsing [TUVE's issue page](https://github.com/dinerk/tuve/issues). Commits that can close these issues will most likely make everyone happy and make the project a step improved. But what if you have a new smart idea and no one seems to have like yours? What if you see a bug and would like to be the first reporter? Opening an issue is always welcome.

#### Opening issues
...
#### Lables and Milestones
...
#### branch name and commit message convention for community
...
#### branch name
...
#### commit message
...
#### documentation for community
...
##### Changelog
...
##### Releasenote
...
### When you git something...
...
### Back-end
...
### Front-end
...
### Back and forth
...
### Using iPython
...
## API Spec Classes
...
## TokyoMetro API
...
### Low-level Interface
...
### High-level Interface
...
## Tornado Handlers
...
### Frontend Proxy
...
### API Handler
...
# TUVE Command Line Interface
...
## Command
...
## Context
...
## Options
..
