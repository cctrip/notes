# 提交历史

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

 选项 |	说明 
 ---- | ----- 
 %H   | 提交对象（commit）的完整哈希字串
 %h   | 提交对象的简短哈希字串
 %T   | 树对象（tree）的完整哈希字串
 %t   | 树对象的简短哈希字串
 %P   | 父对象（parent）的完整哈希字串
 %p   | 父对象的简短哈希字串
 %an  | 作者（author）的名字
 %ae  | 作者的电子邮件地址
 %ad  | 作者修订日期（可以用 --date= 选项定制格式）
 %ar  | 作者修订日期，按多久以前的方式显示
 %cn  | 提交者(committer)的名字
 %ce  | 提交者的电子邮件地址
 %cd  | 提交日期
 %cr  | 提交日期，按多久以前的方式显示
 %s   | 提交说明



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

 选项            | 说明
 --------        | -----
 -p              | 按补丁格式显示每个更新之间的差异。
 --stat          | 显示每次更新的文件修改统计信息。
 --shortstat     | 只显示 --stat 中最后的行数修改添加移除统计。
 --name-only     | 仅在提交信息后显示已修改的文件清单。
 --name-status   | 显示新增、修改、删除的文件清单。
 --abbrev-commit | 仅显示 SHA-1 的前几个字符，而非所有的 40 个字符。
 --relative-date | 使用较短的相对时间显示（比如，“2 weeks ago”）。
 --pretty        | 使用其他格式显示历史提交信息。可用的选项包括 oneline，short，full，fuller 和 format（后跟指定格式）。



限制输出长度
除了定制输出格式的选项之外，git log 还有许多非常实用的限制输出长度的选项，也就是只输出部分提交信息。 

另外还有按照时间作限制的选项，比如 --since 和 --until 也很有用。 例如，下面的命令列出所有最近两周内的提交：

    $ git log --since=2.weeks

这个命令可以在多种格式下工作，比如说具体的某一天 "2008-01-15"，或者是相对地多久以前 "2 years 1 day 3 minutes ago"。

另一个非常有用的筛选选项是 -S，可以列出那些添加或移除了某些字符串的提交。 比如说，你想找出添加或移除了某一个特定函数的引用的提交，你可以这样使用：

    $ git log -Sfunction_name



限制 git log 输出的选项

 选项	| 说明
 ------- | ----
 -(n)    | 仅显示最近的 n 条提交
 --since, --after | 仅显示指定时间之后的提交。
 --until, --before | 仅显示指定时间之前的提交。
 --author | 仅显示指定作者相关的提交。
 --committer | 仅显示指定提交者相关的提交。
 --grep | 仅显示含指定关键字的提交
 -S      | 仅显示添加或移除了某个关键字的提交
 --all-match | 显示满足所有匹配条件的提交
 --(path)  | 仅显示某些文件或者目录的提交（选项最后指定）


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
