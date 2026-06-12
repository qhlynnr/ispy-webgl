import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3
process = cms.Process("process", Run3)

process.load("Configuration.StandardSequences.GeometryDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.GlobalTag.globaltag = '160X_dataRun3_Express_v1'

r = 404812
start = 1
end = 50
events_per_file = 50

ls = [l for l in range(start,end+1)]
#ls = [254,275,309,84,96,59,156,168,185,202,204,239]

eventNumbers = [
    6215161,
    6403979,
    6310501,
    6395463,
    6768278,
    6801315,
    7559918,
    8138793,
    8385502,
    8255019,
    43031349,
    44389675
]


eventRanges = [f"{r}:{evt}" for evt in eventNumbers]


fileNames = [
    f'file:/eos/cms/store/group/visualization/run{r}/run{r}_ls{"%4.4i"% (l)}_streamEvDOutput2_dqmcluster.root' for l in ls
    #'file:/eos/cms/store/hidata/HIRun2026A/HIPhysicsRawPrime35/MINIAOD/PromptReco-v1/000/404/469/00000/bb338b85-54c3-4233-a455-7aa42a8ed713.root'
    #f'file:/eos/cms/store/group/phys_heavyions/wangj/RECO2026PbPb/miniaod_PhysicsHIPhysicsRawPrime0_{r}_prompt/reco_run{r}_ls{"%4.4i"% (l)}_streamPhysicsHIPhysicsRawPrime0_StorageManager.root' for l in ls
    ]

process.source = cms.Source(
    "PoolSource",
    fileNames=cms.untracked.vstring(*fileNames),
    eventsToProcess=cms.untracked.VEventRange(*eventRanges)
)


from FWCore.MessageLogger.MessageLogger_cfi import *

process.add_(
    cms.Service("ISpyService",
    outputFileName = cms.untracked.string(f'run3pbpb-2026_{r}_calojets_selectedEvents.ig'),
    outputMaxEvents = cms.untracked.int32(events_per_file)
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.load('ISpy.Analyzers.ISpyCSCRecHit2D_cfi')
process.load("ISpy.Analyzers.ISpyCSCSegment_cfi")
process.load("ISpy.Analyzers.ISpyCSCStripDigi_cfi")
process.load("ISpy.Analyzers.ISpyCSCWireDigi_cfi")
process.load("ISpy.Analyzers.ISpyCSCCorrelatedLCTDigi_cfi")
process.load('ISpy.Analyzers.ISpyDTDigi_cfi')
process.load('ISpy.Analyzers.ISpyDTRecHit_cfi')
process.load("ISpy.Analyzers.ISpyDTRecSegment4D_cfi")
process.load('ISpy.Analyzers.ISpyRPCRecHit_cfi')

process.load('ISpy.Analyzers.ISpyEvent_cfi')
process.load('ISpy.Analyzers.ISpyEBRecHit_cfi')
process.load('ISpy.Analyzers.ISpyEERecHit_cfi')
process.load('ISpy.Analyzers.ISpyESRecHit_cfi')

process.load('ISpy.Analyzers.ISpyHBRecHit_cfi')
process.load('ISpy.Analyzers.ISpyHERecHit_cfi')
process.load('ISpy.Analyzers.ISpyHFRecHit_cfi')
process.load('ISpy.Analyzers.ISpyHORecHit_cfi')

process.load('ISpy.Analyzers.ISpyMET_cfi')
process.load('ISpy.Analyzers.ISpyPFMET_cfi')
process.load('ISpy.Analyzers.ISpyMuon_cfi')
process.load('ISpy.Analyzers.ISpyJet_cfi')
process.load('ISpy.Analyzers.ISpyPFJet_cfi')
process.load('ISpy.Analyzers.ISpyPhoton_cfi')
process.load('ISpy.Analyzers.ISpyRPCRecHit_cfi')
process.load('ISpy.Analyzers.ISpySuperCluster_cfi')

#process.load('ISpy.Analyzers.ISpyMuon_cfi')
process.load('ISpy.Analyzers.ISpyVertex_cfi')
process.load("ISpy.Analyzers.ISpyTrack_cfi")
process.load("ISpy.Analyzers.ISpyTrackingRecHit_cfi")

#process.load('ISpy.Analyzers.ISpyJet_cfi')


#Added by Lynn
process.ISpyJet.iSpyJetTag = cms.InputTag("ak4CaloJets")

process.ISpyMET.iSpyMETTag = cms.InputTag("htMetIC5")
process.ISpyMuon.iSpyMuonTag = cms.InputTag("muons")
process.ISpyPFJet.iSpyPFJetTag = cms.InputTag('ak4PFJets')
process.ISpyPhoton.iSpyPhotonTag = cms.InputTag('photons')
process.ISpyRPCRecHit.iSpyRPCRecHitTag = cms.InputTag("rpcRecHits")
process.ISpyVertex.iSpyVertexTag = cms.InputTag('offlinePrimaryVertices')


process.ISpyCSCRecHit2D.iSpyCSCRecHit2DTag = cms.InputTag("csc2DRecHits")
process.ISpyCSCSegment.iSpyCSCSegmentTag = cms.InputTag("cscSegments")
process.ISpyEBRecHit.iSpyEBRecHitTag = cms.InputTag('ecalRecHit:EcalRecHitsEB')
process.ISpyEERecHit.iSpyEERecHitTag = cms.InputTag('ecalRecHit:EcalRecHitsEE')
process.ISpyHBRecHit.iSpyHBRecHitTag = cms.InputTag("hbhereco")
process.ISpyHERecHit.iSpyHERecHitTag = cms.InputTag("hbhereco")
process.ISpyHFRecHit.iSpyHFRecHitTag = cms.InputTag("hfreco")
process.ISpyHORecHit.iSpyHORecHitTag = cms.InputTag("horeco")


process.ISpyPFJet.etMin = cms.double(0)
process.ISpyPFJet.etaMax = cms.double(2.5)
process.ISpyJet.energyCut = cms.untracked.double(100)

'''
process.out = cms.OutputModule(
        "PoolOutputModule",
            fileName = cms.untracked.string("run3pbpb-2026.root")
        )
'''

process.iSpy = cms.Path(process.ISpyEvent*
                        process.ISpyCSCRecHit2D*
                        process.ISpyCSCSegment*
                        process.ISpyDTRecHit*
                        process.ISpyDTRecSegment4D*
                        process.ISpyTrack*
                        process.ISpyTrackingRecHit*
                        process.ISpyEBRecHit*
                        process.ISpyEERecHit*
                        process.ISpyESRecHit*
                        process.ISpyHBRecHit*
                        process.ISpyHERecHit*
                        process.ISpyHFRecHit*
                        process.ISpyHORecHit*
                        process.ISpyRPCRecHit*
                       # process.ISpyTrackExtrapolation*
                        process.ISpyPFJet*
                        process.ISpyJet*
                        process.ISpyPFMET*
                        process.ISpyPhoton*
                        process.ISpyMuon*
                        process.ISpyVertex)


#process.ISpyPFJet.etMin = cms.double(100.0)
#process.ISpyPFJet.etaMax = cms.double(1.6)
                      
process.schedule = cms.Schedule(process.iSpy)
#process.outpath = cms.EndPath(process.out)

