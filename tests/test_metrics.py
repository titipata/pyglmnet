import numpy as np
from pyglmnet import GLM
from nose.tools import assert_true, assert_equal, assert_raises

def test_deviance():
	n_samples, n_features = 1000, 100

	beta0 = np.random.normal(0.0, 1.0, 1)
	beta = np.random.normal(0.0, 1.0, n_features)

    # sample train and test data
	glm_sim = GLM(score_metric='deviance')
	X = np.random.randn(n_samples, n_features)
	y = glm_sim.simulate(beta0, beta, X)

	glm_sim.fit(X, y)
	score = glm_sim[-1].score(X, y)
	print score
	assert_equal(score.shape[0], 1)

def test_pseudoR2():
	n_samples, n_features = 1000, 100

	beta0 = np.random.normal(0.0, 1.0, 1)
	beta = np.random.normal(0.0, 1.0, n_features)

    # sample train and test data
	glm_sim = GLM(score_metric='pseudo_R2')
	X = np.random.randn(n_samples, n_features)
	y = glm_sim.simulate(beta0, beta, X)

	glm_sim.fit(X, y)
	score = glm_sim[-1].score(X, y)
	print score
	assert_equal(score.shape[0], 1)