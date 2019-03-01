#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from  exampleModule import *
#from  exampleModuleDATA import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jecUncertainties import *
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.muonScaleResProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.hepmcDump import *



#p=PostProcessor(".",["/afs/cern.ch/user/g/gimandor/private/Hmumu/nanoAODtest/CMSSW_9_4_6/GluGlu_HToMuMu_M125_13TeV_powheg_pythia8_NANOAOD.root"],"Jet_pt>20 && Muon_pt > 9 && Entry$ < 10000","keep_and_drop.txt",[hepmcDump(),jetmetUncertainties2016(), btagSF2016(), muonScaleRes2016(), puAutoWeight(), exampleModule()],provenance=True)
#p=PostProcessor(".",["/afs/cern.ch/user/g/gimandor/private/Hmumu/nanoAODtest/CMSSW_9_4_6/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_NANOAOD.root"],"Jet_pt>20 && Muon_pt > 9 && Entry$ < 10000","keep_and_drop.txt",[hepmcDump(),jetmetUncertainties2016(), btagSF2016(), muonScaleRes2016(), puAutoWeight(), exampleModule()],provenance=True)

#p=PostProcessor(".",["/afs/cern.ch/user/g/gimandor/private/Hmumu/nanoAODtest/CMSSW_9_4_6/SingleMuon_NANOAOD.root"],"Jet_pt>20 && Muon_pt > 9 && Entry$ < 10000","keep_and_drop.txt",[exampleModuleDATA()],provenance=True)
#p=PostProcessor(".",["root://xrootd-cms.infn.it//store/data/Run2017F/SingleMuon/NANOAOD/31Mar2018-v1/10000/80641B83-4D45-E811-9DAA-FA163E7EEF99.root"],"Jet_pt>20 && Muon_pt > 9","keep_and_drop.txt",[exampleModuleDATA()],provenance=True)

#p=PostProcessor(".",["root://xrootd-cms.infn.it//store/mc/RunIISummer16NanoAOD/VBF_HToMuMu_M125_13TeV_powheg_pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/00000/C26667F7-7216-E811-8ADD-B496910A9A24.root"],"Jet_pt>5 && Muon_pt >1","keep_and_drop.txt",[exampleModule()],provenance=True)

#p=PostProcessor(".",["root://xrootd-cms.infn.it//store/mc/RunIISummer16NanoAOD/VBF_HToMuMu_M125_13TeV_powheg_pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/00000/C26667F7-7216-E811-8ADD-B496910A9A24.root"], "Jet_pt>15 && Muon_pt > 9 && Entry$ < 10000", "keep_and_drop.txt",[hepmcDump(),jetmetUncertainties2016(), btagSF2016(), muonScaleRes2016(), puAutoWeight(), exampleModule()],provenance=True)


#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndRegMulti/VBF_HToMuMu_M125_13TeV_powheg_pythia8/RunIIMoriond17-DeepAndReg_M2_2016_TrancheIV_v6-v1/180904_090509/0000/test_data_80X_NANO_1.root"],"Jet_pt>15 && Muon_pt > 9","keep_and_drop.txt",[hepmcDump(),jetmetUncertainties2016(), btagSF2016(), muonScaleRes2016(), puAutoWeight(), exampleModule()],provenance=True)
#p=PostProcessor(".",["/afs/cern.ch/user/g/gimandor/private/Hmumu/nanoAODtest/CMSSW_9_4_6/test80X_NANO_1_TTJets_DiLept.root"],"Entry$ < 10000","keep_and_drop.txt",[hepmcDump(),jetmetUncertainties2016(), btagSF2016(), muonScaleRes2016(), puAutoWeight(), exampleModule()],provenance=True)
p=PostProcessor(".",["/afs/cern.ch/user/g/gimandor/private/Hmumu/nanoAODtest/CMSSW_9_4_6/test80X_NANO_2.root"],"Entry$ < 10000",modules=[hepmcDump(),jetmetUncertainties2016(), btagSF2016(), muonScaleRes2016(), puAutoWeight(), exampleModule()],provenance=True)

