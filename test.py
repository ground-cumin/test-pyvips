import pyvips
img = pyvips.Image.new_from_array([[-1, -1, -1],
                                    [-1, 16, -1],
                                    [-1, -1, -1]
                                   ], scale=8)
img.write_to_file('x.jpg')
