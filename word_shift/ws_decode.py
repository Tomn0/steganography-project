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


if __name__ == "__main__":
    if len(sys.argv) == 1:
        pdf_path = "encoded.pdf"
    else:
        pdf_path = sys.argv[1]

    spacing_values = get_word_spacing(pdf_path)

    # print("spacing values:", spacing_values)

    decoded_str = decode(spacing_values)
    print(f"Decoded message: {decoded_str}")

    # now take only even indexes
    # res_list = spacing_values[1::2]
    # print("Line Spacing Values:", res_list)
    # print("as string:", "".join([str(x) for x in res_list]))

