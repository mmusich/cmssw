from __future__ import print_function
import json
import ROOT
from pprint import pprint
from optparse import OptionParser
from array import array

def makeNiceTrend(hist):
    hist.GetXaxis().CenterTitle(True)
    hist.GetYaxis().CenterTitle(True)
    hist.GetXaxis().SetTitleFont(42) 
    hist.GetYaxis().SetTitleFont(42)  
    hist.GetXaxis().SetTitleSize(0.065)
    hist.GetYaxis().SetTitleSize(0.065)
    hist.GetXaxis().SetTitleOffset(1.0)
    hist.GetYaxis().SetTitleOffset(1.0)
    hist.GetXaxis().SetLabelFont(42)
    hist.GetYaxis().SetLabelFont(42)
    hist.GetYaxis().SetLabelSize(.05)
    hist.GetXaxis().SetLabelSize(.05)


ROOT.TGaxis.SetMaxDigits(6);   

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="open FILE and extract info", metavar="FILE")
parser.add_option("-g", "--file2", dest="filename2", default = None,
                  help="open FILE and extract info", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=False,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

with open(options.filename) as data_file:    
    data = json.load(data_file)
    values = data["data"]
    annotations = data["annotations"]
    title   = annotations["title"]
    x_label = annotations["x_label"].replace("_"," ")
    y_label = annotations["y_label"]

if(options.filename2 is not None):
    with open(options.filename2) as data_file2:    
        data2 = json.load(data_file2)
        values2 = data2["data"]

if(options.verbose):
    pprint(values)

bins=len(values)
print("n. of bins",bins)
xvec, yvec, xvec2, yvec2 = array( 'd' ), array( 'd' ), array( 'd' ), array( 'd' )

for i,value in enumerate(values):
    xvec.append(value['x'])
    yvec.append(value['y'])

if(options.filename2 is not None):
    bins2=len(values2)
    print("n. of bins",bins2)
    for j,value2 in enumerate(values2):
        xvec2.append(value2['x'])
        yvec2.append(value2['y'])

#histo=ROOT.TH1F("histo",title+";"+x_label+";"+y_label,bins,values[0]['x'],values[bins-1]['x'])
graph=ROOT.TGraph(bins,xvec,yvec)
graph.SetTitle( title )
graph.GetXaxis().SetTitle(x_label)
graph.GetYaxis().SetTitle(y_label)

makeNiceTrend(graph)

graph.SetMarkerColor(ROOT.kBlue)
graph.SetLineColor(ROOT.kBlue)
graph.SetMarkerStyle(ROOT.kFullCircle)
graph.SetMarkerSize(1)

if(options.filename2 is not None):
    graph2=ROOT.TGraph(bins2,xvec2,yvec2)
    graph2.SetTitle( title )
    graph2.GetXaxis().SetTitle(x_label)
    graph2.GetYaxis().SetTitle(y_label)
    makeNiceTrend(graph2)
    graph2.SetMarkerColor(ROOT.kRed)
    graph2.SetLineColor(ROOT.kRed)
    graph2.SetMarkerStyle(ROOT.kFullSquare)
    graph2.SetMarkerSize(1)


canv=ROOT.TCanvas("c1","c1",1200,600)
canv.cd().SetBottomMargin(0.14);
canv.cd().SetLeftMargin(0.12);
canv.cd().SetRightMargin(0.05);
canv.cd().SetTopMargin(0.06);

canv.SetGrid()
canv.cd()
graph.Draw("APL")

if(options.filename2 is not None):
    print("printing second graph")
    graph2.Draw("PLsame")

    legend = ROOT.TLegend(0.70,0.83,0.90,0.93)
    legend.AddEntry(graph,"New Alignment","PL")
    legend.AddEntry(graph2,"Old Alignment","PL")
    legend.Draw("same")

canv.Update()

canv.SaveAs(options.filename.replace(".json",".png"))

    
