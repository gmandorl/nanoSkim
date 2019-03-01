import sys
from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = Configuration()

version = "112"

config.section_("General")
config.General.requestName = 'NanoPost8'
config.General.transferLogs=True
config.General.workArea = '/afs/cern.ch/work/g/gimandor/public/testNANOAOD'#+version
config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.scriptExe = 'crab_script.sh'
config.JobType.inputFiles = ['crab_script.py','../scripts/haddnano.py'] #hadd nano will not be needed once nano tools are in cmssw
config.JobType.sendPythonFolder	 = True
config.section_("Data")
#config.Data.inputDataset = '/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PUMoriond17_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'Automatic'
#config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 5
#config.Data.totalUnits = 2000
#config.Data.inputDBS='global'#'phys03'
config.Data.outLFNDirBase = '/store/user/gimandor/'
config.Data.publication = True
config.Data.outputDatasetTag = 'NanoTestPost5'
#config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON.txt'
config.section_("Site")
config.Site.storageSite = "T2_IT_Bari"



sites=['T2_IT_Pisa']
extentionPostname = ["_ext10", "_ext9", "_ext8", "_ext7", "_ext6", "_ext5", "_ext4", "_ext3", "_ext2", "_ext1"]








if __name__ == '__main__':
   
    
    f=open(sys.argv[1]) 
    if sys.argv[1].startswith("samples_2018") : version = "2018_V" + version
    if sys.argv[1].startswith("samples_2017") : version = "2017_V" + version
    if sys.argv[1].startswith("samples_2016") : version = "2016_V" + version


    content = f.readlines()
    content = [x.strip() for x in content]
    content = list(filter(lambda x: len(x) > 0, content))
    from CRABAPI.RawCommand import crabCommand
    n=200
    oldRequestName = ""
    for dataset in content :
        
        if not (dataset[0].startswith("/"))  : continue
        ext = ""
        prod = str(dataset.split('/')[-1])
        if prod.startswith("NANO")  : config.Data.inputDBS = 'global'
        if prod == "USER" :           config.Data.inputDBS = 'phys03'
        config.Data.inputDataset = dataset
        config.Data.unitsPerJob = 1


        requestName = dataset.split('/')[1]+"_"+version
        if oldRequestName.startswith(requestName) :
            ext = extentionPostname.pop()
            requestName = requestName + ext
            #print requestName
        else :
            extentionPostname = ["_ext10", "_ext9", "_ext8", "_ext7", "_ext6", "_ext5", "_ext4", "_ext3", "_ext2", "_ext1"]
        oldRequestName = requestName
        
        
        config.General.requestName = requestName
        config.Data.outputDatasetTag = dataset.split('/')[2][:30]+"_"+version + ext
        crabCommand('submit', config = config)
        
        
        
###config.Data.inputDBS = 'phys03'    
###config.Data.userInputFiles = ["/store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016G-03Feb2017-v1/180516_082336/0000/test_data_80X_NANO_734.root"]
###config.Data.outputPrimaryDataset = "SingleMuon"
####config.Data.inputDataset = "/store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016G-03Feb2017-v1/180516_082336/0000/test_data_80X_NANO_734.root"
###config.Data.unitsPerJob = 1   

###config.General.requestName = "SingleMuonRun2016G_test_data_80X_NANO_734_V2"




#config.Data.inputDBS = 'phys03' 
#userInputFiles = []
#for n in range(1, 962) :
    #if n != 226 and  n != 679 and  n != 609 :
        #userInputFiles.append("root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndRegMulti/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIMoriond17-DeepAndReg_M2_2016_TrancheIV_v6-v1/180912_122048/0000/test80X_NANO_" + str(n) + ".root")

##config.Data.userInputFiles = ["root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndRegMulti/DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIMoriond17-DeepAndReg_M2_2016_TrancheIV_v6-v1/180912_122048/0000/test80X_NANO_100.root"]
#config.Data.userInputFiles = userInputFiles
#config.Data.outputPrimaryDataset = "DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8"
##config.Data.inputDataset = "/store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016G-03Feb2017-v1/180516_082336/0000/test_data_80X_NANO_734.root"
#config.Data.unitsPerJob = 10 

