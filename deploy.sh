export C_INCLUDE_PATH=/System/Library/Frameworks/Python.framework/Headers
python setup.py build_ext
rsync -r --delete --exclude=.DS_Store --exclude=.git --exclude=*.sh --exclude=*.c cytokine ~/Library/Application\ Support/Blender/2.80/scripts/addons/
