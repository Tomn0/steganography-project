import fitz  # PyMuPDF
import sys

def get_line_spacing(pdf_path):
    # TODO iterate over all pages, or take the text as a whole (to check if we are not already doing it by taking the whole block)s
    doc = fitz.open(pdf_path)
    line_spacing = []
    for page_number in range(doc.page_count):
        page = doc[page_number]

        text_blocks = page.get_text("dict")
        # extract blocks:
        # iterate over all text blocks and merge all lines together:
        lines = []
        for block in text_blocks['blocks']:
            for block_line in block['lines']:
                lines.append(block_line)
        
        # FIXME: this is hardcoded!! very bad and stupid, but works :)
        start_of_the_page = (50.0, 50.0)        # modify accordingly if the margin is changed
        
        # get first line
        prev_line = lines[0]
        prev_origin = prev_line['spans'][0]['origin']
        distance = abs(start_of_the_page[1] - prev_origin[1])
        # print("\n\nNew page")
        # print(distance)
        if distance == 13:
            line_spacing.append(0)
        else:
            line_spacing.append(1)

        for line in lines[1:]:
            # get coordinates
            origin = line['spans'][0]['origin']
            prev_origin = prev_line['spans'][0]['origin']

            # compare distance to previous line
            distance = abs(origin[1] - prev_origin[1])

            # FIXME: again - hardcoded distance
            if distance == 13:
                line_spacing.append(0)
            else:
                line_spacing.append(1)
            prev_line = line
                
    doc.close()

    return line_spacing



if __name__ == "__main__":
    if len(sys.argv) == 1:
        pdf_path = "encoded.pdf"
    else:
        pdf_path = sys.argv[1]

    # pdf_path = "lorem-ipsum.pdf"
    # page_number = 0  # Replace with the desired page number
    spacing_values = get_line_spacing(pdf_path)

    # now take only even indexes
    res_list = spacing_values[1::2]
    print("Line Spacing Values:", res_list)
    print("as string:", "".join([str(x) for x in res_list]))

