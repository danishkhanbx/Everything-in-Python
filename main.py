# part of how to create and run Packages
# Directories and Files related to packages are: packages, main.py, and Packages.py

import package.characters.player
package.characters.player.get_player_info()
#from package.characters import player
#player.get_player_info()
from package.characters.boss import get_boss_info
get_boss_info()