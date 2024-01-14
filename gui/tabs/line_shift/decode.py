import fitz  # PyMuPDF

def get_line_spacing(pdf_path, page_number) -> list[int]:
    # TODO iterate over all pages, or take the text as a whole (to check if we are not already doing it by taking the whole block)s
    doc = fitz.open(pdf_path)
    page = doc[page_number]

    text_blocks = page.get_text("dict")
    # extract blocks:
    lines = text_blocks['blocks'][0]['lines']
    line_spacing = []
    # get first line
    prev_line = lines[0]

    # TODO: bierz co drugą linię a nie każdą po kolei!!
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
            
    doc.close()

    return line_spacing

def get_page_count(pdf_path) -> int:
    doc = fitz.open(pdf_path)
    pages = len(doc)
    doc.close()
    return pages

# pdf_path = "lorem-ipsum.pdf"
# page_number = 0  # Replace with the desired page number
# spacing_values = get_line_spacing(pdf_path, page_number)

# print("Line Spacing Values:", spacing_values)
