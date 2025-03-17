import FWCore.ParameterSet.Config as cms

from RecoBTag.FeatureTools.DeepFlavourTagInfoProducer import DeepFlavourTagInfoProducer as _DeepFlavourTagInfoProducer

hltPfDeepFlavourTagInfos = _DeepFlavourTagInfoProducer(
    candidates = ("hltParticleFlowTmp"),
    compute_probabilities = False,
    fallback_puppi_weight = False,
    fallback_vertex_association = False,
    flip = False,
    jet_radius = 0.4,
    jets = ("hltAK4PFPuppiJets"),
    unsubjet_map = (""),
    max_jet_eta = 2.5,
    mightGet = cms.optional.untracked.vstring,
    min_candidate_pt = 0.95,
    min_jet_pt = 15,
    puppi_value_map = ("hltPFPuppi"),
    run_deepVertex = False,
    secondary_vertices = ("hltDeepInclusiveSecondaryVerticesPF"),
    shallow_tag_infos = ("hltDeepCombinedSecondaryVertexBJetTagsInfosPuppi"),
    vertex_associator = ("hltPrimaryVertexAssociation","original"),
    vertices = ("hltOfflinePrimaryVertices")
)
