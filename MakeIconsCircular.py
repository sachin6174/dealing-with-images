from PIL import Image, ImageDraw

# Load the uploaded icon
image_path = "C:/Users/sachinkumar/Desktop/chrome ext/extenxion app/secure-text-chrome-extension/icons/icon128.png"
image = Image.open(image_path)

# Create a circular mask
mask = Image.new("L", image.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)

# Apply the circular mask to the image
circular_image = Image.new("RGBA", image.size)
circular_image.paste(image, (0, 0), mask)

# Resize to match the proportions of the Spotify icon
spotify_icon_size = (96, 96)
circular_image = circular_image.resize(spotify_icon_size, Image.LANCZOS)

# Save the circular icon
circular_icon_path = "C:/Users/sachinkumar/Desktop/chrome ext/extenxion app/secure-text-chrome-extension/icons/circular_spotify_style_icon96.png"
circular_image.save(circular_icon_path)

circular_icon_path
