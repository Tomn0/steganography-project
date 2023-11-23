import fitz

def shift_point(point, dx, dy):
    """
    Shift a Fitz Point by a relative value (dx, dy).
    """
    new_x = point.x + dx
    new_y = point.y + dy
    return fitz.Point(new_x, new_y)


def encode_to_pdf(text, name, p):
  lines = text.split("\n")
  # lines_num = len(lines)

  for i, line in enumerate(lines):
    if i % 2 == 0:
      p = shift_point(p, 0, 14)
    else: 
      p = shift_point(p, 0, 13)
    page.insert_text(p,
                      line,  # the text (honors '\n')
                      fontname = "helv",  # the default font
                      fontsize = 11,  # the default font size
                      rotate = 0,  # also available: 90, 180, 270
                      )

  doc.save(f"{name}.pdf")


if __name__ == '__main__':
  doc = fitz.open()  # new or existing PDF
  page = doc.new_page()  # new or existing page via doc[n]
  p = fitz.Point(50, 72)  # start point of 1st line
  with open("data/anthem.txt", "r", encoding="utf-8") as f:
    filetxt = "".join(f.readlines())
    encode_to_pdf(filetxt, "anthem", p)

# text = "Some text,sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssAAAAAAAAAAAAAAAAAAAAAAAsss\nspread across\nseveral lines."
# text1 = "Some text,"
# text2 = "spread across"
# text3 = "several lines."
# the same result is achievable by
# text = ["Some text", "spread across", "several lines."]

# page.insert_text(p,  # bottom-left of 1st char
#                      text,  # the text (honors '\n')
#                      fontname = "helv",  # the default font
#                      fontsize = 11,  # the default font size
#                      rotate = 0,  # also available: 90, 180, 270
#                      )

# p = fitz.Point(150, 172)
# page.insert_text(p,  # bottom-left of 1st char
#                      text2,  # the text (honors '\n')
#                      fontname = "helv",  # the default font
#                      fontsize = 11,  # the default font size
#                      rotate = 0,  # also available: 90, 180, 270
#                      )
# p = fitz.Point(300, 272)
# page.insert_text(p,  # bottom-left of 1st char
#                      text3,  # the text (honors '\n')
#                      fontname = "helv",  # the default font
#                      fontsize = 11,  # the default font size
#                      rotate = 0,  # also available: 90, 180, 270
#                      )
# # print("%i lines printed on page %i." % (rc, page.number))

# doc.save("text.pdf")


'''
funkcja do 
przyjmuje listów bitów
przyjmuje text
zwraca pdf z liniami odpowiadającymi bitom przesuniętymi w góre lub dól
'''