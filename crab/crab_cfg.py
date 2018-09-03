import sys
from WMCore.Configuration import Configuration
config = Configuration()

version = "83"

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
config.Data.inputDataset = '/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PUMoriond17_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
#config.Data.splitting = 'Automatic'
#config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 1
#config.Data.totalUnits = 2000
config.Data.inputDBS='global'#'phys03'
config.Data.outLFNDirBase = '/store/user/gimandor/'
config.Data.publication = True
config.Data.outputDatasetTag = 'NanoTestPost5'
config.section_("Site")
config.Site.storageSite = "T2_IT_Pisa"




sites=['T2_IT_Pisa']
extentionPostname = ["_ext10", "_ext9", "_ext8", "_ext7", "_ext6", "_ext5", "_ext4", "_ext3", "_ext2", "_ext1"]


if __name__ == '__main__':
   
    
    f=open(sys.argv[1]) 
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
        
        
        
        
        
        
