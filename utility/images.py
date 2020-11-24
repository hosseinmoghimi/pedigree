import base64


def imagebase64(image_field):
    if image_field and image_field is not None:
        with open(image_field.path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        return encoded_string
    return None
