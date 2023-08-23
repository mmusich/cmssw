#include "Alignment/OfflineValidation/interface/TkAlMap.h"

void TkAlMap::set_var(std::string var, std::vector<double> var_range) {
  std::cout << "TkAlMap: setting#include <sstream> variable to " << var << std::endl;
  
  this->var = var;
  this->var_name = var;
  this->var_units = "cm";
  this->var_scale = 1.0;
  this->var_min = var_range[0];
  this->var_max = var_range[1];
  
  // Placeholder for KNOWN_VARIABLES
  std::map<std::string, std::map<std::string, std::string>> KNOWN_VARIABLES;
  
  if (KNOWN_VARIABLES.find(var) != KNOWN_VARIABLES.end()) {
    this->var_name = KNOWN_VARIABLES[var]["name"];
    this->var_units = KNOWN_VARIABLES[var]["units"];
    this->var_scale = std::stod(KNOWN_VARIABLES[var]["scale"]);
    if (std::isnan(this->var_min)) this->var_min = std::stod(KNOWN_VARIABLES[var]["range"][0]);
    if (std::isnan(this->var_max)) this->var_max = std::stod(KNOWN_VARIABLES[var]["range"][1]);
  }
  
  // Implement the set_canvas function
  this->set_canvas();
}

void TkAlMap::set_canvas() {
    std::string canv_name = "canvas_" + this->tracker + "_" + this->var;
    if (this->two_sigma_cap) {
        canv_name += "_cap";
    }
    this->canvas = new TCanvas(canv_name.c_str(), ("TkAlMap " + this->var + " canvas").c_str(), this->width, this->height);
    std::cout << "Actual w: " << this->canvas->GetWw() << ", Actual h: " << this->canvas->GetWh() << std::endl;
}

void TkAlMap::setup_colors() {
    this->load_var();
    this->prepare_map_colors();
    this->fill_colors();
}

void TkAlMap::prepare_map_colors() {
  std::cout << "TkAlMap: preparing map colors" << std::endl;
  
  this->colors.clear();
  int col_idx = this->start_color_idx + this->n_color_color_bar + 10;
  this->col_dic.clear();
  this->rgb_map.clear();
  
  for (auto val : this->val_list) {
    double cap_val = val;
    if (cap_val > this->max_val) cap_val = this->max_val;
    if (cap_val < this->min_val) cap_val = this->min_val;
    
    double r, g, b;
    std::tie(r, g, b) = this->get_color_rgb(cap_val);
    
    int idx = this->get_color_rgb_idx(cap_val);
    if (std::find(this->colors.begin(), this->colors.end(), idx) != this->colors.end()) continue;
    
    this->colors.push_back(idx);
    col_idx++;
    
    this->rgb_map[idx] = col_idx;
    
    try {
      TColor *col = gROOT->GetColor(col_idx);
      col->SetRGB(r / 255.0, g / 255.0, b / 255.0);
      this->col_dic[idx] = col;
    } catch (...) {
      this->col_dic[idx] = new TColor(col_idx, r / 255.0, g / 255.0, b / 255.0);
    }
  }
  std::cout << "TkAlMap: map contains " << this->colors.size() << " colors" << std::endl;
}

void TkAlMap::set_palette(int palette) {
    this->palette = palette;
    std::string pal_str = "TkAlMap: setting the palette to " + std::to_string(palette);
    
    if (palette == 1)
        pal_str += " (rainbow)";
    else if (palette == 2)
        pal_str += " (B->R diverging)";
    else
        throw std::invalid_argument("TkAlMap: unknown palette value " + std::to_string(palette) +
                                    ", allowed values are 1 and 2");

    std::cout << pal_str << std::endl;
    // ROOT.gStyle.SetPalette(len(this->colors), this->colors);
    // ROOT.gStyle.SetPalette(len(this->palette), this->palette);
    // Note: The equivalent C++ functions to set the palette should be called here
}

