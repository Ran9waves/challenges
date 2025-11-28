from rembg import remove
from PIL import Image

input_path = "test.png"
output_path = "test.png"
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
Image.open(output_path)
