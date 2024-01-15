import fitz  # PyMuPDF
import sys


def get_word_spacing(pdf_path):
    # TODO iterate over all pages, or take the text as a whole (to check if we are not already doing it by taking the whole block)s
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
                    print(f"Span: {span['text']}")
                    if span['text'] == " ":
                        word_spacing.append(span['size'])
                    
    doc.close()

    return word_spacing



if __name__ == "__main__":
    if len(sys.argv) == 1:
        pdf_path = "outpud.pdf"
    else:
        pdf_path = sys.argv[1]

    spacing_values = get_word_spacing(pdf_path)

    print("spacing values:", spacing_values)

    # now take only even indexes
    # res_list = spacing_values[1::2]
    # print("Line Spacing Values:", res_list)
    # print("as string:", "".join([str(x) for x in res_list]))