#p=PostProcessor(".",["/afs/cern.ch/user/g/gimandor/private/Hmumu/nanoAODtest/CMSSW_9_4_6/test80X_NANO_1_TTTo2L2Nu.root"],"Entry$ < 1000","keep_and_drop.txt",[hepmcDump(),jetmetUncertainties2017(), btagSF2017(), muonScaleRes2017(), puAutoWeight(), exampleModule()],provenance=True)
#p=PostProcessor(".",["/afs/cern.ch/user/g/gimandor/private/Hmumu/nanoAODtest/CMSSW_9_4_6/EA2B7FA6-0032-7C47-A078-A7E3DD8003D6.root"],"Entry$ < 1000","keep_and_drop.txt",[hepmcDump(),jetmetUncertainties2017(), btagSF2017(), muonScaleRes2017(), puAutoWeight(), exampleModule()],provenance=True)
#p=PostProcessor(".",["/afs/cern.ch/user/g/gimandor/private/Hmumu/nanoAODtest/CMSSW_9_4_6/test80X_ttHToMuMu_NANO2018.root"],"Entry$ < 1000","keep_and_drop.txt",[hepmcDump(),jetmetUncertainties2018(), btagSF2018(), muonScaleRes2017(), puAutoWeight(), exampleModule()],provenance=True)
#p=PostProcessor(".",["/afs/cern.ch/user/g/gimandor/private/Hmumu/nanoAODtest/CMSSW_9_4_6/test80X_ttHToMuMu_NANO2018.root"],"Entry$ < 10000",modules=[hepmcDump(),jetmetUncertainties2018(), btagSF2018(), muonScaleRes2017(), puAutoWeight(), exampleModule()],provenance=True)

#p=PostProcessor(".",["/afs/cern.ch/user/g/gimandor/private/Hmumu/nanoAODtest/CMSSW_9_4_6/test80X_NANO_1_TTTo2L2Nu.root"],"Entry$ < 10000","keep_and_drop.txt",[jetmetUncertainties2016(), muonScaleRes2016(), exampleModule()],provenance=True)
#p=PostProcessor(".",["/afs/cern.ch/user/g/gimandor/private/Hmumu/nanoAODtest/CMSSW_9_4_6/test80X_NANO_1_TTTo2L2Nu.root"],"Entry$ < 10000","keep_and_drop.txt",[hepmcDump(),jetmetUncertainties2016(), btagSF2016(), muonScaleRes2016(), puAutoWeight(), exampleModule()],provenance=True)


#p=PostProcessor(".",["/afs/cern.ch/user/g/gimandor/private/Hmumu/nanoAODtest/CMSSW_9_4_6/test80X_NANO_20.root"],"Jet_pt>15 && Muon_pt > 9 && Entry$ < 10000","keep_and_drop.txt",[hepmcDump(),jetmetUncertainties2016(), btagSF2016(), muonScaleRes2016(), puAutoWeight(), exampleModule()],provenance=True)



