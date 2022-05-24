Website's open source technology stack
======================================
Here's a quick outline of open source technologies used to power the site.

* [Python 3](https://www.python.org) using [Django](https://www.djangoproject.com) web framework and
   [Gunicorn](http://gunicorn.org) server
* [Nginx](http://nginx.com) frontend server for static files with reverse proxy to backend
* [MySQL 8](https://www.mysql.com) database
* HTML5 / [SASS](http://sass-lang.com) / [jQuery](https://jquery.com)
* [Ubuntu](http://www.ubuntu.com) 20.04 LTS

...and here are some of the [open source applications](https://github.com/fmalina)
that were developed for this site.

---

Website currently runs on 2 x 4GB RAM SSD Ubuntu 20.04 servers hosted by
Linode in their London data centre:

* Primary database server
* Main web server (database replication, PostFix mail server, git repository)
	+ extended disk volume for storage of image uploads

---

Development tools:

* [Git](http://git-scm.com) and [SourceTree](http://www.sourcetreeapp.com),
  which allows deployment using just `git push` and `pull`
* [PyCharm](https://www.jetbrains.com/pycharm/) a great text editor and IDE for Python programming
* ssh, [fabric](http://www.fabfile.org) for admin, backups and syncing
