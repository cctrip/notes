---
weight: 1
title: "Git操作"
---

# Git操作

## 创建版本库


1. 创建一个空目录

   $ cd /usr/local/src

		$ mkdir project

2. 创建版本库

   * 初始化

     $ git init
     Initialized empty Git repository in /usr/local/src/project/.git/

   * 克隆现有仓库

     $ git clone [url]

3. 添加文件

   $ git add README.md

		$ git commit -m 'first commit'

***

## 记录更新

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

***

## 提交历史

### 查看提交历史

git log 命令，查看提交历史。

    $ git log
    commit ca82a6dff817ec66f44342007202690a93763949
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Mon Mar 17 21:52:11 2008 -0700
    
        changed the version number
    
    commit 085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Sat Mar 15 16:40:33 2008 -0700
    
        removed unnecessary test
    
    commit a11bef06a3f659402fe7563abf99ad00de2209e6
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Sat Mar 15 10:31:28 2008 -0700
    
        first commit


​      
默认不用任何参数的话，git log 会按提交时间列出所有的更新，最近的更新排在最上面。 正如你所看到的，这个命令会列出每个提交的 SHA-1 校验和、作者的名字和电子邮件地址、提交时间以及提交说明。

***

### git log 常用选项

-p，用来显示每次提交的内容差异。 你也可以加上 -2 来仅显示最近两次提交：

    $ git log -p -2
    commit ca82a6dff817ec66f44342007202690a93763949
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Mon Mar 17 21:52:11 2008 -0700
    
        changed the version number
    
    diff --git a/Rakefile b/Rakefile
    index a874b73..8f94139 100644
    --- a/Rakefile
    +++ b/Rakefile
    @@ -5,7 +5,7 @@ require 'rake/gempackagetask'
     spec = Gem::Specification.new do |s|
         s.platform  =   Gem::Platform::RUBY
         s.name      =   "simplegit"
    -    s.version   =   "0.1.0"
    +    s.version   =   "0.1.1"
         s.author    =   "Scott Chacon"
         s.email     =   "schacon@gee-mail.com"
         s.summary   =   "A simple gem for using Git in Ruby code."
    
    commit 085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Sat Mar 15 16:40:33 2008 -0700
    
    removed unnecessary test
    
    diff --git a/lib/simplegit.rb b/lib/simplegit.rb
    index a0a60ae..47c6340 100644
    --- a/lib/simplegit.rb
    +++ b/lib/simplegit.rb
    @@ -18,8 +18,3 @@ class SimpleGit
         end
    
     end
    -
    -if $0 == __FILE__
    -  git = SimpleGit.new
    -  puts git.show
    -end
    \ No newline at end of file


--stat，查看每次提交的简略的统计信息

    $ git log --stat
    commit ca82a6dff817ec66f44342007202690a93763949
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Mon Mar 17 21:52:11 2008 -0700
    
        changed the version number
    
     Rakefile | 2 +-
     1 file changed, 1 insertion(+), 1 deletion(-)
    
    commit 085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Sat Mar 15 16:40:33 2008 -0700
    
        removed unnecessary test
    
     lib/simplegit.rb | 5 -----
     1 file changed, 5 deletions(-)
    
    commit a11bef06a3f659402fe7563abf99ad00de2209e6
    Author: Scott Chacon <schacon@gee-mail.com>
    Date:   Sat Mar 15 10:31:28 2008 -0700
    
    first commit
    
     README           |  6 ++++++
     Rakefile         | 23 +++++++++++++++++++++++
     lib/simplegit.rb | 25 +++++++++++++++++++++++++
     3 files changed, 54 insertions(+)



--pretty。 指定使用不同于默认格式的方式展示提交历史。 这个选项有一些内建的子选项供你使用。 比如用 oneline 将每个提交放在一行显示，查看的提交数很大时非常有用。 另外还有 short，full 和 fuller 可以用。

    $ git log --pretty=oneline
    ca82a6dff817ec66f44342007202690a93763949 changed the version number
    085bb3bcb608e1e8451d4b2432f8ecbe6306e7e7 removed unnecessary test
    a11bef06a3f659402fe7563abf99ad00de2209e6 first commit

