# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
# Copyright (c) 2023 Thimo Rene Pischel
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import qtile
import subprocess


# colors = {
#     "background": '#282a36',
#     "highlight": '#44475a',
#     "focus": '#ffb86c',
#     "normal": {
#         "black": '#21222c',
#         "red": '#ff5555',
#         "green": '#50fa7b',
#         "yellow": '#f1fa8c',
#         "blue": '#bd93f9',
#         "magenta": '#ff79c6',
#         "cyan": '#8be9fd',
#         "white": '#f8f8f2',
#     },
#     "bright": {
#         "black": '#6272a4',
#         "red": '#ff6e6e',
#         "green": '#69ff94',
#         "yellow": '#ffffa5',
#         "blue": '#d6acff',
#         "magenta": '#ff92df',
#         "cyan": '#a4ffff',
#         "white": '#ffffff',
#     }
# }

color = {
    "bg1": "#44475a",
    "bgbs1": "#21222c",
    "bgb1": "#44475a",
    "bgb2": "#31323c",
    "fg1": "#a4ffff",
    "fgh": '#ff6e6e'
}


win = "mod4"
shift = "shift"
alt_l = "mod1"
control = "control"


terminal = guess_terminal()

def kb_default(q):
    subprocess.run("xmodmap /home/thimo/.config/qtile/key_mods/default.xmm", shell=True)

def kb_greek(q):
    subprocess.run("xmodmap /home/thimo/.config/qtile/key_mods/default.xmm && xmodmap /home/thimo/.config/qtile/key_mods/greek.xmm", shell=True)



