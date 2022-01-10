import base64


def pngimagefile_to_base64(filepath):
    with open(filepath, 'rb') as image:
        image_read = image.read()
    base64_encoded = base64.b64encode(image_read).decode('utf-8')
    return base64_encoded


def convert_markdown_image_tag(filepath, base64_encoded):
    filepath = filepath.replace('image/', '')
    image_tag = '![' + filepath + '](' + 'data:image/png;base64,' + base64_encoded + ')'''


    return image_tag