但最有意思的是 format，可以定制要显示的记录格式。 这样的输出对后期提取分析格外有用 — 因为你知道输出的格式不会随着Git的更新而发生改变：

    $ git log --pretty=format:"%h - %an, %ar : %s"
    ca82a6d - Scott Chacon, 6 years ago : changed the version number
    085bb3b - Scott Chacon, 6 years ago : removed unnecessary test
    a11bef0 - Scott Chacon, 6 years ago : first commit



git log --pretty=format 常用的选项

| 选项 | 说明                                        |
| ---- | ------------------------------------------- |
| %H   | 提交对象（commit）的完整哈希字串            |
| %h   | 提交对象的简短哈希字串                      |
| %T   | 树对象（tree）的完整哈希字串                |
| %t   | 树对象的简短哈希字串                        |
| %P   | 父对象（parent）的完整哈希字串              |
| %p   | 父对象的简短哈希字串                        |
| %an  | 作者（author）的名字                        |
| %ae  | 作者的电子邮件地址                          |
| %ad  | 作者修订日期（可以用 --date= 选项定制格式） |
| %ar  | 作者修订日期，按多久以前的方式显示          |
| %cn  | 提交者(committer)的名字                     |
| %ce  | 提交者的电子邮件地址                        |
| %cd  | 提交日期                                    |
| %cr  | 提交日期，按多久以前的方式显示              |
| %s   | 提交说明                                    |



当 oneline 或 format 与另一个 log 选项 --graph 结合使用时尤其有用。 这个选项添加了一些ASCII字符串来形象地展示你的分支、合并历史：

    $ git log --pretty=format:"%h %s" --graph
    * 2d3acf9 ignore errors from SIGCHLD on trap
    *  5e3ee11 Merge branch 'master' of git://github.com/dustin/grit
    |\
    | * 420eac9 Added a method for getting the current branch.
    * | 30e367c timeout code and tests
    * | 5a09431 add timeout protection to grit
    * | e1193f8 support for heads with slashes in them
    |/
    * d6016bc require time for xmlschema
    *  11d191e Merge branch 'defunkt' into local


git log 的常用选项

| 选项            | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| -p              | 按补丁格式显示每个更新之间的差异。                           |
| --stat          | 显示每次更新的文件修改统计信息。                             |
| --shortstat     | 只显示 --stat 中最后的行数修改添加移除统计。                 |
| --name-only     | 仅在提交信息后显示已修改的文件清单。                         |
| --name-status   | 显示新增、修改、删除的文件清单。                             |
| --abbrev-commit | 仅显示 SHA-1 的前几个字符，而非所有的 40 个字符。            |
| --relative-date | 使用较短的相对时间显示（比如，“2 weeks ago”）。              |
| --pretty        | 使用其他格式显示历史提交信息。可用的选项包括 oneline，short，full，fuller 和 format（后跟指定格式）。 |



限制输出长度
除了定制输出格式的选项之外，git log 还有许多非常实用的限制输出长度的选项，也就是只输出部分提交信息。 

另外还有按照时间作限制的选项，比如 --since 和 --until 也很有用。 例如，下面的命令列出所有最近两周内的提交：

    $ git log --since=2.weeks

这个命令可以在多种格式下工作，比如说具体的某一天 "2008-01-15"，或者是相对地多久以前 "2 years 1 day 3 minutes ago"。

另一个非常有用的筛选选项是 -S，可以列出那些添加或移除了某些字符串的提交。 比如说，你想找出添加或移除了某一个特定函数的引用的提交，你可以这样使用：

    $ git log -Sfunction_name



限制 git log 输出的选项

| 选项              | 说明                                         |
| ----------------- | -------------------------------------------- |
| -(n)              | 仅显示最近的 n 条提交                        |
| --since, --after  | 仅显示指定时间之后的提交。                   |
| --until, --before | 仅显示指定时间之前的提交。                   |
| --author          | 仅显示指定作者相关的提交。                   |
| --committer       | 仅显示指定提交者相关的提交。                 |
| --grep            | 仅显示含指定关键字的提交                     |
| -S                | 仅显示添加或移除了某个关键字的提交           |
| --all-match       | 显示满足所有匹配条件的提交                   |
| --(path)          | 仅显示某些文件或者目录的提交（选项最后指定） |

