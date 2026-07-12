from PIL import Image

img_path = '/home/edisones/.gemini/antigravity-ide/brain/0d87b3c6-1439-4ee9-8232-860f9c657b8c/mrz_signature_logo_1783648336869.png'
out_path = '/home/edisones/Documents/author-page/modern-site/images/author/mrz-logo.png'

img = Image.open(img_path).convert('L')

# Stronger curve to eliminate the AI-generated vignette background
def process_pixel(p):
    if p < 120:
        return 0 # pure transparent
    elif p > 220:
        return 255 # pure opaque white
    else:
        return int(((p - 120) / 100) * 255)

img = img.point(process_pixel)

white = Image.new('RGBA', img.size, (255, 255, 255, 255))
white.putalpha(img)

bbox = white.getbbox()
if bbox:
    white = white.crop(bbox)

white.save(out_path)
print("Saved perfect transparency logo")
