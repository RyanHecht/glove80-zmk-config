#!/usr/bin/env python3
"""Keep layer_GameSuper an exact copy of the base layer (HRM_WinLinx).

GameSuper is what you get while holding Super in Gaming: the normal layout, so
Super shortcuts type as usual. ZMK can't reference another layer, so it's a copy;
re-run this after changing the base layer:

    python3 tools/sync_game_super.py config/glove80.keymap
"""
import sys

path = sys.argv[1]
s = open(path, encoding="utf-8").read()
i = s.index("layer_HRM_WinLinx {")
base = s[s.index("bindings = <", i): s.index(">;", i) + 2]
block = ("        // Normal layout while holding Super in Gaming. GENERATED copy of layer_HRM_WinLinx:\n"
         "        // run tools/sync_game_super.py after changing the base layer.\n"
         "        layer_GameSuper {\n            " + base + "\n        };")
if "layer_GameSuper {" in s:
    a = s.index("        // Normal layout while holding Super in Gaming.")
    b = s.index("};", s.index(">;", s.index("layer_GameSuper {"))) + 2
    s = s[:a] + block + s[b:]
else:
    j = s.index("layer_GameChat {")
    end = s.index("};", s.index(">;", j)) + 2
    s = s[:end] + "\n\n" + block + s[end:]
open(path, "w", encoding="utf-8").write(s)
print("layer_GameSuper synced from layer_HRM_WinLinx")
