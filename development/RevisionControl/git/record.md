# 记录更新

### 记录每次更新到仓库

* 文件状态 

    * 已跟踪文件

        * 未修改

        * 已修改

        * 已放入暂存区

    * 未跟踪文件

使用 Git 时文件的生命周期如下：

![](lifecycle.png)

***

### 文件状态

git status 命令，用于查看哪些文件处于什么状态。

已跟踪文件未被更改过，且没有处于未跟踪状态的新文件。会看到类似这样的输出：

    $ git status
    On branch master
    nothing to commit, working directory clean


存在新的未跟踪文件。会看到类似这样的输出：

    $ echo 'My Project' > README.md
    $ git status
    # On branch master
    #
    # Initial commit
    #
    # Untracked files:
    #   (use "git add <file>..." to include in what will be committed)
    #
    #       README.md
    nothing added to commit but untracked files present (use "git add" to track)

***

### 跟踪新文件

使用命令 git add 开始跟踪一个文件。 

    $ git add README.md

存在已跟踪文件，并处于暂存状态。会看到类似这样的输出：

    # On branch master
    #
    # Initial commit
    #
    # Changes to be committed:
    #   (use "git rm --cached <file>..." to unstage)
    #
    #       new file:   README.md
    #


***

### 暂存已修改文件

已跟踪文件的内容发生了变化，但还没有放到暂存区。会看到类似这样的输出：

    $ git status
    # On branch master
    # Changes to be committed:
    #   (use "git reset HEAD <file>..." to unstage)
    #
    #       new file:   README.md
    #
    # Changed but not updated:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #       modified:   CONTRIBUTING.md
    #

要暂存这次更新，需要运行 git add 命令。这是个多功能命令：可以用它开始跟踪新文件，或者把已跟踪的文件放到暂存区，还能用于合并时把有冲突的文件标记为已解决状态等。 将这个命令理解为“添加内容到下一次提交中”而不是“将一个文件添加到项目中”要更加合适。  

    $ git add CONTRIBUTING.md
    $ git status
    # On branch master
    # Changes to be committed:
    #   (use "git reset HEAD <file>..." to unstage)
    #
    #       modified:   CONTRIBUTING.md
    #       new file:   README.md
    #

***

### 状态简览
使用 git status -s 命令或 git status --short 命令，获取一种更为紧凑的格式输出。 状态报告输出如下：

    $ git status -s
    M  CONTRIBUTING.md
    A  README.md
    ?? HELLO.md

状态标记详解

    ??：新添加的未跟踪文件
    A ：新添加到暂存区中的文件
    M ：修改过得文件，并放入暂存区
     M：修改过得文件，还未放入暂存区
    MM：修改并提交到暂存区后又在工作区被修改
    
***

### 忽略文件

创建一个名为 .gitignore 的文件，列出要忽略的文件模式。

    $ cat .gitignore
    *.[oa]
    *~

文件 .gitignore 的格式规范如下：

* 所有空行或者以 # 开头的行都会被 Git 忽略。

* 可以使用标准的 glob 模式匹配。
    
    * 星号（*）匹配零个或多个任意字符；
    * [abc] 匹配任何一个列在方括号中的字符（这个例子要么匹配一个 a，要么匹配一个 b，要么匹配一个 c）;
    * 问号（?）只匹配一个任意字符；如果在方括号中使用短划线分隔两个字符，表示所有在这两个字符范围内的都可以匹配（比如 [0-9] 表示匹配所有 0 到 9 的数字）。
    * 使用两个星号（*) 表示匹配任意中间目录，比如a/**/z 可以匹配 a/z, a/b/z 或 a/b/c/z等。

* 匹配模式可以以（/）开头防止递归。

* 匹配模式可以以（/）结尾指定目录。

* 要忽略指定模式以外的文件或目录，可以在模式前加上惊叹号（!）取反。

我们再看一个 .gitignore 文件的例子：

    # no .a files
    *.a

    # but do track lib.a, even though you're ignoring .a files above
    !lib.a

    # only ignore the TODO file in the current directory, not subdir/TODO
    /TODO

    # ignore all files in the build/ directory
    build/

    # ignore doc/notes.txt, but not doc/server/arch.txt
    doc/*.txt

    # ignore all .pdf files in the doc/ directory
    doc/**/*.pdf

TIP
GitHub 有一个十分详细的针对数十种项目及语言的 .gitignore 文件列表，你可以在 https://github.com/github/gitignore 找到它.

***

### 查看已暂存和未暂存的修改

git diff 命令，查看具体修改内容。 git diff 将通过文件补丁的格式显示具体哪些行发生了改变。

查看尚未暂存的文件更新内容，直接输入 git diff：

    $ git diff
    diff --git a/CONTRIBUTING.md b/CONTRIBUTING.md
    index 23509e0..90f904d 100644
    --- a/CONTRIBUTING.md
    +++ b/CONTRIBUTING.md
    @@ -1,2 +1,3 @@
    hello
    git
    +add con

此命令比较的是工作目录中当前文件和暂存区域快照之间的差异， 也就是修改之后还没有暂存起来的变化内容。

若要查看已暂存的将要添加到下次提交里的内容，可以用 git diff --cached 命令。（Git 1.6.1 及更高版本还允许使用 git diff --staged，效果是相同的，但更好记些。）

    $ git diff --staged
    diff --git a/CONTRIBUTING.md b/CONTRIBUTING.md
    index ce01362..90f904d 100644
    --- a/CONTRIBUTING.md
    +++ b/CONTRIBUTING.md
    @@ -1 +1,3 @@
     hello
    +git
    +add con
    diff --git a/README.md b/README.md
    new file mode 100644
    index 0000000..de369b6
    --- /dev/null
    +++ b/README.md
    @@ -0,0 +1,2 @@
    +My Project
    +abc

