# CompAutoLevelUP
Tired of not having the doctrins or skins you want to have in "Company of Heroes II"? The solution is simple. Just make a script fighting against a bot that kills him in 5 minutes with the help of a cheat menue (available on the steam workshop). Or just download this python script to avoid doing your own script.

**Installation**

Test if python is installed with ```$python``` in your terminal.

U made shure python is installed, then follow these instructions
```
git clone https://github.com/BlacklightYT/CompAutoLevelUP.git
cd CompAutoLevelUP
pip install -r requirements.txt

```
Now the dependecies are installed and you should be able to run this script
```
python Comp_Makro.py 
```
Now you have to start the script with the requiered keypress
Tab inside the Game and enjoy! <3
For the script to properly work, the Monitor needs to be turned on
This script is far from being perfect, the current issues are:
* We are killing the enemies base with ```misc>kill>15m``` or so, the base spawn in kind of random and it would be more suficient to set the teams1 as winner [didn't think of that in the moment]
* You can only use Nexus as map, since we are dependent on pictures for the input
