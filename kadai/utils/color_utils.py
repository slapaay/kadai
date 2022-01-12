import colorsys
from PIL import Image, ImageDraw


def rgb_to_hex(color: tuple) -> str:
    """
    Convert an rgb color to hex.

    Arguments:
        color (list) -- list of red, green, and blue for a color [r, g, b]
    """

    return "#%02x%02x%02x" % (*color,)


def hex_to_rgb(color: str) -> tuple:
    """
    Convert a hex color to rgb.
    Arguments:
        color (string) -- hexadecimal value with the leading '#'
    """

    return tuple(bytes.fromhex(color.strip("#")))


def rgb_to_hsv(color: tuple) -> tuple:
    """
    Converts from rgb to hsv

    Arguments:
        color (list) -- list of red, green, and blue for a color [r, g, b]
    """
    return tuple(colorsys.rgb_to_hsv(*[float(x / 255) for x in color]))


def hsv_to_rgb(color: tuple) -> tuple:
    """
    Converts from hsv to rgb

    Arguments:
        color (list) -- list of hue, saturation, and value for a color [h, s, v]
    """

    color_rgb = [col for col in colorsys.hsv_to_rgb(*color)]
    return tuple([int(col * 255) for col in color_rgb])


def change_hsv_hue(color: tuple, hue: float) -> tuple:
    if hue is None:
        return color
    return (hue, color[1], color[2])


def change_hsv_saturation(color: tuple, saturation: int) -> tuple:
    if saturation is None:
        return color
    return (color[0], saturation, color[2])


def change_hsv_value(color: tuple, value: int) -> tuple:
    if value is None:
        return color
    return (color[0], color[1], value)


def change_rgb_hue(color: tuple, hue: int) -> tuple:
    if hue is None:
        return color
    hsv_color = rgb_to_hsv(color)
    hsv_color = (hue, hsv_color[1], hsv_color[2])
    return hsv_to_rgb(hsv_color)


def change_rgb_value(color: tuple, value: int) -> tuple:
    if value is None:
        return color
    hsv_color = rgb_to_hsv(color)
    hsv_color = (hsv_color[0], hsv_color[1], value)
    return hsv_to_rgb(hsv_color)


def change_rgb_saturation(color: tuple, saturation: int) -> tuple:
    if saturation is None:
        return color
    hsv_color = rgb_to_hsv(color)
    hsv_color = (hsv_color[0], saturation, hsv_color[2])
    return hsv_to_rgb(hsv_color)


def get_rgb_hue(color: tuple) -> int:
    hsv_color = rgb_to_hsv(color)
    return hsv_color[0]