std::tuple<int, int, int> TkAlMap::get_color_rgb(double val) {
    double value_frac = 0.0;  // Initialize value_frac
    if (this->max_val == nullptr || this->min_val == nullptr) {
        value_frac = val;
    } else {
        if (this->do_tanh) {
            double val_th = std::tanh((val - this->mean_val) / (this->std_val));
            double max_th = std::tanh((this->max_val - this->mean_val) / (this->std_val));
            double min_th = std::tanh((this->min_val - this->mean_val) / (this->std_val));
            value_frac = (val_th - min_th + 0.0) / (max_th - min_th);
        } else {
            double value_range = this->max_val - this->min_val;
            if (value_range == 0.0) {
                value_frac = 0.5;
            } else {
                value_frac = (val - this->min_val + 0.0) / (value_range + 0.0);
            }
        }
    }

    int r, g, b;
    if (this->palette == 1) {
        r = 255;
        g = 255;
        b = 255;

        if (value_frac < 0.25) {
            r = 0;
            g = static_cast<int>(255. * (value_frac / 0.25));
            b = 255;
        } else if (value_frac < 0.5) {
            r = 0;
            g = 255;
            b = static_cast<int>(255. * (1. - (value_frac - 0.25) / 0.25));
        } else if (value_frac < 0.75) {
            r = static_cast<int>(255. * ((value_frac - 0.5) / 0.25));
            g = 255;
            b = 0;
        } else {
            r = 255;
            g = static_cast<int>(255. * (1. - (value_frac - 0.75) / 0.25));
            b = 0;
        }
    } else if (this->palette == 2) {
        std::array<int, 3> red   = {59, 76, 192};
        std::array<int, 3> blue  = {180, 4, 38};
        std::array<int, 3> white = {255, 255, 255};
        std::tie(r, g, b) = DivergingColor(red, blue, white, value_frac);
    } else {
        throw std::invalid_argument("TkAlMap: unknown palette value " + std::to_string(this->palette) +
                                    ", allowed values are 1 and 2");
    }

    return std::make_tuple(r, g, b);
}

int TkAlMap::get_color_rgb_idx(double val) {
    auto [r, g, b] = get_color_rgb(val);
    int offset = 100;
    return static_cast<int>(r * 255 * 255 + g * 255 + r + g + b + offset);
}

void TkAlMap::fill_colors() {
    std::cout << "TkAlMap: filling the colors" << std::endl;
    for (const auto& module : mod_val_dict) {
        if (TkAlMap_TPL_dict.count(module.first)) {
            double val = module.second;
            double cap_val = val;
            if (cap_val > max_val) cap_val = max_val;
            if (cap_val < min_val) cap_val = min_val;
            int rgb = get_color_rgb_idx(cap_val);
            int col = rgb_map[rgb];
            TkAlMap_TPL_dict[module.first]->SetFillColor(col);
        } // else: std::cout << "Warning: Unknown module " << module.first << std::endl;
    }
}

void TkAlMap::set_colorbar_axis() {
    std::cout << "TkAlMap: setting color bar axis" << std::endl;
    double b_x1 = image_x1;
    double b_x2 = image_x2;
    double b_y1 = 0.06;
    double b_y2 = 0.06;
    double b_width = 0.01;
    color_bar_axis = new TGaxis(b_x1, b_y1, b_x2, b_y2, min_val, max_val, 50510, "+S");
    color_bar_axis->SetName("color_bar_axis");
    color_bar_axis->SetLabelSize(0.02);
    color_bar_axis->SetTickSize(0.01);
    if (two_sigma_cap && !default_range)
        color_bar_axis->SetTitle("{#mu - 2#sigma #leq " + var_name + " #leq #mu + 2#sigma} [" + var_units + "]");
    else if (default_range)
      color_bar_axis->SetTitle("{" + std::to_string(min_val) + " #leq " + var_name + " #leq " + std::to_string(max_val) + "} [" + var_units + "]");
    else
        color_bar_axis->SetTitle(var_name + " [" + var_units + "]");
    color_bar_axis->SetTitleSize(0.025);
}

void TkAlMap::set_colorbar_colors() {
    std::cout << "TkAlMap: initialize color bar colors" << std::endl;
    double col_step, val;

    if (max_val == nullptr || min_val == nullptr) {
        col_step = 1. / (n_color_color_bar + 0.);
        val = col_step / 2.;
    } else {
        double b_range = *max_val - *min_val;
        col_step = (b_range + 0.) / (n_color_color_bar + 0.);
        val = *min_val + col_step / 2.;
    }

    double b_x1 = image_x1;
    double b_x2 = image_x2;
    double b_y1 = 0.06;
    double b_y2 = 0.06;
    double b_width = 0.01;
    double b_xrange = b_x2 - b_x1;
    double b_yrange = b_y2 - b_y1;
    double b_dx = (b_xrange + 0.) / (n_color_color_bar + 0.);
    double b_dy = (b_yrange + 0.) / (n_color_color_bar + 0.);

    for (int col_idx = start_color_idx; col_idx < start_color_idx + n_color_color_bar; ++col_idx) {
        double r, g, b;
        std::tie(r, g, b) = get_color_rgb(val);

        TColor *col = nullptr;
        try {
            col = gROOT->GetColor(col_idx);
            col->SetRGB((r + 0.) / 255., (g + 0.) / 255., (b + 0.) / 255.);
            color_bar_colors[col_idx] = col;
        } catch (...) {
            col = new TColor(col_idx, (r + 0.) / 255., (g + 0.) / 255., (b + 0.) / 255.);
            color_bar_colors[col_idx] = col;
        }

        double x1 = b_x1;
        double y1 = b_y1;
        double x2 = x1 + b_dx;
        double y2 = y1 + b_dy + b_width;
        double x[4] = {x1, x1, x2, x2};
        double y[4] = {y1, y2, y2, y1};

        color_bar[col_idx] = new TPolyLine(4, x, y);
        color_bar[col_idx]->SetFillColor(col_idx);
        color_bar[col_idx]->SetLineColor(col_idx);

        val += col_step;
        b_x1 += b_dx;
        b_y1 += b_dy;
    }
}

