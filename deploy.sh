export C_INCLUDE_PATH=/Users/micah/.pyenv/versions/3.7.1/include/python3.7m/
/Applications/blender-2.80.0-git20181129.8850875866a-x86_64/blender.app/Contents/Resources/2.80/python/bin/python3.7m setup.py build_ext --inplace
rsync -r --delete --exclude=.DS_Store --exclude=.git --exclude=*.sh --exclude=*.h --exclude=*.c --exclude=*.cpp cytokine ~/Library/Application\ Support/Blender/2.80/scripts/addons/
