Website's open source technology stack
======================================

Here's a quick outline of open source technologies used to power the site.


* [Python 3](https://www.python.org) using [Django](https://www.djangoproject.com) web framework and [Gunicorn](http://gunicorn.org) server
* [Nginx](http://nginx.com) frontend server for static files with reverse proxy to Gunicorn workers
* [MySQL](https://www.mysql.com) database
* HTML5 / [SASS](http://sass-lang.com) / [jQuery](https://jquery.com)
* [Ubuntu](http://www.ubuntu.com) 18.04 LTS


...and here are some of the [open
source applications](https://github.com/fmalina) that were initailly developed
for this site.




---


FlatmateRooms currently runs on 2 x 4GB RAM SSD Ubuntu 18.04 servers hosted by
[Linode](https://www.linode.com/?r=0e93596acefccf3b3fb413934e67d1cb6bcaeb55) in
their London data centre:


* Primary database server
* Main web server (database replication, PostFix mail server, git repository)
	+ extended disk volume for storage of image uploads




---


Development tools:


* [Git](http://git-scm.com) and [SourceTree](http://www.sourcetreeapp.com), which allows deployment using just `git push` and `pull`
* [PyCharm](https://www.jetbrains.com/pycharm/) a great text editor and IDE for Python programming
* ssh, [fabric](http://www.fabfile.org) for admin, backups and syncing