例子，
查看 Git 仓库中，2008 年 10 月期间，Junio Hamano 提交的但未合并的测试文件，可以用下面的查询命令：

    $ git log --pretty="%h - %s" --author=Junio Hamano --since="2008-10-01" \
       --before="2008-11-01" --no-merges -- t/
    5610e3b - Fix testcase failure when extended attributes are in use
    acd3b9e - Enhance hold_lock_file_for_{update,append}() API
    f563754 - demonstrate breakage of detached checkout with symbolic link HEAD
    d1a43f2 - reset --hard/read-tree --reset -u: remove unmerged new paths
    51a94af - Fix "checkout --track -b newbranch" on detached HEAD
    b0ad11e - pull: allow "git pull origin $something:$current_branch" into an unborn branch



***

## 撤销操作

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

## 远程仓库

远程仓库是指托管在因特网或其他网络中的你的项目的版本库。 你可以有好几个远程仓库，通常有些仓库对你只读，有些则可以读写。 与他人协作涉及管理远程仓库以及根据需要推送或拉取数据。 

管理远程仓库包括了解如何添加远程仓库、移除无效的远程仓库、管理不同的远程分支并定义它们是否被跟踪等等。 

***

### 查看远程仓库

git remote ： 列出指定的每一个远程服务器的简写。 如果你已经克隆了自己的仓库，那么至少应该能看到 origin

    $ git remote
    origin

指定选项 -v，会显示需要读写远程仓库使用的 Git 保存的简写与其对应的 URL。

    $ git remote -v
    origin  https://github.com/Code-CC/leetcode (fetch)
    origin  https://github.com/Code-CC/leetcode (push)

***


### 添加远程仓库

运行 git remote add <shortname> <url> 添加一个新的远程 Git 仓库，同时指定一个你可以轻松引用的简写：

    $ git remote
    origin
    $ git remote add pb https://github.com/paulboone/ticgit
    $ git remote -v
    origin	https://github.com/schacon/ticgit (fetch)
    origin	https://github.com/schacon/ticgit (push)
    pb	https://github.com/paulboone/ticgit (fetch)
    pb	https://github.com/paulboone/ticgit (push)

现在你可以在命令行中使用字符串 pb 来代替整个 URL。 例如，如果你想拉取 Paul 的仓库中有但你没有的信息，可以运行 git fetch pb：

    $ git fetch pb
    remote: Counting objects: 43, done.
    remote: Compressing objects: 100% (36/36), done.
    remote: Total 43 (delta 10), reused 31 (delta 5)
    Unpacking objects: 100% (43/43), done.
    From https://github.com/paulboone/ticgit
     * [new branch]      master     -> pb/master
     * [new branch]      ticgit     -> pb/ticgit

***

### 从远程仓库中抓取与拉取

从远程仓库中获得数据，可以执行：

    $ git fetch [remote-name]

这个命令会访问远程仓库，从中拉取所有你还没有的数据。（不进行合并分支） 

    $ git pull [remote-name] [buranch-name]

这个命令会自动的抓取然后合并远程分支到当前分支。

***


### 推送到远程仓库

当你想分享你的项目时，必须将其推送到上游。可以使用下面的命令： 

    git push [remote-name] [branch-name]

只有当你有所克隆服务器的写入权限，并且之前没有人推送过时，这条命令才能生效。 当你和其他人在同一时间克隆，他们先推送到上游然后你再推送到上游，你的推送就会毫无疑问地被拒绝。 你必须先将他们的工作拉取下来并将其合并进你的工作后才能推送。

***

### 查看远程仓库

git remote show [remote-name] ：查看远程仓库信息。 

    $ git remote show origin
    * remote origin
      Fetch URL: https://github.com/Code-CC/leetcode
      Push  URL: https://github.com/Code-CC/leetcode
      HEAD branch: master
      Remote branch:
        master tracked
      Local branch configured for 'git pull':
        master merges with remote master
      Local ref configured for 'git push':
        master pushes to master (local out of date)


它同样会列出远程仓库的 URL 与跟踪分支的信息。 