void TkAlMap::load_tree() {
  std::cout << "TkAlMap: loading tree" << std::endl;
  TString tree_name = "alignTree";
  TFile *r_file = new TFile(root_file.c_str());
  if (!r_file || r_file->IsZombie()) {
    std::cerr << "The file \"" << root_file << "\" could not be opened" << std::endl;
    throw std::runtime_error("File open error");
  }
  
  TTree *tree_tmp = nullptr;
  r_file->GetObject(tree_name, tree_tmp);
  if (!tree_tmp) {
    std::cerr << "The tree \"" << tree_name << "\" was not found in file \"" << root_file << "\"" << std::endl;
    throw std::runtime_error("Tree not found error");
  }
  
  tmp_file_name = Form("%lld_TkAlMapTempFile.root", time(0));
  tmp_file = new TFile(tmp_file_name, "recreate");
  tree = tree_tmp->CloneTree();
  r_file->Close();
  is_cleaned = false;
  
  if (!tree) {
    std::cerr << "The tree \"" << tree_name << "\" could not be cloned" << std::endl;
    throw std::runtime_error("Tree clone error");
  }
}

void TkAlMap::load_var() {
    std::cout << "TkAlMap: loading variable values" << std::endl;

    mod_val_dict.clear();
    val_list.clear();

    for (Long64_t eventIdx = 0; eventIdx < tree->GetEntries(); ++eventIdx) {
        tree->GetEntry(eventIdx);
        Long64_t module = alignTree.id;
        double val;

        if (var == "rdphi") {
            val = alignTree.r * alignTree.dphi;
        } else {
            val = getVal(alignTree, var);
        }
        
        val *= var_scale;

        mod_val_dict[module] = val;
        
        if (TkAlMap_TPL_dict.find(module) != TkAlMap_TPL_dict.end()) {
            val_list.push_back(val);
        }
    }

    if (val_list.empty()) {
        std::cout << "Warning: no values filled, 0 moduleId's matched" << std::endl;
        for (int idx = 0; idx < 41; ++idx) {
            val_list.push_back(-10 + idx * 0.5);
        }
    }

    sort(val_list.begin(), val_list.end());

    mean_val = mean(val_list);
    std_val = StdDev(val_list);
    min_val = *std::min_element(val_list.begin(), val_list.end());
    max_val = *std::max_element(val_list.begin(), val_list.end());

    if (two_sigma_cap && !default_range) {
        std::cout << "-- Capping max and min: " << std::endl;
        std::cout << "---- True values   : " << max_val << ", " << min_val << std::endl;
        min_val = std::max(min_val, mean_val - 2 * std_val);
        max_val = std::min(max_val, mean_val + 2 * std_val);
        std::cout << "---- Capped values : " << max_val << ", " << min_val << std::endl;
    }

    if (default_range && var_min != nullptr && var_max != nullptr) {
        std::cout << "-- Capping max and min to default ranges: " << std::endl;
        std::cout << "---- True values   : " << max_val << ", " << min_val << std::endl;
        min_val = *var_min;
        max_val = *var_max;
        std::cout << "---- Capped values : " << max_val << ", " << min_val << std::endl;
    }

    if (min_val == max_val) {
        std::cout << "Warning: minimum value was equal to maximum value, " << max_val << std::endl;
        min_val = mean_val - 1.0;
        max_val = mean_val + 1.0;
    }
}

