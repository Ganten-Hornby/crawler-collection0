from PIL import Image
import pytesseract
import base64
import io
import os


# from Base64image import base64_to_Image
def clean_blank_space(string: str):
    return ''.join(string.split())


def OCRbase64(base64encode_string: str, BlankSpace=False):
    img_b64decode = base64.b64decode(base64encode_string)  # base64解码
    image = io.BytesIO(img_b64decode)
    result = pytesseract.image_to_string(Image.open(image))
    if BlankSpace:
        return result.strip()
    else:
        return clean_blank_space(result)


def OCRimage(image_path: str, BlankSpace=False):
    if os.path.exists(image_path):
        result = pytesseract.image_to_string(Image.open(image_path))
        if BlankSpace:
            return result.strip()
        else:
            return clean_blank_space(result)
    else:
        print('not found image path')


if __name__ == '__main__':
    a = OCRbase64(
        'iVBORw0KGgoAAAANSUhEUgAAAMgAAABFCAIAAACAFD7PAAACOklEQVR42u3c0U3DMBSFYQ/AEAzDGDABIzAIm8AjAzFEeENR1SY3jn3PsfP/yhNqRdV+ujataVmIOlR4CghYBCwCFhGwCFgELCJgEbAIWNV9Pf3+Xzyh1ADWmhSwCFg0GixsaXt+e717jbfHApY5KZWwss0FWHN4yrdVTi5trIYDkcq0VbaJ1NniVbcllWZrf2LtWgGWlS2THX0U1gYXVkMTWA1v337z3soWr70VrHxbx2A9EgOs3T5fvu9eDW31uEserLtugFWn6gwv86FVgnsmbLnBMh9a9bBu6GhhvX/83L2GUKWF1clWCNaGNjmsR6S0vNZcOqmqVmIEy9ZWRJXEVlDSSVjOq2E5+lfehq1kWHFVybY6zad+W3gLWIdGmo+qTFv91r4mULxgRWxlvgUfcTPKgigfWnmwIuPHDdaZm40+uqaCFbQlVKWFlbkgnvzcUAzLx9agsG5+rtrCi2HFN+PACo6rrr9xQli7vIDVW1V8aCk/0jm6GubbAlbFKEo+7rfzXzpNjsBfDZZE1cbQkhxQbgwr521SYB2ypT+afH41XN+r34N2hpW/ba+D1fuRFIcJ1MnW1cZVEFbOI5kH1pqO8LNCLaxdW2kPowaWua0rq1oU/5BTCWsxPnbsf65B8rRoSdXAWvwyPy0jhKV9XWb4qkjb833LhZvtO0jl59yBNScsVagCVpIwYBEBi4BFwCICFgGLgEUELAIWAYsIWAQsAhYRsAhYBCwiYBGwCFhEwCJg0XX6A3ZI1/BL5smvAAAAAElFTkSuQmCC')
    print(a)
    b=OCRimage('../v2-45607077bfc108f6ad0a581d7d470293_720w.jpg')
    print(b)