keys = [
    Key([win], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([win], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([win], "j", lazy.layout.down(), desc="Move focus down"),
    Key([win], "k", lazy.layout.up(), desc="Move focus up"),
    Key([win], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([win, shift], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([win, shift], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([win, shift], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([win, shift], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([win, control], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([win, control], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([win, control], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([win, control], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([win], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key(
        [win, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    #qtile key that has the modifier win and the key d that triggers the method kb_default äääααα
    


    Key([win], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([win], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([win], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([win, control], "r", lazy.reload_config(), desc="Reload the config"),
    Key([win, control], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([win], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    Key([win], 'o', lazy.run_extension(extension.DmenuRun(
        dmenu_prompt="M",
        dmenu_font="sans",
        background=color['bg1'],
        foreground=color['fg1'],
        selected_background=color["bg1"],
        selected_foreground=color['fgh']
    ))),

    Key([win], "f", lazy.spawn("thunar"), desc="FileExplorer"),
    Key([win], "d", lazy.spawn("thunar Downloads/"), desc="FileExplorer"),
    Key([win], "c", lazy.spawn("code"), desc="vsCode"),
    Key([win], "g", lazy.spawn("firefox-developer-edition mail.google.com"), desc="gmail"),

    KeyChord([win], "b", [
        Key([], "c", lazy.spawn("chromium"), desc="Chromium"),
        Key([], "g", lazy.spawn("google-chrome-stable"), desc="Google-Chrome"),
        KeyChord([], "f", [
            Key([], "s", lazy.spawn("firefox"), lazy.ungrab_chord(), desc="Firefox-stable"),
            Key([], "d", lazy.spawn("firefox-developer-edition"), lazy.ungrab_chord(), desc="Firefox-devel")
        ], name="Firefox [s/d]", mode=False),
        KeyChord([], "e", [
            Key([], "s", lazy.spawn("microsoft-edge-stable"), lazy.ungrab_chord(), desc="Edge-stable"),
            Key([], "d", lazy.spawn("microsoft-edge-dev"), lazy.ungrab_chord(), desc="Edge-devel")
        ], name="Edge [s/d]", mode=False),   
    ], name="Browser-Selection [c/g/f/e]", mode=False),

    KeyChord([win], "m", [
        Key([], "d", lazy.function(kb_default)),
        Key([], "g", lazy.function(kb_greek))
    ], name="Keyboard-Selection [d/g]", mode=False)
]
#
groups = [Group(i) for i in "123456789"]

layout_theme = {
    "margin": 0,
    "border_width": 1,
    "border_focus": color["fgh"],
    "border_normal": color["bg1"]
}

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [win],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [win, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(**layout_theme),
    # layout.Max(**layout_theme),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(**layout_theme),
    # layout.Matrix(**layout_theme),
    # layout.MonadTall(**layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(**layout_theme),
    # layout.TreeTab(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme),
]

widget_defaults = dict(
    font="sans",
    fontsize=13,
    padding=4,
)
extension_defaults = widget_defaults.copy()

# Mouse Callbacks #
def open_htop():
    qtile.cmd_spawn("alacritty -e htop")


screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.Prompt(
                    background=color["bg1"],
                    foreground=color["fg1"]
                ),
                widget.CurrentScreen(
                    background=color["bg1"],
                    foreground=color["fg1"]
                ),
                widget.Spacer(
                    length=2,
                    background=color["bgbs1"]
                ),
                widget.GroupBox(
                    background=color["bgb1"],
                    foreground=color["fg1"],
                    rounded=False,
                    inactive=color["bgb1"],
                    active=color["fg1"],
                    borderwidth=2,
                    block_highlight_text_color=color["fgh"]
                ),
                widget.Spacer(
                    length=2,
                    background=color["bgbs1"]
                ),
                widget.Chord(

                ),
                widget.Notify(
                    background=color["bgb2"],
                    foreground=color["fgh"]
                ),


                widget.Spacer(),



                widget.Spacer(
                    length=2,
                    background=color["bgbs1"]
                ),
                widget.TextBox(
                    text="Network",
                    mouse_callbacks={'Button1': lazy.spawn("nm-connection-editor")},
                    background=color["bgb1"],
                    foreground=color["fg1"]
                ),
                widget.Net(
                    mouse_callbacks={'Button1': lazy.spawn("nm-connection-editor")},
                    background=color["bgb1"],
                    foreground=color["fg1"]
                ),
                widget.Wlan(
                    interface="wlp4s0",
                    mouse_callbacks={'Button1': lazy.spawn("nm-connection-editor")},
                    background=color["bgb1"],
                    foreground=color["fg1"]
                ),
                widget.Spacer(
                    length=2,
                    background=color["bgbs1"]
                ),
                widget.CPU(
                    mouse_callbacks={'Button1': open_htop},
                    background=color["bgb2"],
                    foreground=color["fg1"]
                ),
                widget.Spacer(
                    length=2,
                    background=color["bgbs1"]
                ),
                widget.TextBox(
                    text="Mem",
                    mouse_callbacks={'Button1': open_htop},
                    background=color["bgb1"],
                    foreground=color["fg1"]
                ),
                widget.Memory(
                    mouse_callbacks={'Button1': open_htop},
                    background=color["bgb1"],
                    foreground=color["fg1"]
                ),
                widget.Spacer(
                    length=2,
                    background=color["bgbs1"]
                ),
                widget.TextBox(
                    text="Disk",
                    background=color["bgb2"],
                    foreground=color["fg1"]
                ),
                widget.DF(
                    visible_on_warn=False,
                    background=color["bgb2"],
                    foreground=color["fg1"]
                ),
                widget.Spacer(
                    length=2,
                    background=color["bgbs1"]
                ),
                widget.TextBox(
                    text="Battery",
                    background=color["bgb1"],
                    foreground=color["fg1"]
                ),
                widget.Battery(
                    background=color["bgb1"],
                    foreground=color["fg1"]
                ),
                widget.Spacer(
                    length=2,
                    background=color["bgbs1"]
                ),
                widget.TextBox(
                    text="Vol",
                    background=color["bgb2"],
                    foreground=color["fg1"]
                    ),
                widget.Volume(
                    background=color["bgb2"],
                    foreground=color["fg1"]
                ),
                widget.Spacer(
                    length=2,
                    background=color["bgbs1"]
                ),
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p",
                    background=color["bgb1"],
                    foreground=color["fg1"]
                ) 
            ],
            24,
            background=color["bg1"],
            border_width=[1, 0, 0, 0],  # Draw top and bottom borders
            border_color=[color["bgbs1"], color["bgbs1"], color["bgbs1"], color["bgbs1"]],
        ),
        
        wallpaper='~/Pictures/wallpaper.png',
        wallpaper_mode='stretch',
    ),
]

# Drag floating layouts.
mouse = [
    Drag([win], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([win], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([win], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


