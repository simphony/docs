# Contribute
This section aims to explain how we develop and organise,
in order to help those that want to contribute to SimPhoNy.

## Background
### Tools
The following are some of the technologies and concepts we use regularly.
It might be useful to become familiar with them:
 - Version control: Git, GitHub and GitLab
 - Python virtual environments/conda
 - Docker
 - Unittesting
 - Continuous Integration

### Code Organisation
There are 3 main categories of repos:
 - [_OSP-core_](https://github.com/simphony/osp-core) contains the nucleus of SimPhoNy, the base on which the wrappers build.
 - Each _wrapper_ will be in its own repository on GitHub or GitLab,
   mimicking [wrapper_development](https://github.com/simphony/wrapper-development).
 - [_docs_](https://github.com/simphony/docs) holds the source for this documentation.

There are also 3 types of branches:
 - `master/main` contains all the releases, and should always be stable.
 - `dev` holds the code for the newest release that is being developed.
 - `issue branch` is where an specific issues is being solved.

All wrappers and OSP-core are part of a common directory structure:
- _`osp/`_: contains all the SimPhoNy source code.
  - _`core/`_: OSP-core source code.
  - _`wrappers/`_: wrappers source code.
    - _`wrapper_xyz/`_: one folder per wrapper implementation.
- _`tests/`_: unittests of the code.
- _`examples/`_: simple examples of how to use a certain feature.

## Developing workflow
- Every new feature or bug is defined in an issue and labelled accordingly.  
 If there is something that is missing or needs improving,
 make an issue in the appropriate project.
- For each new release a milestone is created and assigned to issues and Pull/Merge Requests.
- The issues are fixed by creating a new `issue branch` from the `dev` branch, committing to that branch and making a new Pull/Merge Request when done.  
  An owner of the project should be tagged for review.
  They will review and merge the PR if the fix is correct.
  The changes should be clearly explained in the issue/Pull Request.
- Once the features for a release have been reached, `dev` will be merged to 
  `master/main`. Every new commit in the `master/main` branch generally corresponds 
  to a new release, which is labeled with a 
  [git tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging) matching its 
  version number. In regard to version numbering, we adhere to the 
  [_Semantic versioning_](https://semver.org/) rules.

In the next image it can be seen how the branches usually look during this workflow, and the different commits used to synchronise them:

<figure style="display: table; text-align:center; margin-left: auto; margin-right:auto">

![](./_static/img/branch_workflow.png "Branches and commits")

</figure>

## Coding
### Documenting
- All code must be  properly documented with meaningful comments.
- For readability, we now follow the [Google docstring format](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings).
- If some behaviour is very complex, in-line comments can be used. 
  However, proper naming and clear operations are always preferred.

### Testing
- All Python code should pass Flake8 tests.
- All complex functionality must be tested.
- If some implementation can not be checked through unittest, it should be at least manually run in different systems to assure an expected behaviour.

### Continuous Integration
- We currently run the CI through Github Actions/GitLab CI.
- Flake8 and unittests are automatically run for all PR.

### Naming conventions
- Use `cuds_object` as the argument name of your methods (not `entity`, `cuds`, `cuds_instance`...).
- The official spelling is `OSP-core` (as opposed to _osp core_, _OSP-Core_ or similar).

## Contribute to OSP-core
If you are not a member of the [SimPhoNy organisation](https://github.com/simphony), rather than creating a branch
from `dev`, you will have to fork the repository and create the Pull Request.

## Contribute to wrapper development
For a sample wrapper, visit the [wrapper_development](https://github.com/simphony/wrapper-development) repo.

README files should include:
- Information regarding the purpose of the wrapper and the backend used.
- A compatibility matrix with OSP-core.
- Installation instructions.
- Folder structure.
- Any other necessary information for users and other developers.

## Contribute to the docs
If you have any suggestion for this documentation, whether it is something that needs more explanation, is inaccurate or simply a note on anything that could be improved, you can open an issue [here](https://github.com/simphony/docs/issues), and we will look into it!.


