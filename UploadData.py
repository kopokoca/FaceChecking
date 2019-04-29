from skimage import io

def facedataset(set):
    train = []
    datasets = []
    labels = [i for i in range(set)]
    for i in range(1, set+1):
        dataset = []
        
        for j in range(1, 10):
            img = io.imread("data/att/s%i/%i.pgm" % (i, j))
            dataset.append(img)
        datasets.append(dataset)

        img = io.imread("data/att/s%i/%i.pgm" % (i, 3))
        train.append(img)
    return datasets, labels, train 