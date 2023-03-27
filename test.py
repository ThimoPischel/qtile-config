import subprocess

#subprocess.run(["xmodmap ~/.config/qtile/key_mods/default.xmm && xmodmap ~/.config/qtile/key_mods/greek.xmm"], shell=True)

subprocess.run(["xmodmap /home/thimo/.config/qtile/key_mods/default.xmm"], shell=True)