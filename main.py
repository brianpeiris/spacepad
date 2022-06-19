import pyspacemouse
import vgamepad

def fmap(v, a=-1, b=1, c=0, d=1):
    return (v - a) / (b - a) * (d - c) + c;

def clamp(v, a=-1, b=1):
    return min(max(v, a), b)

if pyspacemouse.open():
    gp = vgamepad.VX360Gamepad()
    gp.update()

    while 1:
        state = pyspacemouse.read()

        gp.left_joystick_float(
            x_value_float=clamp(state.x),
            y_value_float=clamp(state.y),
        )
        gp.right_joystick_float(
            x_value_float=clamp(state.roll),
            y_value_float=(-1 * clamp(state.z)),
        )
        gp.left_trigger_float(
            value_float=fmap(clamp(state.pitch)),
        )
        gp.right_trigger_float(
            value_float=fmap(clamp(state.yaw)),
        )

        gp.update()
