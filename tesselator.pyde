import os

SCALE_IMAGE = 1
IMAGE_SOURCE="/Users/alp/Documents/Processing3_ws/sketches/tesselator/sample_pics/smurflib"
#IMAGE_SOURCE="/Users/alp/Desktop/caixa_gridding"
DIR_SAVED_FRAMES="saved_tesselations"
GRID_X=5
GRID_Y=5

IMAGE_RE = re.compile("\.jpg$|\.png$")

def setup():
    size(500,500)
    frameRate(1)
    frame.setResizable(True) # use frame instead.
    
def draw():
    grid_width, grid_height = get_grid_sizes(IMAGE_SOURCE, SCALE_IMAGE)

    # Draw the images to the screen 
    for img, pos in zip(imiterator(IMAGE_SOURCE), griderator(GRID_X, GRID_Y, grid_width, grid_height)):
        img.resize(grid_width, grid_height)
        image(img, pos[0], pos[1])

    noLoop()
    
def get_grid_sizes(image_source, scale=1):
    get_from_dir = os.path.isdir(image_source)
    if get_from_dir:
        image_filenames = os.listdir(image_source) 
        image_filenames.sort()
        image_files = [os.path.join(image_source, fn) for fn in image_filenames if IMAGE_RE.search(fn)]
        image_file = image_files[0]
    else:
        image_file = image_source
    
    img = loadImage(image_file)
        
    image_width = int(img.width * scale)
    image_height = int(img.height * scale)
    return image_width, image_height

def griderator(grid_x, grid_y, grid_width, grid_height, x_0=0, y_0=0):
    y_pos = y_0
    for y_i in range(grid_y):
        x_pos = x_0
        for x_i in range(grid_x):
            yield x_pos, y_pos
            x_pos += grid_width
        y_pos += grid_height
    
#an iterator for images. 
def imiterator(image_source):
    get_from_dir = os.path.isdir(image_source)
    if get_from_dir:
        image_filenames = os.listdir(image_source) 
        image_filenames.sort()
        image_files = [os.path.join(image_source, fn) for fn in image_filenames if IMAGE_RE.search(fn)]
    else:
        image_files = [image_source]
    
    image_index = 0
        
    while True:
        img = loadImage(image_files[image_index])
        yield img
        
        if get_from_dir:
            image_index += 1
            if image_index >= len(image_files):
                image_index = 0
                
def keyPressed():
    if key == 'X' or key == 'x':
        print("exiting")
        exit()
    if key == 'S' or key == 's':
        file_id = os.path.basename(IMAGE_SOURCE)
        saveFrame("%s/%s.png"%(DIR_SAVED_FRAMES, file_id))
        print("Saved frame to %s/%s.png"%(DIR_SAVED_FRAMES, file_id))