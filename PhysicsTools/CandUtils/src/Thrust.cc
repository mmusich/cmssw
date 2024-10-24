#include "PhysicsTools/CandUtils/interface/Thrust.h"
#include <cmath>
#include <vector>

using namespace reco;

const double pi = M_PI, pi2 = 2 * pi, pi_2 = pi / 2, pi_4 = pi / 4;

void Thrust::init(const std::vector<const Candidate*>& cands) {
  int i = 0;
  for (const Candidate* cand : cands) {
    pSum_ += (p_[i] = cand->momentum()).r();
    ++i;
  }
  axis_ = axis(finalAxis(initialAxis()));
  if (axis_.z() < 0) {
    axis_ *= -1;
  }
  thrust_ = thrust(axis_);
}

Thrust::ThetaPhi Thrust::initialAxis() const {
  static const int nSegsTheta = 10, nSegsPhi = 10, nSegs = nSegsTheta * nSegsPhi;

  // Precompute cos(theta) and sin(theta) for each segment of theta
  std::vector<double> cosTheta(nSegsTheta);
  std::vector<double> sinTheta(nSegsTheta);

  for (int i = 0; i < nSegsTheta; ++i) {
    cosTheta[i] = cos(pi * i / (nSegsTheta - 1));
    sinTheta[i] = sqrt(1 - cosTheta[i] * cosTheta[i]);  // sin(theta) from cos(theta)
  }

  // Arrays to hold thrust values
  double thr[nSegs];
  double maxThrust = 0.0;
  int maxIndex = 0, maxI = 0, maxJ = 0;

  // Compute the thrust for each (theta, phi) segment
  for (int i = 0; i < nSegsTheta; ++i) {
    for (int j = 0; j < nSegsPhi; ++j) {
      double phi = pi2 * j / nSegsPhi;
      thr[i * nSegsPhi + j] = thrust(Vector(sinTheta[i] * cos(phi), sinTheta[i] * sin(phi), cosTheta[i]));
      if (thr[i * nSegsPhi + j] > maxThrust) {
        maxThrust = thr[i * nSegsPhi + j];
        maxIndex = i * nSegsPhi + j;
        maxI = i;
        maxJ = j;
      }
    }
  }

  // Interpolation: Maximize thrust using parabolic fit
  double maxPhiInd = parabolicFit(thr, maxIndex, maxI, maxJ, nSegsTheta, nSegsPhi);

  double maxThetaInd;
  if (maxI == 0 || maxI == (nSegsTheta - 1)) {
    maxThetaInd = maxI;  // Edge cases
  } else {
    maxThetaInd = parabolicFit(thr, maxIndex, maxI, maxJ, nSegsTheta, nSegsPhi);
  }

  return ThetaPhi(pi * (maxThetaInd + maxI) / (nSegsTheta - 1), pi2 * (maxPhiInd + maxJ) / nSegsPhi);
}

// Helper for parabolic fitting
double Thrust::parabolicFit(double* thr, int index, int indI, int indJ, int nSegsTheta, int nSegsPhi) const {
  double a, b, c = thr[index];
  int ind1 = indJ + 1, ind2 = indJ - 1;

  if (ind1 >= nSegsPhi)
    ind1 -= nSegsPhi;
  if (ind2 < 0)
    ind2 += nSegsPhi;

  // Parabolic fitting on phi
  a = (thr[ind1] + thr[ind2] - 2 * c) / 2;
  b = thr[ind1] - a - c;

  double maxPhiInd = 0;
  if (a != 0) {
    maxPhiInd = -b / (2 * a);  // Maximize the parabola
  }
  return maxPhiInd;
}

Thrust::ThetaPhi Thrust::finalAxis(ThetaPhi best) const {
  static const double epsilon = 0.0001;
  double maxChange1 = 0.0, maxChange2 = 0.0;
  int iterations = 0, maxIterations = 1000;

  do {
    // Theta refinement
    parabola(best.theta, best.phi, epsilon, maxChange1);
    best.theta += maxChange1 * epsilon;

    // Correct theta and phi if out of bounds
    if (best.theta > pi) {
      best.theta = pi - (best.theta - pi);
      best.phi += pi;
    }
    if (best.theta < 0) {
      best.theta *= -1;
      best.phi += pi;
    }
    if (best.phi > pi2)
      best.phi -= pi2;

    // Phi refinement
    parabola(best.theta, best.phi, epsilon, maxChange2);
    best.phi += maxChange2 * epsilon;

    if (best.phi < 0)
      best.phi += pi2;
    if (best.phi > pi2)
      best.phi -= pi2;

    iterations++;
  } while (iterations < maxIterations && (fabs(maxChange1) > 1e-5 || fabs(maxChange2) > 1e-5));

  return best;
}

// Optimized parabola fitting using known axis vectors
void Thrust::parabola(double theta, double phi, double epsilon, double& maxChange) const {
  Vector a1 = axis(theta, phi);
  Vector a2 = axis(theta + epsilon, phi);
  Vector a3 = axis(theta - epsilon, phi);

  double t1 = thrust(a1);
  double t2 = thrust(a2);
  double t3 = thrust(a3);

  double a = (t2 - 2 * t1 + t3) / 2;
  double b = t2 - a - t1;
  maxChange = (a != 0) ? -b / (2 * a) : 0;
}

Thrust::Vector Thrust::axis(double theta, double phi) const {
  double sinTheta = sin(theta);
  return Vector(sinTheta * cos(phi), sinTheta * sin(phi), cos(theta));
}

double Thrust::thrust(const Vector& axis) const {
  double sum = 0;
  for (unsigned int i = 0; i < n_; ++i) {
    sum += fabs(axis.Dot(p_[i]));  // Accumulate dot products
  }
  return (pSum_ > 0) ? sum / pSum_ : 0;
}
