from PIL import Image

def convtobin(text):
    return ''.join(format(ord(c), '08b') for c in text)

def convtotext(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

def dtl():
    print("\nselect delimiter type:")
    print("1. binary")
    print("2. text")

    while True:
        choice = input("1 or 2?: ")
        if choice == '1':
            return "binary", None
        elif choice == '2':
            custom_text = input("enter your text delimiter: ")
            return "text", custom_text
        else:
            print("INVALID CHOICE! Choose 1 or 2.")

def decoded(image_path, delimiter, custom_text=None, dllen=None):
    image = Image.open(image_path)
    pixels = image.load()

    binmessage = ""

    for y in range(image.height):
        for x in range(image.width):
            pixel = pixels[x, y]
            for i in range(3):
                binmessage += str(pixel[i] & 1)

    if delimiter == "binary":
        if dllen is None:
            raise ValueError("you must specify a length.")
        delimiter = "0" * dllen
    elif delimiter == "text":
        if custom_text is None:
            raise ValueError("you must provide the text.")
        delimiter = ''.join(format(ord(c), '08b') for c in custom_text)
    else:
        raise ValueError("invalid delimiter type.")

    endindex = binmessage.find(delimiter)
    if endindex == -1:
        raise ValueError("delimiter not found in the image.")

    binmessage = binmessage[:endindex]
    message = convtotext(binmessage)
    return message

image_path = input("enter the encoded image path: ")
dtl_type, custom_text = dtl()

if dtl_type == "binary":
    dllen = int(input("enter the delimiter length (8, 16, or 32): "))
else:
    dllen = None

decoded_message = decoded(image_path, dtl_type, custom_text, dllen)
print("\ndecoded message:", decoded_message)
