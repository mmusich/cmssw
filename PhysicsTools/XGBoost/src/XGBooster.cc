#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>  // For std::snprintf
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <stdexcept>
#include <vector>

#include "PhysicsTools/XGBoost/interface/XGBooster.h"

using namespace pat;

std::vector<std::string> read_features(const std::string& content) {
  std::vector<std::string> result;

  std::istringstream stream(content);
  char ch;

  // Expect opening '['
  stream >> ch;
  if (ch != '[') {
    throw std::runtime_error("Expected '[' at the beginning of the JSON array!");
  }

  while (stream) {
    stream >> ch;

    if (ch == ']') {
      break;
    } else if (ch == ',') {
      continue;
    } else if (ch == '"') {
      std::string feature;
      std::getline(stream, feature, '"');
      result.push_back(feature);
    } else {
      throw std::runtime_error("Unexpected character in the JSON array!");
    }
  }

  return result;
}

XGBooster::XGBooster(std::string model_file) {
  int status = XGBoosterCreate(nullptr, 0, &booster_);
  if (status != 0)
    throw std::runtime_error("Failed to create XGBooster");
  status = XGBoosterLoadModel(booster_, model_file.c_str());
  if (status != 0)
    throw std::runtime_error("Failed to load XGBoost model");
  XGBoosterSetParam(booster_, "nthread", "1");
  featuresSize_ = 0;
}

XGBooster::XGBooster(std::string model_file, std::string model_features) : XGBooster(model_file) {
  std::ifstream file(model_features);
  if (!file.is_open())
    throw std::runtime_error("Failed to open file: " + model_features);

  std::string content((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
  file.close();

  std::vector<std::string> features = read_features(content);

  for (const auto& feature : features) {
    addFeature(feature);
  }
  featuresSize_ = 0;
}

void XGBooster::addFeature(std::string name) {
  featuresSize_++;
  feature_name_to_index_[name] = featuresSize_ - 1;
}

float XGBooster::predict(std::vector<float> const& features, const int iterationEnd) {
  float result(-999.);

  if (featuresSize_ != features.size())
    throw std::runtime_error("Feature size mismatch");

  DMatrixHandle dvalues;
  XGDMatrixCreateFromMat(&features[0], 1, features.size(), 9e99, &dvalues);

  bst_ulong out_len = 0;
  const float* score = nullptr;

  char json[256];  // Make sure the buffer is large enough to hold the resulting JSON string

  // Use snprintf to format the JSON string with the external value
  std::snprintf(json,
                sizeof(json),
                R"({
    "type": 0,
    "training": false,
    "iteration_begin": 0,
    "iteration_end": %d,
    "strict_shape": false
   })",
                iterationEnd);

  // Shape of output prediction
  bst_ulong const* out_shape = nullptr;

  auto ret = XGBoosterPredictFromDMatrix(booster_, dvalues, json, &out_shape, &out_len, &score);

  if (ret == 0) {
    assert(out_len == 1 && "Unexpected prediction format");
    result = score[0];
  }

  XGDMatrixFree(dvalues);

  return result;
}
