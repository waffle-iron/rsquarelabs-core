#Contributing to rl-core


The best way to contribute to the roadmap and feature discussions is by talking with the RSQUARELABS Team and rsquarelabs-core Community in realtime through the Gitter chat, or by starting a new issue as a discussion thread.

- [Got a Question or Problem](#gaqp)
- [Browsing the code](#code)
- [Found a Bug](#bug)
- [Want a feature](#want-feature)
- [Submission Guidelines](#guidelines)
	- [Submitting an issue](#submit-issue)
	- [Submitting a Pull Request](#submit-pullrequest)
- [Git Commit Guidelines](#commit-guidelines)
 

##<a name="gaqp"></a> Got a question or problem?
Discuss it on the [Google Group](https://groups.google.com/d/forum/rsquarelabs-core
) or chat with us on [Gitter](https://gitter.im/rsquarelabs/rsquarelabs-core).


##<a name="code"></a> Browsing the code?
We work on two branches: 
- `master` for stable, released code
- `dev`, a development branch. 

It might be important to distinguish them when you are reading the commit history searching for a feature or a bugfix, or when you are unsure of where to base your work from when contributing.

##<a name="bug"></a>Found a bug?
We would like to hear about it. Please [submit an issue][new-issue] on GitHub and we will follow up. Even better, we would appreciate a [Pull Request][new-pr] with a fix for it!

- If the bug was found in a release, it is best to base your work on `master` and submit your PR against it.
- If the bug was found on `dev` (the development branch), base your work on `dev` and submit your PR against it.

Please follow the [Pull Request Guidelines][new-pr].


##<a name="want-feature"></a> Want a feature?

Feel free to request a feature by [submitting an issue][new-issue] on GitHub and open the discussion.

If you'd like to implement a new feature, please consider opening an issue first to talk about it. It may be that somebody is already working on it, or that there are particular issues that you should be aware of before implementing the change. If you are about to open a Pull Request, please make sure to follow the [submissions guidelines][new-pr].

## <a name="guidelines"></a>Submission Guidelines

### <a name="submit-issue"></a>Submitting an issue

Before you submit an issue, search the archive, maybe you will find that a similar one already exists.

If you are submitting an issue for a bug, please include the following:

- An overview of the issue
- Your use case (why is this a bug for you?)
- The version of rsquarelabs-core you are running
- The platform you are running rsquarelabs-core on
- Steps to reproduce the issue
- Eventually, logs from your `error.log` file. You can find this file at `<nginx_working_dir>/logs/error.log`
- Ideally, a suggested fix

The more informations you give us, the more able to help we will be!

### <a name="submit-pullrequest"></a>Submitting a Pull Request

- First of all, make sure to base your work on the `dev` branch (the development branch):

  ```
  # a bugfix branch for dev would be prefixed by fix/
  # a bugfix branch for master would be prefixed by hotfix/
  $ git checkout -b feature/my-feature dev
  ```

- Please create commits containing **related changes**. For example, two different bugfixes should produce two separate commits. A feature should be made of commits splitted by **logical chunks** (no half-done changes). Use your best judgement as to how many commits your changes require.

- Write insightful and descriptive commit messages. It lets us and future contributors quickly understand your changes without having to read your changes. Please provide a summary in the first line (50-72 characters) and eventually, go to greater lengths in your message's body. We also like commit message with a **type** and **scope**. We generally follow the [Angular commit message format](https://github.com/angular/angular.js/blob/master/CONTRIBUTING.md#commit-message-format).

- Please **include the appropriate test cases** for your patch.

- Make sure all tests pass before submitting your changes. See the [Makefile operations](/README.md#makefile-operations).

- Make sure the linter does not throw any error: `make lint`.

- Rebase your commits. It may be that new commits have been introduced on `dev`. Rebasing will update your branch with the most recent code and make your changes easier to review:

  ```
  $ git fetch
  $ git rebase origin/dev
  ```

- Push your changes:

  ```
  $ git push origin -u feature/my-feature
  ```

- Open a pull request against the `dev` branch.

- If we suggest changes:
  - Please make the required updates (after discussion if any)
  - Only create new commits if it makes sense. Generally, you will want to amend your latest commit or rebase your branch after the new changes:

    ```
    $ git rebase -i dev
    # choose which commits to edit and perform the updates
    ```

  - Re-run the test suite
  - Force push to your branch:

    ```
    $ git push origin feature/my-feature -f
    ```

##<a name="commit-guidelines"></a>Git Commit Guidelines
We have very precise rules over how our git commit messages can be formatted. This leads to more readable messages that are easy to follow when looking through the project history. But also, we use the git commit messages to generate the AngularJS change log.

The commit message formatting can be added using a typical git workflow or through the use of a CLI wizard ([Commitizen](https://github.com/commitizen/cz-cli)). To use the wizard, run npm run commit in your terminal after staging your changes in git.

Every Commit must be one of the following Type :


* **feat**: A new feature
* **fix**: A bug fix
* **docs**: Documentation only changes
* **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing
  semi-colons, etc)
* **refactor**: A code change that neither fixes a bug nor adds a feature
* **perf**: A code change that improves performance
* **test**: Adding missing tests
* **chore**: Changes to the build process or auxiliary tools and libraries such as documentation
  generation
  

----------
We are eager to see your contribution!

We collect all requests and ideas and share with the community for feedback, you should watch the milestones and issues for further roadmap updates.


[new-issue]: #submitting-an-issue
[new-pr]: #submitting-a-pull-request
