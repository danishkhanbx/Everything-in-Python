# Python Packages
# A package is a directory containing multiple modules and other sub-packages.
# Suppose we are developing a package with multiple objects, so it may have these different modules.
# 1. player.py
# 2. oss.py
# 3. gun.py
# 4. knife.py
# Since these modules are in the same location, they look cluttered. We can structure them in this way:
# 1. package
# a. characters
# a.1. player.py
# a.2. boss.py
# b. weapons
# b.1. gun.py
# b.2. knife.py
# Here, the similar player and boss modules are kept under the characters package.
# Also, gun and knife modules are kept inside the weapons package.
# Then, both characters and weapons packages are kept inside the main package package.
# As you can see, our project looks much more organized and structured with the use of packages.

# Create a directory named package that will contain all our package components.
# We also need to create an __init__.py file inside package directory.
# This special file tells Python that this directory is a Python package.
# Also create the characters package with an __init__.py file.
# Now, create player.py and boss.py modules inside characters package.
# In player.py:
def get_player_info():
     print("I am the main player.")
# In boss.py:
def get_boss_info():
    print("I am the enemy player.")
# While developing large programs, these modules might contain classes and multiple functions.

# Let's create a main.py file outside package package.
# I can now import and use them in the following ways:
import package.characters.player
package.character.player.get_player_info()
# OR
from package.characters import player
player.get_player_info()
# Output: I am the main player.
from package.characters.boss import get_boss_info
get_boss_info()
# Output: I am the enemy player.

# Using __init__.py
# The code inside __init__.py runs automatically when we import the package.
# Let's add a print statement in this file inside the package package.
print("Initializing package features")
# When we run this code:
from package.characters import player
from package.characters.boss import get_boss_info
player.get_player_info()
get_boss_info()
