#!/usr/bin/env python
__import__('sys').path.append(__import__('os').path.join(__import__('os').path.dirname(__file__), '..'))
__import__('testfwk').setup(__file__)
# - prolog marker
import os
from testfwk import TestsuiteStream, create_config, run_test, try_catch
from grid_control.datasets import DataProvider, DataSplitter
from web_replay import replay_start


os.environ['X509_USER_PROXY'] = 'web_replay.py'
replay_start('cms_web_responses')

def get(provider, ds, cfg={}):
	cfg['dataset processor +'] = 'sort'
	cfg['dataset sort'] = 'True'
	cfg['dataset block sort'] = 'True'
	cfg['dataset files sort'] = 'True'
	cfg['dataset location sort'] = 'True'
	config = create_config(config_dict={'dataset': cfg})
	ds = DataProvider.create_instance(provider, config, 'dataset', ds)
	blocks = ds.get_block_list_cached(show_stats=False)
	stream = TestsuiteStream()
	for block in DataProvider.save_to_stream(stream, ds.get_block_list_cached(show_stats=False), strip_metadata=False):
		pass

class Test_CMSProvider:
	"""
	>>> try_catch(DataProvider.create_instance('CMSBaseProvider', create_config(), 'dataset', '*').get_dataset_name_list, 'AbstractError', 'is an abstract function')
	caught

	>>> dbs3 = DataProvider.create_instance('DBS3Provider', create_config(config_dict={'dataset': {'lumi filter': '1-'}}), 'dataset', '/SingleMuon/Run2015E-PromptReco-v1/RECO#92f50192-8e3c-11e5-9687-001e67abf228')
	Runs/lumi section filter enabled!
	>>> dbs3.check_splitter(DataSplitter.get_class('EventBoundarySplitter')).__name__
	Active lumi section filter forced selection of HybridSplitter
	'HybridSplitter'
	>>> dbs3.check_splitter(DataSplitter.get_class('FileBoundarySplitter')).__name__
	'FileBoundarySplitter'
	>>> dbs3.get_query_interval() >= 60*60
	True

	>>> try_catch(lambda: get('DBS2Provider', '/SingleMuon/Run2015E-PromptReco-v1/*'), 'DatasetError', 'CMS deprecated all')
	caught
	>>> try_catch(lambda: get('DBS3Provider', '/SingleX/Run2015E-PromptReco-v1/*'), 'DatasetError', 'No datasets selected by DBS wildcard')
	caught

	>>> get('DBS3Provider', '/SingleMuon/Run2015E-PromptReco-v1/*')
	Dataset block '/SingleMuon/Run2015E-PromptReco-v1/DQMIO#5447977a-8e3c-11e5-9687-001e67abf228' is not available at the selected locations!
	Available locations: cmssrm.fnal.gov, cmssrm.fnal.gov
	[/SingleMuon/Run2015E-PromptReco-v1/AOD#a7c3638c-8e3e-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_AOD
	events = 267049
	se list = cmsdcadisk01.fnal.gov,node12.datagrid.cea.fr
	prefix = /store/data/Run2015E/SingleMuon/AOD/PromptReco-v1/000/261
	397/00000/A0C59AAD-3B8E-E511-8DEA-02163E0145B4.root = 56118
	397/00000/E44E2AAB-3B8E-E511-8BB2-02163E0141DC.root = 95082
	398/00000/8AAB12A5-3D8E-E511-83FF-02163E011EA8.root = 16788
	399/00000/9CFF9D75-3F8E-E511-AE38-02163E014244.root = 78409
	401/00000/E803ABDA-408E-E511-BA79-02163E013522.root = 13073
	402/00000/32DC2434-418E-E511-AC71-02163E0142D8.root = 7576
	422/00000/3424AE0E-438E-E511-B5C0-02163E014491.root = 3
	-----
	[/SingleMuon/Run2015E-PromptReco-v1/MINIAOD#17df3a8a-8e3d-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_MINIAOD
	events = 267049
	se list = cmsdcadisk01.fnal.gov,srm-cms.jinr-t1.ru,srm.unl.edu,storage01.lcg.cscs.ch
	prefix = /store/data/Run2015E/SingleMuon/MINIAOD/PromptReco-v1/000/261
	397/00000/A8DA65A7-3B8E-E511-8C33-02163E013745.root = 56118
	397/00000/CAAB76A3-3B8E-E511-9482-02163E0134F1.root = 95082
	398/00000/4C3D439E-3D8E-E511-A01D-02163E0119C2.root = 16788
	399/00000/00AC9572-3F8E-E511-AE17-02163E014602.root = 78409
	401/00000/3E4C8AD5-408E-E511-B6E5-02163E0134DB.root = 13073
	402/00000/44A8DF36-418E-E511-AECD-02163E013522.root = 7576
	422/00000/A0C10611-438E-E511-93BE-02163E013522.root = 3
	-----
	[/SingleMuon/Run2015E-PromptReco-v1/RECO#92f50192-8e3c-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_RECO
	events = 267049
	se list = cmsdcadisk01.fnal.gov,polgrid4.in2p3.fr
	prefix = /store/data/Run2015E/SingleMuon/RECO/PromptReco-v1/000/261
	397/00000/1E8961BE-3B8E-E511-9F86-02163E0145D7.root = 26631
	397/00000/5E5C8BAE-3B8E-E511-80AB-02163E013945.root = 25986
	397/00000/826CD5B2-3B8E-E511-AD15-02163E01393B.root = 26906
	397/00000/86FE27C0-3B8E-E511-88E1-02163E014781.root = 5714
	397/00000/96D80DAF-3B8E-E511-89B0-02163E0141E2.root = 24834
	397/00000/BA2F0AB5-3B8E-E511-BC53-02163E0143E9.root = 18408
	397/00000/FC3880C1-3B8E-E511-B858-02163E01440B.root = 22721
	398/00000/6031549E-3D8E-E511-9BBD-02163E014348.root = 16788
	399/00000/1EA98C88-3F8E-E511-9C0D-02163E014462.root = 21221
	399/00000/54435C84-3F8E-E511-8F3E-02163E0137BA.root = 26832
	399/00000/ACCCA383-3F8E-E511-9EB4-02163E0146E9.root = 25922
	399/00000/DEAFB87C-3F8E-E511-A4EE-02163E01440B.root = 4434
	401/00000/782C1BE9-408E-E511-8CD0-02163E013945.root = 13073
	402/00000/E8D05DD6-428E-E511-B51A-02163E0145F6.root = 7576
	422/00000/34BAD50F-438E-E511-9C7C-02163E011DD8.root = 3

	>>> get('DASProvider', '/SingleMuon/Run2015E-PromptReco-v1/*')
	Dataset block '/SingleMuon/Run2015E-PromptReco-v1/DQMIO#5447977a-8e3c-11e5-9687-001e67abf228' is not available at the selected locations!
	Available locations: cmssrm.fnal.gov, cmssrm.fnal.gov
	[/SingleMuon/Run2015E-PromptReco-v1/AOD#a7c3638c-8e3e-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_AOD
	events = 267049
	se list = cmsdcadisk01.fnal.gov,node12.datagrid.cea.fr,srm.rcac.purdue.edu
	prefix = /store/data/Run2015E/SingleMuon/AOD/PromptReco-v1/000/261
	397/00000/A0C59AAD-3B8E-E511-8DEA-02163E0145B4.root = 56118
	397/00000/E44E2AAB-3B8E-E511-8BB2-02163E0141DC.root = 95082
	398/00000/8AAB12A5-3D8E-E511-83FF-02163E011EA8.root = 16788
	399/00000/9CFF9D75-3F8E-E511-AE38-02163E014244.root = 78409
	401/00000/E803ABDA-408E-E511-BA79-02163E013522.root = 13073
	402/00000/32DC2434-418E-E511-AC71-02163E0142D8.root = 7576
	422/00000/3424AE0E-438E-E511-B5C0-02163E014491.root = 3
	-----
	[/SingleMuon/Run2015E-PromptReco-v1/MINIAOD#17df3a8a-8e3d-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_MINIAOD
	events = 267049
	se list = cmsdcadisk01.fnal.gov,srm-cms.jinr-t1.ru,srm.unl.edu,storage01.lcg.cscs.ch
	prefix = /store/data/Run2015E/SingleMuon/MINIAOD/PromptReco-v1/000/261
	397/00000/A8DA65A7-3B8E-E511-8C33-02163E013745.root = 56118
	397/00000/CAAB76A3-3B8E-E511-9482-02163E0134F1.root = 95082
	398/00000/4C3D439E-3D8E-E511-A01D-02163E0119C2.root = 16788
	399/00000/00AC9572-3F8E-E511-AE17-02163E014602.root = 78409
	401/00000/3E4C8AD5-408E-E511-B6E5-02163E0134DB.root = 13073
	402/00000/44A8DF36-418E-E511-AECD-02163E013522.root = 7576
	422/00000/A0C10611-438E-E511-93BE-02163E013522.root = 3
	-----
	[/SingleMuon/Run2015E-PromptReco-v1/RECO#92f50192-8e3c-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_RECO
	events = 267049
	se list = cmsdcadisk01.fnal.gov,polgrid4.in2p3.fr
	prefix = /store/data/Run2015E/SingleMuon/RECO/PromptReco-v1/000/261
	397/00000/1E8961BE-3B8E-E511-9F86-02163E0145D7.root = 26631
	397/00000/5E5C8BAE-3B8E-E511-80AB-02163E013945.root = 25986
	397/00000/826CD5B2-3B8E-E511-AD15-02163E01393B.root = 26906
	397/00000/86FE27C0-3B8E-E511-88E1-02163E014781.root = 5714
	397/00000/96D80DAF-3B8E-E511-89B0-02163E0141E2.root = 24834
	397/00000/BA2F0AB5-3B8E-E511-BC53-02163E0143E9.root = 18408
	397/00000/FC3880C1-3B8E-E511-B858-02163E01440B.root = 22721
	398/00000/6031549E-3D8E-E511-9BBD-02163E014348.root = 16788
	399/00000/1EA98C88-3F8E-E511-9C0D-02163E014462.root = 21221
	399/00000/54435C84-3F8E-E511-8F3E-02163E0137BA.root = 26832
	399/00000/ACCCA383-3F8E-E511-9EB4-02163E0146E9.root = 25922
	399/00000/DEAFB87C-3F8E-E511-A4EE-02163E01440B.root = 4434
	401/00000/782C1BE9-408E-E511-8CD0-02163E013945.root = 13073
	402/00000/E8D05DD6-428E-E511-B51A-02163E0145F6.root = 7576
	422/00000/34BAD50F-438E-E511-9C7C-02163E011DD8.root = 3

	>>> get('DBS3Provider', '/SingleMuon/Run2015E-PromptReco-v1/MINIAOD#17df3a8a-8e3d-11e5-9687-001e67abf228')
	[/SingleMuon/Run2015E-PromptReco-v1/MINIAOD#17df3a8a-8e3d-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_MINIAOD
	events = 267049
	se list = cmsdcadisk01.fnal.gov,srm-cms.jinr-t1.ru,srm.unl.edu,storage01.lcg.cscs.ch
	prefix = /store/data/Run2015E/SingleMuon/MINIAOD/PromptReco-v1/000/261
	397/00000/A8DA65A7-3B8E-E511-8C33-02163E013745.root = 56118
	397/00000/CAAB76A3-3B8E-E511-9482-02163E0134F1.root = 95082
	398/00000/4C3D439E-3D8E-E511-A01D-02163E0119C2.root = 16788
	399/00000/00AC9572-3F8E-E511-AE17-02163E014602.root = 78409
	401/00000/3E4C8AD5-408E-E511-B6E5-02163E0134DB.root = 13073
	402/00000/44A8DF36-418E-E511-AECD-02163E013522.root = 7576
	422/00000/A0C10611-438E-E511-93BE-02163E013522.root = 3

	>>> get('DASProvider', '/SingleMuon/Run2015E-PromptReco-v1/MINIAOD#17df3a8a-8e3d-11e5-9687-001e67abf228')
	[/SingleMuon/Run2015E-PromptReco-v1/MINIAOD#17df3a8a-8e3d-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_MINIAOD
	events = 267049
	se list = cmsdcadisk01.fnal.gov,srm-cms.jinr-t1.ru,srm.unl.edu,storage01.lcg.cscs.ch
	prefix = /store/data/Run2015E/SingleMuon/MINIAOD/PromptReco-v1/000/261
	397/00000/A8DA65A7-3B8E-E511-8C33-02163E013745.root = 56118
	397/00000/CAAB76A3-3B8E-E511-9482-02163E0134F1.root = 95082
	398/00000/4C3D439E-3D8E-E511-A01D-02163E0119C2.root = 16788
	399/00000/00AC9572-3F8E-E511-AE17-02163E014602.root = 78409
	401/00000/3E4C8AD5-408E-E511-B6E5-02163E0134DB.root = 13073
	402/00000/44A8DF36-418E-E511-AECD-02163E013522.root = 7576
	422/00000/A0C10611-438E-E511-93BE-02163E013522.root = 3

	>>> try_catch(lambda: get('DASProvider', '/SingleMuon/Run2015E-PromptReco-v1/MINIAOD#ffffffff-ffff-ffff-ffff-ffffffffffff'), 'DatasetError', 'contains 1 blocks, but none were selected')
	caught

	>>> get('DASProvider', '/SingleMuon/Run2015E-PromptReco-v1/MINIAOD#17df3a8a-8e3d-11e5-9687-001e67abf228 @ https://cmsweb.cern.ch/das/cache')
	[/SingleMuon/Run2015E-PromptReco-v1/MINIAOD#17df3a8a-8e3d-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_MINIAOD
	events = 267049
	se list = cmsdcadisk01.fnal.gov,srm-cms.jinr-t1.ru,srm.unl.edu,storage01.lcg.cscs.ch
	prefix = /store/data/Run2015E/SingleMuon/MINIAOD/PromptReco-v1/000/261
	397/00000/A8DA65A7-3B8E-E511-8C33-02163E013745.root = 56118
	397/00000/CAAB76A3-3B8E-E511-9482-02163E0134F1.root = 95082
	398/00000/4C3D439E-3D8E-E511-A01D-02163E0119C2.root = 16788
	399/00000/00AC9572-3F8E-E511-AE17-02163E014602.root = 78409
	401/00000/3E4C8AD5-408E-E511-B6E5-02163E0134DB.root = 13073
	402/00000/44A8DF36-418E-E511-AECD-02163E013522.root = 7576
	422/00000/A0C10611-438E-E511-93BE-02163E013522.root = 3

	>>> cfg = {'lumi filter': '261400-', 'location format': 'sitedb'}
	>>> get('DBS3Provider', '/SingleMuon/Run2015E-PromptReco-v1/*', cfg)
	Runs/lumi section filter enabled!
	Dataset block '/SingleMuon/Run2015E-PromptReco-v1/DQMIO#5447977a-8e3c-11e5-9687-001e67abf228' is not available at the selected locations!
	Available locations: T1_US_FNAL_Buffer, T1_US_FNAL_MSS
	[/SingleMuon/Run2015E-PromptReco-v1/AOD#a7c3638c-8e3e-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_AOD
	events = 20652
	se list = T1_US_FNAL_Disk,T2_FR_GRIF_IRFU
	prefix = /store/data/Run2015E/SingleMuon/AOD/PromptReco-v1/000/261
	metadata = ["Runs"]
	401/00000/E803ABDA-408E-E511-BA79-02163E013522.root = 13073 [[261401]]
	402/00000/32DC2434-418E-E511-AC71-02163E0142D8.root = 7576 [[261402]]
	422/00000/3424AE0E-438E-E511-B5C0-02163E014491.root = 3 [[261422]]
	-----
	[/SingleMuon/Run2015E-PromptReco-v1/MINIAOD#17df3a8a-8e3d-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_MINIAOD
	events = 20652
	se list = T1_RU_JINR_Disk,T1_US_FNAL_Disk,T2_CH_CSCS,T2_US_Nebraska
	prefix = /store/data/Run2015E/SingleMuon/MINIAOD/PromptReco-v1/000/261
	metadata = ["Runs"]
	401/00000/3E4C8AD5-408E-E511-B6E5-02163E0134DB.root = 13073 [[261401]]
	402/00000/44A8DF36-418E-E511-AECD-02163E013522.root = 7576 [[261402]]
	422/00000/A0C10611-438E-E511-93BE-02163E013522.root = 3 [[261422]]
	-----
	[/SingleMuon/Run2015E-PromptReco-v1/RECO#92f50192-8e3c-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_RECO
	events = 20652
	se list = T1_US_FNAL_Disk,T2_FR_GRIF_LLR
	prefix = /store/data/Run2015E/SingleMuon/RECO/PromptReco-v1/000/261
	metadata = ["Runs"]
	401/00000/782C1BE9-408E-E511-8CD0-02163E013945.root = 13073 [[261401]]
	402/00000/E8D05DD6-428E-E511-B51A-02163E0145F6.root = 7576 [[261402]]
	422/00000/34BAD50F-438E-E511-9C7C-02163E011DD8.root = 3 [[261422]]

	>>> cfg = {'lumi filter': '261400-', 'location format': 'both'}
	>>> get('DBS3Provider', '/SingleMuon/Run2015E-PromptReco-v1/*', cfg)
	Runs/lumi section filter enabled!
	Dataset block '/SingleMuon/Run2015E-PromptReco-v1/DQMIO#5447977a-8e3c-11e5-9687-001e67abf228' is not available at the selected locations!
	Available locations: T1_US_FNAL_Buffer/cmssrm.fnal.gov, T1_US_FNAL_MSS/cmssrm.fnal.gov
	[/SingleMuon/Run2015E-PromptReco-v1/AOD#a7c3638c-8e3e-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_AOD
	events = 20652
	se list = T1_US_FNAL_Disk/cmsdcadisk01.fnal.gov,T2_FR_GRIF_IRFU/node12.datagrid.cea.fr
	prefix = /store/data/Run2015E/SingleMuon/AOD/PromptReco-v1/000/261
	metadata = ["Runs"]
	401/00000/E803ABDA-408E-E511-BA79-02163E013522.root = 13073 [[261401]]
	402/00000/32DC2434-418E-E511-AC71-02163E0142D8.root = 7576 [[261402]]
	422/00000/3424AE0E-438E-E511-B5C0-02163E014491.root = 3 [[261422]]
	-----
	[/SingleMuon/Run2015E-PromptReco-v1/MINIAOD#17df3a8a-8e3d-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_MINIAOD
	events = 20652
	se list = T1_RU_JINR_Disk/srm-cms.jinr-t1.ru,T1_US_FNAL_Disk/cmsdcadisk01.fnal.gov,T2_CH_CSCS/storage01.lcg.cscs.ch,T2_US_Nebraska/srm.unl.edu
	prefix = /store/data/Run2015E/SingleMuon/MINIAOD/PromptReco-v1/000/261
	metadata = ["Runs"]
	401/00000/3E4C8AD5-408E-E511-B6E5-02163E0134DB.root = 13073 [[261401]]
	402/00000/44A8DF36-418E-E511-AECD-02163E013522.root = 7576 [[261402]]
	422/00000/A0C10611-438E-E511-93BE-02163E013522.root = 3 [[261422]]
	-----
	[/SingleMuon/Run2015E-PromptReco-v1/RECO#92f50192-8e3c-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_RECO
	events = 20652
	se list = T1_US_FNAL_Disk/cmsdcadisk01.fnal.gov,T2_FR_GRIF_LLR/polgrid4.in2p3.fr
	prefix = /store/data/Run2015E/SingleMuon/RECO/PromptReco-v1/000/261
	metadata = ["Runs"]
	401/00000/782C1BE9-408E-E511-8CD0-02163E013945.root = 13073 [[261401]]
	402/00000/E8D05DD6-428E-E511-B51A-02163E0145F6.root = 7576 [[261402]]
	422/00000/34BAD50F-438E-E511-9C7C-02163E011DD8.root = 3 [[261422]]

	>>> get('DBS3Provider', '/SingleMuon/Run2015E-PromptReco-v1/MINIAOD#17df3a8a-8e3d-11e5-9687-001e67abf228', cfg)
	Runs/lumi section filter enabled!
	[/SingleMuon/Run2015E-PromptReco-v1/MINIAOD#17df3a8a-8e3d-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_MINIAOD
	events = 20652
	se list = T1_RU_JINR_Disk/srm-cms.jinr-t1.ru,T1_US_FNAL_Disk/cmsdcadisk01.fnal.gov,T2_CH_CSCS/storage01.lcg.cscs.ch,T2_US_Nebraska/srm.unl.edu
	prefix = /store/data/Run2015E/SingleMuon/MINIAOD/PromptReco-v1/000/261
	metadata = ["Runs"]
	401/00000/3E4C8AD5-408E-E511-B6E5-02163E0134DB.root = 13073 [[261401]]
	402/00000/44A8DF36-418E-E511-AECD-02163E013522.root = 7576 [[261402]]
	422/00000/A0C10611-438E-E511-93BE-02163E013522.root = 3 [[261422]]

	>>> get('DBS3Provider', '/ZeeHbb_PHG/zixu-ZeeHbb_PHG-RAW-06e6bebb6525c1c46ccfcc56d82513c0/USER @ phys03')
	[/ZeeHbb_PHG/zixu-ZeeHbb_PHG-RAW-06e6bebb6525c1c46ccfcc56d82513c0/USER#cae48e0a-eba4-43f4-85ff-dda11b78dc29]
	nickname = ZeeHbb_PHG_zixu-ZeeHbb_PHG-RAW-06e6bebb6525c1c46ccfcc56d82513c0_USER
	events = 99737
	se list = cmseos.fnal.gov
	prefix = /store/user/lpcmbja/zixu/ZeeHbb_PHG/ZeeHbb_PHG-RAW/06e6bebb6525c1c46ccfcc56d82513c0
	WH_JHUGen_RAWSIM_100_1_aY7.root = 249
	WH_JHUGen_RAWSIM_101_1_wCn.root = 249
	WH_JHUGen_RAWSIM_102_1_Hc4.root = 249
	WH_JHUGen_RAWSIM_103_1_XsE.root = 249
	WH_JHUGen_RAWSIM_104_1_UwT.root = 249
	WH_JHUGen_RAWSIM_105_1_Ztf.root = 249
	WH_JHUGen_RAWSIM_106_1_670.root = 249
	WH_JHUGen_RAWSIM_107_1_2JJ.root = 249
	WH_JHUGen_RAWSIM_108_1_zSZ.root = 249
	WH_JHUGen_RAWSIM_109_1_saN.root = 249
	WH_JHUGen_RAWSIM_10_1_Z15.root = 249
	WH_JHUGen_RAWSIM_110_1_CH5.root = 249
	WH_JHUGen_RAWSIM_111_1_Vi3.root = 249
	WH_JHUGen_RAWSIM_112_1_l5m.root = 249
	WH_JHUGen_RAWSIM_113_1_aqx.root = 249
	WH_JHUGen_RAWSIM_114_1_I4U.root = 249
	WH_JHUGen_RAWSIM_115_1_HjW.root = 249
	WH_JHUGen_RAWSIM_116_1_g1C.root = 249
	WH_JHUGen_RAWSIM_117_1_kbR.root = 249
	WH_JHUGen_RAWSIM_118_1_QP9.root = 249
	WH_JHUGen_RAWSIM_119_1_730.root = 249
	WH_JHUGen_RAWSIM_11_1_e1x.root = 249
	WH_JHUGen_RAWSIM_120_1_aT3.root = 249
	WH_JHUGen_RAWSIM_121_1_81C.root = 249
	WH_JHUGen_RAWSIM_122_1_E7G.root = 249
	WH_JHUGen_RAWSIM_123_1_RAv.root = 249
	WH_JHUGen_RAWSIM_124_1_kN5.root = 249
	WH_JHUGen_RAWSIM_125_1_evD.root = 249
	WH_JHUGen_RAWSIM_126_1_iKx.root = 249
	WH_JHUGen_RAWSIM_127_1_syD.root = 249
	WH_JHUGen_RAWSIM_128_1_5ry.root = 249
	WH_JHUGen_RAWSIM_129_1_2Tm.root = 249
	WH_JHUGen_RAWSIM_12_1_Twe.root = 249
	WH_JHUGen_RAWSIM_130_1_sHa.root = 249
	WH_JHUGen_RAWSIM_131_1_uFo.root = 249
	WH_JHUGen_RAWSIM_132_1_KlU.root = 249
	WH_JHUGen_RAWSIM_133_1_Ssz.root = 249
	WH_JHUGen_RAWSIM_134_1_4uI.root = 249
	WH_JHUGen_RAWSIM_135_1_5Jr.root = 249
	WH_JHUGen_RAWSIM_136_1_10y.root = 249
	WH_JHUGen_RAWSIM_137_1_GKs.root = 249
	WH_JHUGen_RAWSIM_138_1_dV0.root = 249
	WH_JHUGen_RAWSIM_139_1_XgC.root = 249
	WH_JHUGen_RAWSIM_13_1_eL5.root = 249
	WH_JHUGen_RAWSIM_140_1_HmQ.root = 249
	WH_JHUGen_RAWSIM_141_1_PLx.root = 249
	WH_JHUGen_RAWSIM_142_1_iSP.root = 249
	WH_JHUGen_RAWSIM_143_1_avP.root = 249
	WH_JHUGen_RAWSIM_144_1_6S6.root = 249
	WH_JHUGen_RAWSIM_145_1_Rwq.root = 249
	WH_JHUGen_RAWSIM_146_1_Hgp.root = 249
	WH_JHUGen_RAWSIM_147_1_LBT.root = 249
	WH_JHUGen_RAWSIM_148_1_Xeh.root = 249
	WH_JHUGen_RAWSIM_149_1_KGR.root = 249
	WH_JHUGen_RAWSIM_14_1_Rge.root = 249
	WH_JHUGen_RAWSIM_150_1_UB8.root = 249
	WH_JHUGen_RAWSIM_151_1_yNo.root = 249
	WH_JHUGen_RAWSIM_152_1_ARv.root = 249
	WH_JHUGen_RAWSIM_153_1_CkY.root = 249
	WH_JHUGen_RAWSIM_154_1_rKe.root = 249
	WH_JHUGen_RAWSIM_155_1_1ET.root = 249
	WH_JHUGen_RAWSIM_156_1_8LB.root = 249
	WH_JHUGen_RAWSIM_157_1_Mu4.root = 249
	WH_JHUGen_RAWSIM_158_1_Wat.root = 249
	WH_JHUGen_RAWSIM_159_1_CJ9.root = 249
	WH_JHUGen_RAWSIM_15_1_LxP.root = 249
	WH_JHUGen_RAWSIM_160_1_6tz.root = 249
	WH_JHUGen_RAWSIM_161_1_Fx6.root = 249
	WH_JHUGen_RAWSIM_162_1_P1Z.root = 249
	WH_JHUGen_RAWSIM_163_1_lqB.root = 249
	WH_JHUGen_RAWSIM_164_1_P8P.root = 249
	WH_JHUGen_RAWSIM_165_1_ioW.root = 249
	WH_JHUGen_RAWSIM_166_1_Dbu.root = 249
	WH_JHUGen_RAWSIM_167_1_XQT.root = 249
	WH_JHUGen_RAWSIM_168_1_TxA.root = 249
	WH_JHUGen_RAWSIM_169_1_ybV.root = 249
	WH_JHUGen_RAWSIM_16_1_As1.root = 249
	WH_JHUGen_RAWSIM_170_1_FxT.root = 249
	WH_JHUGen_RAWSIM_171_1_KBx.root = 249
	WH_JHUGen_RAWSIM_172_1_tdi.root = 249
	WH_JHUGen_RAWSIM_173_1_pKE.root = 249
	WH_JHUGen_RAWSIM_174_1_SUS.root = 249
	WH_JHUGen_RAWSIM_175_1_J9w.root = 249
	WH_JHUGen_RAWSIM_176_1_v9r.root = 249
	WH_JHUGen_RAWSIM_177_1_Hvs.root = 249
	WH_JHUGen_RAWSIM_178_1_pJV.root = 249
	WH_JHUGen_RAWSIM_179_1_CbV.root = 249
	WH_JHUGen_RAWSIM_17_1_x5n.root = 249
	WH_JHUGen_RAWSIM_180_1_Z8Q.root = 249
	WH_JHUGen_RAWSIM_181_1_3S5.root = 249
	WH_JHUGen_RAWSIM_182_1_sx6.root = 249
	WH_JHUGen_RAWSIM_183_1_lvi.root = 249
	WH_JHUGen_RAWSIM_184_1_7BL.root = 249
	WH_JHUGen_RAWSIM_185_1_3Fw.root = 249
	WH_JHUGen_RAWSIM_186_1_Lwq.root = 249
	WH_JHUGen_RAWSIM_187_1_WNA.root = 249
	WH_JHUGen_RAWSIM_188_1_PVo.root = 249
	WH_JHUGen_RAWSIM_189_1_oyZ.root = 249
	WH_JHUGen_RAWSIM_18_1_Ir0.root = 249
	WH_JHUGen_RAWSIM_190_1_GKR.root = 249
	WH_JHUGen_RAWSIM_191_1_w7l.root = 249
	WH_JHUGen_RAWSIM_192_1_DgO.root = 249
	WH_JHUGen_RAWSIM_193_1_DmI.root = 249
	WH_JHUGen_RAWSIM_194_1_ZMk.root = 249
	WH_JHUGen_RAWSIM_195_1_FXt.root = 249
	WH_JHUGen_RAWSIM_196_1_Thi.root = 249
	WH_JHUGen_RAWSIM_197_1_oIp.root = 249
	WH_JHUGen_RAWSIM_198_1_BFO.root = 249
	WH_JHUGen_RAWSIM_199_1_3c6.root = 249
	WH_JHUGen_RAWSIM_19_1_Vr0.root = 249
	WH_JHUGen_RAWSIM_1_1_rBu.root = 249
	WH_JHUGen_RAWSIM_200_1_r1T.root = 249
	WH_JHUGen_RAWSIM_201_1_9lM.root = 249
	WH_JHUGen_RAWSIM_202_1_B6y.root = 249
	WH_JHUGen_RAWSIM_203_1_Fld.root = 249
	WH_JHUGen_RAWSIM_204_1_lID.root = 249
	WH_JHUGen_RAWSIM_205_1_jPy.root = 249
	WH_JHUGen_RAWSIM_206_1_1Yj.root = 249
	WH_JHUGen_RAWSIM_207_1_7Vk.root = 249
	WH_JHUGen_RAWSIM_208_1_mhh.root = 249
	WH_JHUGen_RAWSIM_209_1_3in.root = 249
	WH_JHUGen_RAWSIM_20_1_vvO.root = 249
	WH_JHUGen_RAWSIM_210_1_SRO.root = 249
	WH_JHUGen_RAWSIM_211_1_HtB.root = 249
	WH_JHUGen_RAWSIM_212_1_Gv7.root = 249
	WH_JHUGen_RAWSIM_213_1_Dp2.root = 249
	WH_JHUGen_RAWSIM_214_1_Mvl.root = 249
	WH_JHUGen_RAWSIM_215_1_b0l.root = 249
	WH_JHUGen_RAWSIM_216_1_nDr.root = 249
	WH_JHUGen_RAWSIM_217_1_0Km.root = 249
	WH_JHUGen_RAWSIM_218_1_qqZ.root = 249
	WH_JHUGen_RAWSIM_219_1_7fb.root = 249
	WH_JHUGen_RAWSIM_21_1_wJw.root = 249
	WH_JHUGen_RAWSIM_220_1_ul4.root = 249
	WH_JHUGen_RAWSIM_221_1_3Sk.root = 249
	WH_JHUGen_RAWSIM_222_1_Il9.root = 249
	WH_JHUGen_RAWSIM_223_1_3mC.root = 249
	WH_JHUGen_RAWSIM_224_1_QLI.root = 249
	WH_JHUGen_RAWSIM_225_1_InT.root = 249
	WH_JHUGen_RAWSIM_226_1_WiQ.root = 249
	WH_JHUGen_RAWSIM_227_1_Gmm.root = 249
	WH_JHUGen_RAWSIM_228_1_lMH.root = 249
	WH_JHUGen_RAWSIM_229_1_DtZ.root = 249
	WH_JHUGen_RAWSIM_22_1_TdF.root = 249
	WH_JHUGen_RAWSIM_230_1_VbE.root = 249
	WH_JHUGen_RAWSIM_231_1_7rd.root = 249
	WH_JHUGen_RAWSIM_232_1_oRG.root = 249
	WH_JHUGen_RAWSIM_233_1_sEN.root = 249
	WH_JHUGen_RAWSIM_234_1_cDD.root = 249
	WH_JHUGen_RAWSIM_235_1_3jD.root = 249
	WH_JHUGen_RAWSIM_236_1_AMC.root = 249
	WH_JHUGen_RAWSIM_237_1_rqC.root = 249
	WH_JHUGen_RAWSIM_238_1_tjh.root = 249
	WH_JHUGen_RAWSIM_239_1_hNy.root = 249
	WH_JHUGen_RAWSIM_23_1_YJZ.root = 249
	WH_JHUGen_RAWSIM_240_1_o0h.root = 249
	WH_JHUGen_RAWSIM_241_1_khJ.root = 249
	WH_JHUGen_RAWSIM_242_1_DC1.root = 249
	WH_JHUGen_RAWSIM_243_1_WwW.root = 249
	WH_JHUGen_RAWSIM_244_1_y6s.root = 249
	WH_JHUGen_RAWSIM_245_1_Hee.root = 249
	WH_JHUGen_RAWSIM_246_1_Qj9.root = 249
	WH_JHUGen_RAWSIM_247_1_xdX.root = 249
	WH_JHUGen_RAWSIM_248_1_hbw.root = 249
	WH_JHUGen_RAWSIM_249_1_Tqr.root = 249
	WH_JHUGen_RAWSIM_24_1_7CR.root = 249
	WH_JHUGen_RAWSIM_250_1_5FL.root = 249
	WH_JHUGen_RAWSIM_251_1_t8m.root = 249
	WH_JHUGen_RAWSIM_252_1_5lm.root = 249
	WH_JHUGen_RAWSIM_253_1_PNt.root = 249
	WH_JHUGen_RAWSIM_254_1_cZW.root = 249
	WH_JHUGen_RAWSIM_255_1_m3h.root = 249
	WH_JHUGen_RAWSIM_256_1_M3d.root = 249
	WH_JHUGen_RAWSIM_257_1_SgI.root = 249
	WH_JHUGen_RAWSIM_258_1_lqS.root = 249
	WH_JHUGen_RAWSIM_259_1_Fy6.root = 249
	WH_JHUGen_RAWSIM_25_1_h0T.root = 249
	WH_JHUGen_RAWSIM_260_1_ZlA.root = 249
	WH_JHUGen_RAWSIM_261_1_4x6.root = 249
	WH_JHUGen_RAWSIM_262_1_yai.root = 249
	WH_JHUGen_RAWSIM_263_1_2sR.root = 249
	WH_JHUGen_RAWSIM_264_1_oPq.root = 249
	WH_JHUGen_RAWSIM_265_1_A09.root = 249
	WH_JHUGen_RAWSIM_266_1_kxV.root = 249
	WH_JHUGen_RAWSIM_267_1_8mV.root = 249
	WH_JHUGen_RAWSIM_268_1_eHE.root = 249
	WH_JHUGen_RAWSIM_269_1_nWQ.root = 249
	WH_JHUGen_RAWSIM_26_1_xyR.root = 249
	WH_JHUGen_RAWSIM_270_1_zpH.root = 249
	WH_JHUGen_RAWSIM_271_1_Ew8.root = 249
	WH_JHUGen_RAWSIM_272_1_Lzb.root = 249
	WH_JHUGen_RAWSIM_273_1_ILF.root = 249
	WH_JHUGen_RAWSIM_274_1_Pol.root = 249
	WH_JHUGen_RAWSIM_275_1_IoI.root = 249
	WH_JHUGen_RAWSIM_276_1_JDd.root = 249
	WH_JHUGen_RAWSIM_277_1_uX3.root = 249
	WH_JHUGen_RAWSIM_278_1_HkI.root = 249
	WH_JHUGen_RAWSIM_279_1_YsI.root = 249
	WH_JHUGen_RAWSIM_27_1_ES2.root = 249
	WH_JHUGen_RAWSIM_280_1_woC.root = 249
	WH_JHUGen_RAWSIM_281_1_4G8.root = 249
	WH_JHUGen_RAWSIM_282_1_bxp.root = 249
	WH_JHUGen_RAWSIM_283_1_9oR.root = 249
	WH_JHUGen_RAWSIM_284_1_M9V.root = 249
	WH_JHUGen_RAWSIM_285_1_Fcf.root = 249
	WH_JHUGen_RAWSIM_286_1_Afp.root = 249
	WH_JHUGen_RAWSIM_287_1_WZd.root = 249
	WH_JHUGen_RAWSIM_288_1_TYC.root = 249
	WH_JHUGen_RAWSIM_289_1_2he.root = 249
	WH_JHUGen_RAWSIM_28_1_chU.root = 249
	WH_JHUGen_RAWSIM_290_1_EQN.root = 249
	WH_JHUGen_RAWSIM_291_1_IUI.root = 249
	WH_JHUGen_RAWSIM_292_1_Bg9.root = 249
	WH_JHUGen_RAWSIM_293_1_O8u.root = 249
	WH_JHUGen_RAWSIM_294_1_1Ln.root = 249
	WH_JHUGen_RAWSIM_295_1_bBf.root = 249
	WH_JHUGen_RAWSIM_296_1_jf8.root = 249
	WH_JHUGen_RAWSIM_297_1_NTV.root = 249
	WH_JHUGen_RAWSIM_298_1_csy.root = 249
	WH_JHUGen_RAWSIM_299_1_g3K.root = 249
	WH_JHUGen_RAWSIM_29_1_PZ4.root = 249
	WH_JHUGen_RAWSIM_2_1_hLd.root = 249
	WH_JHUGen_RAWSIM_300_1_S7i.root = 249
	WH_JHUGen_RAWSIM_301_1_e5e.root = 249
	WH_JHUGen_RAWSIM_302_1_QO9.root = 249
	WH_JHUGen_RAWSIM_303_1_m5t.root = 249
	WH_JHUGen_RAWSIM_304_1_7Pa.root = 249
	WH_JHUGen_RAWSIM_305_1_q4t.root = 249
	WH_JHUGen_RAWSIM_306_1_06f.root = 249
	WH_JHUGen_RAWSIM_307_1_8E2.root = 249
	WH_JHUGen_RAWSIM_308_1_WLx.root = 249
	WH_JHUGen_RAWSIM_309_1_Tlw.root = 249
	WH_JHUGen_RAWSIM_30_1_iGm.root = 249
	WH_JHUGen_RAWSIM_310_1_5bk.root = 249
	WH_JHUGen_RAWSIM_311_1_mOB.root = 249
	WH_JHUGen_RAWSIM_312_1_cRK.root = 249
	WH_JHUGen_RAWSIM_313_1_Yuf.root = 249
	WH_JHUGen_RAWSIM_314_1_H0h.root = 249
	WH_JHUGen_RAWSIM_315_1_TYN.root = 249
	WH_JHUGen_RAWSIM_316_1_p74.root = 249
	WH_JHUGen_RAWSIM_317_1_M6c.root = 249
	WH_JHUGen_RAWSIM_318_1_f1t.root = 249
	WH_JHUGen_RAWSIM_319_1_8Sm.root = 249
	WH_JHUGen_RAWSIM_31_1_nZP.root = 249
	WH_JHUGen_RAWSIM_320_1_CbY.root = 249
	WH_JHUGen_RAWSIM_321_1_DDI.root = 249
	WH_JHUGen_RAWSIM_322_1_0Hz.root = 249
	WH_JHUGen_RAWSIM_323_1_ptK.root = 249
	WH_JHUGen_RAWSIM_324_1_R5R.root = 249
	WH_JHUGen_RAWSIM_325_1_iXH.root = 249
	WH_JHUGen_RAWSIM_326_1_epZ.root = 249
	WH_JHUGen_RAWSIM_327_1_NMx.root = 249
	WH_JHUGen_RAWSIM_328_1_p1T.root = 249
	WH_JHUGen_RAWSIM_329_1_WHU.root = 249
	WH_JHUGen_RAWSIM_32_1_yXt.root = 249
	WH_JHUGen_RAWSIM_330_1_obx.root = 249
	WH_JHUGen_RAWSIM_331_1_rR6.root = 249
	WH_JHUGen_RAWSIM_332_1_85C.root = 249
	WH_JHUGen_RAWSIM_333_1_Q4H.root = 249
	WH_JHUGen_RAWSIM_334_1_5Sg.root = 249
	WH_JHUGen_RAWSIM_335_1_Px0.root = 249
	WH_JHUGen_RAWSIM_336_1_ZRx.root = 249
	WH_JHUGen_RAWSIM_337_1_weo.root = 249
	WH_JHUGen_RAWSIM_338_1_TJn.root = 249
	WH_JHUGen_RAWSIM_339_1_u3x.root = 249
	WH_JHUGen_RAWSIM_33_1_iFh.root = 249
	WH_JHUGen_RAWSIM_340_1_OA3.root = 249
	WH_JHUGen_RAWSIM_341_1_X7A.root = 249
	WH_JHUGen_RAWSIM_342_1_Z0Z.root = 249
	WH_JHUGen_RAWSIM_343_1_Wuz.root = 249
	WH_JHUGen_RAWSIM_344_1_qoH.root = 249
	WH_JHUGen_RAWSIM_345_1_m8N.root = 249
	WH_JHUGen_RAWSIM_346_1_Gpd.root = 249
	WH_JHUGen_RAWSIM_347_1_Nzt.root = 249
	WH_JHUGen_RAWSIM_348_1_UCQ.root = 249
	WH_JHUGen_RAWSIM_349_1_5gp.root = 249
	WH_JHUGen_RAWSIM_34_1_rR3.root = 249
	WH_JHUGen_RAWSIM_350_1_hvQ.root = 249
	WH_JHUGen_RAWSIM_351_1_7KZ.root = 249
	WH_JHUGen_RAWSIM_352_1_vOY.root = 249
	WH_JHUGen_RAWSIM_353_1_xNi.root = 249
	WH_JHUGen_RAWSIM_354_1_ila.root = 249
	WH_JHUGen_RAWSIM_355_1_R6o.root = 249
	WH_JHUGen_RAWSIM_356_1_XPQ.root = 249
	WH_JHUGen_RAWSIM_357_1_jMs.root = 249
	WH_JHUGen_RAWSIM_358_1_fRV.root = 249
	WH_JHUGen_RAWSIM_359_1_0YH.root = 249
	WH_JHUGen_RAWSIM_35_1_cOZ.root = 249
	WH_JHUGen_RAWSIM_360_1_7PY.root = 249
	WH_JHUGen_RAWSIM_361_1_B1P.root = 249
	WH_JHUGen_RAWSIM_362_1_nYY.root = 249
	WH_JHUGen_RAWSIM_363_1_gyJ.root = 249
	WH_JHUGen_RAWSIM_364_1_OD8.root = 249
	WH_JHUGen_RAWSIM_365_1_Fgt.root = 249
	WH_JHUGen_RAWSIM_366_1_hp3.root = 249
	WH_JHUGen_RAWSIM_367_1_Nz7.root = 249
	WH_JHUGen_RAWSIM_368_1_Awn.root = 249
	WH_JHUGen_RAWSIM_36_1_VuF.root = 249
	WH_JHUGen_RAWSIM_370_1_vXA.root = 249
	WH_JHUGen_RAWSIM_371_1_xvX.root = 249
	WH_JHUGen_RAWSIM_372_1_lRl.root = 249
	WH_JHUGen_RAWSIM_373_1_JCQ.root = 249
	WH_JHUGen_RAWSIM_374_1_1Xg.root = 249
	WH_JHUGen_RAWSIM_375_1_BiP.root = 249
	WH_JHUGen_RAWSIM_376_1_RIk.root = 249
	WH_JHUGen_RAWSIM_377_1_7aa.root = 249
	WH_JHUGen_RAWSIM_378_1_2Hx.root = 249
	WH_JHUGen_RAWSIM_379_1_pgy.root = 249
	WH_JHUGen_RAWSIM_37_1_QYQ.root = 249
	WH_JHUGen_RAWSIM_380_1_2bi.root = 249
	WH_JHUGen_RAWSIM_381_1_1YA.root = 249
	WH_JHUGen_RAWSIM_382_1_jvD.root = 249
	WH_JHUGen_RAWSIM_383_1_zDf.root = 249
	WH_JHUGen_RAWSIM_384_1_rDo.root = 249
	WH_JHUGen_RAWSIM_385_1_0to.root = 249
	WH_JHUGen_RAWSIM_386_1_ZK3.root = 249
	WH_JHUGen_RAWSIM_387_1_4Sv.root = 249
	WH_JHUGen_RAWSIM_388_1_qU2.root = 249
	WH_JHUGen_RAWSIM_389_1_F6Q.root = 249
	WH_JHUGen_RAWSIM_38_1_es2.root = 249
	WH_JHUGen_RAWSIM_390_1_rq8.root = 249
	WH_JHUGen_RAWSIM_391_1_K9o.root = 249
	WH_JHUGen_RAWSIM_392_1_NIj.root = 249
	WH_JHUGen_RAWSIM_393_1_ihZ.root = 249
	WH_JHUGen_RAWSIM_394_1_nKn.root = 249
	WH_JHUGen_RAWSIM_395_1_rx4.root = 249
	WH_JHUGen_RAWSIM_396_1_qEf.root = 249
	WH_JHUGen_RAWSIM_397_1_IUV.root = 249
	WH_JHUGen_RAWSIM_398_1_BFC.root = 249
	WH_JHUGen_RAWSIM_399_1_BoT.root = 249
	WH_JHUGen_RAWSIM_39_1_CH0.root = 249
	WH_JHUGen_RAWSIM_3_1_yqE.root = 249
	WH_JHUGen_RAWSIM_400_1_6w4.root = 249
	WH_JHUGen_RAWSIM_401_1_gc0.root = 249
	WH_JHUGen_RAWSIM_402_1_IYk.root = 137
	WH_JHUGen_RAWSIM_40_1_NoH.root = 249
	WH_JHUGen_RAWSIM_41_1_QUQ.root = 249
	WH_JHUGen_RAWSIM_42_1_EH2.root = 249
	WH_JHUGen_RAWSIM_43_1_Cpl.root = 249
	WH_JHUGen_RAWSIM_44_1_aAf.root = 249
	WH_JHUGen_RAWSIM_45_1_ukg.root = 249
	WH_JHUGen_RAWSIM_46_1_XWk.root = 249
	WH_JHUGen_RAWSIM_47_1_XrO.root = 249
	WH_JHUGen_RAWSIM_48_1_17t.root = 249
	WH_JHUGen_RAWSIM_49_1_jHu.root = 249
	WH_JHUGen_RAWSIM_4_1_5Au.root = 249
	WH_JHUGen_RAWSIM_50_1_yBQ.root = 249
	WH_JHUGen_RAWSIM_51_1_t1s.root = 249
	WH_JHUGen_RAWSIM_52_1_AFj.root = 249
	WH_JHUGen_RAWSIM_53_1_tJ1.root = 249
	WH_JHUGen_RAWSIM_54_1_nUx.root = 249
	WH_JHUGen_RAWSIM_55_1_PVj.root = 249
	WH_JHUGen_RAWSIM_56_1_lbk.root = 249
	WH_JHUGen_RAWSIM_57_1_RSW.root = 249
	WH_JHUGen_RAWSIM_58_1_qxm.root = 249
	WH_JHUGen_RAWSIM_59_1_yt8.root = 249
	WH_JHUGen_RAWSIM_5_1_2I7.root = 249
	WH_JHUGen_RAWSIM_60_1_IV4.root = 249
	WH_JHUGen_RAWSIM_61_1_ePl.root = 249
	WH_JHUGen_RAWSIM_62_1_eo9.root = 249
	WH_JHUGen_RAWSIM_63_1_ja0.root = 249
	WH_JHUGen_RAWSIM_64_1_hJ0.root = 249
	WH_JHUGen_RAWSIM_65_1_Blv.root = 249
	WH_JHUGen_RAWSIM_66_1_qZh.root = 249
	WH_JHUGen_RAWSIM_67_1_HN7.root = 249
	WH_JHUGen_RAWSIM_68_1_4dd.root = 249
	WH_JHUGen_RAWSIM_69_1_0Nb.root = 249
	WH_JHUGen_RAWSIM_6_1_ZKQ.root = 249
	WH_JHUGen_RAWSIM_70_1_V0f.root = 249
	WH_JHUGen_RAWSIM_71_1_egc.root = 249
	WH_JHUGen_RAWSIM_72_1_aRf.root = 249
	WH_JHUGen_RAWSIM_73_1_3ZH.root = 249
	WH_JHUGen_RAWSIM_74_1_LAy.root = 249
	WH_JHUGen_RAWSIM_75_1_gVW.root = 249
	WH_JHUGen_RAWSIM_76_1_ZLO.root = 249
	WH_JHUGen_RAWSIM_77_1_QDQ.root = 249
	WH_JHUGen_RAWSIM_78_1_AIb.root = 249
	WH_JHUGen_RAWSIM_79_1_ZE6.root = 249
	WH_JHUGen_RAWSIM_7_1_avP.root = 249
	WH_JHUGen_RAWSIM_80_1_FRt.root = 249
	WH_JHUGen_RAWSIM_81_1_I9G.root = 249
	WH_JHUGen_RAWSIM_82_1_qqQ.root = 249
	WH_JHUGen_RAWSIM_83_1_rQC.root = 249
	WH_JHUGen_RAWSIM_84_1_ALN.root = 249
	WH_JHUGen_RAWSIM_85_1_J6t.root = 249
	WH_JHUGen_RAWSIM_86_1_qCS.root = 249
	WH_JHUGen_RAWSIM_87_1_4qN.root = 249
	WH_JHUGen_RAWSIM_88_1_j06.root = 249
	WH_JHUGen_RAWSIM_89_1_2nd.root = 249
	WH_JHUGen_RAWSIM_8_1_l4q.root = 249
	WH_JHUGen_RAWSIM_90_1_5Uc.root = 249
	WH_JHUGen_RAWSIM_91_1_NsI.root = 249
	WH_JHUGen_RAWSIM_92_1_hTk.root = 249
	WH_JHUGen_RAWSIM_93_1_kcC.root = 249
	WH_JHUGen_RAWSIM_94_1_mjH.root = 249
	WH_JHUGen_RAWSIM_95_1_jkz.root = 249
	WH_JHUGen_RAWSIM_96_1_m35.root = 249
	WH_JHUGen_RAWSIM_97_1_6YN.root = 249
	WH_JHUGen_RAWSIM_98_1_AYX.root = 249
	WH_JHUGen_RAWSIM_99_1_lWI.root = 249
	WH_JHUGen_RAWSIM_9_1_MG0.root = 249

	>>> get('DASProvider', '/ZeeHbb_PHG/zixu-ZeeHbb_PHG-RAW-06e6bebb6525c1c46ccfcc56d82513c0/USER @ phys03')
	[/ZeeHbb_PHG/zixu-ZeeHbb_PHG-RAW-06e6bebb6525c1c46ccfcc56d82513c0/USER#cae48e0a-eba4-43f4-85ff-dda11b78dc29]
	nickname = ZeeHbb_PHG_zixu-ZeeHbb_PHG-RAW-06e6bebb6525c1c46ccfcc56d82513c0_USER
	events = 99737
	se list = cmseos.fnal.gov
	prefix = /store/user/lpcmbja/zixu/ZeeHbb_PHG/ZeeHbb_PHG-RAW/06e6bebb6525c1c46ccfcc56d82513c0
	WH_JHUGen_RAWSIM_100_1_aY7.root = 249
	WH_JHUGen_RAWSIM_101_1_wCn.root = 249
	WH_JHUGen_RAWSIM_102_1_Hc4.root = 249
	WH_JHUGen_RAWSIM_103_1_XsE.root = 249
	WH_JHUGen_RAWSIM_104_1_UwT.root = 249
	WH_JHUGen_RAWSIM_105_1_Ztf.root = 249
	WH_JHUGen_RAWSIM_106_1_670.root = 249
	WH_JHUGen_RAWSIM_107_1_2JJ.root = 249
	WH_JHUGen_RAWSIM_108_1_zSZ.root = 249
	WH_JHUGen_RAWSIM_109_1_saN.root = 249
	WH_JHUGen_RAWSIM_10_1_Z15.root = 249
	WH_JHUGen_RAWSIM_110_1_CH5.root = 249
	WH_JHUGen_RAWSIM_111_1_Vi3.root = 249
	WH_JHUGen_RAWSIM_112_1_l5m.root = 249
	WH_JHUGen_RAWSIM_113_1_aqx.root = 249
	WH_JHUGen_RAWSIM_114_1_I4U.root = 249
	WH_JHUGen_RAWSIM_115_1_HjW.root = 249
	WH_JHUGen_RAWSIM_116_1_g1C.root = 249
	WH_JHUGen_RAWSIM_117_1_kbR.root = 249
	WH_JHUGen_RAWSIM_118_1_QP9.root = 249
	WH_JHUGen_RAWSIM_119_1_730.root = 249
	WH_JHUGen_RAWSIM_11_1_e1x.root = 249
	WH_JHUGen_RAWSIM_120_1_aT3.root = 249
	WH_JHUGen_RAWSIM_121_1_81C.root = 249
	WH_JHUGen_RAWSIM_122_1_E7G.root = 249
	WH_JHUGen_RAWSIM_123_1_RAv.root = 249
	WH_JHUGen_RAWSIM_124_1_kN5.root = 249
	WH_JHUGen_RAWSIM_125_1_evD.root = 249
	WH_JHUGen_RAWSIM_126_1_iKx.root = 249
	WH_JHUGen_RAWSIM_127_1_syD.root = 249
	WH_JHUGen_RAWSIM_128_1_5ry.root = 249
	WH_JHUGen_RAWSIM_129_1_2Tm.root = 249
	WH_JHUGen_RAWSIM_12_1_Twe.root = 249
	WH_JHUGen_RAWSIM_130_1_sHa.root = 249
	WH_JHUGen_RAWSIM_131_1_uFo.root = 249
	WH_JHUGen_RAWSIM_132_1_KlU.root = 249
	WH_JHUGen_RAWSIM_133_1_Ssz.root = 249
	WH_JHUGen_RAWSIM_134_1_4uI.root = 249
	WH_JHUGen_RAWSIM_135_1_5Jr.root = 249
	WH_JHUGen_RAWSIM_136_1_10y.root = 249
	WH_JHUGen_RAWSIM_137_1_GKs.root = 249
	WH_JHUGen_RAWSIM_138_1_dV0.root = 249
	WH_JHUGen_RAWSIM_139_1_XgC.root = 249
	WH_JHUGen_RAWSIM_13_1_eL5.root = 249
	WH_JHUGen_RAWSIM_140_1_HmQ.root = 249
	WH_JHUGen_RAWSIM_141_1_PLx.root = 249
	WH_JHUGen_RAWSIM_142_1_iSP.root = 249
	WH_JHUGen_RAWSIM_143_1_avP.root = 249
	WH_JHUGen_RAWSIM_144_1_6S6.root = 249
	WH_JHUGen_RAWSIM_145_1_Rwq.root = 249
	WH_JHUGen_RAWSIM_146_1_Hgp.root = 249
	WH_JHUGen_RAWSIM_147_1_LBT.root = 249
	WH_JHUGen_RAWSIM_148_1_Xeh.root = 249
	WH_JHUGen_RAWSIM_149_1_KGR.root = 249
	WH_JHUGen_RAWSIM_14_1_Rge.root = 249
	WH_JHUGen_RAWSIM_150_1_UB8.root = 249
	WH_JHUGen_RAWSIM_151_1_yNo.root = 249
	WH_JHUGen_RAWSIM_152_1_ARv.root = 249
	WH_JHUGen_RAWSIM_153_1_CkY.root = 249
	WH_JHUGen_RAWSIM_154_1_rKe.root = 249
	WH_JHUGen_RAWSIM_155_1_1ET.root = 249
	WH_JHUGen_RAWSIM_156_1_8LB.root = 249
	WH_JHUGen_RAWSIM_157_1_Mu4.root = 249
	WH_JHUGen_RAWSIM_158_1_Wat.root = 249
	WH_JHUGen_RAWSIM_159_1_CJ9.root = 249
	WH_JHUGen_RAWSIM_15_1_LxP.root = 249
	WH_JHUGen_RAWSIM_160_1_6tz.root = 249
	WH_JHUGen_RAWSIM_161_1_Fx6.root = 249
	WH_JHUGen_RAWSIM_162_1_P1Z.root = 249
	WH_JHUGen_RAWSIM_163_1_lqB.root = 249
	WH_JHUGen_RAWSIM_164_1_P8P.root = 249
	WH_JHUGen_RAWSIM_165_1_ioW.root = 249
	WH_JHUGen_RAWSIM_166_1_Dbu.root = 249
	WH_JHUGen_RAWSIM_167_1_XQT.root = 249
	WH_JHUGen_RAWSIM_168_1_TxA.root = 249
	WH_JHUGen_RAWSIM_169_1_ybV.root = 249
	WH_JHUGen_RAWSIM_16_1_As1.root = 249
	WH_JHUGen_RAWSIM_170_1_FxT.root = 249
	WH_JHUGen_RAWSIM_171_1_KBx.root = 249
	WH_JHUGen_RAWSIM_172_1_tdi.root = 249
	WH_JHUGen_RAWSIM_173_1_pKE.root = 249
	WH_JHUGen_RAWSIM_174_1_SUS.root = 249
	WH_JHUGen_RAWSIM_175_1_J9w.root = 249
	WH_JHUGen_RAWSIM_176_1_v9r.root = 249
	WH_JHUGen_RAWSIM_177_1_Hvs.root = 249
	WH_JHUGen_RAWSIM_178_1_pJV.root = 249
	WH_JHUGen_RAWSIM_179_1_CbV.root = 249
	WH_JHUGen_RAWSIM_17_1_x5n.root = 249
	WH_JHUGen_RAWSIM_180_1_Z8Q.root = 249
	WH_JHUGen_RAWSIM_181_1_3S5.root = 249
	WH_JHUGen_RAWSIM_182_1_sx6.root = 249
	WH_JHUGen_RAWSIM_183_1_lvi.root = 249
	WH_JHUGen_RAWSIM_184_1_7BL.root = 249
	WH_JHUGen_RAWSIM_185_1_3Fw.root = 249
	WH_JHUGen_RAWSIM_186_1_Lwq.root = 249
	WH_JHUGen_RAWSIM_187_1_WNA.root = 249
	WH_JHUGen_RAWSIM_188_1_PVo.root = 249
	WH_JHUGen_RAWSIM_189_1_oyZ.root = 249
	WH_JHUGen_RAWSIM_18_1_Ir0.root = 249
	WH_JHUGen_RAWSIM_190_1_GKR.root = 249
	WH_JHUGen_RAWSIM_191_1_w7l.root = 249
	WH_JHUGen_RAWSIM_192_1_DgO.root = 249
	WH_JHUGen_RAWSIM_193_1_DmI.root = 249
	WH_JHUGen_RAWSIM_194_1_ZMk.root = 249
	WH_JHUGen_RAWSIM_195_1_FXt.root = 249
	WH_JHUGen_RAWSIM_196_1_Thi.root = 249
	WH_JHUGen_RAWSIM_197_1_oIp.root = 249
	WH_JHUGen_RAWSIM_198_1_BFO.root = 249
	WH_JHUGen_RAWSIM_199_1_3c6.root = 249
	WH_JHUGen_RAWSIM_19_1_Vr0.root = 249
	WH_JHUGen_RAWSIM_1_1_rBu.root = 249
	WH_JHUGen_RAWSIM_200_1_r1T.root = 249
	WH_JHUGen_RAWSIM_201_1_9lM.root = 249
	WH_JHUGen_RAWSIM_202_1_B6y.root = 249
	WH_JHUGen_RAWSIM_203_1_Fld.root = 249
	WH_JHUGen_RAWSIM_204_1_lID.root = 249
	WH_JHUGen_RAWSIM_205_1_jPy.root = 249
	WH_JHUGen_RAWSIM_206_1_1Yj.root = 249
	WH_JHUGen_RAWSIM_207_1_7Vk.root = 249
	WH_JHUGen_RAWSIM_208_1_mhh.root = 249
	WH_JHUGen_RAWSIM_209_1_3in.root = 249
	WH_JHUGen_RAWSIM_20_1_vvO.root = 249
	WH_JHUGen_RAWSIM_210_1_SRO.root = 249
	WH_JHUGen_RAWSIM_211_1_HtB.root = 249
	WH_JHUGen_RAWSIM_212_1_Gv7.root = 249
	WH_JHUGen_RAWSIM_213_1_Dp2.root = 249
	WH_JHUGen_RAWSIM_214_1_Mvl.root = 249
	WH_JHUGen_RAWSIM_215_1_b0l.root = 249
	WH_JHUGen_RAWSIM_216_1_nDr.root = 249
	WH_JHUGen_RAWSIM_217_1_0Km.root = 249
	WH_JHUGen_RAWSIM_218_1_qqZ.root = 249
	WH_JHUGen_RAWSIM_219_1_7fb.root = 249
	WH_JHUGen_RAWSIM_21_1_wJw.root = 249
	WH_JHUGen_RAWSIM_220_1_ul4.root = 249
	WH_JHUGen_RAWSIM_221_1_3Sk.root = 249
	WH_JHUGen_RAWSIM_222_1_Il9.root = 249
	WH_JHUGen_RAWSIM_223_1_3mC.root = 249
	WH_JHUGen_RAWSIM_224_1_QLI.root = 249
	WH_JHUGen_RAWSIM_225_1_InT.root = 249
	WH_JHUGen_RAWSIM_226_1_WiQ.root = 249
	WH_JHUGen_RAWSIM_227_1_Gmm.root = 249
	WH_JHUGen_RAWSIM_228_1_lMH.root = 249
	WH_JHUGen_RAWSIM_229_1_DtZ.root = 249
	WH_JHUGen_RAWSIM_22_1_TdF.root = 249
	WH_JHUGen_RAWSIM_230_1_VbE.root = 249
	WH_JHUGen_RAWSIM_231_1_7rd.root = 249
	WH_JHUGen_RAWSIM_232_1_oRG.root = 249
	WH_JHUGen_RAWSIM_233_1_sEN.root = 249
	WH_JHUGen_RAWSIM_234_1_cDD.root = 249
	WH_JHUGen_RAWSIM_235_1_3jD.root = 249
	WH_JHUGen_RAWSIM_236_1_AMC.root = 249
	WH_JHUGen_RAWSIM_237_1_rqC.root = 249
	WH_JHUGen_RAWSIM_238_1_tjh.root = 249
	WH_JHUGen_RAWSIM_239_1_hNy.root = 249
	WH_JHUGen_RAWSIM_23_1_YJZ.root = 249
	WH_JHUGen_RAWSIM_240_1_o0h.root = 249
	WH_JHUGen_RAWSIM_241_1_khJ.root = 249
	WH_JHUGen_RAWSIM_242_1_DC1.root = 249
	WH_JHUGen_RAWSIM_243_1_WwW.root = 249
	WH_JHUGen_RAWSIM_244_1_y6s.root = 249
	WH_JHUGen_RAWSIM_245_1_Hee.root = 249
	WH_JHUGen_RAWSIM_246_1_Qj9.root = 249
	WH_JHUGen_RAWSIM_247_1_xdX.root = 249
	WH_JHUGen_RAWSIM_248_1_hbw.root = 249
	WH_JHUGen_RAWSIM_249_1_Tqr.root = 249
	WH_JHUGen_RAWSIM_24_1_7CR.root = 249
	WH_JHUGen_RAWSIM_250_1_5FL.root = 249
	WH_JHUGen_RAWSIM_251_1_t8m.root = 249
	WH_JHUGen_RAWSIM_252_1_5lm.root = 249
	WH_JHUGen_RAWSIM_253_1_PNt.root = 249
	WH_JHUGen_RAWSIM_254_1_cZW.root = 249
	WH_JHUGen_RAWSIM_255_1_m3h.root = 249
	WH_JHUGen_RAWSIM_256_1_M3d.root = 249
	WH_JHUGen_RAWSIM_257_1_SgI.root = 249
	WH_JHUGen_RAWSIM_258_1_lqS.root = 249
	WH_JHUGen_RAWSIM_259_1_Fy6.root = 249
	WH_JHUGen_RAWSIM_25_1_h0T.root = 249
	WH_JHUGen_RAWSIM_260_1_ZlA.root = 249
	WH_JHUGen_RAWSIM_261_1_4x6.root = 249
	WH_JHUGen_RAWSIM_262_1_yai.root = 249
	WH_JHUGen_RAWSIM_263_1_2sR.root = 249
	WH_JHUGen_RAWSIM_264_1_oPq.root = 249
	WH_JHUGen_RAWSIM_265_1_A09.root = 249
	WH_JHUGen_RAWSIM_266_1_kxV.root = 249
	WH_JHUGen_RAWSIM_267_1_8mV.root = 249
	WH_JHUGen_RAWSIM_268_1_eHE.root = 249
	WH_JHUGen_RAWSIM_269_1_nWQ.root = 249
	WH_JHUGen_RAWSIM_26_1_xyR.root = 249
	WH_JHUGen_RAWSIM_270_1_zpH.root = 249
	WH_JHUGen_RAWSIM_271_1_Ew8.root = 249
	WH_JHUGen_RAWSIM_272_1_Lzb.root = 249
	WH_JHUGen_RAWSIM_273_1_ILF.root = 249
	WH_JHUGen_RAWSIM_274_1_Pol.root = 249
	WH_JHUGen_RAWSIM_275_1_IoI.root = 249
	WH_JHUGen_RAWSIM_276_1_JDd.root = 249
	WH_JHUGen_RAWSIM_277_1_uX3.root = 249
	WH_JHUGen_RAWSIM_278_1_HkI.root = 249
	WH_JHUGen_RAWSIM_279_1_YsI.root = 249
	WH_JHUGen_RAWSIM_27_1_ES2.root = 249
	WH_JHUGen_RAWSIM_280_1_woC.root = 249
	WH_JHUGen_RAWSIM_281_1_4G8.root = 249
	WH_JHUGen_RAWSIM_282_1_bxp.root = 249
	WH_JHUGen_RAWSIM_283_1_9oR.root = 249
	WH_JHUGen_RAWSIM_284_1_M9V.root = 249
	WH_JHUGen_RAWSIM_285_1_Fcf.root = 249
	WH_JHUGen_RAWSIM_286_1_Afp.root = 249
	WH_JHUGen_RAWSIM_287_1_WZd.root = 249
	WH_JHUGen_RAWSIM_288_1_TYC.root = 249
	WH_JHUGen_RAWSIM_289_1_2he.root = 249
	WH_JHUGen_RAWSIM_28_1_chU.root = 249
	WH_JHUGen_RAWSIM_290_1_EQN.root = 249
	WH_JHUGen_RAWSIM_291_1_IUI.root = 249
	WH_JHUGen_RAWSIM_292_1_Bg9.root = 249
	WH_JHUGen_RAWSIM_293_1_O8u.root = 249
	WH_JHUGen_RAWSIM_294_1_1Ln.root = 249
	WH_JHUGen_RAWSIM_295_1_bBf.root = 249
	WH_JHUGen_RAWSIM_296_1_jf8.root = 249
	WH_JHUGen_RAWSIM_297_1_NTV.root = 249
	WH_JHUGen_RAWSIM_298_1_csy.root = 249
	WH_JHUGen_RAWSIM_299_1_g3K.root = 249
	WH_JHUGen_RAWSIM_29_1_PZ4.root = 249
	WH_JHUGen_RAWSIM_2_1_hLd.root = 249
	WH_JHUGen_RAWSIM_300_1_S7i.root = 249
	WH_JHUGen_RAWSIM_301_1_e5e.root = 249
	WH_JHUGen_RAWSIM_302_1_QO9.root = 249
	WH_JHUGen_RAWSIM_303_1_m5t.root = 249
	WH_JHUGen_RAWSIM_304_1_7Pa.root = 249
	WH_JHUGen_RAWSIM_305_1_q4t.root = 249
	WH_JHUGen_RAWSIM_306_1_06f.root = 249
	WH_JHUGen_RAWSIM_307_1_8E2.root = 249
	WH_JHUGen_RAWSIM_308_1_WLx.root = 249
	WH_JHUGen_RAWSIM_309_1_Tlw.root = 249
	WH_JHUGen_RAWSIM_30_1_iGm.root = 249
	WH_JHUGen_RAWSIM_310_1_5bk.root = 249
	WH_JHUGen_RAWSIM_311_1_mOB.root = 249
	WH_JHUGen_RAWSIM_312_1_cRK.root = 249
	WH_JHUGen_RAWSIM_313_1_Yuf.root = 249
	WH_JHUGen_RAWSIM_314_1_H0h.root = 249
	WH_JHUGen_RAWSIM_315_1_TYN.root = 249
	WH_JHUGen_RAWSIM_316_1_p74.root = 249
	WH_JHUGen_RAWSIM_317_1_M6c.root = 249
	WH_JHUGen_RAWSIM_318_1_f1t.root = 249
	WH_JHUGen_RAWSIM_319_1_8Sm.root = 249
	WH_JHUGen_RAWSIM_31_1_nZP.root = 249
	WH_JHUGen_RAWSIM_320_1_CbY.root = 249
	WH_JHUGen_RAWSIM_321_1_DDI.root = 249
	WH_JHUGen_RAWSIM_322_1_0Hz.root = 249
	WH_JHUGen_RAWSIM_323_1_ptK.root = 249
	WH_JHUGen_RAWSIM_324_1_R5R.root = 249
	WH_JHUGen_RAWSIM_325_1_iXH.root = 249
	WH_JHUGen_RAWSIM_326_1_epZ.root = 249
	WH_JHUGen_RAWSIM_327_1_NMx.root = 249
	WH_JHUGen_RAWSIM_328_1_p1T.root = 249
	WH_JHUGen_RAWSIM_329_1_WHU.root = 249
	WH_JHUGen_RAWSIM_32_1_yXt.root = 249
	WH_JHUGen_RAWSIM_330_1_obx.root = 249
	WH_JHUGen_RAWSIM_331_1_rR6.root = 249
	WH_JHUGen_RAWSIM_332_1_85C.root = 249
	WH_JHUGen_RAWSIM_333_1_Q4H.root = 249
	WH_JHUGen_RAWSIM_334_1_5Sg.root = 249
	WH_JHUGen_RAWSIM_335_1_Px0.root = 249
	WH_JHUGen_RAWSIM_336_1_ZRx.root = 249
	WH_JHUGen_RAWSIM_337_1_weo.root = 249
	WH_JHUGen_RAWSIM_338_1_TJn.root = 249
	WH_JHUGen_RAWSIM_339_1_u3x.root = 249
	WH_JHUGen_RAWSIM_33_1_iFh.root = 249
	WH_JHUGen_RAWSIM_340_1_OA3.root = 249
	WH_JHUGen_RAWSIM_341_1_X7A.root = 249
	WH_JHUGen_RAWSIM_342_1_Z0Z.root = 249
	WH_JHUGen_RAWSIM_343_1_Wuz.root = 249
	WH_JHUGen_RAWSIM_344_1_qoH.root = 249
	WH_JHUGen_RAWSIM_345_1_m8N.root = 249
	WH_JHUGen_RAWSIM_346_1_Gpd.root = 249
	WH_JHUGen_RAWSIM_347_1_Nzt.root = 249
	WH_JHUGen_RAWSIM_348_1_UCQ.root = 249
	WH_JHUGen_RAWSIM_349_1_5gp.root = 249
	WH_JHUGen_RAWSIM_34_1_rR3.root = 249
	WH_JHUGen_RAWSIM_350_1_hvQ.root = 249
	WH_JHUGen_RAWSIM_351_1_7KZ.root = 249
	WH_JHUGen_RAWSIM_352_1_vOY.root = 249
	WH_JHUGen_RAWSIM_353_1_xNi.root = 249
	WH_JHUGen_RAWSIM_354_1_ila.root = 249
	WH_JHUGen_RAWSIM_355_1_R6o.root = 249
	WH_JHUGen_RAWSIM_356_1_XPQ.root = 249
	WH_JHUGen_RAWSIM_357_1_jMs.root = 249
	WH_JHUGen_RAWSIM_358_1_fRV.root = 249
	WH_JHUGen_RAWSIM_359_1_0YH.root = 249
	WH_JHUGen_RAWSIM_35_1_cOZ.root = 249
	WH_JHUGen_RAWSIM_360_1_7PY.root = 249
	WH_JHUGen_RAWSIM_361_1_B1P.root = 249
	WH_JHUGen_RAWSIM_362_1_nYY.root = 249
	WH_JHUGen_RAWSIM_363_1_gyJ.root = 249
	WH_JHUGen_RAWSIM_364_1_OD8.root = 249
	WH_JHUGen_RAWSIM_365_1_Fgt.root = 249
	WH_JHUGen_RAWSIM_366_1_hp3.root = 249
	WH_JHUGen_RAWSIM_367_1_Nz7.root = 249
	WH_JHUGen_RAWSIM_368_1_Awn.root = 249
	WH_JHUGen_RAWSIM_36_1_VuF.root = 249
	WH_JHUGen_RAWSIM_370_1_vXA.root = 249
	WH_JHUGen_RAWSIM_371_1_xvX.root = 249
	WH_JHUGen_RAWSIM_372_1_lRl.root = 249
	WH_JHUGen_RAWSIM_373_1_JCQ.root = 249
	WH_JHUGen_RAWSIM_374_1_1Xg.root = 249
	WH_JHUGen_RAWSIM_375_1_BiP.root = 249
	WH_JHUGen_RAWSIM_376_1_RIk.root = 249
	WH_JHUGen_RAWSIM_377_1_7aa.root = 249
	WH_JHUGen_RAWSIM_378_1_2Hx.root = 249
	WH_JHUGen_RAWSIM_379_1_pgy.root = 249
	WH_JHUGen_RAWSIM_37_1_QYQ.root = 249
	WH_JHUGen_RAWSIM_380_1_2bi.root = 249
	WH_JHUGen_RAWSIM_381_1_1YA.root = 249
	WH_JHUGen_RAWSIM_382_1_jvD.root = 249
	WH_JHUGen_RAWSIM_383_1_zDf.root = 249
	WH_JHUGen_RAWSIM_384_1_rDo.root = 249
	WH_JHUGen_RAWSIM_385_1_0to.root = 249
	WH_JHUGen_RAWSIM_386_1_ZK3.root = 249
	WH_JHUGen_RAWSIM_387_1_4Sv.root = 249
	WH_JHUGen_RAWSIM_388_1_qU2.root = 249
	WH_JHUGen_RAWSIM_389_1_F6Q.root = 249
	WH_JHUGen_RAWSIM_38_1_es2.root = 249
	WH_JHUGen_RAWSIM_390_1_rq8.root = 249
	WH_JHUGen_RAWSIM_391_1_K9o.root = 249
	WH_JHUGen_RAWSIM_392_1_NIj.root = 249
	WH_JHUGen_RAWSIM_393_1_ihZ.root = 249
	WH_JHUGen_RAWSIM_394_1_nKn.root = 249
	WH_JHUGen_RAWSIM_395_1_rx4.root = 249
	WH_JHUGen_RAWSIM_396_1_qEf.root = 249
	WH_JHUGen_RAWSIM_397_1_IUV.root = 249
	WH_JHUGen_RAWSIM_398_1_BFC.root = 249
	WH_JHUGen_RAWSIM_399_1_BoT.root = 249
	WH_JHUGen_RAWSIM_39_1_CH0.root = 249
	WH_JHUGen_RAWSIM_3_1_yqE.root = 249
	WH_JHUGen_RAWSIM_400_1_6w4.root = 249
	WH_JHUGen_RAWSIM_401_1_gc0.root = 249
	WH_JHUGen_RAWSIM_402_1_IYk.root = 137
	WH_JHUGen_RAWSIM_40_1_NoH.root = 249
	WH_JHUGen_RAWSIM_41_1_QUQ.root = 249
	WH_JHUGen_RAWSIM_42_1_EH2.root = 249
	WH_JHUGen_RAWSIM_43_1_Cpl.root = 249
	WH_JHUGen_RAWSIM_44_1_aAf.root = 249
	WH_JHUGen_RAWSIM_45_1_ukg.root = 249
	WH_JHUGen_RAWSIM_46_1_XWk.root = 249
	WH_JHUGen_RAWSIM_47_1_XrO.root = 249
	WH_JHUGen_RAWSIM_48_1_17t.root = 249
	WH_JHUGen_RAWSIM_49_1_jHu.root = 249
	WH_JHUGen_RAWSIM_4_1_5Au.root = 249
	WH_JHUGen_RAWSIM_50_1_yBQ.root = 249
	WH_JHUGen_RAWSIM_51_1_t1s.root = 249
	WH_JHUGen_RAWSIM_52_1_AFj.root = 249
	WH_JHUGen_RAWSIM_53_1_tJ1.root = 249
	WH_JHUGen_RAWSIM_54_1_nUx.root = 249
	WH_JHUGen_RAWSIM_55_1_PVj.root = 249
	WH_JHUGen_RAWSIM_56_1_lbk.root = 249
	WH_JHUGen_RAWSIM_57_1_RSW.root = 249
	WH_JHUGen_RAWSIM_58_1_qxm.root = 249
	WH_JHUGen_RAWSIM_59_1_yt8.root = 249
	WH_JHUGen_RAWSIM_5_1_2I7.root = 249
	WH_JHUGen_RAWSIM_60_1_IV4.root = 249
	WH_JHUGen_RAWSIM_61_1_ePl.root = 249
	WH_JHUGen_RAWSIM_62_1_eo9.root = 249
	WH_JHUGen_RAWSIM_63_1_ja0.root = 249
	WH_JHUGen_RAWSIM_64_1_hJ0.root = 249
	WH_JHUGen_RAWSIM_65_1_Blv.root = 249
	WH_JHUGen_RAWSIM_66_1_qZh.root = 249
	WH_JHUGen_RAWSIM_67_1_HN7.root = 249
	WH_JHUGen_RAWSIM_68_1_4dd.root = 249
	WH_JHUGen_RAWSIM_69_1_0Nb.root = 249
	WH_JHUGen_RAWSIM_6_1_ZKQ.root = 249
	WH_JHUGen_RAWSIM_70_1_V0f.root = 249
	WH_JHUGen_RAWSIM_71_1_egc.root = 249
	WH_JHUGen_RAWSIM_72_1_aRf.root = 249
	WH_JHUGen_RAWSIM_73_1_3ZH.root = 249
	WH_JHUGen_RAWSIM_74_1_LAy.root = 249
	WH_JHUGen_RAWSIM_75_1_gVW.root = 249
	WH_JHUGen_RAWSIM_76_1_ZLO.root = 249
	WH_JHUGen_RAWSIM_77_1_QDQ.root = 249
	WH_JHUGen_RAWSIM_78_1_AIb.root = 249
	WH_JHUGen_RAWSIM_79_1_ZE6.root = 249
	WH_JHUGen_RAWSIM_7_1_avP.root = 249
	WH_JHUGen_RAWSIM_80_1_FRt.root = 249
	WH_JHUGen_RAWSIM_81_1_I9G.root = 249
	WH_JHUGen_RAWSIM_82_1_qqQ.root = 249
	WH_JHUGen_RAWSIM_83_1_rQC.root = 249
	WH_JHUGen_RAWSIM_84_1_ALN.root = 249
	WH_JHUGen_RAWSIM_85_1_J6t.root = 249
	WH_JHUGen_RAWSIM_86_1_qCS.root = 249
	WH_JHUGen_RAWSIM_87_1_4qN.root = 249
	WH_JHUGen_RAWSIM_88_1_j06.root = 249
	WH_JHUGen_RAWSIM_89_1_2nd.root = 249
	WH_JHUGen_RAWSIM_8_1_l4q.root = 249
	WH_JHUGen_RAWSIM_90_1_5Uc.root = 249
	WH_JHUGen_RAWSIM_91_1_NsI.root = 249
	WH_JHUGen_RAWSIM_92_1_hTk.root = 249
	WH_JHUGen_RAWSIM_93_1_kcC.root = 249
	WH_JHUGen_RAWSIM_94_1_mjH.root = 249
	WH_JHUGen_RAWSIM_95_1_jkz.root = 249
	WH_JHUGen_RAWSIM_96_1_m35.root = 249
	WH_JHUGen_RAWSIM_97_1_6YN.root = 249
	WH_JHUGen_RAWSIM_98_1_AYX.root = 249
	WH_JHUGen_RAWSIM_99_1_lWI.root = 249
	WH_JHUGen_RAWSIM_9_1_MG0.root = 249

	>>> cfg = {'lumi filter': '1:MIN-1:20', 'lumi keep': 'RunLumi', 'location format': 'both'}
	>>> get('DBS3Provider', '/ZeeHbb_PHG/zixu-ZeeHbb_PHG-RAW-06e6bebb6525c1c46ccfcc56d82513c0/USER @ phys03', cfg)
	Runs/lumi section filter enabled!
	[/ZeeHbb_PHG/zixu-ZeeHbb_PHG-RAW-06e6bebb6525c1c46ccfcc56d82513c0/USER#cae48e0a-eba4-43f4-85ff-dda11b78dc29]
	nickname = ZeeHbb_PHG_zixu-ZeeHbb_PHG-RAW-06e6bebb6525c1c46ccfcc56d82513c0_USER
	events = 4233
	se list = T3_US_FNALLPC/cmseos.fnal.gov
	prefix = /store/user/lpcmbja/zixu/ZeeHbb_PHG/ZeeHbb_PHG-RAW/06e6bebb6525c1c46ccfcc56d82513c0
	metadata = ["Lumi", "Runs"]
	WH_JHUGen_RAWSIM_320_1_CbY.root = 249 [[1, 426], [1, 1]]
	WH_JHUGen_RAWSIM_321_1_DDI.root = 249 [[1, 2], [1, 1]]
	WH_JHUGen_RAWSIM_322_1_0Hz.root = 249 [[2, 3], [1, 1]]
	WH_JHUGen_RAWSIM_323_1_ptK.root = 249 [[5, 3, 4], [1, 1, 1]]
	WH_JHUGen_RAWSIM_324_1_R5R.root = 249 [[5, 6], [1, 1]]
	WH_JHUGen_RAWSIM_325_1_iXH.root = 249 [[7, 6], [1, 1]]
	WH_JHUGen_RAWSIM_326_1_epZ.root = 249 [[8, 7], [1, 1]]
	WH_JHUGen_RAWSIM_327_1_NMx.root = 249 [[10, 8, 9], [1, 1, 1]]
	WH_JHUGen_RAWSIM_328_1_p1T.root = 249 [[11, 10], [1, 1]]
	WH_JHUGen_RAWSIM_329_1_WHU.root = 249 [[12, 11], [1, 1]]
	WH_JHUGen_RAWSIM_330_1_obx.root = 249 [[13, 12], [1, 1]]
	WH_JHUGen_RAWSIM_331_1_rR6.root = 249 [[15, 13, 14], [1, 1, 1]]
	WH_JHUGen_RAWSIM_332_1_85C.root = 249 [[16, 15], [1, 1]]
	WH_JHUGen_RAWSIM_333_1_Q4H.root = 249 [[17, 16], [1, 1]]
	WH_JHUGen_RAWSIM_334_1_5Sg.root = 249 [[18, 17], [1, 1]]
	WH_JHUGen_RAWSIM_335_1_Px0.root = 249 [[18, 19, 20], [1, 1, 1]]
	WH_JHUGen_RAWSIM_336_1_ZRx.root = 249 [[20, 21], [1, 1]]

	>>> get('DBS3Provider', '/ZeeHbb_PHG/zixu-ZeeHbb_PHG-RAW-06e6bebb6525c1c46ccfcc56d82513c0/USER @ prod/phys03', cfg)
	Runs/lumi section filter enabled!
	[/ZeeHbb_PHG/zixu-ZeeHbb_PHG-RAW-06e6bebb6525c1c46ccfcc56d82513c0/USER#cae48e0a-eba4-43f4-85ff-dda11b78dc29]
	nickname = ZeeHbb_PHG_zixu-ZeeHbb_PHG-RAW-06e6bebb6525c1c46ccfcc56d82513c0_USER
	events = 4233
	se list = T3_US_FNALLPC/cmseos.fnal.gov
	prefix = /store/user/lpcmbja/zixu/ZeeHbb_PHG/ZeeHbb_PHG-RAW/06e6bebb6525c1c46ccfcc56d82513c0
	metadata = ["Lumi", "Runs"]
	WH_JHUGen_RAWSIM_320_1_CbY.root = 249 [[1, 426], [1, 1]]
	WH_JHUGen_RAWSIM_321_1_DDI.root = 249 [[1, 2], [1, 1]]
	WH_JHUGen_RAWSIM_322_1_0Hz.root = 249 [[2, 3], [1, 1]]
	WH_JHUGen_RAWSIM_323_1_ptK.root = 249 [[5, 3, 4], [1, 1, 1]]
	WH_JHUGen_RAWSIM_324_1_R5R.root = 249 [[5, 6], [1, 1]]
	WH_JHUGen_RAWSIM_325_1_iXH.root = 249 [[7, 6], [1, 1]]
	WH_JHUGen_RAWSIM_326_1_epZ.root = 249 [[8, 7], [1, 1]]
	WH_JHUGen_RAWSIM_327_1_NMx.root = 249 [[10, 8, 9], [1, 1, 1]]
	WH_JHUGen_RAWSIM_328_1_p1T.root = 249 [[11, 10], [1, 1]]
	WH_JHUGen_RAWSIM_329_1_WHU.root = 249 [[12, 11], [1, 1]]
	WH_JHUGen_RAWSIM_330_1_obx.root = 249 [[13, 12], [1, 1]]
	WH_JHUGen_RAWSIM_331_1_rR6.root = 249 [[15, 13, 14], [1, 1, 1]]
	WH_JHUGen_RAWSIM_332_1_85C.root = 249 [[16, 15], [1, 1]]
	WH_JHUGen_RAWSIM_333_1_Q4H.root = 249 [[17, 16], [1, 1]]
	WH_JHUGen_RAWSIM_334_1_5Sg.root = 249 [[18, 17], [1, 1]]
	WH_JHUGen_RAWSIM_335_1_Px0.root = 249 [[18, 19, 20], [1, 1, 1]]
	WH_JHUGen_RAWSIM_336_1_ZRx.root = 249 [[20, 21], [1, 1]]

	>>> cfg = {'lumi filter': '1:MIN-1:20', 'lumi keep': 'RunLumi', 'location format': 'both', 'dbs instance': 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader'}
	>>> get('DBS3Provider', '/ZeeHbb_PHG/zixu-ZeeHbb_PHG-RAW-06e6bebb6525c1c46ccfcc56d82513c0/USER', cfg)
	Runs/lumi section filter enabled!
	[/ZeeHbb_PHG/zixu-ZeeHbb_PHG-RAW-06e6bebb6525c1c46ccfcc56d82513c0/USER#cae48e0a-eba4-43f4-85ff-dda11b78dc29]
	nickname = ZeeHbb_PHG_zixu-ZeeHbb_PHG-RAW-06e6bebb6525c1c46ccfcc56d82513c0_USER
	events = 4233
	se list = T3_US_FNALLPC/cmseos.fnal.gov
	prefix = /store/user/lpcmbja/zixu/ZeeHbb_PHG/ZeeHbb_PHG-RAW/06e6bebb6525c1c46ccfcc56d82513c0
	metadata = ["Lumi", "Runs"]
	WH_JHUGen_RAWSIM_320_1_CbY.root = 249 [[1, 426], [1, 1]]
	WH_JHUGen_RAWSIM_321_1_DDI.root = 249 [[1, 2], [1, 1]]
	WH_JHUGen_RAWSIM_322_1_0Hz.root = 249 [[2, 3], [1, 1]]
	WH_JHUGen_RAWSIM_323_1_ptK.root = 249 [[5, 3, 4], [1, 1, 1]]
	WH_JHUGen_RAWSIM_324_1_R5R.root = 249 [[5, 6], [1, 1]]
	WH_JHUGen_RAWSIM_325_1_iXH.root = 249 [[7, 6], [1, 1]]
	WH_JHUGen_RAWSIM_326_1_epZ.root = 249 [[8, 7], [1, 1]]
	WH_JHUGen_RAWSIM_327_1_NMx.root = 249 [[10, 8, 9], [1, 1, 1]]
	WH_JHUGen_RAWSIM_328_1_p1T.root = 249 [[11, 10], [1, 1]]
	WH_JHUGen_RAWSIM_329_1_WHU.root = 249 [[12, 11], [1, 1]]
	WH_JHUGen_RAWSIM_330_1_obx.root = 249 [[13, 12], [1, 1]]
	WH_JHUGen_RAWSIM_331_1_rR6.root = 249 [[15, 13, 14], [1, 1, 1]]
	WH_JHUGen_RAWSIM_332_1_85C.root = 249 [[16, 15], [1, 1]]
	WH_JHUGen_RAWSIM_333_1_Q4H.root = 249 [[17, 16], [1, 1]]
	WH_JHUGen_RAWSIM_334_1_5Sg.root = 249 [[18, 17], [1, 1]]
	WH_JHUGen_RAWSIM_335_1_Px0.root = 249 [[18, 19, 20], [1, 1, 1]]
	WH_JHUGen_RAWSIM_336_1_ZRx.root = 249 [[20, 21], [1, 1]]
	"""

