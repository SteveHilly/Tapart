from dimensions import raw_dimensions

# init lists for the dimensions
d_length = []
d_width = []
d_height = []

raw_dimensions = raw_dimensions.split("\n")  # split at newline

# Make each combination of dimensions a list in a list
temp_raw = []
for a in raw_dimensions:
    temp_raw.append([a])

# split at x to get the individual dimensions
dimensions = [[x.split("x") for x in l] for l in temp_raw]

for b in dimensions:
    for c in b:
        # add lengths, heights and widths to their own lists and cast to int for multiplication use
        d_length.append(int(c[0]))
        d_width.append(int(c[1]))
        d_height.append(int(c[2]))

# multiply the dimensions that we need with each other
length_width = [a*b for a, b in zip(d_length, d_width)]
height_length = [a*b for a, b in zip(d_height, d_length)]
width_height = [a*b for a, b in zip(d_width, d_height)]


i = 0
while i < len(raw_dimensions):
    # determine smallest side
    smallest_side = length_width[i]
    if height_length[i] < smallest_side:
        smallest_side = height_length[i]
    elif width_height[i] < smallest_side:
        smallest_side = width_height[i]
    # calculate the surface of paper needed
    surface = (2 * length_width[i]) + (2 * width_height[i]) + (2 * height_length[i]) + smallest_side
    # calculate the amount of ribbon needed
    x = d_length[i] + d_length[i] + d_width[i] + d_width[i]
    y = d_length[i] * d_width[i] * d_height[i]
    ribbon = x + y
    # print the output
    print("With dimensions ", raw_dimensions[i], " you need ", surface, " square feet of paper and ", ribbon,
          " feet of ribbon.")
    i += 1














