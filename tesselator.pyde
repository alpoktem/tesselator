import os
#CONSTANTS
IMAGE_RE = re.compile("\.jpg$|\.png$") #extensions of image types should come here

#CONFIGS 
SCALE_IMAGE = 0.2
IMAGE_SOURCE="/Users/alp/Documents/Processing3_ws/sketches/tesselator/sample_pics/kabak/Bild (75).jpg"
IMAGE2_SOURCE="/Users/alp/Documents/Processing3_ws/sketches/tesselator/sample_pics/kabak/Bild (75).jpg"
#IMAGE_SOURCE="/Users/alp/Desktop/caixa_gridding"
DIR_SAVED_FRAMES="saved_tesselations"
GRID_X=4
GRID_Y=4
MODE = 'filter'
FILTER_TYPE = INVERT
WEIRD='randomset'
SET_SIZE = 2

def settings():
    global grid_width, grid_height, grid_no
    grid_width, grid_height = get_grid_sizes(IMAGE_SOURCE, SCALE_IMAGE)
    grid_no = GRID_X * GRID_Y
    size(grid_width*GRID_X, grid_height*GRID_Y)

def setup():
    frameRate(1)
    this.surface.setResizable(True) 
    this.surface.setTitle("Tesselator")
    
def draw():
    global grid_width, grid_height, grid_no
    
    if WEIRD == 'random':
        weird_one = [int(random(1, grid_no ))]
    elif WEIRD == 'randomset':
        weird_one = [int(random(1, grid_no )) for i in range(SET_SIZE)]
    else:
        weird_one = [WEIRD]
    print('weird:%s'%weird_one)
    
    # Draw the images to the screen 
    im_no = 1
    for img, pos in zip(imiterator(IMAGE_SOURCE), griderator(GRID_X, GRID_Y, grid_width, grid_height)):
        if MODE == 'place' and im_no in weird_one:
            img2 = loadImage(IMAGE2_SOURCE)
            print(IMAGE2_SOURCE)
            img2.resize(grid_width, grid_height)
            image(img2, pos[0], pos[1])
        elif MODE == 'filter' and im_no in weird_one:
            img.resize(grid_width, grid_height)
            img.filter(FILTER_TYPE)
            image(img, pos[0], pos[1])
        else:
            img.resize(grid_width, grid_height)
            image(img, pos[0], pos[1])
        
        im_no += 1
        
    noLoop()
    
#gets sizes of the output tiles
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

#iterator for tile positions
def griderator(grid_x, grid_y, grid_width, grid_height, x_0=0, y_0=0):
    y_pos = y_0
    for y_i in range(grid_y):
        x_pos = x_0
        for x_i in range(grid_x):
            yield x_pos, y_pos
            x_pos += grid_width
        y_pos += grid_height
    
#iterator for images
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
    if key == 'Q' or key == 'q':
        print("exiting")
        exit()
    if key == 'S' or key == 's':
        file_id = os.path.basename(IMAGE_SOURCE)
        filename = "%s/%s_%ix%i_%s.png"%(DIR_SAVED_FRAMES, file_id, GRID_X, GRID_Y, MODE)
        saveFrame(filename)
        print("Saved frame to %s"%(filename))
    if key == 'R' or key =='r':
        loop()
