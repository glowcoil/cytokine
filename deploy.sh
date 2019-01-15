clang cytokine/engine/mesh.c -dynamiclib -o cytokine/engine/mesh.dylib
rsync -r --delete --exclude=.DS_Store --exclude=.git --exclude=*.sh --exclude=*.h --exclude=*.c --exclude=*.cpp cytokine ~/Library/Application\ Support/Blender/2.80/scripts/addons/
