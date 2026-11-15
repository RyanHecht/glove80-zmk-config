# Glove80 ZMK config

My Glove80 keymap (`config/glove80.keymap`, exported from the MoErgo Layout Editor), built on MoErgo's ZMK (v26.09) plus the [KeyPeek layer notifier](https://github.com/srwi/zmk-keypeek-layer-notifier) for a live layer display.

Every push builds firmware and publishes a Release with both halves' UF2s, a `flash.json` manifest and a [layerview](https://github.com/RyanHecht/layerview) display file.

## Flash

```sh
zmk-uf2-flash --repo RyanHecht/glove80-zmk-config
```

It downloads the latest release, waits for each half's bootloader drive, copies the firmware (skipping a half whose firmware didn't change), and registers the keymap for the layer display.
