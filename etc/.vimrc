set backupdir-=.
set backupdir^=~/tmp,/tmp
set nocompatible              " required
"filetype off                  " required
filetype plugin indent on
set modelines=3
set scrolloff=3
set autoindent
set hidden "remember ls
set wildmenu
set wildmode=list:longest
set visualbell
set ttyfast
set backspace=indent,eol,start
set laststatus=2
set splitbelow
set paste
"ascii mouse
set mouse=a
"place buffer name into window title
set title
"show line numbers
set number
" auto-change directory to that of the current buffer
autocmd BufEnter * cd %:p:h
" Shows the matching bracket when entering expressions
" (you'll never miss one again!)
set showmatch
set matchtime=15
"pretty colors
set background=light
set syntax=on
syntax enable
"" Incremental search
" (as you type in the search query, it will show you
" whether your query currently matches anything)
set ignorecase
set incsearch
set smartcase
set showmatch
set hlsearch
" set the runtime path to include Vundle and initialize
"set rtp+=~/.vim/bundle/Vundle.vim
"call vundle#begin()
"" alternatively, pass a path where Vundle should install plugins
""call vundle#begin('~/some/path/here')
"" let Vundle manage Vundle, required
"Plugin 'gmarik/Vundle.vim'
"" Add all your plugins here (note older versions of Vundle used Bundle instead of Plugin)
"Plugin 'scrooloose/nerdtree'
"Plugin 'tmhedberg/SimpylFold'
"Plugin 'vim-scripts/indentpython.vim'
""Plugin 'Valloric/YouCompleteMe'
"Plugin 'scrooloose/syntastic'
"Plugin 'jnurmine/Zenburn'
"Plugin 'altercation/vim-colors-solarized'
"Plugin 'kien/ctrlp.vim'
""Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
"Plugin 'bling/vim-airline'
"Plugin 'vim-airline/vim-airline-themes'
"Plugin 'croaker/mustang-vim'
"Plugin 'ap/vim-buftabline'
"Plugin 'wolfgangmehner/vim-support'
"Plugin 'kovisoft/slimv'
"Plugin 'airblade/vim-gitgutter'
"
"" All of your Plugins must be added before the following line
"call vundle#end()            " required
"filetype plugin indent on    " required
"colorscheme delek 
"set hlsearch!
"nnoremap <F3> :set hlsearch!<CR>
"" autocmd VimEnter * NERDTree
"autocmd VimEnter * wincmd w
"autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
"
"set hidden
"nnoremap <C-N> :bnext<CR>
"nnoremap <C-P> :bprev<CR>
"set vb
"colorscheme slate
""autocmd VimEnter * NERDTree
"autocmd VimEnter * wincmd w
"autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
set nofoldenable    " disable folding
set ruler
set statusline=%F\ \(%M\)\ %=%l\:%c\ 
  
set lispwords+=defthing   
set lispwords+=doitems    
set lispwords+=deftest
set lispwords+=defkeep
set lispwords+=labels
set lispwords+=labels
set lispwords+=doread
set lispwords+=while
set lispwords+=until
set path+=../**

if has("mouse_sgr")
    set ttymouse=sgr
else
    set ttymouse=xterm2 
end        
colorscheme default
set termguicolors
let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"

aug python
    " ftype/python.vim overwrites this
    au FileType python setlocal ts=2 sts=2 sw=2 expandtab
aug end
autocmd BufRead,BufNewFile *.md setlocal spell

au BufRead,BufNewFile *.py setlocal textwidth=60
map Z 1z=
set spell spelllang=en_us
set spellsuggest=fast,20 "Don't show too much suggestion for spell check

nn <F7> :setlocal spell! spell?<CR>


let g:vim_markdown_fenced_languages = ['awk=awk']
set spellfile=./.mywords.add

colorscheme evening
hi Normal guibg=NONE ctermbg=NONE
