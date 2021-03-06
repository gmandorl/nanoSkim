

import ROOT
import array
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class exampleProducer(Module):
    def __init__(self, jetSelection, muSelection):
        self.jetSel = jetSelection
        self.muSel = muSelection
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("EventMass",  "F");
        self.out.branch("MuonMass",  "F");
        self.out.branch("qqMass",  "F");
        self.out.branch("jetIdx1",  "I");
        self.out.branch("jetIdx2",  "I");
        self.out.branch("jetNumber",  "I");
        self.out.branch("muonNumber",  "I");
        self.out.branch("Jet_VBFselected", "F", 1, "nJet");
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        jets = Collection(event, "Jet")
        eventSum = ROOT.TLorentzVector()
        
        mu1_charge = 0
        count_mu = 0
        dimuonSelection = False
        mu1 = ROOT.TLorentzVector()
        mu2 = ROOT.TLorentzVector()
        dimuonMass = 0
        
        jet1 = ROOT.TLorentzVector()
        jet2 = ROOT.TLorentzVector()


        if len(filter(self.muSel,muons)) < 2:
            return False
        muonNumber = len(filter(self.muSel,muons))
        for lep in muons :
            eventSum += lep.p4()
            if lep.pfRelIso04_all<0.25 and abs(lep.pdgId)==13 and abs(lep.dz) < 0.2 and lep.dxy < 0.05 and not dimuonSelection :
                if count_mu == 1 and (lep.charge*mu1_charge)<0:
                    mu2.SetPtEtaPhiM(lep.pt,lep.eta, lep.phi, 0.105658375)
                    dimuonSelection = True
                if count_mu == 0:
                    mu1.SetPtEtaPhiM(lep.pt,lep.eta, lep.phi, 0.105658375)#105,6583745(24) MeV
                    mu1_charge = lep.charge
                    count_mu +=1
        #if not dimuonSelection : return False           
        if max(mu1.Pt(), mu2.Pt())<29 : return False # muons are ordered in lep.pt, not in lep.pt_corrected
        if min(mu1.Pt(), mu2.Pt())<9  : return False # muons are ordered in lep.pt, not in lep.pt_corrected
        #print "muon pt:   ", mu1.Pt(), mu2.Pt()
        dimuon = mu1 + mu2
        dimuonMass = dimuon.M()
        if dimuon.M()<100:
            return False
                
        
        
        
        jetIdx1=-1
        jetIdx2=-1
        VBFselectedJet = array.array('f', [0 for x in range(len(jets))])     
        if len(filter(self.jetSel,jets)) < 2:
            return False    
        jetNumber = len(filter(self.jetSel,jets))
        dijetSelection  = False
        count_jet = 0
        for n in range(len(jets)) :
            j = jets[n]
            VBFselectedJet[n] = 0
            if self.jetSel(j) :
                eventSum += j.p4()
                if j.jetId>0 and j.puId>0 and not dijetSelection:
                    if j.muonIdx1>-1 and muons[j.muonIdx1].pfRelIso04_all<0.25 : continue   
                    if j.muonIdx2>-1 and muons[j.muonIdx2].pfRelIso04_all<0.25 : continue   
                    if count_jet ==1:
                        jet2=j.p4()
                        jet2.SetPtEtaPhiM(j.pt,jet2.Eta(), jet2.Phi(), j.mass)
                        dijetSelection = True
                        VBFselectedJet[n] = 1
                        jetIdx2=n
                    if count_jet == 0:
                        jet1=j.p4()
                        jet1.SetPtEtaPhiM(j.pt,jet1.Eta(), jet1.Phi(), j.mass)
                        count_jet +=1
                        VBFselectedJet[n] = 1
                        jetIdx1=n

        if not dijetSelection : return False
        #print "jet pt:   ", jet1.Pt(), jet2.Pt()
        if min(jet1.Pt(), jet2.Pt())<20  : return False
        if max(jet1.Pt(), jet2.Pt())<30 : return False

        dijetMass = 0    
        dijetMass = (jet1 + jet2).M()
        if dijetMass < 180 : return False


        self.out.fillBranch("EventMass",eventSum.M())
        self.out.fillBranch("MuonMass",dimuonMass)
        self.out.fillBranch("qqMass",dijetMass)
        self.out.fillBranch("jetIdx1",jetIdx1)
        self.out.fillBranch("jetIdx2",jetIdx2)
        self.out.fillBranch("jetNumber",jetNumber)
        self.out.fillBranch("muonNumber",muonNumber)
        self.out.fillBranch("Jet_VBFselected",VBFselectedJet)
        return True
    
    
    
exampleModuleDATA = lambda : exampleProducer(jetSelection= lambda j : j.pt > 20, muSelection= lambda mu : mu.pt > 9 ) 












