from PIL import Image, ImageDraw
import random

DIV_MODIFIER = 16
NUM_CIRCLES = 30

def generate_circles(num, radius, size):
    ret = []
    for i in range(num):
        x = random.randint(radius, size - radius)
        y = random.randint(radius, size - radius)
        ret.append((x - radius, y - radius, x + radius, y + radius))

    return ret

def draw_rorschach(draw, circle, size):
    (x0, y0, x1, y1) = circle
    draw.ellipse(circle, fill = 0)
    draw.ellipse((size - x1, y0, size - x0, y1), fill = 0)

def create_rorschach_image(size):
    im = Image.new('1', (size, size), "white")
    draw = ImageDraw.Draw(im)

    radius = size / DIV_MODIFIER
    circles = generate_circles(NUM_CIRCLES, radius, size)
    for c in circles:
        draw_rorschach(draw, c, size)
    del draw

    return im

if __name__ == '__main__':
    im = create_rorschach_image(500)
    im.save('test.png', 'PNG')
