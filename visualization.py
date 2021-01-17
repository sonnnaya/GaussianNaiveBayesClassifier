import matplotlib.pyplot as plt
from main import clusters, test_images


image_clusters = [cluster.images for cluster in clusters]


x_es = [[image[0] for image in images] for images in image_clusters]
y_es = [[image[1] for image in images] for images in image_clusters]

names = [' z' + str(i + 1) for i in range(len(image_clusters))]

for i in range(len(x_es)):
    plt.scatter(x_es[i], y_es[i])

for i, txt in enumerate(names):
    for j in range(len(x_es[i])):
        plt.annotate(txt, (x_es[i][j], y_es[i][j]))

test_x = [image[0] for image in test_images]
test_y = [image[1] for image in test_images]

for i in range(len(test_x)):
    plt.scatter(test_x[i], test_y[i], c="r")

plt.show()
