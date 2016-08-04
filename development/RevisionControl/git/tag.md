# 打标签

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