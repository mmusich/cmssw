// system includes
#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <string>
#include <sstream>

// ROOT includes
#include "TString.h"
#include "TColor.h"
#include "TCanvas.h"
#include "TTree.h"
#include "TLatex.h"
#include "TFile.h"
#include "TPolyLine.h"
#include "TStyle.h"

struct VariableInfo {
  std::string name;
  std::string units;
  double scale;
  std::vector<double> range;
};

std::map<std::string, VariableInfo> KNOWN_VARIABLES = {
  {"dr", {"#Deltar", "#mum", 10000.0, {-200.0, 200.0}}},
  {"dx", {"#Deltax", "#mum", 10000.0, {-200.0, 200.0}}},
  {"dy", {"#Deltay", "#mum", 10000.0, {-200.0, 200.0}}},
  {"dz", {"#Deltaz", "#mum", 10000.0, {-200.0, 200.0}}},
  {"rdphi", {"r #Delta#phi", "#mum rad", 10000.0, {-200.0, 200.0}}},
  {"dphi", {"#Delta#phi", "mrad", 1000.0, {-100.0, 100.0}}},
  {"dalpha", {"#Delta#alpha", "mrad", 1000.0, {-100.0, 100.0}}},
  {"dbeta", {"#Delta#beta", "mrad", 1000.0, {-100.0, 100.0}}},
  {"dgamma", {"#Delta#gamma", "mrad", 1000.0, {-100.0, 100.0}}},
  {"du", {"#Deltau", "#mum", 10000.0, {-200.0, 200.0}}},
  {"dv", {"#Deltav", "#mum", 10000.0, {-200.0, 200.0}}},
  {"dw", {"#Deltaw", "#mum", 10000.0, {-200.0, 200.0}}},
  {"da", {"#Deltaa", "mrad", 1000.0, {-100.0, 100.0}}},
  {"db", {"#Deltab", "mrad", 1000.0, {-100.0, 100.0}}},
  {"dg", {"#Deltag", "mrad", 1000.0, {-100.0, 100.0}}}};

double mean(const std::vector<double>& data_list) {
  double sum = 0.0;
  for (double point : data_list) {
    sum += point;
  }
  return sum / (data_list.size() + 0.0);
}

double StdDev(const std::vector<double>& data_list) {
  double s2 = 0.0;
  double m = mean(data_list);
  for (double point : data_list) {
    s2 += (point - m) * (point - m);
  }
  return sqrt(s2 / (data_list.size() + 0.0));
}

std::map<int, std::map<std::string, std::vector<double>>> read_TPLfile(const std::string& file_name) {
  std::ifstream o_file(file_name);
  std::vector<std::string> lines;
  std::string line;
  
  while (std::getline(o_file, line)) {
    lines.push_back(line);
  }
  o_file.close();
  
  std::map<int, std::map<std::string, std::vector<double>>> TPL_dict;
  for (const std::string& line : lines) {
    if (line.find('#') != std::string::npos) {
      continue;
    }
    std::vector<std::string> splt_line;
    std::string coo;
    std::istringstream iss(line);
    while (iss >> coo) {
      splt_line.push_back(coo);
    }
    
    int det_id = std::stoi(splt_line[0]);
    std::vector<double> x;
    std::vector<double> y;
    for (size_t idx = 1; idx < splt_line.size(); ++idx) {
      try {
	double val = std::stod(splt_line[idx]);
	if (idx % 2 == 0) {
	  y.push_back(val);
	} else {
	  x.push_back(val);
	}
      } catch (const std::invalid_argument& e) {
	continue;
      }
    }
    TPL_dict[det_id] = {{"x", x}, {"y", y}};
  }
  return TPL_dict;
}


class TkAlMap {
private:
    std::string GEO_file;
    std::string tracker;
    int width;
    int height;
    std::string title;
    bool default_range;
    bool two_sigma_cap;
    std::string root_file;
    bool do_tanh;
    
    // ... Other private members ...

public:
  TkAlMap(std::string variable, std::string title, std::string root_file,
	  bool use_default_range = false, bool two_sigma_cap = false, int height = 1400,
	  std::string GEO_file = "TkAlMapDesign_phase1_cfg.py", std::string tracker = "full",
	  int palette = 2, bool do_tanh = false, bool check_tracker = true){
    
    gStyle->SetLineScalePS(1);
    
    GEO_file = GEO_file;
    tracker = tracker;
    width = height;
    height = height;
    title = title;
    default_range = use_default_range;
    two_sigma_cap = two_sigma_cap;
    root_file = root_file;
    do_tanh = do_tanh;
    
    // ... Initialize other members ...
  }
  
  ~TkAlMap(); // destructor

  // ... Define other member functions ...
  void set_var(std::string var, std::vector<double> var_range = {NAN, NAN});   
  void set_canvas() ;
  void setup_colors() ;
  void prepare_map_colors() ;
  void set_palette(int palette) ;
  std::tuple<int, int, int> get_color_rgb(double val) ;
  int get_color_rgb_idx(double val) ;
  void fill_colors() ;
  void set_colorbar_axis() ;
  void set_colorbar_colors() ;
  void load_tree() ;
  void load_var() ;
  void detect_tracker_version() ;
  void load_geometry() ;
  void draw_title() ;
  void draw_cms_prelim() ;
  void draw_event_info(double y) ;
  void draw_text() ;
  void draw_TPL() ;
  void draw_color_bar() ;
  void save(const std::string& out_dir, const std::string& extension) ;
  void analyse() ;
  void plot_variable_distribution(int nbins, const std::string& out_dir) ;
  void clean_up() ;
};
