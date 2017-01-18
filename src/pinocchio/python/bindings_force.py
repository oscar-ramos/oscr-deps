import unittest
import pinocchio as se3
import numpy as np
from pinocchio.utils import eye,zero,rand

ones = lambda n: np.matrix(np.ones([n, 1] if isinstance(n, int) else n), np.double)

class TestForceBindings(unittest.TestCase):

    v3zero = zero(3)
    v6zero = zero(6)
    v3ones = ones(3)
    m3zero = zero([3,3])
    m3ones = eye(3)
    m4ones = eye(4)

    def test_zero_getters(self):
        f = se3.Force.Zero()
        self.assertTrue(np.allclose(self.v3zero, f.linear))
        self.assertTrue(np.allclose(self.v3zero, f.angular))
        self.assertTrue(np.allclose(self.v6zero, f.vector))

    def test_setRandom(self):
        f = se3.Force.Zero()
        f.setRandom()
        self.assertFalse(np.allclose(self.v3zero, f.linear))
        self.assertFalse(np.allclose(self.v3zero, f.angular))
        self.assertFalse(np.allclose(self.v6zero, f.vector))

    def test_setZero(self):
        f = se3.Force.Zero()
        f.setRandom()
        f.setZero()
        self.assertTrue(np.allclose(self.v3zero, f.linear))
        self.assertTrue(np.allclose(self.v3zero, f.angular))
        self.assertTrue(np.allclose(self.v6zero, f.vector))

    def test_set_linear(self):
        f = se3.Force.Zero()
        lin =  rand(3)  # TODO np.matrix([1,2,3],np.double) OR np.matrix( np.array([1,2,3], np.double), np.double)
        f.linear = lin
        self.assertTrue(np.allclose(f.linear, lin))

    def test_set_angular(self):
        f = se3.Force.Zero()
        ang = rand(3)
        f.angular = ang
        self.assertTrue(np.allclose(f.angular, ang))

    def test_set_vector(self):
        f = se3.Force.Zero()
        vec =  rand(6)
        f.vector = vec
        self.assertTrue(np.allclose(f.vector, vec))

    def test_internal_sums(self):
        f1 = se3.Force.Random()
        f2 = se3.Force.Random()
        self.assertTrue(np.allclose((f1+f2).vector,f1.vector + f2.vector))
        self.assertTrue(np.allclose((f1 - f2).vector, f1.vector - f2.vector))

    def test_se3_action(self):
        f = se3.Force.Random()
        m = se3.SE3.Random()
        self.assertTrue(np.allclose((m * f).vector, np.linalg.inv(m.action.T) * f.vector))
        self.assertTrue(np.allclose((m.actInv(f)).vector, m.action.T * f.vector))
        v = se3.Motion.Random()
        f = se3.Force(np.vstack([v.vector[3:], v.vector[:3]]))
        self.assertTrue(np.allclose((v ** f).vector, zero(6)))



