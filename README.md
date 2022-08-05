# budgie-window-preview-custom-shortcut

____

:brazil:

Esta aplicação foi criada para suprir uma necessidade muito especíca minha, no D.E Budgie desktop a unica forma de navegar entre os previews de janelas no menu `ALT + TAB` é só apertando o `TAB` ou `SHIFT + TAB` várias vezes para chegar onde precisa, o que eu fiz foi criar esse script para conseguir também usar as setas `RIGHT` ou `LEFT`

:us:

This application was developed to fufill a very specific need of mine, by default the Budgie D.E only works with the `ALT + TAB` or`ALT + SHIFT + TAB` to navigate beteween the window previews on the window switcher, but i wanted to use the Left and the Right arrow keys to do the same thing, so, i developed this python script that does exactly that

It is working 100%, i've not tested on other computers but the script is so simple that it should work out-of-the-box, there is only one dependencie that needs to be installed using `pip`, wich is `pynput` 

> [pynput Package Documentation &#8212; pynput 1.7.6 documentation](https://pynput.readthedocs.io/en/latest/index.html):

```shell
pip install pynput
```

* `pynput` is used to handle the keyboard events.

* This does not check for any keys other than the Left and Right arrows.

## Instalation

To download this you can download the **.zip** file, or clone the repository with `git`

[Download .zip](https://github.com/lneute/budgie-window-preview-custom-shortcut/archive/refs/heads/master.zip)

`wget` alternative:

```shell
cd ~/Downloads
wget https://github.com/lneute/budgie-window-preview-custom-shortcut/archive/refs/heads/master.zip
unzip master.zip
```

Or, clone using `git`

```shell
mkdir ~/.budgie-desktop-custom-shortcut
cd ~/.budgie-desktop-custom-shortcut
git clone https://github.com/lneute/budgie-window-preview-custom-shortcut.git
```

There is no need to compile this script, just give the permission to be executed and set it to start with your system

To give permission of exection:

```shell
cd ./budgie-window-preview-custom-shortcut
chmod +x budgie-window-preview-shortcut-deamon.py
```

Now you have to setup the script to run on system boot:

1. Using `budgie-desktop-settings`  go to **Autostart**, then, click on the **+** (Plus) sign
    ![](/home/neute/Code/Python/budgie-window-preview-custom-shortcut/.img/step1.png)

2. On the context menu, click on "**Add Command**"
   
   ![](/home/neute/Code/Python/budgie-window-preview-custom-shortcut/.img/step2.png)

3. On the dialog box enter the required fields, the *Title* and the *Name* can be watherever you want, only the *Command* field is important, fill it accordingly
   
   ![](/home/neute/Code/Python/budgie-window-preview-custom-shortcut/.img/step3.png)
   
   E.g: on my computer it is set like this: `python ~/Code/Python/budgie-window-preview-custom-shortcut -n`, just set the correct location of the script wherever you've saved it.

    Done!, now on the system startup the script will be up and running.

## Usage

##### Options:

* `-h, --help`, If running from a terminal wil display a help message

* `-d path_to_dir`, Set custom location for the 'triggers' directory

* `-n`, Enable toasty notification on startup

> If you use the `-d`flag the trigger files will be stored on the folder you defined, if the folder don't exists the fallback dir is `~/.triggers-budgie`



I think that's it, feel free to reach out if you need anything!
