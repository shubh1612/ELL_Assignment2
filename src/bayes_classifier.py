import numpy as np 
import class_conditional_estimator as cc 

class bayes_model:

	def __init__(self, estimator_type, param):
		self.estimator = estimator_type
		self.X = None 
		self.Y = None
		self.parameters = param
		self.per_class_estimator = []
		self.prior = []

	def train(self, X_train, Y_train):
		self.X = X_train
		self.Y = Y_train

		self._estimate_px_theta()

	def _get_est_object(self):
		if self.estimator == 'GMM':
			comp = self.parameters[0]
			toler = self.parameters[1]
			max_it = self.parameters[2]
			dim = self.parameters[3]
			reg = self.parameters[4]
			return cc.gaussian_mixture_model(n_comp = comp, tol = toler, max_iter = max_it, dimension = dim, regularize = reg)

		if self.estimator == '':
			return None

		if self.estimator == '':
			return None

		if self.estimator == '':
			return None

	def _estimate_px_theta(self):
		classes = np.unique(self.Y)
		for i in classes:
			model = self._get_est_object()
			X_temp = (self.X)[np.repeat(self.Y == i, (self.X).shape[1], axis = 1)]
			X_temp = X_temp.reshape(int(X_temp.shape[0] / (self.X).shape[1]), (self.X).shape[1] )
			model.estimate_parameters(X_temp)
			(self.per_class_estimator).append(model)

			(self.prior).append(np.sum(self.Y == i) / self.Y.shape[0])

	def predict(self, X_test):
		classes = np.expand_dims(np.unique(self.Y), axis = 1)
		Q = np.zeros((X_test.shape[0], classes.shape[0]))
		Q
		for i in range(len(classes)):
			Q[:, i] = ((self.per_class_estimator)[i].get_likelihood(X_test) * (self.prior)[i]).ravel()
		class_idx = np.argmax(Q, axis = 1)

		return classes[class_idx]


if __name__ == "__main__":
	num_ex = 1000
	dim = 5
	X_train = (1000*np.random.rand(num_ex, dim)).astype('int')
	Y_train = (5*np.random.rand(num_ex, 1)).astype('int')

	parameters = [3, 0.001, 100, dim, 0.00001]

	model1 = bayes_model(estimator_type = 'GMM', param = parameters)
	model1.train(X_train, Y_train)

	X_test = (1000*np.random.rand(10, dim)).astype('int')
	print(model1.predict(X_test))