请注意，git diff 本身只显示尚未暂存的改动，而不是自上次提交以来所做的所有改动。 所以有时候你一下子暂存了所有更新过的文件后，运行 git diff 后却什么也没有，就是这个原因。

***

### 提交更新

现在的暂存区域已经准备妥当可以提交了。 在此之前，请一定要确认还有什么修改过的或新建的文件还没有 git add 过，否则提交的时候不会记录这些还没暂存起来的变化。 这些修改过的文件只保留在本地磁盘。 所以，每次准备提交前，先用 git status 看下，是不是都已暂存起来了， 然后再运行提交命令 git commit, 命令后添加 -m 选项，将提交信息与命令放在同一行，如下所示：

    $ git commit -m 'modify file'
    [master d19800e] modify file
     2 files changed, 4 insertions(+), 0 deletions(-)
     create mode 100644 README.md

好，现在你已经创建了第一个提交！ 可以看到，提交后它会告诉你，当前是在哪个分支（master）提交的，本次提交的完整 SHA-1 校验和是什么（463dc4f），以及在本次提交中，有多少文件修订过，多少行添加和删改过。

请记住，提交时记录的是放在暂存区域的快照。 任何还未暂存的仍然保持已修改状态，可以在下次提交时纳入版本管理。 每一次运行提交操作，都是对你项目作一次快照，以后可以回到这个状态，或者进行比较。

***

### 跳过使用暂存区域

尽管使用暂存区域的方式可以精心准备要提交的细节，但有时候这么做略显繁琐。 Git 提供了一个跳过使用暂存区域的方式， 只要在提交的时候，给 git commit 加上 -a 选项，Git 就会自动把所有已经跟踪过的文件暂存起来一并提交，从而跳过 git add 步骤：

    $ echo "follow me" >> CONTRIBUTING.md
    $ git status
    # On branch master
    # Changed but not updated:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #       modified:   CONTRIBUTING.md
    #
    no changes added to commit (use "git add" and/or "git commit -a")

    $ git commit -a -m 'added new benchmarks'
    [master 3bcc140] added new benchmarks
     1 files changed, 1 insertions(+), 0 deletions(-)

***

### 移除文件

要从 Git 中移除某个文件，就必须要从已跟踪文件清单中移除（确切地说，是从暂存区域移除），然后提交。 可以用 git rm 命令完成此项工作，并连带从工作目录中删除指定的文件，这样以后就不会出现在未跟踪文件清单中了。

如果只是简单地从工作目录中手工删除文件，运行 git status 时就会在 “Changes not staged for commit” 部分（也就是 未暂存清单）看到：

    $ rm project.md
    $ git status
    # On branch master
    # Changed but not updated:
    #   (use "git add/rm <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #       deleted:    project.md
    #
    no changes added to commit (use "git add" and/or "git commit -a")

然后再运行 git rm 记录此次移除文件的操作：

    $ git rm project.md
    rm 'project.md'
    $ git status
    # On branch master
    # Changes to be committed:
    #   (use "git reset HEAD <file>..." to unstage)
    #
    #       deleted:    project.md
    #
下一次提交时，该文件就不再纳入版本管理了。 如果删除之前修改过并且已经放到暂存区域的话，则必须要用强制删除选项 -f（译注：即 force 的首字母）。 这是一种安全特性，用于防止误删还没有添加到快照的数据，这样的数据不能被 Git 恢复。

另外一种情况是，我们想把文件从 Git 仓库中删除（亦即从暂存区域移除），但仍然希望保留在当前工作目录中。 换句话说，你想让文件保留在磁盘，但是并不想让 Git 继续跟踪。 当你忘记添加 .gitignore 文件，不小心把一个很大的日志文件或一堆 .a 这样的编译生成文件添加到暂存区时，这一做法尤其有用。 为达到这一目的，使用 --cached 选项：

    $ git rm --cached README
git rm 命令后面可以列出文件或者目录的名字，也可以使用 glob 模式。 比方说：

    $ git rm log/\*.log
注意到星号 * 之前的反斜杠 \， 因为 Git 有它自己的文件模式扩展匹配方式，所以我们不用 shell 来帮忙展开。 此命令删除 log/ 目录下扩展名为 .log 的所有文件。 类似的比如：

    $ git rm \*~
该命令为删除以 ~ 结尾的所有文件。

***

### 移动文件

不像其它的 VCS 系统，Git 并不显式跟踪文件移动操作。 如果在 Git 中重命名了某个文件，仓库中存储的元数据并不会体现出这是一次改名操作。 不过 Git 非常聪明，它会推断出究竟发生了什么，至于具体是如何做到的，我们稍后再谈。

既然如此，当你看到 Git 的 mv 命令时一定会困惑不已。 要在 Git 中对文件改名，可以这么做：

$ git mv file_from file_to
它会恰如预期般正常工作。 实际上，即便此时查看状态信息，也会明白无误地看到关于重命名操作的说明：

    $ git mv README.md README
    # On branch master
    # Changes to be committed:
    #   (use "git reset HEAD <file>..." to unstage)
    #
    #       renamed:    README.md -> README
    #
其实，运行 git mv 就相当于运行了下面三条命令：

    $ mv README.md README
    $ git rm README.md
    $ git add README
如此分开操作，Git 也会意识到这是一次改名，所以不管何种方式结果都一样。 两者唯一的区别是，mv 是一条命令而另一种方式需要三条命令，直接用 git mv 轻便得多。 不过有时候用其他工具批处理改名的话，要记得在提交前删除老的文件名，再添加新的文件名。