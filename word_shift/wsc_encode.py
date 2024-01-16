import fitz  # PyMuPDF
import sys


def merge_paragraphs(text):
    paragraphs = text.split('\n\n')

    if len(paragraphs) == 1:
        paragraphs = text.split('\n')

    merged_text = ' '.join(paragraphs)

    return merged_text


def shift_point(point, dx, dy):
    """
    Shift a Fitz Point by a relative value (dx, dy).
    """
    new_x = point.x + dx
    new_y = point.y + dy
    return fitz.Point(new_x, new_y)


def new_page(doc, margin_size):
    # Move to the next page
    page = doc.new_page()

    # reset text pointer
    p = fitz.Point(margin_size, margin_size)

    return page, p


def get_line_height(page, line_number):
    # Get the text on the page
    text = page.getText("text")

    # Split the text into lines
    lines = text.split("\n")

    # Check if the requested line number is valid
    if 0 <= line_number < len(lines):
        # Get the bounding box of the line
        _, _, _, _, bbox = page.get_text("bbox", clip=page.rect, clip_text=lines[line_number])

        # Calculate the height of the line
        line_height = bbox[3] - bbox[1]

        return line_height
    
def encode_spaces(filetxt, msg_to_encode):
    spaces = [
      '<span class="small-text"> </span>',
      '<span class="large-text"> </span>'
        ]
    
    modified_text = []

    for i, char in enumerate(filetxt):
      if char == ' ':
          if msg_to_encode:
            modified_text.append(spaces[int(msg_to_encode.pop(0))])
          else:
             modified_text.append(spaces[0])

      else: 
          modified_text.append(char)

    return modified_text

def split_with_spaces(str_to_split):
  return [i for j in str_to_split.split() for i in (j, ' ')][:-1]


def insrt_html(doc,
              filetxt,
              text_to_encode, 
              word_spaces = [11, 16],   # czcionka musi być różna od czcionki uzywanej globalnie - inaczej nie działa!!!
              savename = "encoded",
              fontname="helv", 
              fontsize=12, 
              margin_size=72, 
              max_line_width=100):
  text_to_encode = text_to_encode.replace(" ", "").replace("\n", "")
  text_to_encode = list(text_to_encode)
  guard_space = 13

  margin = margin_size

  # Calculate the available height on the page
  page = doc.new_page()
  p = fitz.Point(margin, margin)
  rect = fitz.Rect(page.rect)
  page_height = page.rect.height
  available_height = page_height - 2 * margin

  page_width = page.rect.width
  available_width = page_width - 2 * margin


  # tekst trzymamy jako listę
  filetxt = split_with_spaces(filetxt)
  encoded_txt = encode_spaces(filetxt, text_to_encode)

  len_checker = ""
  line_to_print = ""
  
  for i, word in enumerate(filetxt):
    # check first with unmodified text
    len_checker += word   # we use this to check length of the string
    line_to_print += encoded_txt[i]   # but we print this as it contains additional html
    if fitz.get_text_length(len_checker, fontname=fontname, fontsize=fontsize) < available_width and i < len(filetxt) - 1:
      continue
      # go and add more words

    p = shift_point(p, 0, 20)
    rect.x0 = p.x
    rect.y0 = p.y

    # hande the last line (by printing the next space at the end of the line)
    # dont need to pop the next space as it will not be printed anyways!!!!
    # filetxt.pop(i+1)    # bad practice!
    # encoded_txt.pop(i+1)  # bad practice!
    if i < len(filetxt) - 1:    # don't do this at the very end of the list
      next_space = encoded_txt[i+1]
      line_to_print += next_space
    
    line_to_print += '&nbsp;'   # insert non-breaking space
    # line_to_print += "."
    page.insert_htmlbox(rect, line_to_print, css=f"""
        .small-text {{
          font-size: {word_spaces[0]}px;
        }}
        .medium-text {{     # not used
          font-size: 13px;
        }}
        .large-text {{
          font-size: {word_spaces[1]}px;
      }}
      .testing {{         # not used, only for testing
          font-size: 24px;
      }}""")
    line_to_print = ""
    len_checker = ""
    
    if p.y >= available_height - guard_space:
      page, p = new_page(doc, margin_size)

  doc.save("encoded.pdf")
  doc.close()
  # doc.ez_save(__file__.replace(".py", ".pdf"))


if __name__ == '__main__':
  doc = fitz.open()  # new or existing PDF

  if len(sys.argv) == 1:
      filename = "lorem-ipsum"
  else:
      filename = sys.argv[1]

  with open(f"data/{filename}.txt", "r", encoding="utf-8") as f:
    filetxt = "".join(f.readlines())
    filetxt = merge_paragraphs(filetxt)


  msg_to_encode = "01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100 00100000 01110100 01101000 01101001 01110011 00100000 01101001 01110011 00100000 01110111 01101111 01110010 01100100 00100000 01110011 01101000 01101001 01100110 01110100 00100000 01100011 01101111 01100100 01101001 01101110 01100111"  # Replace with your actual message
  insrt_html(doc, text_to_encode=msg_to_encode, filetxt=filetxt)