#FAILED DATA IN VZ96
#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016H-03Feb2017_ver2-v1/180516_082401/0000/test_data_80X_NANO_733.root", "root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016H-03Feb2017_ver2-v1/180516_082401/0000/test_data_80X_NANO_788.root", "root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016D-03Feb2017-v1/180516_082218/0000/test_data_80X_NANO_205.root", "root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016D-03Feb2017-v1/180516_082218/0000/test_data_80X_NANO_292.root", "root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016D-03Feb2017-v1/180516_082218/0000/test_data_80X_NANO_320.root", "root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016D-03Feb2017-v1/180516_082218/0000/test_data_80X_NANO_429.root", "root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016D-03Feb2017-v1/180516_082218/0000/test_data_80X_NANO_324.root", "root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016B-03Feb2017_ver2-v2/180516_082129/0000/test_data_80X_NANO_54.root", "root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016B-03Feb2017_ver2-v2/180516_082129/0000/test_data_80X_NANO_608.root", "root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016B-03Feb2017_ver2-v2/180516_082129/0000/test_data_80X_NANO_73.root", "root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016E-03Feb2017-v1/180516_082243/0000/test_data_80X_NANO_323.root", "root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016E-03Feb2017-v1/180516_082243/0000/test_data_80X_NANO_444.root", "root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016E-03Feb2017-v1/180516_082243/0000/test_data_80X_NANO_94.root", "root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016B-03Feb2017_ver2-v2/180516_082129/0000/test_data_80X_NANO_54.root", "root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016B-03Feb2017_ver2-v2/180516_082129/0000/test_data_80X_NANO_54.root"],"Jet_pt>20 && Muon_pt > 9","keep_and_drop.txt",[exampleModuleDATA()],provenance=True)

#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016G-03Feb2017-v1/180516_082336/0000/test_data_80X_NANO_734.root"],"Jet_pt>20 && Muon_pt > 9","keep_and_drop.txt",[exampleModuleDATA()],provenance=True)



# 2016 V85 ext6 
#p=PostProcessor(".",["root://cms-xrd-global.cern.ch//store/data/Run2016G/SingleMuon/NANOAOD/05Feb2018-v1/20000/EC7C30D1-6C0C-E811-B042-0242AC130002.root"],"Jet_pt>20 && Muon_pt > 9 && Entry$ < 10000","keep_and_drop.txt",[exampleModuleDATA()],provenance=True)

# 2016 V79 ext5 
#p=PostProcessor(".",["root://xrootd-cms.infn.it//store/data/Run2016F/SingleMuon/NANOAOD/05Feb2018-v1/80000/1006BFED-640C-E811-8500-44A84225C827.root"],"Jet_pt>20 && Muon_pt > 9","keep_and_drop.txt",[exampleModuleDATA()],provenance=True)
# 2016 V79 ext2 
#p=PostProcessor(".",["root://xrootd-cms.infn.it//store/data/Run2016C/SingleMuon/NANOAOD/05Feb2018-v1/00000/6CE972C3-500C-E811-B67E-6CC2173D6140.root"],"Jet_pt>20 && Muon_pt > 9","keep_and_drop.txt",[exampleModuleDATA()],provenance=True)

# 2016 V79 all 
#p=PostProcessor(".",["root://xrootd-cms.infn.it//store/data/Run2016F/SingleMuon/NANOAOD/05Feb2018-v1/80000/1006BFED-640C-E811-8500-44A84225C827.root", "root://xrootd-cms.infn.it//store/data/Run2016C/SingleMuon/NANOAOD/05Feb2018-v1/00000/6CE972C3-500C-E811-B67E-6CC2173D6140.root"],"Jet_pt>20 && Muon_pt > 9","keep_and_drop.txt",[exampleModuleDATA()],provenance=True)

# 2016 V79 ext8
#p=PostProcessor(".",["root://xrootd-cms.infn.it//store/data/Run2016G/SingleMuon/NANOAOD/05Feb2018-v1/40000/9EF4B56A-510C-E811-905E-0CC47A4D7636.root", "root://xrootd-cms.infn.it//store/data/Run2016G/SingleMuon/NANOAOD/05Feb2018-v1/40000/B4C781C8-610C-E811-9343-0242AC130002.root", "root://xrootd-cms.infn.it//store/data/Run2016G/SingleMuon/NANOAOD/05Feb2018-v1/40000/CC9FBCB0-5D0C-E811-9601-34E6D7BDDEDB.root"],"Jet_pt>20 && Muon_pt > 9","keep_and_drop.txt",[exampleModuleDATA()],provenance=True)




#p=PostProcessor(".",["../../../../NanoAOD/test/lzma.root"],"Jet_pt>150","keep_and_drop.txt",[exampleModule()],provenance=True)
p.run()
