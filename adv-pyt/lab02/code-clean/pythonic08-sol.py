# Code sample inspired from: https://www.mattlayman.com/blog/2017/pythonic-code-the-with-statement/
def cat_memes():
    try:
        with open('kitteh.jpg', 'rb') as f:
            cat_pic = f.read()
    except:
        print('oops, file opening went wrong.')
        return None
    try:
        # Do other stuff with the cat picture in memory.
        print("Meow meow")
    except:
        print('oops, something went wrong.')


cat_memes()
