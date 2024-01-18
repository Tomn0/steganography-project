import fitz  # PyMuPDF
import sys


def get_word_spacing(pdf_path):
    doc = fitz.open(pdf_path)

    page = doc[0]
    text_blocks = page.get_text("dict")

    word_spacing = []

    for page_number in range(doc.page_count):
        page = doc[page_number]

        text_blocks = page.get_text("dict")

        # text_blocks['blocks'][1]['lines'][0]['spans'][0]['size'] -> check for sizes
        # text_blocks['blocks'][1]['lines'][0]['spans'][0]['size'] -> check for spaces

        for block in text_blocks['blocks']:
            for line in block['lines']:
                for span in line['spans']:
                    # print(f"Span: {span['text']}")
                    # if '\u00A0' in span['text']:
                    #     print("nbsp found!!!")
                    #     word_spacing.append(span['size'])
                    if span['text'] == " ":
                        word_spacing.append(span['size'])
                    
    doc.close()

    return word_spacing

def decode(word_spacing):
    decoded_string = ""
    zero = min(word_spacing)
    one = max(word_spacing)
    for space in word_spacing:
        if space < one:
            decoded_string += "0"
        elif space == one:
            decoded_string += "1"

    return decoded_string
