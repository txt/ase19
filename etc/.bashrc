#!/usr/bin/env bash

uname="$(uname -s)"
#for i in sbcl clisp tmux htop; do
#  case "${uname}" in
#      Linux*)     
#        which $i > /dev/null || sudo apt get $i;;
#      Darwin*)    
#        which $i > /dev/null || brew install $i;;
#      *) echo "UNKNOWN:${uname}"; exit 1;;
#  esac
#done
#
_c0="\033[00m"     # white
_c1="\033[01;32m"  # green
_c2="\033[01;34m"  # blue
_c3="\033[31m"     # red
_c5="\033[35m"     # purple
_c6="\033[33m"     # yellow
_c7="\033[36m"     # turquoise
_c8="\033[96m"     # magenta

here() { cd $1; basename "$PWD"; }
base=$(basename $Ell)

PROMPT_COMMAND='echo -ne "${_c2}$base:${_c6}$(git branch 2>/dev/null | grep '^*' | colrm 1 2) ";PS1="${_c1}$_c0$(here ../..)/$(here ..)/$(here .) ${_c3}\!>${_c0}\e[m "'


gfig() {
  git config --global credential.helper cache
  git config credential.helper 'cache --timeout=3600'
}

alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias get='gfig; git pull'
alias grep='grep --color=auto'
alias put='gfig; git commit -am saving; git push; git status'
alias vi="vim -u $Ell/etc/.vimrc "
alias tmux="$(which tmux) -f $Ell/etc/.tmuxrc "

py() { 
  p=$(which python3)
  $p -B $1.py
}
ok() { 
  py ok$1
}

header() { gawk '
BEGIN {
n="\n"
head="<a name=top>&nbsp;<p> </a>" n \
"[home](http://tiny.cc/ase19#top) | " n \
"[copyright](https://github.com/txt/ase19/blob/master/LICENSE.md#top) &copy;2019, tjmenzie&commat;ncsu.edu " n \
"<br> " \
"[<img width=900 src=\"https://raw.githubusercontent.com/txt/ase19/master/etc/img/banner.png\">](http://tiny.cc/ase19)<br> " n \
"[syllabus](https://github.com/txt/ase19/blob/master/syllabus.md#top) | " n \
"[src](http://menzies.us/fun) | " n \
"[submit](http://tiny.cc/ase19give) | " n \
"[chat](https://ase19.slack.com/) " n
}

BEGIN               { Start=1 }
Start && /^[ \t]*$/ { print head; Start=0; next }
Start               { next }
1
'
}

headers() {
  files=$(find $Ell -name "*.md")
  for f in $files; do
    echo "# $f..."
    cat $f | header > /tmp/$$
    mv /tmp/$$ $f
  done
}

case "${uname}" in
      Linux*)     
        alias ls='ls --color=auto';;
      Darwin*)    
        alias ls='ls -G' ;;
      *) ;;
esac

alias reload=". $Ell/etc/.bashrc"
echo -e "${_c5}sh ell v2.0 (c) 2019 <timm@ieee.org> "
