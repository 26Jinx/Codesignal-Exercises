# https://app.codesignal.com/arcade/intro/level-5/5xPitc3yT3dqS7XkP

def boxBlur(image):
    pixelated = []
    
    def get_box_on_origin(row, col):
        box = []
        for r in range(row, row+3):
            box.append(image[r][col:col+3])
         
        return box
        
    def get_average(box):
        combined = []
        for row in box:
            combined += row
            
        avg = sum(combined) // (len(box) * len(box[0]))
        
        return avg
    
    for x in range(0, len(image)-2):
        for y in range(0, len(image[0])-2):
            if 0 <= x < len(pixelated):
                pixelated[x].append(get_average(get_box_on_origin(x, y)))
            else:
                pixelated.append([get_average(get_box_on_origin(x, y))])  
                    
    return pixelated 