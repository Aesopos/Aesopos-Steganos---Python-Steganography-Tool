from PIL import Image

def dtl():
    print("\nselect delimiter type:")
    print("1. binary")
    print("2. text (not stealth at all!)")

    while True:
        choice = input("1 or 2?: ")
        if choice == '1':
            print("\ngood choice! now choose the length range:")
            print("1. short (8-16 bits) - fast, not so stealthy")
            print("2. medium (16-32 bits) - balanced")
            print("3. long (32+ bits) - super stealth, much slower")

            while True:
                lench = input("choose 1 or 2 or 3: ")
                if lench == '1':
                    return "binary", None, 8
                elif lench == '2':
                    return "binary", None, 16
                elif lench == '3':
                    return "binary", None, 32
                else:
                    print("gotta play according to the rules! INVALID CHOICE!")
        elif choice == '2':
            print("\nman...you are making it easy to detect your message... but okay, you decide.")
            custom_text = input("go on, write your delimiter: ")
            return "text", custom_text, None
        else:
            print("gotta play according to the rules! INVALID CHOICE!")

def convtobin(text):
    return ''.join(format(ord(c), '08b') for c in text)

def convtotext(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

def encod(image_path, message, delimiter, custom_text=None):
    binmessage = convtobin(message)

    if delimiter == "binary":
        if custom_text is not None:
            print("error: custom_text should be None for binary delimiter.")
            return
        binmessage += '00000000'  # Default binary delimiter
    elif delimiter == "text":
        if custom_text is None:
            print("error: custom_text must be provided for text delimiter.")
            return
        binmessage += convtobin(custom_text)

    image = Image.open(image_path)
    pixels = image.load()

    if len(binmessage) > image.width * image.height * 3:
        raise ValueError("\nare u trying to write a book in a napkin? choose a bigger image for your text!")

    idx = 0
    for y in range(image.height):
        for x in range(image.width):
            pixel = list(pixels[x, y])

            for i in range(3):
                if idx < len(binmessage):
                    pixel[i] = (pixel[i] & 0b11111110) | int(binmessage[idx])
                    idx += 1

            pixels[x, y] = tuple(pixel)

    while True:
        encodedimgpath = input("\nenter the name for the output image (include the extension): ")
        try:
            image.save(encodedimgpath)
            print(f"\nwe saved your secret as {encodedimgpath}")
            break
        except Exception as e:
            print(f"ops... some problem saving the file!: {e}. try again.")

image_path = input("enter the image file path: ")
message = input("enter the message to hide: ")

delimiter_type, custom_text, _ = dtl()

encod(image_path, message, delimiter_type, custom_text)
