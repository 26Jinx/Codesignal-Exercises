# https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN

def addBorder(picture):
    # let's first determine the size of the picture
    picture_width = len(picture[0])
    
    # adding a picture frame
    framed_picture = []    
    frame_width = picture_width + 2
    
    top = bottom = '*' * frame_width
    for el in picture:
        framed_picture.append('*' + el + '*')
    
    # now let's add the frame to the picture    
    framed_picture.insert(0, top)
    framed_picture.append(bottom)
    
    return framed_picture