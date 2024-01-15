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


def insrt_html(doc,
              filetxt,
              text_to_encode = "10101010", 
              word_spaces = [12, 16],
              savename = "encoded",
              fontname="helv", 
              fontsize=12, 
              margin_size=50, 
              max_line_width=100):
  text_to_encode = text_to_encode.replace(" ", "").replace("\n", "")
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

  # filetxt = """
  #   space1<span class="small-text"> </span>space <br>
  #   space2<span class="medium-text"> </span>space <br>
  #   space3<span class="large-text"> </span>space <br>
  #   """*50
  filetxt = [
     'space1<span class="small-text"> </span>space <br>', 
      'space2<span class="medium-text"> </span>space <br>', 
      'space3<span class="large-text"> </span>space <br>'
      ] * 50
  for line in filetxt:
    p = shift_point(p, 0, 13)
    rect.x0 = p.x
    rect.y0 = p.y
    page.insert_htmlbox(rect, line, css="""
        .small-text {
          font-size: 18px;
        }
        .medium-text {
          font-size: 18px;
        }
        .large-text {
          font-size: 20px;
      }}
                        """)
    
    if p.y >= available_height - guard_space:
      page, p = new_page(doc, margin_size)

  doc.save("outpud.pdf")
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


  message_to_encode = "01010101"  # Replace with your actual message
  insrt_html(doc, filetxt="example space1 space2 space3")
