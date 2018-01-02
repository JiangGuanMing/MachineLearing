from matplotlib.colors import ListedColormap
def plot_decision_regions(X, y, classfier, resolution=0.2):
    
    # setup maker generator and color map
    markers = ('s','x','o','^','>')
    colors = ('red', 'blue','lightgreen','gray','cyan')
    cmap = ListedColormap(color[: len(np.unique(y))])
    
    # plot the decision surface
    import numpy as np
    x1_min, x2_max = X[:,0].min() - 1, X[:,0].max() + 1
    x2_min, x2_max = X[:,1].min() - 1, X[:,1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),np.arange(x2_min, x2_max, resolution))
    Z = classifer.predict(np.arrary([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha = 0.4, cmap = cmap)
    plt.xlim(xx1.min(),xx1.max())
    plt.ylim(xx2.min(),xx2.max())
    
    #plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x = X[ y == cl, 0], y = X[y == cl, 1], alpha = 0.8, c = camp(idx),marker = markers[idx],label=cl)
    