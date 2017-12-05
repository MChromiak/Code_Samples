# Bash

To assure the bash comletition run: `sudo apt-get install bash-completion`

# [Powerline](https://github.com/powerline/powerline)
Under Ubuntu, the problem is that apt-get is not installing bindings for vim.
Instead use the pip installations instructions as explained:

* Prerequisite: git and pip `sudo apt-get install python-pip git`

#### Install:
```$ sudo pip install git+git://github.com/Lokaltog/powerline```

In presented example the Ubuntu default python2.7 uses its default pip  
version:
```
$ which python
/usr/bin/python
$ python -V
Python 2.7.12
$ which pip
/usr/local/bin/pip
$ pip -V
pip 9.0.1 from /usr/local/lib/python2.7/dist-packages (python 2.7)

```
To use Python 3.x simply install python 3.x and use `pip3` instead.

Verify powerline installation:
```
$ pip show powerline-status
Name: powerline-status
Version: 2.6.dev9999+git.5198b50463c7a29a9f5ef94bbc45a995223dac2d
Summary: The ultimate statusline/prompt utility.
Home-page: https://github.com/powerline/powerline
Author: Kim Silkebaekken
Author-email: kim.silkebaekken+vim@gmail.com
License: MIT
Location: /usr/local/lib/python2.7/dist-packages
Requires: 

```

The user Powerline config will be merged to the general one. To change theme 
to one that will display git info:
```
$ mkdir -p ~/.config/powerline
$ cat <<-'EOF' > ~/.config/powerline/config.json
  {
     "ext": {
     "shell": {
        "theme": "default_leftonly"
        }
     }
  }
  EOF

$ powerline-daemon --replace
``` 
#### Font Installation:
In Ubuntu one can install the fonts: `$ sudo apt-get install fonts-powerline`.
If this will not work after rebooting and 
[changing the terminal config](https://askubuntu.com/questions/283830/how-to-change-the-font-of-various-terminal-emulators),
you can try one of the following methods.

Powerline provides two ways of installing the required fonts. If you're using
one of following terminal: Gnome Terminal, Konsole, lxterminal, st, Xfce 
Terminal, Terminator, Guake, Yakuake then you should use "Fontconfig" method.

* Fontconfig: 

  * Per User:
        Run the following commands in terminal:

        wget \
        https://github.com/Lokaltog/powerline/raw/develop/font/PowerlineSymbols.otf \
        https://github.com/Lokaltog/powerline/raw/develop/font/10-powerline-symbols.conf
        mkdir -p ~/.fonts/ && mv PowerlineSymbols.otf ~/.fonts/
        fc-cache -vf ~/.fonts
        mkdir -p ~/.config/fontconfig/conf.d/ && mv 10-powerline-symbols.conf ~/.config/fontconfig/conf.d/

  * System wide:
        Run the following commands in terminal:

        wget \
        https://github.com/Lokaltog/powerline/raw/develop/font/PowerlineSymbols.otf \
        https://github.com/Lokaltog/powerline/raw/develop/font/10-powerline-symbols.conf
        sudo mv PowerlineSymbols.otf /usr/share/fonts/
        sudo fc-cache -vf
        sudo mv 10-powerline-symbols.conf /etc/fonts/conf.d/

* Patched font:

Use this method only if "Fontconfig" method doesn't work for you or you're 
using a terminal other than mentioned above.

   1. Download the font of your choice from powerline-fonts.
   2. Move your patched font to ~/.fonts/ for per user installation or 
   /usr/share/fonts for system wide installation.
   3. Run fc-cache -vf ~/.fonts to update your font cache, sudo fc-cache -vf to
    do it system wide.

To use patched font see this answer and to change the font of your respective
 terminal check this question: [How to change the font of various terminal 
 emulators?](https://askubuntu.com/questions/283830/how-to-change-the-font-of-various-terminal-emulators). You may have to reboot your system after font installation for 
 changes to take effect.

   * ##### Add Powerline to bash:

 Add following lines to your `.bashrc` file which will enable powerline to base shell by default.
```
#powerline
if [ -f `which powerline-daemon` ]; then
	powerline-daemon -q
	POWERLINE_BASH_CONTINUATION=1
	POWERLINE_BASH_SELECT=1
	. /usr/local/lib/python2.7/dist-packages/powerline/bindings/bash/powerline.sh
fi

```
Reload the `.bashrc` file: `$ source ~/.bashrc`

   * ##### Add Powerline to Vim:
Append the following lines to `.vimrc`
```
# vi ~/.vmrc

set  rtp+=/usr/local/lib/python2.7/dist-packages/powerline/bindings/vim/
set laststatus=2
set t_Co=256
```
   * ##### Add Powerline to Tmux:
Tmux is an alternative to screen. It is a terminal emulator with support to 
multi-tab and multi-panes per one session. Add following line to your  `.tmux
.conf` file which will enable powerline to tmux by default. If you don’t 
found `.tmux.conf` file then create a new one.
```
$ vim ~/.tmux.conf
source "/usr/local/lib/python2.7/site-packages/powerline/bindings/tmux/powerline.conf"
``` 
   * #### Add right side git status plugin to Powerline
Follow the instructions from
[here](https://github.com/jaspernbrouwer/powerline-gitstatus)    

To make it active you can run `powerline-config --reload`. If you have any  
errors in your configuration (I actually ran into this when playing with the 
colorscheme setting and used “solorized” instead of “solarized”), you can 
check  it with `powerline-lint`.  

If everything looks fine restart the daemon with `powerline-daemon --replace`.  
# [Gitsome](https://github.com/donnemartin/gitsome#pip-installation)
Gitsome is a nice git shell. To install for python 3.x use: `sudo pip3 
install gitsome` . Than simply commence `gisome` to enter gitsome shell.

# Fish

You need to have powerline-fonts installed. Installation:
Add repo for fish:

```
sudo apt-add-repository ppa:fish-shell/release-2
sudo apt-get update
sudo apt-get install fish
``` 
then install: 
` $ sudo apt-get install fish` 

To config the fish use: `fish_config`
#### Oh-My-Fish
Oh My Fish provides core infrastructure to allow you to install packages 
which extend or modify the look of your shell. It's fast, extensible and 
easy to use.

You can get started right away with the default setup by running this in your
 terminal:

`curl -L https://get.oh-my.fish | fish`

This will download the installer script and start the installation.

Now you can install new themes like [bobthefish](https://github.com/oh-my-fish/theme-bobthefish) 
or agnoster: `omf install bobthefish`

Use `omf list` to see installed packages.  Note: `fish_cinfig` might override
 the omf themes