from mtcnn import MTCNN
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle, Circle

def draw_image_with_boxes(filename, result_list):
    #load the image
    data = plt.imread(filename)

    #plot image
    plt.imshow(data)

    #get context for drawing boxes
    ax = plt.gca()

    #plot each box
    for result in result_list:
        #get coordinates
        x, y, width, height = result['box']

        # create the shape
        rect = Rectangle((x, y), width, height, fill = False, color = 'red')

        # draw the box
        ax.add_patch(rect)

        for key, value in result['keypoints'].items():
            dot = Circle(value, radius = 2, color = 'red')
            ax.add_patch(dot)

    # show plot
    plt.show()

# draw each face separately
def draw_faces(filename, result_list):
    # load the image
    data = plt.imread(filename)

    # plot each face as a subplot
    for i in range(len(result_list)):
        # get coordinates
        x1, y1, width, height = result_list[i]['box']
        x2, y2 = x1 + width, y1 + height

        # define subplot
        try:
            plt.subplot(1, len(result_list), i + 1)
            plt.axis('off')

        except ValueError:
            pass

        # plot face
        plt.imshow(data[y1:y2, x1:x2])

    # show the plot
    plt.show()

#Load image
filename = 'test2.jpg'
pixels = plt.imread(filename)

#Default MTCNN detector
detector = MTCNN()

#Detect faces in images
faces = detector.detect_faces(pixels)

draw_faces(filename, faces)
