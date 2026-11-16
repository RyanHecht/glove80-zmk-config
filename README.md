# Glove80 ZMK config

My Glove80 keymap (`config/glove80.keymap`): [TailorKey 5.2](https://sites.google.com/view/tailorkey/moergo/glove80) (Windows/Linux, home row mods) with these changes: symmetric thumb clusters (Enter / Ctrl / Super on the upper row and Space / Shift on the lower row of both hands; left Space holds Cursor, right Space holds Symbol, left Enter holds Lower, right Enter holds Mouse; Backspace on the left outer key, Dictate (Super+Alt+Space) on the right), combos that clashed with modifier chords removed (both Shifts = Caps Word), and per-key LEDs for Gaming/Typing/Autoshift. Exported from the MoErgo Layout Editor,, built on MoErgo's ZMK (v26.09) plus the [KeyPeek layer notifier](https://github.com/srwi/zmk-keypeek-layer-notifier) for a live layer display.

Every push builds firmware and publishes a Release with both halves' UF2s, a `flash.json` manifest and a [layerview](https://github.com/RyanHecht/layerview) display file.

## Flash

```sh
zmk-uf2-flash --repo RyanHecht/glove80-zmk-config
```

It downloads the latest release, waits for each half's bootloader drive, copies the firmware (skipping a half whose firmware didn't change), and registers the keymap for the layer display.
