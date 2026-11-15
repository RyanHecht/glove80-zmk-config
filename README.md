# Glove80 ZMK config

My Glove80 keymap, built with GitHub Actions on MoErgo's ZMK (v26.09) plus:

- **ZMK Studio** so tools can read the keymap straight from the keyboard
- **[zmk-raw-hid](https://github.com/zzeneg/zmk-raw-hid)** + **[zmk-keypeek-layer-notifier](https://github.com/srwi/zmk-keypeek-layer-notifier)**, which report the active layers and key presses to the host (the [KeyPeek](https://github.com/srwi/keypeek) protocol)

`config/glove80.keymap` is exported from the MoErgo Layout Editor. Studio's unlock key is on the Magic layer (Magic + H).

## Build & flash

Push, then download the `firmware` artifact from the Actions run. Flash `glove80_lh` to the left half and `glove80_rh` to the right half (MoErgo's [flashing guide](https://docs.moergo.com/glove80-user-guide/customizing-key-layout/)).
