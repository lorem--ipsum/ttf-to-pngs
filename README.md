ttf-to-pngs
===========

Utility script to convert ttf symbol font to png images.


Usage
-----

    ttf_to_pngs.py -h

outputs :

    Usage: ttf_to_pngs.py [options]

    Options:
      -h, --help            show this help message and exit
      -f FONT, --font=FONT  the font file (must be a .ttf font)
      -g GLYPHS, --glyphs=GLYPHS
                            the csv codes file (a line must follow this syntax:
                            "name, unicode")
      -o OUTPUT_DIR, --output=OUTPUT_DIR
                            the output directory
      -s SIZE, --size=SIZE  the font size
      -c COLOR, --color=COLOR
                            a string for the color (black, grey...)
      --overwrite           overwrite existing images


You basically need a ttf font, a codes file (csv) that contains lines following this syntax :
    
    glyph_label, glyph_code


And you're almost done ! Simply call
    
    ttf_to_pngs.py -f font_ligatures.ttf  -g codes_ligatures.csv -o images

Why ?
-----

I've been frustrated by the wonderful [Ligatures](http://kudakurage.com/ligature_symbols/) font, since I wanted to use it as regular png icons. So I made this script.


Issues
------

It probably is very focused on the [Ligatures](http://kudakurage.com/ligature_symbols/) font, so offset and stuff may not be accurate for other fonts. Feel free to contact me or send a pull request on this repo.


Can I contact you for a specific need ?
---------------------------------------
No.

Just kidding, of course you can.