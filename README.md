# spacepad

A simple python script that turns a 3Dconnexion SpaceMouse device into a standard Xbox-style gamepad device, using pyspacemouse and vgamepad.

You do not need to install 3Dconnexion's software or drivers to use this script.

The mapping used is a bit quirky, since it was designed to be used with a fork of the [Figma SpaceMouse plugin](https://github.com/brianpeiris/figma-plugin-spacemouse).

| gamepad | spacemouse |
| - | - |
| left thumbstick x | spacemouse x |
| left thumbstick y | spacemouse y |
| right thumbstick x | spacemouse roll |
| right thumbstick y | spacemouse z |
| left trigger | spacemouse pitch |
| right trigger | spacemouse yaw |

This repo also includes hidapi.dll for Windows, from [libusb](https://github.com/libusb/hidapi), under the BSD license detailed in LICENSE-hidapi.md.

# usage

```bash
pip install -r requirements.txt
python main.py
```
