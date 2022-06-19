# spacepad

A simple python script that turns a 3Dconnexion SpaceMouse device into a standard Xbox-style gamepad device, using pyspacemouse and vgamepad.

You do not need to install 3Dconnexion's software or drivers to use this script.

This repo also includes hidapi.dll for Windows, from [libusb](https://github.com/libusb/hidapi), under the BSD license detailed in LICENSE-hidapi.md.

# usage

```bash
pip install -r requirements.txt
python main.py
```

# mapping 

The mapping used is a bit quirky, since it was designed to be used with a fork of the [Figma SpaceMouse plugin](https://github.com/brianpeiris/figma-plugin-spacemouse).

| gamepad | spacemouse |
| - | - |
| left thumbstick x | x |
| left thumbstick y | y |
| right thumbstick x | roll |
| right thumbstick y | z |
| left trigger | pitch |
| right trigger | yaw |
