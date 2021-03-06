from PIL import Image


def load_image(filename):
    image = Image.open(filename)
    width, height = image.size
    pixels = list(image.getdata())
    image = [pixels[i:i + width] for i in range(0, len(pixels), width)]
    return image


def save_image(filename, image):
    flat_image = [item for sublist in image for item in sublist]
    height, width = len(image), len(image[0])
    image_out = Image.new("L", (width, height))
    image_out.putdata(flat_image)
    image_out.save(filename)


def color_to_grey(image):
    pass  # implement me!


if __name__ == "__main__":
    in_file = "decision_tree.jpg"
    out_file = "decision_tree_grey.jpg"
    image = load_image(in_file)
    image = color_to_grey(image)
    save_image(out_file, image)


