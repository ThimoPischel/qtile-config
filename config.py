# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
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
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import qtile


import subprocess


color = {
    "background": '#282a36',
    "highlight": '#44475a',
    "focus": '#ffb86c',
    "normal": {
        "black": '#21222c',
        "red": '#ff5555',
        "green": '#50fa7b',
        "yellow": '#f1fa8c',
        "blue": '#bd93f9',
        "magenta": '#ff79c6',
        "cyan": '#8be9fd',
        "white": '#f8f8f2',
    },
    "bright": {
        "black": '#6272a4',
        "red": '#ff6e6e',
        "green": '#69ff94',
        "yellow": '#ffffa5',
        "blue": '#d6acff',
        "magenta": '#ff92df',
        "cyan": '#a4ffff',
        "white": '#ffffff',
    }
}

mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], 'o', lazy.run_extension(extension.DmenuRun(
        dmenu_prompt="M",
        dmenu_font="sans",
        background=color["highlight"],
        foreground=color["normal"]["cyan"],
        selected_background=color["highlight"],
        selected_foreground=color["focus"],
    ))),
    #apps
    Key([mod], "b", lazy.spawn("firefox-developer-edition"), desc="Firefox"),
    Key([mod], "f", lazy.spawn("alacritty -e mc"), desc="FileExplorer"),
    Key([mod], "c", lazy.spawn("code"), desc="vsCode"),
    Key([mod], "g", lazy.spawn("firefox-developer-edition mail.google.com"), desc="gmail"),
]

groups = [Group(i) for i in "123456789"]

layout_theme = {
    "margin": 0,
    "border_width": 2,
    "border_focus": color["focus"],
    "border_normal": color["bright"]["cyan"]
}

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
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
        top=bar.Bar(
            [
                widget.Prompt(
                    background=color["bright"]["red"],
                    foreground=color["normal"]["black"]
                    ),
                widget.CurrentScreen(
                    background=color["background"],
                    foreground=color["normal"]["black"]
                ),
                widget.GroupBox(
                    background=color["bright"]["cyan"],
                    foreground=color["normal"]["black"],
                    rounded=False,
                    inactive=color["normal"]["white"],
                    active=color["normal"]["blue"],
                    borderwidth=2,
                    block_highlight_text_color=color["normal"]["black"]
                ),
                widget.Notify(
                    background=color["normal"]["red"],
                    foreground=color["normal"]["black"]
                ),
                widget.Spacer(),
                widget.TextBox(
                    text="Network",
                    mouse_callbacks={'Button1': lazy.spawn("nm-connection-editor")},
                    background=color["bright"]["blue"],
                    foreground=color["normal"]["black"]
                    ),
                widget.Net(
                    mouse_callbacks={'Button1': lazy.spawn("nm-connection-editor")},
                    background=color["bright"]["blue"],
                    foreground=color["normal"]["black"]
                    ),
                widget.Wlan(
                    interface="wlp4s0",
                    mouse_callbacks={'Button1': lazy.spawn("nm-connection-editor")},
                    background=color["bright"]["blue"],
                    foreground=color["normal"]["black"]
                    ),
                widget.CPU(
                    mouse_callbacks={'Button1': open_htop},
                    background=color["bright"]["green"],
                    foreground=color["normal"]["black"]

                    ),
                widget.TextBox(
                    text="Mem",
                    mouse_callbacks={'Button1': open_htop},
                    background=color["bright"]["blue"],
                    foreground=color["normal"]["black"]
                    ),
                widget.Memory(
                    mouse_callbacks={'Button1': open_htop},
                    background=color["bright"]["blue"],
                    foreground=color["normal"]["black"]
                    ),
                widget.TextBox(
                    text="Disk",
                    background=color["bright"]["green"],
                    foreground=color["normal"]["black"]
                    ),
                widget.DF(
                    visible_on_warn=False,
                    background=color["bright"]["green"],
                    foreground=color["normal"]["black"]
                    ),
                widget.TextBox(
                    text="Battery",
                    background=color["bright"]["blue"],
                    foreground=color["normal"]["black"]
                    ),
                widget.Battery(
                    background=color["bright"]["blue"],
                    foreground=color["normal"]["black"]
                ),
                widget.TextBox(
                    text="Vol",
                    background=color["bright"]["green"],
                    foreground=color["normal"]["black"]
                    ),
                widget.Volume(
                    background=color["bright"]["green"],
                    foreground=color["normal"]["black"]
                ),
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p",
                    background=color["bright"]["blue"],
                    foreground=color["normal"]["black"]
                    ),
            ],
            24,
            background=color["background"],
            border_width=[0, 0, 2, 0],  # Draw top and bottom borders
            border_color=[color["bright"]["cyan"], color["bright"]["cyan"], color["bright"]["cyan"], color["bright"]["cyan"]],
        ),
        wallpaper='~/Pictures/wallpaper.png',
        wallpaper_mode='stretch',
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
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


