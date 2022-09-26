# Contribute

This section aims to explain how we develop and organise,
in order to help those that want to contribute to SimPhoNy.

## Background

### Tools

The following are some of the technologies and concepts we use regularly.
It might be useful to become familiar with them:

- Version control: [Git](https://git-scm.com/),
  [GitHub](https://github.com/about) and
  [GitLab](https://about.gitlab.com/)
- [Unittest](https://docs.python.org/3/library/unittest.html)
- Continuous integration
- Python virtual environments/[conda](https://docs.conda.io)
- [Docker](https://www.docker.com/resources/what-container/)
- Benchmarks

### Code Organisation

There are 3 main categories of repos:

- The [_SimPhoNy_ repository](https://github.com/simphony/osp-core/tree/v4.0.0rc4)
  contains the nucleus of SimPhoNy, the base on which the wrappers build.
- Each _wrapper_ will be in its own repository on GitHub or GitLab,
  mimicking
  [wrapper_development](https://github.com/simphony/wrapper-development).
- [_docs_](https://github.com/simphony/docs/tree/v4.0.0rc4)
  holds the source for this documentation.

There are also 4 types of branches:

- `master/main` contains all the releases, and should always be stable.
- `dev` holds the code for the newest release that is being developed.
- `issue branch` is where an specific issue is being solved.
- `hotfix branch` is where a critical software bug detected on the stable
  release (more on this later) is being solved.

## Developing workflow

- Every new feature or bug is defined in an issue and labelled accordingly.
  If there is something that is missing or needs improving,
  make an issue in the appropriate project.
- Generally, the issues are fixed by creating a new `issue branch` from the
  `dev` branch, committing to that branch and making a new Pull/Merge
  Request when done. An owner of the project should be tagged for review.
  They will review and merge the PR if the fix is correct, deleting the
  `issue branch` afterwards. The changes should be clearly explained in the
  issue/Pull Request.

```{warning}
   If the issue is a critical software bug detected in the stable release, a
   `hotfix branch` should be created from the `master/main` branch
   instead.

   After committing to such branch, a new Pull/Merge request (targeting
   `dev`) should be created. If the fix is correct, the project owner
   will merge the PR to `dev`, additionally merge the
   `hotfix branch` to `master/main`, and then delete the
   `hotfix branch`.
```

- Once the features for a release have been reached, `dev` will be merged to
  `master/main`. Every new commit in the `master/main` branch generally
  corresponds to a new release, which is labelled with a
  [git tag](https://git-scm.com/book/en/v2/Git-Basics-Tagging) matching its
  version number. An exception to this rule may apply, for example when
  several critical hotfixes are applied in a row, as it would then be
  better to just to publish a single release afterwards. In regard to
  version numbering, we adhere to the
  [_Semantic versioning_](https://semver.org/) rules.

In the next image it can be seen how the branches usually look during this
workflow, and the different commits used to synchronise them:

<figure style="display: table; text-align:center; margin-left: auto; margin-right:auto">

![](_static/branch_workflow.svg "Branches and commits")

</figure>

## Coding

### Documenting

- All code must be properly documented with meaningful comments.
- For readability, we now follow the
  [Google docstring format](https://google.github.io/styleguide/pyguide.html#s3.8-comments-and-docstrings).
- If some behaviour is very complex, in-line comments can be used.
  However, proper naming and clear operations are always preferred.

### Code style

- Code should follow
  [PEP8 code style conventions](https://peps.python.org/pep-0008/).
- All Python code should be validated by the
  [Flake8](https://github.com/pycqa/flake8) tool. The validation is also
  enforced on the repository by the
  [continuous integration](contribute.md#continuous-integration). Click
  [here](https://github.com/simphony/osp-core/blob/master/.github/workflows/ci.yml#L12)
  to see the specific options with which Flake8 is launched.
- All Python code should be reformatted with
  [black](https://github.com/psf/black) and
  [isort](https://github.com/PyCQA/isort). The use of said tools is
  enforced by the
  [continuous integration](contribute.md#continuous-integration). Therefore,
  we strongly recommend that you use the
  [configuration file](https://github.com/simphony/osp-core/blob/master/.pre-commit-config.yaml)
  bundled with the repository to
  [install](https://pre-commit.com/#installation) the
  [pre-commit framework](https://pre-commit.com/), that automates the task
  using git pre-commit hooks.
- A few
  [other style conventions](https://github.com/simphony/osp-core/blob/master/.pre-commit-config.yaml)
  are also enforced by the continuous integration through
  [pre-commit](https://pre-commit.com/) (such as empty lines at the end of
  text files). If you decide not to use it, the CI will let you know what
  to correct.

### Testing

- All complex functionality must be tested.
- If some implementation can not be checked through unittest, it should be
  at least manually run in different systems to assure an expected behaviour.

### Continuous Integration

- We currently run the CI through Github Actions/GitLab CI.
- Code style conventions are enforced through the use of Flake8, black, isort,
  and various
  [pre-commit](https://pre-commit.com/)
  [hooks](https://github.com/simphony/osp-core/blob/master/.pre-commit-config.yaml).
- Tests are automatically run for all pull requests.
- For the OSP-core code, benchmarks are run after every merge to `dev`.
  Benchmark results are available
  [here](https://simphony.github.io/osp-core/dev/bench/index.html). The CI
  will report a failure when a benchmark is 50% slower than in the previous
  run, in addition to automatically commenting on the commit.

### Naming conventions

- Use `cuds_object` as the argument name of your methods (not `entity`,
  `cuds`, `cuds_instance`...).
- The official spelling is `OSP-core` (as opposed to _osp core_, _OSP-Core_
  or similar).

## Contribute to OSP-core

If you are not a member of the
[SimPhoNy organisation](https://github.com/simphony), rather than creating
a branch from `dev`, you will have to fork the repository and create the
Pull Request.

## Contribute to wrapper development

For a sample wrapper, visit the
[wrapper_development](https://github.com/simphony/wrapper-development) repo.

README files should include:

- Information regarding the purpose of the wrapper and the backend used.
- A compatibility matrix with OSP-core.
- Installation instructions.
- Folder structure.
- Any other necessary information for users and other developers.

## Contribute to the docs

If you have any suggestion for this documentation, whether it is something
that needs more explanation, is inaccurate or simply a note on anything
that could be improved, you can open an issue
[here](https://github.com/simphony/docs/issues), and we will look into it!.
