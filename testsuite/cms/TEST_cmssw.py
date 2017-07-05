#!/usr/bin/env python
__import__('sys').path.append(__import__('os').path.join(__import__('os').path.dirname(__file__), '..'))
__import__('testfwk').setup(__file__)
# - prolog marker
from testfwk import create_config, run_test, testfwk_remove_files, try_catch
from grid_control_cms.task_cmssw_advanced import str_lumi_nice
from hpfwk import Plugin


class Test_Tools:
	"""
	>>> str_lumi_nice([([1, 1], [2, None]), ([5, None], [7, 3]), ([3, 1], [None, 2])])
	'1:1-2:MAX, 5:MIN-7:3, 3:1-9999999:2'
	>>> str_lumi_nice([([1, 1], [2, 2]), ([3, 1], [5, 2]), ([5, 2], [7, 3]), ([15, 2], [17, 3]), ([25, 2], [27, 3])])
	'1:1-2:2 ... 25:2-27:3 (5 entries)'
	"""


def create_task(task, options=None):
	config_dict = {'jobs': {'wall time': '1:00'}}
	config_dict['section'] = options or {}
	config = create_config(config_dict=config_dict)
	return Plugin.create_instance(task, config, 'test')

class Test_CMSSW:
	"""
	>>> try_catch(lambda: create_task('ScramTask', {'project area': '.'}), 'ConfigError', 'cannot be parsed')
	Current task ID: GC0000000000
	Task started on: 0000-00-00
	Project area found in: <testsuite dir>/cms
	caught
	>>> try_catch(lambda: create_task('ScramTask', {'scram project': 'CMSSW'}), 'ConfigError', 'needs exactly 2 arguments: <PROJECT> <VERSION>')
	Current task ID: GC0000000000
	Task started on: 0000-00-00
	caught
	>>> try_catch(lambda: create_task('ScramTask', {'scram project': 'CMSSW CMSSW_9_9_9', 'project area': '.'}), 'ConfigError', 'Cannot specify both')
	Current task ID: GC0000000000
	Task started on: 0000-00-00
	caught
	>>> try_catch(lambda: create_task('ScramTask', {'project area': 'CMSSW_X_X_X'}), 'ConfigError', 'Installed program in project area not recognized')
	Current task ID: GC0000000000
	Task started on: 0000-00-00
	Project area found in: <testsuite dir>/cms/CMSSW_X_X_X
	caught
	>>> try_catch(lambda: create_task('CMSSW', {'scram project': 'ORCA ORCA_9_9_9', 'scram arch': 'slc7_amd64_777'}), 'ConfigError', 'Project area contains no CMSSW project')
	Current task ID: GC0000000000
	Task started on: 0000-00-00
	caught
	>>> try_catch(lambda: create_task('CMSSW', {'scram project': 'CMSSW CMSSW_9_9_9', 'scram arch': 'slc7_amd64_777', 'executable': '.'}), 'ConfigError', 'Prefix executable and argument options with either prolog or epilog')
	Current task ID: GC0000000000
	Task started on: 0000-00-00
	caught
	>>> try_catch(lambda: create_task('CMSSW', {'scram project': 'CMSSW CMSSW_9_9_9', 'scram arch': 'slc7_amd64_777', 'config file': 'xyz.py'}), 'ConfigError', 'Could not find')
	Current task ID: GC0000000000
	Task started on: 0000-00-00
	caught
	"""

run_test(cleanup_fun=lambda: testfwk_remove_files(['work/params.dat.gz', 'work/params.map.gz']))
