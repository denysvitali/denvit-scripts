#!/usr/bin/env python3

import sys
import re
import shutil
import argparse
import binascii

#
#   Author: Daxda
#   Date:   02.04.2014
#   WTF:    This is a quick tool I've hacked together to easily remove the meta
#           information as well as the annoying link on each page of eBooks
#           downloaded from it-ebooks.info. The modified file will hold the
#           original file name, and the original file will be renamed to
#           'original.pdf.old'. 'pattern' is the regex pattern which is used to
#           remove the annotation elements, the rough structure of it looks
#           like this:
#
#   obj
#   <<
#   /Type /Annot
#   /Subtype /Link
#   /Rect [ 264 91 348 79 ]   # The digits on this line will differ
#   /Border [ 0 0 0 ]         # The same goes for the digits on this line
#   /A <<
#   /Type /Action
#   /S /URI
#   /URI (http://www.it-ebooks.info/)
#   >>
#   >>
#   endobj
#

pattern = b'''0a2f54797065202f416e6e6f740a2f53756274797065202f4c696e6b0a2f52656
374205b20.*?205d0a2f426f7264657220.*?\n0a2f41203c3c0a2f54797065202f416374696f6e
0a2f53202f5552490a2f5552492028687474703a2f2f7777772e69742d65626f6f6b732e696e666
f2f290a3e3e'''.replace(b'\n', b'').strip()

pattern = b'''3c3c2f547970652f416e6e6f740a2f52656374205b.*?\n5d0a2f426f72646572205b30203020305d0a2f413c3c2f532f5552490a2f55524928687474703a2f2f7777772e69742d65626f6f6b732e6469726563746f72792f293e3e0a2f537562747970652f4c696e6b3e3e'''.replace(b'\n', b'').strip()
pattern = b'''3c3c2f547970652f506167652f4d65646961426f78205b.*?\n5d2f526f7461746520302f506172656e742033203020520a2f47726f75702036203020520a2f5265736f75726365733c3c2f50726f635365745b2f504446202f546578745d'''.replace(b'\n', b'').strip()

def remove_evil_links(pdf_data):
    'Removes all it-ebook links and metadata from the passed PDF data.'
    pdf_data = binascii.hexlify(pdf_data)

    # Remove each annotation element inside the PDF file
    # (This removes the "clickable" it-ebooks.info links)
    new_data = re.sub(pattern, b'', pdf_data)

    # Remove the actual links
    # (link elements which are assigned to the annotations)
    new_data = new_data.replace(binascii.hexlify(b'www.it-ebooks.directory'), b'')
    return binascii.unhexlify(new_data)

def main(args):
    try:
        args.files = list(set(args.files))
        for file_path in args.files:
            if not file_path:
                continue
            if args.verbose:
                print('Processing: {0}'.format(file_path))
            try:
                with open(file_path, 'rb') as input_file:
                    pdf_data = input_file.read()
            except IOError as e:
                sys.stderr.write('{0}: {1}\n'.format(file_path, e.strerror))
                sys.stderr.flush()
                continue

            # Backup the file with a different name
            if not args.no_backup:
                if args.verbose:
                    print('Creating backup: {0}.old'.format(file_path))
                shutil.move(file_path, '{0}.old'.format(file_path))

            # Modify the PDF file
            new_pdf_data = remove_evil_links(pdf_data)
            # Save the new file
            with open(file_path, 'wb') as out_file:
                out_file.write(new_pdf_data)
            if args.verbose:
                print('Saving modified file: {0}'.format(file_path))
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f', '--files',
        help='One or more PDF files to remove it-ebook watermarks.',
        nargs='*', required=True
    )
    parser.add_argument(
        '-n', '--no-backup',
        help='Disables the creating of backups for the files ' +
             'which are being processed.',
        action='store_true'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true'
    )

    args = parser.parse_args()
    main(args)

