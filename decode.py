import fitz  # PyMuPDF

def get_line_spacing(pdf_path, page_number):
    doc = fitz.open(pdf_path)
    page = doc[page_number]

    text_blocks = page.get_text("dict")
    # extract blocks:
    lines = text_blocks['blocks'][0]['lines']
    line_spacing = []
    # get first line
    prev_line = lines[0]

    for line in lines[1:]:
        # get coordinates
        origin = line['spans'][0]['origin']
        prev_origin = prev_line['spans'][0]['origin']

        # compare distance to previous line
        distance = abs(origin[1] - prev_origin[1])
        print(distance)
        # TODO: the line distance will be varaible
        if distance == 14:
            line_spacing.append(1)
        else:
            line_spacing.append(0)
        prev_line = line
            
    # prev_block = text_blocks[0]
    # for block in text_blocks:
    #     lines = block[4].split("\n")  # lines in the block
    #     if len(lines) > 1:  # Check if there are at least two lines in the block
    #         for i in range(1, len(lines)):
    #             prev_line = lines[i - 1]
    #             current_line = lines[i]
    #             distance = current_line[1] - prev_line[3]  # Y-coordinate of current line - Bottom Y-coordinate of previous line
    #             line_spacing.append(distance)

    doc.close()

    return line_spacing



# Example usage
pdf_path = "anthem.pdf"
page_number = 0  # Replace with the desired page number
spacing_values = get_line_spacing(pdf_path, page_number)

print("Line Spacing Values:", spacing_values)
