from ascii_magic import AsciiArt, Back

my_art = AsciiArt.from_image('f.png')
my_art.to_terminal(columns=200, back=Back.BLUE)