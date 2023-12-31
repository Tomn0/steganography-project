
import fontforge                                 #Load the module
amb=fontforge.open("fonts/Ambrosia.sfd")               #Open a font
amb.selection.select(("ranges",None),"A","Z")    #select A-Z
amb.copy()                                       #Copy those glyphs into the clipboard

n=fontforge.font()                               #Create a new font
n.selection.select(("ranges",None),"A","Z")      #select A-Z of it
n.paste()                                        #paste the glyphs above in
print(n["A"].foreground)                          #test to see that something
                                                 #  actually got pasted
n.fontname="NewFont"                             #Give the new font a name
n.save("fonts/NewFont.sfd")       