void TkAlMap::detect_tracker_version() {
    std::cout << "TkAlMap: detecting Tk version" << std::endl;
    int phase = -1;

    for (Long64_t eventIdx = 0; eventIdx < tree->GetEntries(); ++eventIdx) {
        tree->GetEntry(eventIdx);
        Long64_t module = alignTree.id;

        if (module > 303040000 && module < 306450000) {
            phase = 1;
            break;
        } else if (module > 302055000 && module < 302198000) {
            phase = 0;
            break;
        }
    }

    if (phase == -1) {
      throw std::runtime_error("TkAlMap: unknown tracker detected, is this phase2?");
    }

    std::string phase_str = "phase" + std::to_string(phase);
    std::cout << "TkAlMap: " << phase_str << " tracker detected" << std::endl;

    if (GEO_file.find(phase_str) == std::string::npos) {
        std::cout << "TkAlMap: changing tracker to " << phase_str << ", if this is unwanted set \"check_tracker\" to False" << std::endl;
        GEO_file = "TkAlMapDesign_" + phase_str + "_cfg.py";
        // load_geometry(); // You need to implement this function.
    }
}

void TkAlMap::load_geometry() {
    std::string source_path = getenv("CMSSW_BASE") + "/src/";
    std::map<std::string, std::map<std::string, std::map<std::string, dynamic>>> var;

    if (sys.version_info[0] == 2) {
        // execfile(source_path + self.cfg_path + self.GEO_file, var);
    } else if (sys.version_info[0] == 3) {
        // string _filename = source_path + self.cfg_path + self.GEO_file;
        // exec(compile(open(_filename, "rb").read(), _filename, "exec"), var);
    }

    std::map<std::string, std::map<std::string, dynamic>> MapStructure = var["TkMap_GEO"];

    std::map<std::string, std::map<std::string, dynamic>> all_modules;
    std::map<std::string, std::map<std::string, dynamic>> all_text;
    double x_max = -9999.0;
    double y_max = -9999.0;
    double x_min = 9999.0;
    double y_min = 9999.0;

    for (const auto& det_entry : MapStructure) {
        const std::string& det = det_entry.first;
        if (this->tracker.find("pixel") != std::string::npos && det.find("pixel") == std::string::npos) {
            continue;
        } else if (this->tracker.find("strips") != std::string::npos && det.find("strips") == std::string::npos) {
            continue;
        }

        for (const auto& sub_entry : det_entry.second) {
            const std::string& sub = sub_entry.first;
            for (const auto& part_entry : sub_entry.second) {
                const std::string& part = part_entry.first;
                if (part == "latex") {
                    all_text[det + "_" + sub] = part_entry.second;
                    continue;
                }
                
                // ... Implement the rest of the logic here

            } // end part loop
        } // end sub loop
    } // end det loop

    // ... Continue implementing the remaining logic here
}

void TkAlMap::draw_title() {
    ROOT::Math::LatexText TL;
    TL.SetTextSize(0.035);
    TL.SetTextFont(42);
    TL.SetTextAlign(13);
    double x1 = this->image_x1;
    double y1 = 1 - (5. / (this->y_scale + 0.));
    this->canvas->cd();
    TL.DrawLatex(x1, y1, this->title);
}

void TkAlMap::draw_cms_prelim() {
    ROOT::Math::LatexText TL;
    double factor = 1. / 0.82;
    TL.SetTextSize(0.035 * factor);
    TL.SetTextAlign(11);
    TL.SetTextFont(61);

    unsigned int w_cms = 0;
    unsigned int h_cms = 0;
    TL.GetTextExtent(w_cms, h_cms, "CMS");
    double x1 = this->image_x1;
    double y1 = 1. - (h_cms + 0.) / (this->height + 0.) - (1. / (this->y_scale + 0.));
    this->canvas->cd();
    TL.DrawLatex(x1, y1, "CMS");

    TL.SetTextSize(0.035);
    TL.SetTextFont(42);
    double x1_prel = x1 + 1.1 * (w_cms + 0.) / (this->width + 0.);
    TL.DrawLatex(x1_prel, y1, "#it{Preliminary}");

    this->draw_event_info(y1);
}

void TkAlMap::draw_event_info(double y) {
    ROOT::Math::LatexText TL;
    TL.SetTextSize(0.035);
    TL.SetTextFont(42);
    TL.SetTextAlign(31);

    double x1 = this->image_x2;
    double y1 = y;
    this->canvas->cd();
    TL.DrawLatex(x1, y1, "pp collisions 13TeV");
}

