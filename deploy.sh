export C_INCLUDE_PATH=/System/Library/Frameworks/Python.framework/Headers
/Applications/blender-2.79.0-git20170809.f2728939df3-x86_64/blender.app/Contents/Resources/2.79/python/bin/python3.5m setup.py build_ext
rsync -r --delete --exclude=.DS_Store --exclude=.git --exclude=*.sh --exclude=*.c cytokine ~/Library/Application\ Support/Blender/2.79/scripts/addons/
