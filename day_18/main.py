from colorgram import extract

rgb_colors = []
colors = extract('image.jpg', 84)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)
