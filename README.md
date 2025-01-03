Steganos: Image-based Steganography (Encoding & Decoding)

This project implements a basic steganography technique to hide and extract secret messages within images using Python. The user can choose between two delimiter types (binary or text) for encoding the message, and later decode the hidden message from the image.

Features

- Binary Delimiter: Embeds the message using binary format with customizable bit lengths (8, 16, or 32).
- Text Delimiter: Allows you to use a custom text delimiter to hide your message.
- Image Encoding & Decoding: The message can be embedded into an image and later extracted from it.

Requirements

- Python 3.x
- Pillow library for image processing

To install the required library, run:

bash
pip install Pillow

Usage

Step 1: Encode a Message in an Image

1. Run the Encoding Script: Start the script and provide the following inputs:
    - Image File Path: The path to the image where you want to hide the message.
    - Message: The secret message you want to hide in the image.
    - Delimiter Type: Choose between binary or text delimiter.
        - Binary: You will then choose a bit length (8, 16, or 32).
        - Text: You will input a custom delimiter text.
   
2. Save the Encoded Image: The script will ask you for the output image name (including the extension). The encoded image will be saved with the secret message hidden inside.

Step 2: Decode the Message from the Image

1. Run the Decoding Script: To extract the hidden message, provide the following:
    - Encoded Image Path: The path to the image containing the hidden message.
    - Delimiter Type: Choose the delimiter used during encoding (binary or text).
    - For Binary: You will need to specify the delimiter length (8, 16, or 32).
    - For Text: You will need to provide the custom delimiter text.

2. Get the Decoded Message: The script will display the hidden message extracted from the image.

How It Works

1. Message Encoding:
   - The message is converted into a binary string using the `convtobin` function.
   - The delimiter (binary or text) is appended to mark the end of the message.
   - The image pixels are modified by changing the least significant bit of each color channel (RGB) to embed the message.

2. Message Decoding:
   - The binary string is extracted from the image by reading the least significant bits of the pixel values.
   - The delimiter is used to determine where the message ends, and the binary string is converted back into text.

3. Saving and Loading Images:
   - Once the message is embedded, the image is saved with the hidden message.
   - For decoding, the image is loaded, and the message is extracted and displayed.

Notes

- The script will check if the image is large enough to fit the message. If not, you will be prompted to choose a larger image.
- The text delimiter method is less stealthy and can be easily detected, so it's recommended to use the binary method for better security.
- The binary delimiter requires specifying a length (8, 16, or 32 bits) to ensure the message is correctly extracted.

License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
