import fitz

def shift_point(point, dx, dy):
    """
    Shift a Fitz Point by a relative value (dx, dy).
    """
    new_x = point.x + dx
    new_y = point.y + dy
    return fitz.Point(new_x, new_y)


def truncate_line(line, available_width, font, fontsize):
    """
    Truncates a line to fit within the available width without breaking words.
    """
    current_width = font.text_length(line, fontsize)
    if current_width <= available_width:
        return line  # Line already fits within the available width

    truncated_line = ""
    # split on whitespace
    words = line.split()

    for word in words:
        word_width = font.text_length(word, fontsize)

        if font.text_length(truncated_line + " " + word, fontsize) <= available_width:
            if truncated_line:
                truncated_line += " "
            truncated_line += word
        else:
            break  # Stop adding words when the line exceeds the available width

    return truncated_line

def encode_to_pdf(doc, text, name, fontname="helv", fontsize=12, margin_size=50, max_line_width=100):
  # TODO: check the length of the text vs the cover text
  margin = margin_size
  p = fitz.Point(margin, margin)  # start point of 1st line
  page = doc.new_page()  # new or existing page via doc[n]

  # Calculate the available height on the page
  page_height = page.rect.height
  available_height = page_height - 2 * margin

  page_width = page.rect.width
  available_width = page_width - 2 * margin

  lines = []
  remaining_text = text.split("\n")
  
  for line in remaining_text:
    # can also be done using font.text_length()
    line_lenght = fitz.get_text_length(line, fontname=fontname, fontsize=fontsize)
    if line_lenght >= available_width:
       # break line
      font = fitz.Font(fontname)
      truncated_line = truncate_line(line, available_width, font, fontsize)
      lines.append(truncated_line)
    else:
       lines.append(line)


  for i, line in enumerate(lines):
    if i % 2 == 0:
      p = shift_point(p, 0, 14)
    else: 
      p = shift_point(p, 0, 13)
    page.insert_text(p,
                      line,  # the text (honors '\n')
                      fontname = fontname,  # the default font
                      # fontfile = 'fonts\OpenSans_ABCDE-shifted-up-or-down.sfds',
                      fontsize = fontsize,  # the default font size
                      rotate = 0,  # also available: 90, 180, 270
                      )
    margin += fontsize * 1.2
    
    # # Check if there is enough space for the next line
    if margin + fontsize * 1.2 > available_height:
      # Move to the next page
      page = doc.new_page()
      
      # reset text pointer
      p = fitz.Point(50, 72)
      # Reset the margin
      margin = margin_size

  doc.save(f"{name}.pdf")


if __name__ == '__main__':
  doc = fitz.open()  # new or existing PDF


  with open("data/anthem.txt", "r", encoding="utf-8") as f:
    filetxt = "".join(f.readlines())
    # TODO: podawanie di funkcji listy bitów
    encode_to_pdf(doc, filetxt, "anthem")


'''
funkcja do 
przyjmuje listów bitów
przyjmuje text
zwraca pdf z liniami odpowiadającymi bitom przesuniętymi w góre lub dól
'''