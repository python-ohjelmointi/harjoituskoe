"""
This exercise has been borrowed from CS50 course's Python track. The original problem set can
be found at: https://cs50.harvard.edu/python/2022/psets/1/extensions/

The exercise is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International (CC BY-NC-SA 4.0) license. The full text of the license can be found at:
https://cs50.harvard.edu/python/2022/license/


File Extensions

Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix
that starts with a period (.) at the end of their name. For instance, file names for GIFs end
with .gif, and file names for JPEGs end with .jpg or .jpeg. When you double-click on a file to
open it, your computer uses its file extension to determine which program to launch.

Web browsers, by contrast, rely on media types, formerly known as MIME types, to determine how
to display files that live on the web. When you download a file from a web server, that server
sends an HTTP header, along with the file itself, indicating the file's media type. For
instance, the media type for a GIF is image/gif, and the media type for a JPEG is image/jpeg.
To determine the media type for a file, a web server typically looks at the file's extension,
mapping one to the other.

See https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
for common types.

In a file called extensions.py, implement a program that prompts the user for the name of a
file and then outputs that file's media type if the file's name ends, case-insensitively, in
any of these suffixes:

    .gif
    .jpg
    .jpeg
    .png
    .pdf
    .txt
    .zip

If the file's name ends with some other suffix or has no suffix at all, output application/
octet-stream instead, which is a common default.

Hints

    Recall that a str comes with quite a few methods, per
    https://docs.python.org/3/library/stdtypes.html#string-methods.


Examples:

    >>> get_mime_type('cat.gif')
    'image/gif'

    >>> get_mime_type('cat.jpg')
    'image/jpeg'

    >>> get_mime_type('cat.jpeg')
    'image/jpeg'

Your solution needs to be case-insensitive:

    >>> get_mime_type('Cat.Jpeg')
    'image/jpeg'

    The default mime type is application/octet-stream:

    >>> get_mime_type('cat')
    'application/octet-stream'

    >>> get_mime_type('cat.picture')
    'application/octet-stream'
"""

def get_mime_type(filename: str) -> str:
    # Implement this function based on the exercise description
    return "application/octet-stream"


if __name__ == "__main__":
    filename = input("File name: ")
    mime_type = get_mime_type(filename)
    print(mime_type)

    """
    You should also utilize the doctest tests included in the assignment.
    The lines below will run them when this file is executed:
    """
    import doctest
    doctest.testmod(verbose=True)
