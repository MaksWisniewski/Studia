def cat_memes():
    try:
        f = open('kitteh.jpg', 'rb')
        cat_pic = f.read()
        # Do other stuff with the cat picture in memory.
        print("Meow meow")
    except:
        print('oops, something went wrong.')
    finally:
        if "f" in locals():
            f.close()

cat_memes()