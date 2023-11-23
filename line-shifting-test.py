import fitz  # PyMuPDF

def shift_lines(pdf_path, output_path, line_shifts):
    doc = fitz.open(pdf_path)

    for page_num in range(doc.page_count):
        page = doc[page_num]

        for line_num, shift_amount in line_shifts.get(page_num, {}).items():
            if 0 <= line_num < len(page.get_text("text").split('\n')):
                text_line = page.get_text("text").split('\n')[line_num]

                # Calculate new position based on shift amount
                new_position = (0, page.rect.height - shift_amount)

                # Create a new text annotation with the shifted text
                new_text = page.insert_text(new_position, text_line)
                print(new_text)

                # # Remove the original text line
                # page.delete_text(new_text)

                # stream = doc.xref_stream(xref).replace(b'The string to delete', b'')
                # doc.update_stream(xref, stream)

    doc.save(output_path)
    doc.close()

# Example usage:
input_pdf = 'input.pdf'
output_pdf = 'output.pdf'

# Dictionary containing page number and line number pairs with corresponding shift amounts
line_shifts = {
    0: {1: 20, 3: 10},
    1: {0: 15, 2: 5}
}

shift_lines(input_pdf, output_pdf, line_shifts)
