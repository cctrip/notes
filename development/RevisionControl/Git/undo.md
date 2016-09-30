# 撤消操作

### 重新提交

--amend 选项的提交命令尝试重新提交：

    $ git commit --amend

这个命令会将暂存区中的文件提交。 如果自上次提交以来你还未做任何修改（例如，在上次提交后马上执行了此命令），那么快照会保持不变，而你所修改的只是提交信息。
文本编辑器启动后，可以看到之前的提交信息。 编辑后保存会覆盖原来的提交信息。

例如，你提交后发现忘记了暂存某些需要的修改，可以像下面这样操作：

    $ git commit -m 'initial commit'
    $ git add forgotten_file
    $ git commit --amend

最终你只会有一个提交 - 第二次提交将代替第一次提交的结果。

***

### 取消暂存的文件

    $ git add *
    $ git status
    # On branch master
    # Changes to be committed:
    #   (use "git reset HEAD <file>..." to unstage)
    #
    #       modified:   CONTRIBUTING.md
    #       modified:   README
    #

git rest HEAD <FILE> 取消暂存：

    $ git reset HEAD CONTRIBUTING.md
    Unstaged changes after reset:
    M       CONTRIBUTING.md

    $ git status
    # On branch master
    # Changes to be committed:
    #   (use "git reset HEAD <file>..." to unstage)
    #
    #       modified:   README
    #
    # Changed but not updated:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #       modified:   CONTRIBUTING.md
    #

***


### 撤消对文件的修改

git checkout -- <file> ， 将它还原成上次提交时的样子：

    $ git checkout -- CONTRIBUTING.md
    $ git status
    # On branch master
    # Changes to be committed:
    #   (use "git reset HEAD <file>..." to unstage)
    #
    #       modified:   README
    #

***