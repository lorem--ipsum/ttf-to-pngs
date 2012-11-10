#!/usr/bin/env python

import CSV
import ImageFont, Image, ImageDraw
import os
import sys
from optparse import OptionParser


def get_size(character, font):
    size = font.getsize(character)
    
    return (16, 16)


def draw_image(character, font):
    size = get_size(character, font)
    
    image = Image.new("RGBA", size, (255,255,255,0))
    
    dark_grey = (71, 72, 80)
    yellow = (222, 129, 49)
    
    ImageDraw.Draw(image).text((1, -3), character, font=font, fill=dark_grey)
    
    return image
    

def get_path(path, name):
    return path + "/" + name + ".png"


def save(image, path, name):
    image.save(get_path(path, name), "PNG")


def csv_to_dicts(groups):
    return {
        'name': groups[0],
        'code': groups[1].decode('unicode-escape')
    }


def prepare_arg_parser():
    global parser
    
    parser = OptionParser()
    
    parser.add_option('-f', '--font', dest='font',
                        help='the font file (must be a .ttf font)'
    )
    
    parser.add_option('-g', '--glyphs', dest='glyphs',
                        help='the csv codes file (a line must follow this syntax: "name, unicode")'
    )
    
    parser.add_option('-o', '--output', dest='output_dir',
                        help='the output directory'
    )
    
    parser.add_option('-s', '--size', dest='size', default=20, type='int',
                        help='the font size'
    )
    
    parser.add_option('-c', '--color', dest='color', default='grey',
                        help='a string for the color (black, grey...)'
    )
    
    parser.add_option('--overwrite', dest='overwrite', default=False,
                        action="store_true", help='overwrite existing images in output dir'
    )


def check_file_option(path, name):
    if not path:
        yell_and_rage_quit('missing path for ' + name)
    
    if not os.path.isfile(path):
        yell_and_rage_quit('unable to find file at ' + path)


def yell_and_rage_quit(complaint):
    print 'Error: ' + complaint
    print
    parser.print_help()
    sys.exit(1)


def sanitize(options):
    check_file_option(options.font, 'font')
    check_file_option(options.glyphs, 'glyphs')
    
    if not options.output_dir:
        yell_and_rage_quit('missing output dir')
    
    if os.path.isfile(options.output_dir):
        yell_and_rage_quit("specified output is a file, don't play this little game with me")
    
    if not os.path.exists(options.output_dir):
        print 'Creating output directory: ' + options.output_dir
        os.mkdir(options.output_dir)
    

def get_options():
    global parser
    
    prepare_arg_parser()
    
    (options, args) = parser.parse_args()
    
    sanitize(options)
    
    return options


def ensure_no_overwrite(codes, output_dir):
    for item in codes:
        png_file = get_path(output_dir, item['name'])
    
        if os.path.isfile(png_file):
            st = 'a file could be overwritten: ' + png_file
            st += '\nplease use the --overwrite option'
            yell_and_rage_quit(st)


options = get_options()

codes = CSV.load(options.glyphs, csv_to_dicts)

if not options.overwrite:
    ensure_no_overwrite(codes, options.output_dir)


font = ImageFont.truetype(options.font, options.size)
for item in codes:
    save(draw_image(item['code'], font), options.output_dir, item['name'])