***

### 远程仓库的移除与重命名

 git remote rename ：修改一个远程仓库的简写名。 

    $ git remote rename pb paul
    $ git remote
    origin
    paul

git remote rm ：移除一个远程仓库

    $ git remote rm paul
    $ git remote
    origin

***

## 标签

Git 可以给历史中的某一个提交打上标签，以示重要。 比较有代表性的是人们会使用这个功能来标记发布结点（v1.0 等等）。 

***

### 列出标签

git tag：列出已有的标签

	$ git tag
	v0.1
	v1.3


git tag -l ：使用特定的模式查找标签。 

	$ git tag -l 'v1.8.5*'
	v1.8.5
	v1.8.5-rc0
	v1.8.5-rc1
	v1.8.5-rc2
	v1.8.5-rc3
	v1.8.5.1
	v1.8.5.2
	v1.8.5.3
	v1.8.5.4
	v1.8.5.5

***

### 创建标签

Git 使用两种主要类型的标签：轻量标签（lightweight）与附注标签（annotated）。

一个轻量标签很像一个不会改变的分支 - 它只是一个特定提交的引用。

然而，附注标签是存储在 Git 数据库中的一个完整对象。 它们是可以被校验的；其中包含打标签者的名字、电子邮件地址、日期时间；还有一个标签信息；并且可以使用 GNU Privacy Guard （GPG）签名与验证。 通常建议创建附注标签，这样你可以拥有以上所有信息；但是如果你只是想用一个临时的标签，或者因为某些原因不想要保存那些信息，轻量标签也是可用的。

* 附注标签

  git tag -a ：添加一个附注标签。

  	$ git tag -a v1.4 -m 'my version 1.4'
  	$ git tag
  	v0.1
  	v1.3
  	v1.4

  -m 选项指定了一条将会存储在标签中的信息。 如果没有为附注标签指定一条信息，Git 会运行编辑器要求你输入信息。

  git show 命令可以看到标签信息与对应的提交信息：

  	$ git show v1.4
  	tag v1.4
  	Tagger: Ben Straub <ben@straub.cc>
  	Date:   Sat May 3 20:19:12 2014 -0700
  	
  	my version 1.4
  	
  	commit ca82a6dff817ec66f44342007202690a93763949
  	Author: Scott Chacon <schacon@gee-mail.com>
  	Date:   Mon Mar 17 21:52:11 2008 -0700
  	
  	    changed the version number


* 轻量标签

  $ git tag v1.4-lw
  $ git tag
  v0.1
  v1.3
  v1.4
  v1.4-lw
  v1.5

  这时，如果在标签上运行 git show，你不会看到额外的标签信息。 命令只会显示出提交信息：

  	$ git show v1.4-lw
  	commit ca82a6dff817ec66f44342007202690a93763949
  	Author: Scott Chacon <schacon@gee-mail.com>
  	Date:   Mon Mar 17 21:52:11 2008 -0700
  	
  	    changed the version number

* 后期打标签

  你也可以对过去的提交打标签。 假设提交历史是这样的：

  	$ git log --pretty=oneline
  	15027957951b64cf874c3557a0f3547bd83b3ff6 Merge branch 'experiment'
  	a6b4c97498bd301d84096da251c98a07c7723e65 beginning write support
  	0d52aaab4479697da7686c15f77a3d64d9165190 one more thing
  	6d52a271eda8725415634dd79daabbc4d9b6008e Merge branch 'experiment'
  	0b7434d86859cc7b8c3d5e1dddfed66ff742fcbc added a commit function
  	4682c3261057305bdd616e23b64b0857d832627b added a todo file
  	166ae0c4d3f420721acbb115cc33848dfcc2121a started write support
  	9fceb02d0ae598e95dc970b74767f19372d61af8 updated rakefile
  	964f16d36dfccde844893cac5b347e7b3d44abbc commit the todo
  	8a5cbc430f1a9c3d00faaeffd07798508422908a updated readme

  现在，假设在 v1.2 时你忘记给项目打标签，也就是在 “updated rakefile” 提交。 你可以在之后补上标签。 要在那个提交上打标签，你需要在命令的末尾指定提交的校验和（或部分校验和）:

  	$ git tag -a v1.2 9fceb02
  	
  	$ git tag
  	v0.1
  	v1.2
  	v1.3
  	v1.4
  	v1.4-lw
  	v1.5
  	
  	$ git show v1.2
  	tag v1.2
  	Tagger: Scott Chacon <schacon@gee-mail.com>
  	Date:   Mon Feb 9 15:32:16 2009 -0800
  	
  	version 1.2
  	commit 9fceb02d0ae598e95dc970b74767f19372d61af8
  	Author: Magnus Chacon <mchacon@gee-mail.com>
  	Date:   Sun Apr 27 20:43:35 2008 -0700
  	
  	    updated rakefile
  	...