class Test_Incomplete:
	"""
	>>> cfg = {'location format': 'both', 'phedex sites': 'T2_*'}
	>>> get('DBS3Provider', '/SingleMuon/Run2015E-PromptReco-v1/AOD#a7c3638c-8e3e-11e5-9687-001e67abf228', cfg)
	[/SingleMuon/Run2015E-PromptReco-v1/AOD#a7c3638c-8e3e-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_AOD
	events = 267049
	se list = T2_FR_GRIF_IRFU/node12.datagrid.cea.fr
	prefix = /store/data/Run2015E/SingleMuon/AOD/PromptReco-v1/000/261
	397/00000/A0C59AAD-3B8E-E511-8DEA-02163E0145B4.root = 56118
	397/00000/E44E2AAB-3B8E-E511-8BB2-02163E0141DC.root = 95082
	398/00000/8AAB12A5-3D8E-E511-83FF-02163E011EA8.root = 16788
	399/00000/9CFF9D75-3F8E-E511-AE38-02163E014244.root = 78409
	401/00000/E803ABDA-408E-E511-BA79-02163E013522.root = 13073
	402/00000/32DC2434-418E-E511-AC71-02163E0142D8.root = 7576
	422/00000/3424AE0E-438E-E511-B5C0-02163E014491.root = 3

	>>> cfg = {'location format': 'both', 'phedex sites': 'T2_US_*'}
	>>> get('DBS3Provider', '/SingleMuon/Run2015E-PromptReco-v1/AOD#a7c3638c-8e3e-11e5-9687-001e67abf228', cfg)
	Dataset block '/SingleMuon/Run2015E-PromptReco-v1/AOD#a7c3638c-8e3e-11e5-9687-001e67abf228' is not completely available at the selected locations!
	Available locations: T1_US_FNAL_Disk/cmsdcadisk01.fnal.gov, (T2_US_Purdue/srm.rcac.purdue.edu), XT1_US_FNAL_Old_Disk/cmssrmdisk.fnal.gov, T1_US_FNAL_MSS/cmssrm.fnal.gov, T1_US_FNAL_Buffer/cmssrm.fnal.gov, T2_FR_GRIF_IRFU/node12.datagrid.cea.fr
	Block /SingleMuon/Run2015E-PromptReco-v1/AOD#a7c3638c-8e3e-11e5-9687-001e67abf228 is not available at any site!
	[/SingleMuon/Run2015E-PromptReco-v1/AOD#a7c3638c-8e3e-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_AOD
	events = 267049
	se list =
	prefix = /store/data/Run2015E/SingleMuon/AOD/PromptReco-v1/000/261
	397/00000/A0C59AAD-3B8E-E511-8DEA-02163E0145B4.root = 56118
	397/00000/E44E2AAB-3B8E-E511-8BB2-02163E0141DC.root = 95082
	398/00000/8AAB12A5-3D8E-E511-83FF-02163E011EA8.root = 16788
	399/00000/9CFF9D75-3F8E-E511-AE38-02163E014244.root = 78409
	401/00000/E803ABDA-408E-E511-BA79-02163E013522.root = 13073
	402/00000/32DC2434-418E-E511-AC71-02163E0142D8.root = 7576
	422/00000/3424AE0E-438E-E511-B5C0-02163E014491.root = 3

	>>> cfg = {'location format': 'both', 'phedex sites': 'T2_US_*', 'only complete sites': False}
	>>> get('DBS3Provider', '/SingleMuon/Run2015E-PromptReco-v1/AOD#a7c3638c-8e3e-11e5-9687-001e67abf228', cfg)
	[/SingleMuon/Run2015E-PromptReco-v1/AOD#a7c3638c-8e3e-11e5-9687-001e67abf228]
	nickname = SingleMuon_Run2015E-PromptReco-v1_AOD
	events = 267049
	se list = T2_US_Purdue/srm.rcac.purdue.edu
	prefix = /store/data/Run2015E/SingleMuon/AOD/PromptReco-v1/000/261
	397/00000/A0C59AAD-3B8E-E511-8DEA-02163E0145B4.root = 56118
	397/00000/E44E2AAB-3B8E-E511-8BB2-02163E0141DC.root = 95082
	398/00000/8AAB12A5-3D8E-E511-83FF-02163E011EA8.root = 16788
	399/00000/9CFF9D75-3F8E-E511-AE38-02163E014244.root = 78409
	401/00000/E803ABDA-408E-E511-BA79-02163E013522.root = 13073
	402/00000/32DC2434-418E-E511-AC71-02163E0142D8.root = 7576
	422/00000/3424AE0E-438E-E511-B5C0-02163E014491.root = 3
	"""

run_test()
