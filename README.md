# picopic

Picopic is a command-line tool that allows pico-8 developers to import images to the spritesheet directly

# Installation
Download directly from [github]. No fancy installer or pip installation yet :(

# Usage
To use picopic, use the following command:
```
python picopic.py "path/to/file" size offset_x offset_y "path/to/output"
```
Argument explanations:
| Argument | Description |
| ----- | ----- |
| python | You know this one... |
| picopic.py | This lovely command-line tool |
| "path/to/file" | The path of the image to be imported into pico-8 |
| size | A number in range [0,3] corresponding to image area 8x8/16x16/24x24/32x32 |
| offset_x | A number representing how many 8-pixel spaces should appear to the left of the image |
| offset_y | Above... but in y coordinates!!! |
| "path/to/output" | The desired path of the output p8 file (note that this will overwrite existing files) |

# Can you break it?
Short answer: maybe.
Longer answer: There's some decent but not exhaustive error checking going on behind the scenes, so chances are it'll catch some errors. However, this is an early early release and so bugs and errors are bound to be found.

# Future plans
Future plans for the project are as follows:
- Multiple sprite imports
- Imports onto spritesheets 2-4
- User-friendlyish shell
- GUI
- Fancy installer or pip installation

# License
MIT

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

   [github]: <https://github.com/MetalKamina/picopic>