***

### 共享标签

默认情况下，git push 命令并不会传送标签到远程仓库服务器上。 在创建完标签后你必须显式地推送标签到共享服务器上。 这个过程就像共享远程分支一样 - 你可以运行 git push origin [tagname]。

	$ git push origin v1.5
	Counting objects: 14, done.
	Delta compression using up to 8 threads.
	Compressing objects: 100% (12/12), done.
	Writing objects: 100% (14/14), 2.05 KiB | 0 bytes/s, done.
	Total 14 (delta 3), reused 0 (delta 0)
	To git@github.com:schacon/simplegit.git
	 * [new tag]         v1.5 -> v1.5

如果想要一次性推送很多标签，也可以使用带有 --tags 选项的 git push 命令。 

	$ git push origin --tags
	Counting objects: 1, done.
	Writing objects: 100% (1/1), 160 bytes | 0 bytes/s, done.
	Total 1 (delta 0), reused 0 (delta 0)
	To git@github.com:schacon/simplegit.git
	 * [new tag]         v1.4 -> v1.4
	 * [new tag]         v1.4-lw -> v1.4-lw

***

### 检出标签

在 Git 中你并不能真的检出一个标签，因为它们并不能像分支一样来回移动。 如果你想要工作目录与仓库中特定的标签版本完全一样，可以使用 git checkout -b [branchname] [tagname] 在特定的标签上创建一个新分支：

	$ git checkout -b version2 v2.0.0
	Switched to a new branch 'version2'

当然，如果在这之后又进行了一次提交，version2 分支会因为改动向前移动了，那么 version2 分支就会和 v2.0.0 标签稍微有些不同，这时就应该当心了。

***

## 别名

Git 并不会在你输入部分命令时自动推断出你想要的命令。 如果不想每次都输入完整的 Git 命令，可以通过 git config 文件来轻松地为每一个命令设置一个别名。 这里有一些例子你可以试试：

	$ git config --global alias.co checkout
	$ git config --global alias.br branch
	$ git config --global alias.ci commit
	$ git config --global alias.st status

这意味着，当要输入 git commit 时，只需要输入 git ci。 随着你继续不断地使用 Git，可能也会经常使用其他命令，所以创建别名时不要犹豫。

在创建你认为应该存在的命令时这个技术会很有用。 例如，为了解决取消暂存文件的易用性问题，可以向 Git 中添加你自己的取消暂存别名：

	$ git config --global alias.unstage 'reset HEAD --'

这会使下面的两个命令等价：

	$ git unstage fileA
	$ git reset HEAD -- fileA

这样看起来更清楚一些。 通常也会添加一个 last 命令，像这样：

	$ git config --global alias.last 'log -1 HEAD'

这样，可以轻松地看到最后一次提交：

	$ git last
	commit 66938dae3329c7aebe598c2246a8e6af90d04646
	Author: Josh Goebel <dreamer3@example.com>
	Date:   Tue Aug 26 19:48:51 2008 +0800
	
	    test for current head
	
	    Signed-off-by: Scott Chacon <schacon@example.com>

可以看出，Git 只是简单地将别名替换为对应的命令。 然而，你可能想要执行外部命令，而不是一个 Git 子命令。 如果是那样的话，可以在命令前面加入 ! 符号。 如果你自己要写一些与 Git 仓库协作的工具的话，那会很有用。 我们现在演示将 git visual 定义为 gitk 的别名：

	$ git config --global alias.visual '!gitk'