#config.General.requestName = "DYJetsToLL_M-105To160_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_V03"
        

        
        


     
#config.Data.inputDBS = 'phys03' 
#userInputFiles = []
#for n in range(1, 11) :
    #userInputFiles.append("root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndRegMulti/EWK_LLJJ_MLL-50_MJJ-120_13TeV-madgraph-herwigpp/RunIIMoriond17-DeepAndReg_M2_2016_TrancheIV_v6-v1/181002_144208/0000/test80X_NANO_" + str(n) + ".root")


#config.Data.userInputFiles = userInputFiles
#config.Data.outputPrimaryDataset = "EWK_LLJJ_MLL-50_MJJ-120_13TeV-madgraph-herwigpp"
##config.Data.inputDataset = "/store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016G-03Feb2017-v1/180516_082336/0000/test_data_80X_NANO_734.root"
#config.Data.unitsPerJob = 10 

#config.General.requestName = "EWK_LLJJ_MLL-50_MJJ-120_13TeV-madgraph-herwigpp_V90"
           
        
           
#config.Data.inputDBS = 'phys03' 
#userInputFiles = []
#userInputFiles.append("root://cms-xrd-global.cern.ch//gpfs/ddn/srm/cms/store/user/arizzi/nano80XDeepAndRegMulti/LLJJ_INT_SM_5f_LO_13TeV_madgraph-pythia8_TuneCUETP8M1/RunIIMoriond17-DeepAndReg_M2b_2016_TrancheIV_v6-v1/181003_112210/0000/test80X_NANO_1.root")
#userInputFiles.append("root://cms-xrd-global.cern.ch//gpfs/ddn/srm/cms/store/user/arizzi/nano80XDeepAndRegMulti/LLJJ_INT_SM_5f_LO_13TeV_madgraph-pythia8_TuneCUETP8M1/RunIIMoriond17-DeepAndReg_M2b_2016_TrancheIV_v6-v1/181003_112210/0000/test80X_NANO_2.root")
#userInputFiles.append("root://cms-xrd-global.cern.ch//gpfs/ddn/srm/cms/store/user/arizzi/nano80XDeepAndRegMulti/LLJJ_INT_SM_5f_LO_13TeV_madgraph-pythia8_TuneCUETP8M1/RunIIMoriond17-DeepAndReg_M2b_2016_TrancheIV_v6-v1/181003_112210/0000/test80X_NANO_4.root")


#config.Data.userInputFiles = userInputFiles
#config.Data.outputPrimaryDataset = "LLJJ_INT_SM_5f_LO_13TeV_madgraph-pythia8"
##config.Data.inputDataset = "/store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016G-03Feb2017-v1/180516_082336/0000/test_data_80X_NANO_734.root"
#config.Data.unitsPerJob = 10 
#config.Data.outputDatasetTag = 'LLJJ_INT_SM_5f_LO_13TeV_madgraph-pythia8_V90'
#config.General.requestName = "LLJJ_INT_SM_5f_LO_13TeV_madgraph-pythia8_V90"  





#config.Data.inputDBS = 'phys03' 
#userInputFiles = []
#for n in range(1, 888) :
    #userInputFiles.append("root://cms-xrd-global.cern.ch//store/user/arizzi/nano80XDeepAndRegMulti/DYToLL_0J_13TeV-amcatnloFXFX-pythia8/RunIIMoriond17-DeepAndReg_M2b_2016_TrancheIV_v6-v1/181002_145039/0000/test80X_NANO_" + str(n) + ".root")


#config.Data.userInputFiles = userInputFiles
#config.Data.outputPrimaryDataset = "DYToLL_0J_13TeV-amcatnloFXFX-pythia8"
##config.Data.inputDataset = "/store/user/arizzi/nano80XDeepAndReg/SingleMuon/NanoDeepAndReg2016Run2016G-03Feb2017-v1/180516_082336/0000/test_data_80X_NANO_734.root"
#config.Data.unitsPerJob = 10 

#config.General.requestName = "DYToLL_0J_13TeV-amcatnloFXFX-pythia8_V89"





        
