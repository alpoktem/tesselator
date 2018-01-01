SCALE_IMAGE = 1
IMAGE_LOCATION="Che_Guevara_Smurf.jpg"
IMAGE_DIRECTORY=None
GRID_X=7
GRID_Y=7

def setup():
    size(500,500)
    frameRate(1)
    frame.setResizable(True) # use frame instead.
    

def draw():
    x_max = 0
    y_max = 0

    # Draw the images to the screen 
    for img, img_x, img_y, img_width, img_height in griderator(GRID_X, GRID_Y, image_file=IMAGE_LOCATION, image_dir=IMAGE_DIRECTORY):
        image(img, img_x, img_y, img_width, img_height)
        x_max = img_x + img_width
        y_max = img_y + img_height
        
    print("Tesselation size: %i x %i"%(x_max, y_max))
    this.surface.setSize(x_max, y_max)
    
def griderator(grid_x, grid_y, image_file=None, image_dir=None):
    assert (image_file and image_dir == None) or (image_file == None and image_dir)
    if image_file:
        img = loadImage(IMAGE_LOCATION)
        x_pointer = 0
        y_pointer = 0
        image_width = int(img.width * SCALE_IMAGE)
        image_height = int(img.height * SCALE_IMAGE)
        
        for i_y in range(grid_y):
            y_pointer = i_y * image_height
            for i_x in range(grid_x):
                x_pointer = i_x * image_width
                yield img, x_pointer, y_pointer, image_width, image_height
    else:
        #TODO
        yield None, 0,0 
    
