#include <TH1F.h>
#include <TH2F.h>
#include <TCanvas.h>
#include <TFile.h>
#include <TTree.h>
#include <TMath.h>
#include <TLorentzVector.h>
#include <map>
#include <iostream>

void updateSagittaMap(TTree* tree, std::map<std::pair<int, int>, double>& theMap, TH2F*& hSagitta, const int iteration);

void analyzeZtoMM(const char* inputFile) {
  TFile* file = TFile::Open(inputFile);
  TTree* tree = dynamic_cast<TTree*>(file->Get("myanalysis/tree"));

  Float_t posTrackEta, negTrackEta, posTrackPhi, negTrackPhi, posTrackPt, negTrackPt;
  tree->SetBranchAddress("posTrackEta", &posTrackEta);
  tree->SetBranchAddress("negTrackEta", &negTrackEta);
  tree->SetBranchAddress("posTrackPhi", &posTrackPhi);
  tree->SetBranchAddress("negTrackPhi", &negTrackPhi);
  tree->SetBranchAddress("posTrackPt", &posTrackPt);
  tree->SetBranchAddress("negTrackPt", &negTrackPt);

  Float_t invMass;
  TFile* outputFile = TFile::Open("histos.root", "RECREATE");
  TH1F* hMass = new TH1F("hMass", "mass;m_{#mu#mu} [GeV];events", 200, 0., 200.);
  TH1F* hPt = new TH1F("hPt", ";muon p_{T} [GeV];events", 100, 0., 200.);
  TH1F* hEta = new TH1F("hEta", ";muon #eta;events", 100, -3.0, 3.0);
  TH1F* hPhi = new TH1F("hPhi", ";muon #phi;events", 100, -TMath::Pi(), TMath::Pi());
  TH2F* hSagitta =
      new TH2F("hSagitta", "#delta_{sagitta};muon #eta;muon #phi", 24, -2.4, 2.4, 24, -TMath::Pi(), TMath::Pi());

  std::map<std::pair<int, int>, double> sagittaCorrections;
  // initialize the map
  for (unsigned int i = 0; i < 24; i++) {
    for (unsigned int j = 0; j < 24; j++) {
      const auto& index = std::make_pair(i, j);
      sagittaCorrections[index] = 0.f;
    }
  }

  for (Long64_t i = 0; i < tree->GetEntries(); i++) {
    tree->GetEntry(i);

    TLorentzVector posTrack, negTrack, mother;
    posTrack.SetPtEtaPhiM(posTrackPt, posTrackEta, posTrackPhi, 0.105658);  // assume muon mass for tracks
    negTrack.SetPtEtaPhiM(negTrackPt, negTrackEta, negTrackPhi, 0.105658);
    mother = posTrack + negTrack;

    hPt->Fill(posTrackPt);
    hPt->Fill(negTrackPt);

    hEta->Fill(posTrackEta);
    hEta->Fill(negTrackEta);

    hPhi->Fill(posTrackPhi);
    hPhi->Fill(negTrackPhi);

    invMass = mother.M();
    hMass->Fill(invMass);
  }

  for (unsigned int iteration = 0; iteration < 20; iteration++) {
    updateSagittaMap(tree, sagittaCorrections, hSagitta, iteration);  // zero-th iteration
  }
  //updateSagittaMap(tree,sagittaCorrections,hSagitta,1); // first iteration
  //updateSagittaMap(tree,sagittaCorrections,hSagitta,2); // second iteration
  //updateSagittaMap(tree,sagittaCorrections,hSagitta,3); // third iteration

  for (unsigned int i = 0; i < 24; i++) {
    for (unsigned int j = 0; j < 24; j++) {
      const auto& index = std::make_pair(i, j);
      hSagitta->SetBinContent(i + 1, j + 1, sagittaCorrections[index]);
    }
  }

  hMass->Write();
  hPt->Write();
  hEta->Write();
  hPhi->Write();
  hSagitta->Write();

  outputFile->Close();
  file->Close();
}

