BEGIN {
n="\n"
head="<a name=top>&nbsp;<p> </a>" n \
"[home](http://tiny.cc/ase19#top) | " n \
"[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, timm&commat;ieee.org " n \
"<br> " \
"[<img width=900 src=\"https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png\">](http://tiny.cc/ase19)<br> " n \
"[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | " n \
"[src](http://menzies.us/fun) | " n \
"[submit](http://tiny.cc/ase19give) | " n \
"[chat](https://ase19.slack.com/) " n 
}

head && /^[ \t]*$/ { print head; head=""; next }
1