void TkAlMap::draw_text() {
    std::cout << "TkAlMap: drawing text" << std::endl;
    this->canvas->cd();
    ROOT::Math::LatexText TL;
    TL.SetTextSize(0.025);
    for (const auto& key : this->TkAlMap_text_dict) {
        TL.SetTextAlign(this->TkAlMap_text_dict[key]["alignment"]);
        TL.DrawLatex(this->TkAlMap_text_dict[key]["x"], this->TkAlMap_text_dict[key]["y"], this->TkAlMap_text_dict[key]["text"]);
    }
    this->draw_cms_prelim();
    this->draw_title();
    this->canvas->Update();
}

void TkAlMap::draw_TPL() {
    std::cout << "TkAlMap: drawing PolyLines" << std::endl;
    this->canvas->cd();
    for (const auto& module : this->TkAlMap_TPL_dict) {
        this->TkAlMap_TPL_dict[module.first]->Draw("f");
        this->TkAlMap_TPL_dict[module.first]->Draw();
    }
    this->canvas->Update();
}

void TkAlMap::draw_color_bar() {
    std::cout << "TkAlMap: drawing color bar" << std::endl;
    this->canvas->cd();
    for (const auto& box : this->color_bar) {
        this->color_bar[box.first]->Draw("f");
        //this->color_bar[box.first]->Draw();
    }
    this->color_bar_axis->Draw();
    this->canvas->Update();
}

void TkAlMap::save(const std::string& out_dir, const std::string& extension) {
    std::string name = "_";
    name += "TkAlMap" + this->tracker + "_" + this->var;
    if (this->two_sigma_cap && !this->default_range) {
        name += "_4sig";
    } else if (this->default_range) {
        name += "_drange";
    }
    std::string path = out_dir + "/" + name + "." + extension;
    std::cout << "TkAlMap: saving canvas in \"" << path << "\"" << std::endl;
    this->canvas->SaveAs(path.c_str());
}

void TkAlMap::analyse() {
    this->setup_colors();
    this->set_colorbar_axis();
    if (this->do_tanh) {
        this->set_colorbar_colors();
    }
    this->draw_TPL();
    this->draw_text();
    this->draw_color_bar();
}

void TkAlMap::plot_variable_distribution(int nbins, const std::string& out_dir) {
    std::cout << "TkAlMap: drawing variable distribution" << std::endl;
    std::string canv_name = "histogram_canvas_" + this->tracker + "_" + this->var;
    if (this->two_sigma_cap) {
        canv_name += "_cap";
    }
    TCanvas *canvas = new TCanvas(canv_name.c_str(), ("TkAlMap " + this->var + " histogram canvas").c_str(), 800, 800);

    double h_min = std::min(std::min(this->val_list), this->mean_val - 2 * this->std_val) - this->std_val;
    double h_max = std::max(std::max(this->val_list), this->mean_val + 2 * this->std_val) + this->std_val;
    TH1F *hist = new TH1F((this->var + "_hist").c_str(), "Variable distribution", nbins, h_min, h_max);
    for (double val : this->val_list) {
        hist->Fill(val);
    }
    hist->GetXaxis()->SetTitle((this->var_name + " [" + this->var_units + "]").c_str());
    hist->GetYaxis()->SetTitle("modules");
    gStyle->SetOptStat(0);
    hist->Draw("e1");
    canvas->Update();
    TLine *left = new TLine(this->mean_val - 2 * this->std_val, canvas->GetUymin(), this->mean_val - 2 * this->std_val, canvas->GetUymax());
    left->SetLineColor(2);
    left->SetLineStyle(9);
    left->Draw();
    TLine *right = new TLine(this->mean_val + 2 * this->std_val, canvas->GetUymin(), this->mean_val + 2 * this->std_val, canvas->GetUymax());
    right->SetLineColor(2);
    right->SetLineStyle(9);
    right->Draw();
    TLine *mid = new TLine(this->mean_val, canvas->GetUymin(), this->mean_val, canvas->GetUymax());
    mid->SetLineColor(1);
    mid->SetLineStyle(9);
    mid->Draw();
    canvas->Update();
    std::string name = "_VariableDistribution_" + this->var + "_" + this->tracker;
    std::string path = out_dir + "/" + name + ".png";
    canvas->SaveAs(path.c_str());

    // Clean up allocated memory
    delete canvas;
    delete hist;
    delete left;
    delete right;
    delete mid;
}

void TkAlMap::clean_up() {
  if (!this->is_cleaned) {
    std::cout << "TkAlMap: deleting temporary file \"" << this->tmp_file_name << "\"" << std::endl;
    this->tmp_file->Close();
    remove(this->tmp_file_name.c_str());
    this->is_cleaned = true;
  }
}

TkAlMap::~TkAlMap() {
  this->clean_up();
}
