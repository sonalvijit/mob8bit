from PIL import Image, ImageDraw

def create_grid_image(width=800, height=600, grid_size=50, line_color=(0, 0, 0), bg_color=(255, 255, 255)):
    """
    Create an image with a grid pattern.

    :param width: Width of the image
    :param height: Height of the image
    :param grid_size: Distance between grid lines
    :param line_color: Color of grid lines (R, G, B)
    :param bg_color: Background color (R, G, B)
    """
    # Create a blank image
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Draw vertical lines
    for x in range(0, width, grid_size):
        draw.line([(x, 0), (x, height)], fill=line_color, width=1)

    # Draw horizontal lines
    for y in range(0, height, grid_size):
        draw.line([(0, y), (width, y)], fill=line_color, width=1)

    return img


if __name__ == "__main__":
    img = create_grid_image(width=800, height=600, grid_size=50)
    img.save("./helper/grid_image.jpg")
    img.show()
