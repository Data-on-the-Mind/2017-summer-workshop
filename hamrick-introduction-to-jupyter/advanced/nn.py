import numpy as np


def gen_data(m):
    """Generate m random data points from each of two diferent normal 
    distributions with unit variance, for a total of 2*m points.
    
    Parameters
    ----------
    m : int
        Number of points per class
        
    Returns
    -------
    x, y : numpy arrays
        x is a float array with shape (m, 2)
        y is a binary array with shape (m,)
    
    """
    sigma = np.eye(2)
    mu = np.array([[0, 2], [0, 0]])
    mvrandn = np.random.multivariate_normal
    x = np.concatenate([mvrandn(mu[:, 0], sigma, m), mvrandn(mu[:, 1], sigma, m)], axis=0)
    y = np.concatenate([np.zeros(m), np.ones(m)], axis=0)
    idx = np.arange(2 * m)
    np.random.shuffle(idx)
    x = x[idx]
    y = y[idx]
    return x, y


class Perceptron(object):
    
    def __init__(self, alpha=0.5):
        self.alpha = alpha
        self.w = np.array([0, 0.2])
        self.b = 0
        self.normal = np.random.randn(2)
        self.boundary = None
        self.calc_normal()
        
    def calc_normal(self):
        """Calculate the normal vector and decision boundary."""
 
        new_normal = self.normal - (np.dot(self.w, self.normal) / np.dot(self.w, self.w)) * self.w
        new_normal = new_normal / np.dot(new_normal, new_normal)
        offset = -self.b * self.w / np.dot(self.w, self.w)
        normmult = np.array([-1000, 1000])
        boundary = (new_normal[None] * normmult[:, None]) + offset[None]
        self.normal = new_normal
        self.boundary = boundary
        
    def train(self, x, y):
        # compute the output of the perceptron and the error to the true labels
        output = 1 / (1 + np.exp(-(np.dot(self.w, x.T) + self.b)))
        loss = ((y - output) ** 2).sum()

        # update our weights and recalculate the normal vector
        dloss = 2 * (y - output)
        dsigmoid = output * (1 - output)
        self.w += self.alpha * (dloss[:, None] * dsigmoid[:, None] * x).mean(axis=0)
        self.b += self.alpha * (dloss * dsigmoid).mean(axis=0)
        self.calc_normal()
        
        # decay the learning rate
        self.alpha *= 0.99
        
        return loss