void updateSagittaMap(TTree* tree, std::map<std::pair<int, int>, double>& theMap, TH2F*& hSagitta, const int iteration) {
  std::cout << "calling the updateSagittaMap" << std::endl;

  std::map<std::pair<int, int>, double> deltaCorrection;
  for (unsigned int i = 0; i < 24; i++) {
    for (unsigned int j = 0; j < 24; j++) {
      const auto& index = std::make_pair(i, j);
      deltaCorrection[index] = 0.f;
    }
  }

  Float_t posTrackEta, negTrackEta, posTrackPhi, negTrackPhi, posTrackPt, negTrackPt, invMass;
  tree->SetBranchAddress("posTrackEta", &posTrackEta);
  tree->SetBranchAddress("negTrackEta", &negTrackEta);
  tree->SetBranchAddress("posTrackPhi", &posTrackPhi);
  tree->SetBranchAddress("negTrackPhi", &negTrackPhi);
  tree->SetBranchAddress("posTrackPt", &posTrackPt);
  tree->SetBranchAddress("negTrackPt", &negTrackPt);

  for (Long64_t i = 0; i < tree->GetEntries(); i++) {
    tree->GetEntry(i);
    TLorentzVector posTrack, negTrack, mother;
    posTrack.SetPtEtaPhiM(posTrackPt, posTrackEta, posTrackPhi, 0.105658);  // assume muon mass for tracks
    negTrack.SetPtEtaPhiM(negTrackPt, negTrackEta, negTrackPhi, 0.105658);
    mother = posTrack + negTrack;
    invMass = mother.M();

    double MZ_PDG = 91.1876;

    // deal with the positive muon
    const auto& etaPlusBin = hSagitta->GetXaxis()->FindBin(posTrackEta) - 1;
    const auto& phiPlusBin = hSagitta->GetYaxis()->FindBin(posTrackPhi) - 1;
    const auto& indexPlus = std::make_pair(etaPlusBin, phiPlusBin);
    double deltaSagittaPlus = theMap[indexPlus];

    //now deal with negative muon
    const auto& etaMinusBin = hSagitta->GetXaxis()->FindBin(negTrackEta) - 1;
    const auto& phiMinusBin = hSagitta->GetYaxis()->FindBin(negTrackPhi) - 1;
    const auto& indexMinus = std::make_pair(etaMinusBin, phiMinusBin);
    double deltaSagittaMinus = theMap[indexMinus];

    double deltaMass{0.f};
    if (iteration == 0) {
      deltaMass = invMass * invMass - (MZ_PDG * MZ_PDG);
    } else {
      deltaMass = (MZ_PDG * MZ_PDG) * (posTrackPt * deltaSagittaPlus - negTrackPt * deltaSagittaMinus);
    }

    double deltaDeltaSagittaPlus =
        -(deltaMass / (2 * MZ_PDG * MZ_PDG)) * ((1 + posTrackPt * deltaSagittaPlus) / posTrackPt);
    double deltaDeltaSagittaMinus =
        (deltaMass / (2 * MZ_PDG * MZ_PDG)) * ((1 - negTrackPt * deltaSagittaMinus) / negTrackPt);

    //std::cout << "deltaMass: " << deltaMass << " DeltaDeltaSagPlus: " <<   deltaDeltaSagittaPlus << " DeltaDeltaSagMinus: " << deltaDeltaSagittaMinus << std::endl;

    deltaCorrection[indexPlus] += deltaDeltaSagittaPlus;
    deltaCorrection[indexMinus] += deltaDeltaSagittaMinus;
  }

  for (auto& [index, value] : deltaCorrection) {
    deltaCorrection[index] = value / (2 * tree->GetEntries());
  }

  std::cout << " ================================ iteration: " << iteration << std::endl;
  for (unsigned int i = 0; i < 24; i++) {
    for (unsigned int j = 0; j < 24; j++) {
      const auto& index = std::make_pair(i, j);
      std::cout << i << " " << j << " initial: " << theMap[index] << " correction: " << deltaCorrection[index]
                << std::endl;
      theMap[index] += deltaCorrection[index];
    }
  }
}
