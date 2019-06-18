

import ROOT
import array
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class vbfhmmProducer(Module):
    def __init__(self, jetSelection, muSelection, data):
        self.jetSel = jetSelection
        self.muSel = muSelection
        self.data = data
        self.jesVariation = ['pt_nom', 'pt_jesAbsoluteStatDown', 'pt_jesAbsoluteScaleDown', 'pt_jesAbsoluteFlavMapDown', 'pt_jesAbsoluteMPFBiasDown', 'pt_jesFragmentationDown', 'pt_jesSinglePionECALDown', 'pt_jesSinglePionHCALDown', 'pt_jesFlavorQCDDown', 'pt_jesTimePtEtaDown', 'pt_jesRelativeJEREC1Down', 'pt_jesRelativeJEREC2Down', 'pt_jesRelativeJERHFDown', 'pt_jesRelativePtBBDown', 'pt_jesRelativePtEC1Down', 'pt_jesRelativePtEC2Down', 'pt_jesRelativePtHFDown', 'pt_jesRelativeBalDown', 'pt_jesRelativeSampleDown', 'pt_jesRelativeFSRDown', 'pt_jesRelativeStatFSRDown', 'pt_jesRelativeStatECDown', 'pt_jesRelativeStatHFDown', 'pt_jesPileUpDataMCDown', 'pt_jesPileUpPtRefDown', 'pt_jesPileUpPtBBDown', 'pt_jesPileUpPtEC1Down', 'pt_jesPileUpPtEC2Down', 'pt_jesPileUpPtHFDown', 'pt_jesPileUpMuZeroDown', 'pt_jesPileUpEnvelopeDown', 'pt_jesSubTotalPileUpDown', 'pt_jesSubTotalRelativeDown', 'pt_jesSubTotalPtDown', 'pt_jesSubTotalScaleDown', 'pt_jesSubTotalAbsoluteDown', 'pt_jesSubTotalMCDown', 'pt_jesTotalDown', 'pt_jesTotalNoFlavorDown', 'pt_jesTotalNoTimeDown', 'pt_jesTotalNoFlavorNoTimeDown', 'pt_jesFlavorZJetDown', 'pt_jesFlavorPhotonJetDown', 'pt_jesFlavorPureGluonDown', 'pt_jesFlavorPureQuarkDown', 'pt_jesFlavorPureCharmDown', 'pt_jesFlavorPureBottomDown', 'pt_jesTimeRunBDown', 'pt_jesTimeRunCDown', 'pt_jesTimeRunDEDown', 'pt_jesTimeRunFDown', 'pt_jesCorrelationGroupMPFInSituDown', 'pt_jesCorrelationGroupIntercalibrationDown', 'pt_jesCorrelationGroupbJESDown', 'pt_jesCorrelationGroupFlavorDown', 'pt_jesCorrelationGroupUncorrelatedDown', 'pt_jesAbsoluteStatUp', 'pt_jesAbsoluteScaleUp', 'pt_jesAbsoluteFlavMapUp', 'pt_jesAbsoluteMPFBiasUp', 'pt_jesFragmentationUp', 'pt_jesSinglePionECALUp', 'pt_jesSinglePionHCALUp', 'pt_jesFlavorQCDUp', 'pt_jesTimePtEtaUp', 'pt_jesRelativeJEREC1Up', 'pt_jesRelativeJEREC2Up', 'pt_jesRelativeJERHFUp', 'pt_jesRelativePtBBUp', 'pt_jesRelativePtEC1Up', 'pt_jesRelativePtEC2Up', 'pt_jesRelativePtHFUp', 'pt_jesRelativeBalUp', 'pt_jesRelativeSampleUp', 'pt_jesRelativeFSRUp', 'pt_jesRelativeStatFSRUp', 'pt_jesRelativeStatECUp', 'pt_jesRelativeStatHFUp', 'pt_jesPileUpDataMCUp', 'pt_jesPileUpPtRefUp', 'pt_jesPileUpPtBBUp', 'pt_jesPileUpPtEC1Up', 'pt_jesPileUpPtEC2Up', 'pt_jesPileUpPtHFUp', 'pt_jesPileUpMuZeroUp', 'pt_jesPileUpEnvelopeUp', 'pt_jesSubTotalPileUpUp', 'pt_jesSubTotalRelativeUp', 'pt_jesSubTotalPtUp', 'pt_jesSubTotalScaleUp', 'pt_jesSubTotalAbsoluteUp', 'pt_jesSubTotalMCUp', 'pt_jesTotalUp', 'pt_jesTotalNoFlavorUp', 'pt_jesTotalNoTimeUp', 'pt_jesTotalNoFlavorNoTimeUp', 'pt_jesFlavorZJetUp', 'pt_jesFlavorPhotonJetUp', 'pt_jesFlavorPureGluonUp', 'pt_jesFlavorPureQuarkUp', 'pt_jesFlavorPureCharmUp', 'pt_jesFlavorPureBottomUp', 'pt_jesTimeRunBUp', 'pt_jesTimeRunCUp', 'pt_jesTimeRunDEUp', 'pt_jesTimeRunFUp', 'pt_jesCorrelationGroupMPFInSituUp', 'pt_jesCorrelationGroupIntercalibrationUp', 'pt_jesCorrelationGroupbJESUp', 'pt_jesCorrelationGroupFlavorUp', 'pt_jesCorrelationGroupUncorrelatedUp']
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
        self.out.branch("Jet_photonIdx1", "I", 1, "nJet");
        self.out.branch("Jet_photonIdx2", "I", 1, "nJet");
        self.out.branch("jetIdx1",  "I");
        self.out.branch("jetIdx2",  "I");
        self.out.branch("jetNumber",  "I");
        self.out.branch("bjetNumber",  "I");
        self.out.branch("muonNumber",  "I");
        self.out.branch("Jet_VBFselected", "F", 1, "nJet");
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        
        """process event, return True (go to next module) or False (fail, go to next event)"""
        electrons = Collection(event, "Electron")
        muons = Collection(event, "Muon")
        jets = Collection(event, "Jet")
        photons = Collection(event, "Photon")

        eventSum = ROOT.TLorentzVector()
        
        mu1_charge = 0
        count_mu = 0
        dimuonSelection = False
        RaffaeleRequest = False
        mu1 = ROOT.TLorentzVector()
        mu2 = ROOT.TLorentzVector()
        dimuonMass = 0
        
        jet1 = ROOT.TLorentzVector()
        jet2 = ROOT.TLorentzVector()
        jet1s = []
        jet2s = []
        
        jet1_jesTotalDown = ROOT.TLorentzVector()
        jet2_jesTotalDown = ROOT.TLorentzVector()
        jet1_jerUp = ROOT.TLorentzVector()
        jet2_jerUp = ROOT.TLorentzVector()
        jet1_jerDown = ROOT.TLorentzVector()
        jet2_jerDown = ROOT.TLorentzVector()
        
        if len(filter(self.muSel,muons)) < 2:
            return False
        muonNumber = len(filter(self.muSel,muons))
        for lep in muons :

            eventSum += lep.p4()
            if lep.pfRelIso04_all<0.25 and abs(lep.pdgId)==13 and abs(lep.dz) < 0.2 and abs(lep.dxy) < 0.05 and not dimuonSelection :

                if count_mu == 1 and (lep.charge*mu1_charge)<0: # and lep.mediumId 
                    mu2.SetPtEtaPhiM(lep.corrected_pt,lep.eta, lep.phi, 0.105658375)
                    dimuonSelection = True
                if count_mu == 0  :
                    mu1.SetPtEtaPhiM(lep.corrected_pt,lep.eta, lep.phi, 0.105658375)#105,6583745(24) MeV
                    mu1_charge = lep.charge
                    count_mu +=1
        
        if not dimuonSelection : return False           
        if max(mu1.Pt(), mu2.Pt())<28 : return False # muons are ordered in lep.pt, not in lep.pt_corrected
        if min(mu1.Pt(), mu2.Pt())<9  : return False # muons are ordered in lep.pt, not in lep.pt_corrected
    

              
        dimuon = mu1 + mu2
        dimuonMass = dimuon.M()
        #if dimuon.M()<70 or dimuon.M()>110 :
        if dimuon.M()<70  :
            return False
                
        
        #AGGIUNGERE IL SORT SUI JET
        jetIdx1=-1
        jetIdx2=-1
        VBFselectedJet = array.array('f', [0 for x in range(len(jets))])     
        Jet_photonIdx1 =  array.array('i', [0 for x in range(len(jets))]) 
        Jet_photonIdx2 =  array.array('i', [0 for x in range(len(jets))]) 
        
        jetNumber = len(filter(self.jetSel,jets))
        if jetNumber < 2:
            return False    
        bjetNumber = 0
        dijetSelection  = False
        count_jet = 0

        for n in range(len(jets)) :
            j = jets[n]
            VBFselectedJet[n] = 0
            Jet_photonIdx1[n] = -1
            Jet_photonIdx2[n] = -1

            if self.jetSel(j) :
                eventSum += j.p4()
                if j.jetId>0 and j.puId>0 :#and not dijetSelection:
                    if j.muonIdx1>-1 and muons[j.muonIdx1].pfRelIso04_all<0.25 and abs(muons[j.muonIdx1].dz) < 0.2 and abs(muons[j.muonIdx1].dxy) < 0.05 : continue   
                    if j.muonIdx2>-1 and muons[j.muonIdx2].pfRelIso04_all<0.25 and abs(muons[j.muonIdx2].dz) < 0.2 and abs(muons[j.muonIdx2].dxy) < 0.05 : continue  
                    if j.electronIdx1>-1 and electrons[j.electronIdx1].pfRelIso03_all<0.25 and abs(electrons[j.electronIdx1].dz) < 0.2 and abs(electrons[j.electronIdx1].dxy) < 0.05 : continue   
                    if j.electronIdx2>-1 and electrons[j.electronIdx2].pfRelIso03_all<0.25 and abs(electrons[j.electronIdx2].dz) < 0.2 and abs(electrons[j.electronIdx2].dxy) < 0.05 : continue   
                    

                if j.jetId>0 and j.puId>0 and abs(j.eta)<4.7 and (abs(j.eta)<2.5 or j.puId>6) : #and not dijetSelection:
                    for ph in range(len(photons)) : 
                        if n == photons[ph].jetIdx :
                            if Jet_photonIdx1[n]==-1 :
                                Jet_photonIdx1[n] = ph
                            elif Jet_photonIdx2[n]==-1 :
                                Jet_photonIdx2[n] = ph

                

                    #if j.muonIdx1>-1 and muons[j.muonIdx1].pt>10 and abs(muons[j.muonIdx1].eta)<2.4 and muons[j.muonIdx1].softId and muons[j.muonIdx1].pfRelIso04_all<0.25 : continue 
                    #if j.muonIdx2>-1 and muons[j.muonIdx2].pt>10 and abs(muons[j.muonIdx2].eta)<2.4 and muons[j.muonIdx2].softId and muons[j.muonIdx2].pfRelIso04_all<0.25: continue 
                    #if j.electronIdx1>-1 and electrons[j.electronIdx1].pt>10 and abs(electrons[j.electronIdx1].eta) < 2.5 and electrons[j.electronIdx1].mvaSpring16GP_WP90 and electrons[j.electronIdx1].pfRelIso03_all<0.25  and abs(electrons[j.electronIdx1].dz) < 0.2 and abs(electrons[j.electronIdx1].dxy) < 0.05 : continue  
                    #if j.electronIdx2>-1 and electrons[j.electronIdx2].pt>10 and abs(electrons[j.electronIdx2].eta) < 2.5 and electrons[j.electronIdx2].mvaSpring16GP_WP90  and electrons[j.electronIdx2].pfRelIso03_all<0.25  and abs(electrons[j.electronIdx2].dz) < 0.2 and abs(electrons[j.electronIdx2].dxy) < 0.05 : continue

 
                    #if Jet_photonIdx1[n]!=-1 and photons[Jet_photonIdx1[n]].pt > 15 and abs(photons[Jet_photonIdx1[n]].eta) < 2.5 and photons[Jet_photonIdx1[n]].mvaID_WP90 and photons[Jet_photonIdx1[n]].pfRelIso03_all<0.25 : continue
                    #if Jet_photonIdx2[n]!=-1 and photons[Jet_photonIdx2[n]].pt > 15 and abs(photons[Jet_photonIdx2[n]].eta) < 2.5 and photons[Jet_photonIdx2[n]].mvaID_WP90 and photons[Jet_photonIdx2[n]].pfRelIso03_all<0.25 : continue
                    

                    if count_jet ==1:
                        jet2=j.p4()
                        for var in self.jesVariation : jet2s.append(j.p4())

                        count_jet +=1
                        
                        if not self.data : 
                            jet2.SetPtEtaPhiM(j.pt_nom,jet2.Eta(), jet2.Phi(), j.mass_nom)   #--------------------------------------------------------- UNCOMMENT THIS !
                            for vn in range(len(self.jesVariation)) : jet2s[vn].SetPtEtaPhiM(getattr(j, self.jesVariation[vn]),jet2.Eta(), jet2.Phi(), j.mass_nom) 
                        
                        dijetSelection = True
                        jetIdx2=n
                        
                        
                    if count_jet == 0:
                        jet1=j.p4()
                        for var in self.jesVariation : jet1s.append(j.p4())

                        count_jet +=1
                        
                        if not self.data : 
                            #print "jet 1 before:   ", jet1.Pt(), " " , j.pt_nom, " " , j.p4().Pt()
                            jet1.SetPtEtaPhiM(j.pt_nom,jet1.Eta(), jet1.Phi(), j.mass_nom)    #--------------------------------------------------------- UNCOMMENT THIS !
                            for vn in range(len(self.jesVariation)) : jet1s[vn].SetPtEtaPhiM(getattr(j, self.jesVariation[vn]),jet1.Eta(), jet1.Phi(), j.mass_nom) 

                        jetIdx1=n
                                               
                    if (j.pt > 30) :
                    #if (j.pt_nom > 30) :
                        #count_jet +=1
                        if (j.btagCSVV2 > 0.8) : bjetNumber = bjetNumber + 1
                    VBFselectedJet[n] = 1  
                        
                

        if not dijetSelection : return False

        eventToRejection = True
        for vn in range(len(self.jesVariation)) : 
            if max(jet1s[vn].Pt(), jet2s[vn].Pt()) > 25 and min(jet1s[vn].Pt(), jet2s[vn].Pt()) > 20 and (jet1s[vn] + jet2s[vn]).M() > 250   : 
                eventToRejection = False
                break
        if eventToRejection : return False
        
        

        dijetMass = 0    
        dijetMass = (jet1 + jet2).M()




        
        

        self.out.fillBranch("EventMass",eventSum.M())
        self.out.fillBranch("MuonMass",dimuonMass)
        self.out.fillBranch("qqMass",dijetMass)
        self.out.fillBranch("jetIdx1",jetIdx1)
        self.out.fillBranch("jetIdx2",jetIdx2)
        self.out.fillBranch("jetNumber",jetNumber)
        self.out.fillBranch("bjetNumber",bjetNumber)
        self.out.fillBranch("muonNumber",muonNumber)
        self.out.fillBranch("Jet_photonIdx1",Jet_photonIdx1)
        self.out.fillBranch("Jet_photonIdx2",Jet_photonIdx2)
        self.out.fillBranch("Jet_VBFselected",VBFselectedJet)
        return True
    
    
    
vbfhmmModule = lambda : vbfhmmProducer(jetSelection= lambda j : j.pt > 15, muSelection= lambda mu : mu.pt > 9, data = False) 

vbfhmmModuleDATA = lambda : vbfhmmProducer(jetSelection= lambda j : j.pt > 15, muSelection= lambda mu : mu.pt > 9, data = True) 




