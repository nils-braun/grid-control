grid-control options
====================

global options
--------------

  * ``config id`` = <text> (default: <config file name w/o extension> or 'unnamed')
    Identifier for the current configuration
  * ``delete`` = <job selector> (default: '')
    The unfinished jobs selected by this expression are cancelled.
  * ``package paths`` = <list of paths> (default: '')
    Specify paths to additional grid-control packages with user defined plugins that are outside of the base package directory
  * ``plugin paths`` = <list of paths> (default: '<current directory>')
    Specifies paths that are used to search for plugins
  * ``reset`` = <job selector> (default: '')
    The jobs selected by this expression are reset to the INIT state
  * ``variable markers`` = <list of values> (default: '@ __')
    Specifies how variables are marked
  * ``workdir`` = <path> (default: <workdir base>/work.<config file name>)
    Location of the grid-control work directory. Usually based on the name of the config file
  * ``workdir base`` = <path> (default: <config file path>)
    Directory where the default workdir is created
  * ``workdir create`` = <boolean> (default: True)
    Skip interactive question about workdir creation
  * ``workdir space`` = <integer> (default: 10)
    Lower space limit in the work directory. Monitoring can be deactived with 0
  * ``workflow`` = <plugin[:name]> (default: 'Workflow:global')
    Specifies the workflow that is being run

Workflow options
----------------

  * ``task / module`` = <plugin[:name]>
    Select the task module to run
  * ``action`` = <list of values> (default: 'check retrieve submit')
    Specify the actions and the order in which grid-control should perform them
  * ``backend`` = <list of plugin[:name] ...> (default: 'grid')
    Select the backend to use for job submission
  * backend manager = <plugin> (Default: 'MultiWMS')
    Specifiy compositor class to merge the different plugins given in ``backend``
  * ``continuous`` = <boolean> (default: False)
    Enable continuous running mode
  * ``duration`` = <duration hh[:mm[:ss]]> (default: <continuous mode on: infinite (-1), off: exit immediately (0)>)
    Maximal duration of the job processing pass. The default depends on the value of the 'continuous' option.
  * ``gui`` = <plugin> (default: 'SimpleConsole')
    Specify GUI plugin to handle the user interaction
  * ``job manager`` = <plugin[:name]> (default: 'SimpleJobManager')
    Specify the job management plugin to handle the job cycle
  * ``monitor`` = <list of plugin[:name] ...> (default: 'scripts')
    Specify monitor plugins to track the task / job progress
  * monitor manager = <plugin> (Default: 'MultiMonitor')
    Specifiy compositor class to merge the different plugins given in ``monitor``
  * ``submission`` = <boolean> (default: True)
    Toggle to control the submission of jobs
  * ``submission time requirement`` = <duration hh[:mm[:ss]]> (default: <wall time>)
    Toggle to control the submission of jobs

SimpleJobManager options
------------------------

  * ``abort report`` = <text> (default: 'LocationReport')
    Specify report plugin to display in case of job cancellations
  * ``chunks check`` = <integer> (default: 100)
    Specify maximal number of jobs to check in each job cycle
  * ``chunks enabled`` = <boolean> (default: True)
    Toggle to control if only a chunk of jobs are processed each job cycle
  * ``chunks retrieve`` = <integer> (default: 100)
    Specify maximal number of jobs to retrieve in each job cycle
  * ``chunks submit`` = <integer> (default: 100)
    Specify maximal number of jobs to submit in each job cycle
  * ``defect tries / kick offender`` = <integer> (default: 10)
    Threshold for dropping jobs causing status retrieval errors
  * ``in flight`` = <integer> (default: no limit (-1))
    Maximum number of concurrently submitted jobs
  * ``in queue`` = <integer> (default: no limit (-1))
    Maximum number of queued jobs
  * ``job database`` = <plugin> (default: 'TextFileJobDB')
    Specify job database plugin that is used to store job information
  * ``jobs`` = <integer> (default: no limit (-1))
    Maximum number of jobs (truncated to task maximum)
  * ``max retry`` = <integer> (default: no limit (-1))
    Number of resubmission attempts for failed jobs
  * ``output processor`` = <plugin> (default: 'SandboxProcessor')
    Specify plugin that processes the output sandbox of successful jobs
  * ``queue timeout`` = <duration hh[:mm[:ss]]> (default: disabled (-1))
    Resubmit jobs after staying some time in initial state
  * ``selected`` = <text> (default: '')
    Apply general job selector
  * ``shuffle`` = <boolean> (default: False)
    Submit jobs in random order
  * ``unknown timeout`` = <duration hh[:mm[:ss]]> (default: disabled (-1))
    Cancel jobs without status information after staying in this state for the specified time
  * ``verify chunks`` = <list of values> (default: '-1')
    List of job chunk sizes that are enabled after passing the configured verification thresholds
  * ``verify threshold / verify reqs`` = <list of values> (default: '0.5')
    List of job verification thresholds that enable the configured job chunk sizes

backend options
---------------

  * ``<prefix> chunk interval`` = <integer> (default: <depends on the process>)
    Specify the interval between (submit, check, ...) chunks
  * ``<prefix> chunk size`` = <integer> (default: <depends on the process>)
    Specify the size of (submit, check, ...) chunks
  * ``access token / proxy`` = <list of plugin[:name] ...> (default: 'TrivialAccessToken')
    Specify access token plugins that are necessary for job submission
  * access token manager = <plugin> (Default: 'MultiAccessToken')
    Specifiy compositor class to merge the different plugins given in ``access token``
  * ``cancel timeout`` = <duration hh[:mm[:ss]]> (default: 00:01:00)
    Specify timeout of the process that is used to cancel jobs
  * ``sb input manager`` = <plugin[:name]> (default: 'LocalSBStorageManager')
    Specify transfer manager plugin to transfer sandbox input files
  * ``se input manager`` = <plugin[:name]> (default: 'SEStorageManager')
    Specify transfer manager plugin to transfer SE input files
  * ``se output manager`` = <plugin[:name]> (default: 'SEStorageManager')
    Specify transfer manager plugin to transfer SE output files

CMSSW options
-------------

  * ``wall time`` = <duration hh[:mm[:ss]]>
    Requested wall time also used for checking the proxy lifetime
  * ``area files`` = <list of values> (default: '-.* -config bin lib python module */data *.xml *.sql *.db *.cf[if] *.py -*/.git -*/.svn -*/CVS -*/work.*')
    List of files that should be taken from the CMSSW project area for running the job
  * ``arguments`` = <text> (default: '')
    Arguments that will be passed to the *cmsRun* call
  * ``config file`` = <list of paths> (default: <no default> or '' if prolog / epilog script is given)
    List of config files that will be sequentially processed by *cmsRun* calls
  * ``cpu time`` = <duration hh[:mm[:ss]]> (default: <wall time>)
    Requested cpu time
  * ``cpus`` = <integer> (default: 1)
    Requested number of cpus per node
  * ``depends`` = <list of values> (default: '')
    List of environment setup scripts that the jobs depend on
  * ``events per job`` = <text> (default: '0')
    This sets the variable MAX_EVENTS if no datasets are present
  * ``gzip output`` = <boolean> (default: True)
    Toggle the compression of the job log files for stdout and stderr
  * ``input files`` = <list of paths> (default: '')
    List of files that should be transferred to the landing zone of the job on the worker node. Only for small files - send large files via SE!
  * ``instrumentation`` = <boolean> (default: True)
    Toggle to control the instrumentation of CMSSW config files for running over data / initializing the RNG for MC production
  * ``instrumentation fragment`` = <path> (default: <grid-control cms package>/share/fragmentForCMSSW.py)
    Path to the instrumentation fragment that is appended to the CMSSW config file if instrumentation is enabled
  * ``internal parameter factory`` = <plugin> (default: 'BasicParameterFactory')
    Specify the parameter factory plugin that is used to generate the basic grid-control parameters
  * ``job name generator`` = <plugin> (default: 'DefaultJobName')
    Specify the job name plugin that generates the job name that is given to the backend
  * ``landing zone space left`` = <integer> (default: 1)
    Minimum amount of disk space (in MB) that the job has to leave in the landing zone directory while running
  * ``landing zone space used`` = <integer> (default: 100)
    Maximum amount of disk space (in MB) that the job is allowed to use in the landing zone directory while running
  * ``memory`` = <integer> (default: unspecified (-1))
    Requested memory in MB. Some batch farms have very low default memory limits in which case it is necessary to specify this option!
  * ``node timeout`` = <duration hh[:mm[:ss]]> (default: disabled (-1))
    Cancel job after some time on worker node
  * ``output files`` = <list of values> (default: '')
    List of files that should be transferred to the job output directory on the submission machine. Only for small files - send large files via SE!
  * ``parameter adapter`` = <plugin> (default: 'TrackedParameterAdapter')
    Specify the parameter adapter plugin that translates parameter point to job number
  * ``project area`` = <path> (default: <depends on ``scram arch`` and ``scram project``>)
    Specify location of the CMSSW project area that should be send with the job. Instead of the CMSSW project area, it is possible to specify ``scram arch`` and ``scram project`` to use a fresh CMSSW project.
  * ``scram arch`` = <text> (default: <depends on ``project area``>)
    Specify scram architecture that should be used by the job (eg. 'slc7_amd64_gcc777'). When using an existing CMSSW project area with ``project area``, this option uses the default value taken from the project area.
  * ``scram arch requirements`` = <boolean> (default: True)
    Toggle the inclusion of the scram architecture in the job requirements
  * ``scram project`` = <list of values> (default: '')
    Specify scram project that should be used by the job (eg. 'CMSSW CMSSW_9_9_9')
  * ``scram project requirements`` = <boolean> (default: False)
    Toggle the inclusion of the scram project name in the job requirements
  * ``scram project version requirements`` = <boolean> (default: False)
    Toggle the inclusion of the scram project version in the job requirements
  * ``scram version`` = <text> (default: 'scramv1')
    Specify scram version that should be used by the job.
  * ``scratch space left`` = <integer> (default: 1)
    Minimum amount of disk space (in MB) that the job has to leave in the scratch directory while running. If the landing zone itself is the scratch space, the scratch thresholds apply
  * ``scratch space used`` = <integer> (default: 5000)
    Maximum amount of disk space (in MB) that the job is allowed to use in the scratch directory while running. If the landing zone itself is the scratch space, the scratch thresholds apply
  * ``se min size`` = <integer> (default: disabled (-1))
    SE output files below this file size (in MB) trigger a job failure
  * ``se project area / se runtime`` = <boolean> (default: True)
    Toggle to specify how the CMSSW project area should be transferred to the worker node
  * ``subst files`` = <list of values> (default: '')
    List of files that will be subjected to variable substituion
  * ``task date`` = <text> (default: current date: YYYY-MM-DD)
    Persistent date when the task was started.
  * ``task id`` = <text> (default: GCxxxxxxxxxxxx)
    Persistent task identifier that is generated at the start of the task
  * ``vo software dir / cmssw dir`` = <text> (default: '')
    This option allows to override of the VO_CMS_SW_DIR environment variable

CMSSW_Advanced options
----------------------

  * ``wall time`` = <duration hh[:mm[:ss]]>
    Requested wall time also used for checking the proxy lifetime
  * ``area files`` = <list of values> (default: '-.* -config bin lib python module */data *.xml *.sql *.db *.cf[if] *.py -*/.git -*/.svn -*/CVS -*/work.*')
    List of files that should be taken from the CMSSW project area for running the job
  * ``arguments`` = <text> (default: '')
    Arguments that will be passed to the *cmsRun* call
  * ``config file`` = <list of paths> (default: <no default> or '' if prolog / epilog script is given)
    List of config files that will be sequentially processed by *cmsRun* calls
  * ``cpu time`` = <duration hh[:mm[:ss]]> (default: <wall time>)
    Requested cpu time
  * ``cpus`` = <integer> (default: 1)
    Requested number of cpus per node
  * ``depends`` = <list of values> (default: '')
    List of environment setup scripts that the jobs depend on
  * ``events per job`` = <text> (default: '0')
    This sets the variable MAX_EVENTS if no datasets are present
  * ``gzip output`` = <boolean> (default: True)
    Toggle the compression of the job log files for stdout and stderr
  * ``input files`` = <list of paths> (default: '')
    List of files that should be transferred to the landing zone of the job on the worker node. Only for small files - send large files via SE!
  * ``instrumentation`` = <boolean> (default: True)
    Toggle to control the instrumentation of CMSSW config files for running over data / initializing the RNG for MC production
  * ``instrumentation fragment`` = <path> (default: <grid-control cms package>/share/fragmentForCMSSW.py)
    Path to the instrumentation fragment that is appended to the CMSSW config file if instrumentation is enabled
  * ``internal parameter factory`` = <plugin> (default: 'BasicParameterFactory')
    Specify the parameter factory plugin that is used to generate the basic grid-control parameters
  * ``job name generator`` = <plugin> (default: 'DefaultJobName')
    Specify the job name plugin that generates the job name that is given to the backend
  * ``landing zone space left`` = <integer> (default: 1)
    Minimum amount of disk space (in MB) that the job has to leave in the landing zone directory while running
  * ``landing zone space used`` = <integer> (default: 100)
    Maximum amount of disk space (in MB) that the job is allowed to use in the landing zone directory while running
  * ``memory`` = <integer> (default: unspecified (-1))
    Requested memory in MB. Some batch farms have very low default memory limits in which case it is necessary to specify this option!
  * ``nickname config`` = <lookup specifier> (default: {})
    Allows to specify a dictionary with list of config files that will be sequentially processed by *cmsRun* calls. The dictionary key is the job dependent dataset nickname
  * ``nickname config matcher`` = <plugin> (Default: 'regex')
    Specifiy matcher plugin that is used to match the lookup expressions
  * ``nickname constants`` = <list of values> (default: '')
    Allows to specify a list of nickname dependent variables. The value of the variables is specified separately in the form of a dictionary. (This option is deprecated, since *all* variables support this functionality now!)
  * ``nickname lumi filter`` = <dictionary> (default: {})
    Allows to specify a dictionary with nickname dependent lumi filter expressions. (This option is deprecated, since the normal option ``lumi filter`` already supports this!)
  * ``node timeout`` = <duration hh[:mm[:ss]]> (default: disabled (-1))
    Cancel job after some time on worker node
  * ``output files`` = <list of values> (default: '')
    List of files that should be transferred to the job output directory on the submission machine. Only for small files - send large files via SE!
  * ``parameter adapter`` = <plugin> (default: 'TrackedParameterAdapter')
    Specify the parameter adapter plugin that translates parameter point to job number
  * ``project area`` = <path> (default: <depends on ``scram arch`` and ``scram project``>)
    Specify location of the CMSSW project area that should be send with the job. Instead of the CMSSW project area, it is possible to specify ``scram arch`` and ``scram project`` to use a fresh CMSSW project.
  * ``scram arch`` = <text> (default: <depends on ``project area``>)
    Specify scram architecture that should be used by the job (eg. 'slc7_amd64_gcc777'). When using an existing CMSSW project area with ``project area``, this option uses the default value taken from the project area.
  * ``scram arch requirements`` = <boolean> (default: True)
    Toggle the inclusion of the scram architecture in the job requirements
  * ``scram project`` = <list of values> (default: '')
    Specify scram project that should be used by the job (eg. 'CMSSW CMSSW_9_9_9')
  * ``scram project requirements`` = <boolean> (default: False)
    Toggle the inclusion of the scram project name in the job requirements
  * ``scram project version requirements`` = <boolean> (default: False)
    Toggle the inclusion of the scram project version in the job requirements
  * ``scram version`` = <text> (default: 'scramv1')
    Specify scram version that should be used by the job.
  * ``scratch space left`` = <integer> (default: 1)
    Minimum amount of disk space (in MB) that the job has to leave in the scratch directory while running. If the landing zone itself is the scratch space, the scratch thresholds apply
  * ``scratch space used`` = <integer> (default: 5000)
    Maximum amount of disk space (in MB) that the job is allowed to use in the scratch directory while running. If the landing zone itself is the scratch space, the scratch thresholds apply
  * ``se min size`` = <integer> (default: disabled (-1))
    SE output files below this file size (in MB) trigger a job failure
  * ``se project area / se runtime`` = <boolean> (default: True)
    Toggle to specify how the CMSSW project area should be transferred to the worker node
  * ``subst files`` = <list of values> (default: '')
    List of files that will be subjected to variable substituion
  * ``task date`` = <text> (default: current date: YYYY-MM-DD)
    Persistent date when the task was started.
  * ``task id`` = <text> (default: GCxxxxxxxxxxxx)
    Persistent task identifier that is generated at the start of the task
  * ``vo software dir / cmssw dir`` = <text> (default: '')
    This option allows to override of the VO_CMS_SW_DIR environment variable

dataset options
---------------

  * ``dataset`` = <list of [<nickname> : [<protocol> :]] <dataset specifier> > (default: '')
    List of datasets to process (including optional nickname and dataset provider information)
  * dataset manager = <plugin> (Default: ':MultiDatasetProvider:')
    Specifiy compositor class to merge the different plugins given in ``dataset``
  * ``dataset default query interval`` = <duration hh[:mm[:ss]]> (default: 00:01:00)
    Specify the default limit for the dataset query interval
  * ``dataset processor`` = <list of plugins> (default: 'NickNameConsistencyProcessor EntriesConsistencyDataProcessor URLDataProcessor URLCountDataProcessor ' 'EntriesCountDataProcessor EmptyDataProcessor UniqueDataProcessor LocationDataProcessor')
    Specify list of plugins that process datasets before the partitioning
  * dataset processor manager = <plugin> (Default: 'MultiDataProcessor')
    Specifiy compositor class to merge the different plugins given in ``dataset processor``
  * ``dataset provider`` = <text> (default: 'ListProvider')
    Specify the name of the default dataset provider
  * ``dataset refresh`` = <duration hh[:mm[:ss]]> (default: disabled (-1))
    Specify the interval to check for changes in the used datasets
  * ``dataset splitter`` = <plugin> (default: 'FileBoundarySplitter')
    Specify the dataset splitter plugin to partition the dataset
  * ``nickname source`` = <plugin> (default: 'SimpleNickNameProducer')
    Specify nickname plugin that determines the nickname for datasets
  * ``partition processor`` = <list of plugins> (default: 'TFCPartitionProcessor LocationPartitionProcessor MetaPartitionProcessor BasicPartitionProcessor')
    Specify list of plugins that process partitions
  * partition processor manager = <plugin> (Default: 'MultiPartitionProcessor')
    Specifiy compositor class to merge the different plugins given in ``partition processor``
  * ``resync jobs`` = <enum: append|preserve|fillgap|reorder> (default: append)
    Specify how resynced jobs should be handled
  * ``resync metadata`` = <list of values> (default: '')
    List of metadata keys that have configuration options to specify how metadata changes are handled by a dataset resync
  * ``resync mode <metadata key>`` = <enum: disable|complete|changed|ignore> (default: complete)
    Specify how changes in the given metadata key affect partitions during resync
  * ``resync mode expand`` = <enum: disable|complete|changed|ignore> (default: changed)
    Sets the resync mode for expanded files
  * ``resync mode new`` = <enum: disable|complete|changed|ignore> (default: complete)
    Sets the resync mode for new files
  * ``resync mode removed`` = <enum: disable|complete|changed|ignore> (default: complete)
    Sets the resync mode for removed files
  * ``resync mode shrink`` = <enum: disable|complete|changed|ignore> (default: changed)
    Sets the resync mode for shrunken files

TaskExecutableWrapper options
-----------------------------

  * ``[<prefix>] arguments`` = <text> (default: '')
    Specify arguments for the executable
  * ``[<prefix>] executable`` = <text> (default: <no default> or '')
    Path to the executable
  * ``[<prefix>] send executable`` = <boolean> (default: True)
    Toggle to control if the specified executable should be send together with the job

interactive options
-------------------

  * ``<option name>`` = <boolean>
    Toggle to switch interactive questions on and off
  * ``delete jobs`` = <boolean> (default: True)
    Toggle interactivity of job deletion requests
  * ``partition resync`` = <boolean> (default: False)
    Toggle interactivity of dataset resyncs
  * ``reset jobs`` = <boolean> (default: True)
    Toggle interactivity of job reset requests

logging options
---------------

  * ``<logger name> file`` = <text>
    Log file used by file logger
  * ``<logger name> <handler> code context / <logger name> code context`` = <integer> (default: 2)
    Number of code context lines in shown exception logs
  * ``<logger name> <handler> detail lower limit / <logger name> detail lower limit`` = <enum: LEVEL 0..50|NOTSET|DEBUG3...DEBUG|INFO3..INFO|DEFAULT|WARNING|ERROR|CRITICAL> (default: DEBUG)
    Logging messages below this log level will use the long form output
  * ``<logger name> <handler> detail upper limit / <logger name> detail upper limit`` = <enum: LEVEL 0..50|NOTSET|DEBUG3...DEBUG|INFO3..INFO|DEFAULT|WARNING|ERROR|CRITICAL> (default: ERROR)
    Logging messages above this log level will use the long form output
  * ``<logger name> <handler> file stack / <logger name> file stack`` = <integer> (default: 1)
    Level of detail for file stack information shown in exception logs
  * ``<logger name> <handler> tree / <logger name> tree`` = <integer> (default: 2)
    Level of detail for exception tree information shown in exception logs
  * ``<logger name> <handler> variables / <logger name> variables`` = <integer> (default: 1)
    Level of detail for variable information shown in exception logs
  * ``<logger name> debug file`` = <list of paths> (default: '"<gc dir>/debug.log" "/tmp/gc.debug.<uid>.<pid>" "~/gc.debug"')
    Logfile used by debug file logger. In case multiple paths are specified, the first usable path will be used.
  * ``<logger name> handler`` = <list of values> (default: '')
    List of log handlers
  * ``<logger name> level`` = <enum: LEVEL 0..50|NOTSET|DEBUG3...DEBUG|INFO3..INFO|DEFAULT|WARNING|ERROR|CRITICAL> (default: <depends on the logger>)
    Logging level of log handlers
  * ``<logger name> propagate`` = <boolean> (default: <depends on the logger>)
    Toggle log propagation
  * ``debug mode`` = <boolean> (default: False)
    Toggle debug mode (detailed exception output on stdout)
  * ``display logger`` = <boolean> (default: False)
    Toggle display of logging structure

parameters options
------------------

  * ``parameters`` = <text> (default: '')
    Specify the parameter expression that defines the parameter space. The syntax depends on the used parameter factory.

GUI options
-----------

  * ``report`` = <list of plugins> (default: 'BasicReport')
    Type of report to display during operations
  * report manager = <plugin> (Default: 'MultiReport')
    Specifiy compositor class to merge the different plugins given in ``report``
  * ``report options`` = <text> (default: '')
    Specify options for the report plugin

Matcher options
---------------

  * ``<prefix> case sensitive`` = <boolean>
    Toggle case sensitivity for the matcher

CheckJobsWithProcess options
----------------------------

  * ``check promiscuous`` = <boolean> (default: False)
    Toggle the indiscriminate logging of the job status tool output
  * ``check timeout`` = <duration hh[:mm[:ss]]> (default: 00:01:00)
    Specify timeout of the process that is used to check the job status

EmptyDataProcessor options
--------------------------

  * ``dataset remove empty blocks`` = <boolean> (default: True)
    Toggle removal of empty blocks (without files) from the dataset
  * ``dataset remove empty files`` = <boolean> (default: True)
    Toggle removal of empty files (without entries) from the dataset

EntriesCountDataProcessor options
---------------------------------

  * ``dataset limit entries / dataset limit events`` = <integer> (default: -1)
    Specify the number of events after which addition files in the dataset are discarded

LocationDataProcessor options
-----------------------------

  * ``dataset location filter`` = <filter option> (default: '')
    Specify dataset location filter. Dataset without locations have the filter whitelist applied
  * ``dataset location filter matcher`` = <plugin> (Default: 'blackwhite')
    Specifiy matcher plugin that is used to match filter expressions
  * ``dataset location filter plugin`` = <plugin> (Default: 'strict')
    Specifiy matcher plugin that is used to match filter expressions
  * ``dataset location filter order`` = <enum: source|matcher> (Default: source)
    Specifiy the order of the filtered list

LumiDataProcessor options
-------------------------

  * ``lumi filter`` = <lookup specifier> (default: {})
    Specify lumi filter for the dataset (as nickname dependent dictionary)
  * ``lumi filter matcher`` = <plugin> (Default: start)
    Specifiy matcher plugin that is used to match the lookup expressions
  * ``lumi filter strictness`` = <enum: strict|weak> (default: strict)
    Specify if the lumi filter requires the run and lumi information (strict) or just the run information (weak)
  * ``lumi keep`` = <enum: RunLumi|Run|none> (default: <Run/none depending on active/inactive lumi filter>)
    Specify which lumi metadata to retain

MultiDataProcessor options
--------------------------

  * ``dataset processor prune`` = <boolean> (default: True)
    Toggle the removal of unused dataset processors from the dataset processing pipeline

PartitionEstimator options
--------------------------

  * ``target partitions`` = <integer> (default: -1)
    Specify the number of partitions the splitter should aim for
  * ``target partitions per nickname`` = <integer> (default: -1)
    Specify the number of partitions per nickname the splitter should aim for

SortingDataProcessor options
----------------------------

  * ``dataset block sort`` = <boolean> (default: False)
    Toggle sorting of dataset blocks
  * ``dataset files sort`` = <boolean> (default: False)
    Toggle sorting of dataset files
  * ``dataset location sort`` = <boolean> (default: False)
    Toggle sorting of dataset locations
  * ``dataset sort`` = <boolean> (default: False)
    Toggle sorting of datasets

URLCountDataProcessor options
-----------------------------

  * ``dataset limit urls / dataset limit files`` = <integer> (default: -1)
    Specify the number of files after which addition files in the dataset are discarded

URLDataProcessor options
------------------------

  * ``dataset ignore urls / dataset ignore files`` = <filter option> (default: '')
    Specify list of url / data sources to remove from the dataset
  * ``dataset ignore urls matcher`` = <plugin> (Default: 'blackwhite')
    Specifiy matcher plugin that is used to match filter expressions
  * ``dataset ignore urls plugin`` = <plugin> (Default: 'weak')
    Specifiy matcher plugin that is used to match filter expressions
  * ``dataset ignore urls order`` = <enum: source|matcher> (Default: source)
    Specifiy the order of the filtered list

EntriesConsistencyDataProcessor options
---------------------------------------

  * ``dataset check entry consistency`` = <enum: warn|abort|ignore> (default: abort)
    Toggle check for consistency between the number of events given in the block and and the files

NickNameConsistencyProcessor options
------------------------------------

  * ``dataset check nickname collision`` = <enum: warn|abort|ignore> (default: abort)
    Toggle nickname collision checks between datasets
  * ``dataset check nickname consistency`` = <enum: warn|abort|ignore> (default: abort)
    Toggle check for consistency of nicknames between blocks in the same dataset

UniqueDataProcessor options
---------------------------

  * ``dataset check unique block`` = <enum: warn|abort|skip|ignore|record> (default: abort)
    Specify how to react to duplicated dataset and blockname combinations
  * ``dataset check unique url`` = <enum: warn|abort|skip|ignore|record> (default: abort)
    Specify how to react to duplicated urls in the dataset

InlineNickNameProducer options
------------------------------

  * ``nickname expr`` = <text> (default: 'oldnick')
    Specify a python expression (using the variables dataset, block and oldnick) to generate the dataset nickname for the block

SimpleNickNameProducer options
------------------------------

  * ``nickname full name`` = <boolean> (default: True)
    Toggle if the nickname should be constructed from the complete dataset name or from the first part

CMSBaseProvider options
-----------------------

  * ``dbs instance`` = <text> (default: 'prod/global')
    Specify the default dbs instance (by url or instance identifier) to use for dataset queries
  * ``location format`` = <enum: hostname|siteDB|both> (default: hostname)
    Specify the format of the DBS location information
  * ``lumi filter`` = <lookup specifier> (default: {})
    Specify lumi filter for the dataset (as nickname dependent dictionary)
  * ``lumi filter matcher`` = <plugin> (Default: start)
    Specifiy matcher plugin that is used to match the lookup expressions
  * ``lumi metadata`` = <boolean> (default: <True/False for active/inactive lumi filter>)
    Toggle the retrieval of lumi metadata
  * ``only complete sites`` = <boolean> (default: True)
    Toggle the inclusion of incomplete sites in the dataset location information
  * ``only valid`` = <boolean> (default: True)
    Toggle the inclusion of files marked as invalid dataset
  * ``phedex sites`` = <filter option> (default: '-* T1_*_Disk T2_* T3_*')
    Toggle the inclusion of files marked as invalid dataset
  * ``phedex sites matcher`` = <plugin> (Default: 'blackwhite')
    Specifiy matcher plugin that is used to match filter expressions
  * ``phedex sites plugin`` = <plugin> (Default: 'strict')
    Specifiy matcher plugin that is used to match filter expressions
  * ``phedex sites order`` = <enum: source|matcher> (Default: source)
    Specifiy the order of the filtered list

ConfigDataProvider options
--------------------------

  * ``<dataset URL>`` = <int> [<metadata in JSON format>]
    The option name corresponds to the URL of the dataset file. The value consists of the number of entry and some optional file metadata
  * ``events`` = <integer> (default: automatic (-1))
    Specify total number of events in the dataset
  * ``metadata`` = <text> (default: '[]')
    List of metadata keys in the dataset
  * ``metadata common`` = <text> (default: '[]')
    Specify metadata values in JSON format that are common to all files in the dataset
  * ``nickname`` = <text> (default: <determined by dataset expression>)
    Specify the dataset nickname
  * ``prefix`` = <text> (default: '')
    Specify the common prefix of URLs in the dataset
  * ``se list`` = <text> (default: '')
    Specify list of locations where the dataset is available

DASProvider options
-------------------

  * ``das instance`` = <text> (default: 'https://cmsweb.cern.ch/das/cache')
    Specify url to the DAS instance that is used to query the datasets
  * ``dbs instance`` = <text> (default: 'prod/global')
    Specify the default dbs instance (by url or instance identifier) to use for dataset queries
  * ``location format`` = <enum: hostname|siteDB|both> (default: hostname)
    Specify the format of the DBS location information
  * ``lumi filter`` = <lookup specifier> (default: {})
    Specify lumi filter for the dataset (as nickname dependent dictionary)
  * ``lumi filter matcher`` = <plugin> (Default: start)
    Specifiy matcher plugin that is used to match the lookup expressions
  * ``lumi metadata`` = <boolean> (default: <True/False for active/inactive lumi filter>)
    Toggle the retrieval of lumi metadata
  * ``only complete sites`` = <boolean> (default: True)
    Toggle the inclusion of incomplete sites in the dataset location information
  * ``only valid`` = <boolean> (default: True)
    Toggle the inclusion of files marked as invalid dataset
  * ``phedex sites`` = <filter option> (default: '-* T1_*_Disk T2_* T3_*')
    Toggle the inclusion of files marked as invalid dataset
  * ``phedex sites matcher`` = <plugin> (Default: 'blackwhite')
    Specifiy matcher plugin that is used to match filter expressions
  * ``phedex sites plugin`` = <plugin> (Default: 'strict')
    Specifiy matcher plugin that is used to match filter expressions
  * ``phedex sites order`` = <enum: source|matcher> (Default: source)
    Specifiy the order of the filtered list

ScanProvider options
--------------------

  * ``<prefix> guard override`` = <list of values> (default: '')
    Override the list of guard keys that are preventing files from being in the same datasets or block
  * ``<prefix> hash keys`` = <list of values> (default: '')
    Specify list of keys that are used to determine the datasets or block assigment of files
  * ``<prefix> key select`` = <list of values> (default: '')
    Specify list of dataset or block hashes that are selected for this data source
  * ``<prefix> name pattern`` = <text> (default: '')
    Specify the name pattern for the dataset or block (using variables that are common to all files in the dataset or block)
  * ``scanner`` = <list of values> (default: <depends on other configuration options>)
    Specify list of info scanner plugins to retrieve dataset informations

DBSInfoProvider options
-----------------------

  * ``discovery`` = <boolean> (default: False)
    Toggle discovery only mode (without DBS consistency checks)
  * ``scanner`` = <list of values> (default: <depends on other configuration options>)
    Specify list of info scanner plugins to retrieve dataset informations

EventBoundarySplitter options
-----------------------------

  * ``events per job`` = <integer>
    Set granularity of dataset splitter

FLSplitStacker options
----------------------

  * ``splitter stack`` = <list of plugins> (default: 'BlockBoundarySplitter')
    Specify sequence of dataset splitters. All dataset splitters except for the last one have to be of type 'FileLevelSplitter', splitting only along file boundaries.

FileBoundarySplitter options
----------------------------

  * ``files per job`` = <integer>
    Set granularity of dataset splitter

HybridSplitter options
----------------------

  * ``events per job`` = <integer>
    Set guideline for the granularity of the dataset splitter

RunSplitter options
-------------------

  * ``run range`` = <integer> (default: 1)
    Specify number of sequential runs that are processed per job

UserMetadataSplitter options
----------------------------

  * ``split metadata`` = <list of values> (default: '')
    Specify the name of the metadata variable that is used to partition the dataset into equivalence classes.

AddFilePrefix options
---------------------

  * ``filename prefix`` = <text> (default: '')
    Specify prefix that is prepended to the dataset file names

DetermineEvents options
-----------------------

  * ``events command`` = <text> (default: '')
    Specify command that, given the file name as argument, returns with the number of events in the file
  * ``events default`` = <integer> (default: -1)
    Specify the default number of events in a dataset file
  * ``events key`` = <text> (default: '')
    Specify a variable from the available metadata that contains the number of events in a dataset file
  * ``events per key value`` = <float> (default: 1.0)
    Specify the conversion factor between the number of events in a dataset file and the metadata key

FilesFromDataProvider options
-----------------------------

  * ``source dataset path`` = <text>
    Specify path to dataset file that provides the input to the info scanner pipeline

FilesFromLS options
-------------------

  * ``source directory`` = <text> (default: '.')
    Specify source directory that is queried for dataset files
  * ``source recurse`` = <boolean> (default: False)
    Toggle recursion into directories. This is only possible for local source directories!

LFNFromPath options
-------------------

  * ``lfn marker`` = <text> (default: '/store/')
    Specifiy the string that marks the beginning of the LFN

MatchDelimeter options
----------------------

  * ``delimeter block key`` = <delimeter>:<start>:<end> (default: '')
    Specify the the delimeter and range to derive a block key
  * ``delimeter block modifier`` = <text> (default: '')
    Specify a python expression to modify the delimeter block key - using the variable 'value'
  * ``delimeter dataset key`` = <delimeter>:<start>:<end> (default: '')
    Specify the the delimeter and range to derive a dataset key
  * ``delimeter dataset modifier`` = <text> (default: '')
    Specify a python expression to modify the delimeter dataset key - using the variable 'value'
  * ``delimeter match`` = <delimeter>:<count> (default: '')
    Specify the the delimeter and number of delimeters that have to be in the dataset file

MatchOnFilename options
-----------------------

  * ``filename filter`` = <filter option> (default: '*.root')
    Specify filename filter to select files for the dataset
  * ``filename filter matcher`` = <plugin> (Default: 'shell')
    Specifiy matcher plugin that is used to match filter expressions

MetadataFromCMSSW options
-------------------------

  * ``include config infos`` = <boolean> (default: False)
    Toggle the inclusion of config information in the dataset metadata

MetadataFromTask options
------------------------

  * ``ignore task vars`` = <list of values> (default: <list of common task vars>)
    Specifiy the list of task variables that is not included in the dataset metadata

ObjectsFromCMSSW options
------------------------

  * ``include parent infos`` = <boolean> (default: False)
    Toggle the inclusion of parentage information in the dataset metadata
  * ``merge config infos`` = <boolean> (default: True)
    Toggle the merging of config file information according to config file hashes instead of config file names

OutputDirsFromConfig options
----------------------------

  * ``source config`` = <path>
    Specify source config file that contains the workflow whose output is queried for dataset files
  * ``job database`` = <plugin> (default: 'TextFileJobDB')
    Specify job database plugin that is used to store job information
  * ``source job selector`` = <text> (default: '')
    Specify job selector to apply to jobs in the task
  * ``workflow`` = <plugin[:name]> (default: 'Workflow:global')
    Specifies the workflow that is read from the config file

OutputDirsFromWork options
--------------------------

  * ``source directory`` = <path>
    Specify source directory that is queried for output directories of the task
  * ``source job selector`` = <text> (default: '')
    Specify job selector to apply to jobs in the task

ParentLookup options
--------------------

  * ``merge parents`` = <boolean> (default: False)
    Toggle the merging of dataset blocks with different parent paths
  * ``parent keys`` = <list of values> (default: '')
    Specify the dataset metadata keys that contain parentage information
  * ``parent match level`` = <integer> (default: 1)
    Specify the number of path components that is used to match parent files from the parent dataset and the used parent LFN. (0 == full match)
  * ``parent source`` = <text> (default: '')
    Specify the dataset specifier from which the parent information is taken

ConfigurableJobName options
---------------------------

  * ``job name`` = <text> (default: '@GC_TASK_ID@.@GC_JOB_ID@')
    Specify the job name template for the job name given to the backend

BlackWhiteMatcher options
-------------------------

  * ``<prefix> case sensitive`` = <boolean>
    Toggle case sensitivity for the matcher
  * ``<prefix> mode`` = <plugin> (default: 'start')
    Specify the matcher plugin that is used to match the subexpressions of the filter

JobManager options
------------------

  * ``abort report`` = <text> (default: 'LocationReport')
    Specify report plugin to display in case of job cancellations
  * ``chunks check`` = <integer> (default: 100)
    Specify maximal number of jobs to check in each job cycle
  * ``chunks enabled`` = <boolean> (default: True)
    Toggle to control if only a chunk of jobs are processed each job cycle
  * ``chunks retrieve`` = <integer> (default: 100)
    Specify maximal number of jobs to retrieve in each job cycle
  * ``chunks submit`` = <integer> (default: 100)
    Specify maximal number of jobs to submit in each job cycle
  * ``in flight`` = <integer> (default: no limit (-1))
    Maximum number of concurrently submitted jobs
  * ``in queue`` = <integer> (default: no limit (-1))
    Maximum number of queued jobs
  * ``job database`` = <plugin> (default: 'TextFileJobDB')
    Specify job database plugin that is used to store job information
  * ``jobs`` = <integer> (default: no limit (-1))
    Maximum number of jobs (truncated to task maximum)
  * ``max retry`` = <integer> (default: no limit (-1))
    Number of resubmission attempts for failed jobs
  * ``output processor`` = <plugin> (default: 'SandboxProcessor')
    Specify plugin that processes the output sandbox of successful jobs
  * ``queue timeout`` = <duration hh[:mm[:ss]]> (default: disabled (-1))
    Resubmit jobs after staying some time in initial state
  * ``selected`` = <text> (default: '')
    Apply general job selector
  * ``shuffle`` = <boolean> (default: False)
    Submit jobs in random order
  * ``unknown timeout`` = <duration hh[:mm[:ss]]> (default: disabled (-1))
    Cancel jobs without status information after staying in this state for the specified time

GridAccessToken options
-----------------------

  * ``ignore needed time / ignore walltime`` = <boolean> (default: False)
    Toggle if the needed time influences the decision if the proxy allows job submission
  * ``ignore warnings`` = <boolean> (default: False)
    Toggle check for non-zero exit code from voms-proxy-info
  * ``min lifetime`` = <duration hh[:mm[:ss]]> (default: 00:05:00)
    Specify the minimal lifetime of the proxy that is required to enable job submission
  * ``proxy path`` = <text> (default: '')
    Specify the path to the proxy file that is used to check
  * ``query time / min query time`` = <duration hh[:mm[:ss]]> (default: 00:30:00)
    Specify the interval in which queries are performed
  * ``urgent query time / max query time`` = <duration hh[:mm[:ss]]> (default: 00:05:00)
    Specify the interval in which queries are performed when the time is running out

AFSAccessToken options
----------------------

  * ``access refresh`` = <duration hh[:mm[:ss]]> (default: 01:00:00)
    Specify the lifetime threshold at which the access token is renewed
  * ``ignore needed time / ignore walltime`` = <boolean> (default: False)
    Toggle if the needed time influences the decision if the proxy allows job submission
  * ``min lifetime`` = <duration hh[:mm[:ss]]> (default: 00:05:00)
    Specify the minimal lifetime of the proxy that is required to enable job submission
  * ``query time / min query time`` = <duration hh[:mm[:ss]]> (default: 00:30:00)
    Specify the interval in which queries are performed
  * ``tickets`` = <list of values> (default: <all tickets: ''>)
    Specify the subset of kerberos tickets to check the access token lifetime
  * ``urgent query time / max query time`` = <duration hh[:mm[:ss]]> (default: 00:05:00)
    Specify the interval in which queries are performed when the time is running out

CoverageBroker options
----------------------

  * ``<broker name>`` = <filter option> (default: '')
    Specify the subset of entries that is stored sequentially in the job requirements
  * ``<broker name> matcher`` = <plugin> (Default: 'blackwhite')
    Specifiy matcher plugin that is used to match filter expressions
  * ``<broker name> plugin`` = <plugin> (Default: 'try_strict')
    Specifiy matcher plugin that is used to match filter expressions
  * ``<broker name> order`` = <enum: source|matcher> (Default: matcher)
    Specifiy the order of the filtered list
  * ``<broker name> entries`` = <integer> (default: no limit (0))
    Specify the number of broker results to store in the job requirements
  * ``<broker name> randomize`` = <boolean> (default: False)
    Toggle the randomization of broker results

FilterBroker options
--------------------

  * ``<broker name>`` = <filter option> (default: '')
    Specify the filter expression to select entries given to the broker
  * ``<broker name> matcher`` = <plugin> (Default: 'blackwhite')
    Specifiy matcher plugin that is used to match filter expressions
  * ``<broker name> plugin`` = <plugin> (Default: 'try_strict')
    Specifiy matcher plugin that is used to match filter expressions
  * ``<broker name> order`` = <enum: source|matcher> (Default: matcher)
    Specifiy the order of the filtered list
  * ``<broker name> entries`` = <integer> (default: no limit (0))
    Specify the number of broker results to store in the job requirements
  * ``<broker name> randomize`` = <boolean> (default: False)
    Toggle the randomization of broker results

StorageBroker options
---------------------

  * ``<broker name> entries`` = <integer> (default: no limit (0))
    Specify the number of broker results to store in the job requirements
  * ``<broker name> randomize`` = <boolean> (default: False)
    Toggle the randomization of broker results
  * ``<broker name> storage access`` = <lookup specifier> (default: {})
    Specify the lookup dictionary that maps storage requirements into other kinds of requirements
  * ``<broker name> storage access matcher`` = <plugin> (Default: start)
    Specifiy matcher plugin that is used to match the lookup expressions

UserBroker options
------------------

  * ``<broker name>`` = <list of values> (default: '')
    Specify the list of user settings for the broker
  * ``<broker name> entries`` = <integer> (default: no limit (0))
    Specify the number of broker results to store in the job requirements
  * ``<broker name> randomize`` = <boolean> (default: False)
    Toggle the randomization of broker results

DashBoard options
-----------------

  * ``application`` = <text> (default: 'shellscript')
    Specify the name of the application that is reported to dashboard
  * ``dashboard timeout`` = <duration hh[:mm[:ss]]> (default: 00:00:05)
    Specify the timeout for dashboard interactions
  * ``task`` = <text> (default: <'analysis' but can be overridden by task>)
    Specify the task type reported to dashboard
  * ``task name`` = <text> (default: '@GC_TASK_ID@_@DATASETNICK@')
    Specify the task name reported to dashboard

JabberAlarm options
-------------------

  * ``source jid`` = <text>
    source account of the jabber messages
  * ``source password file`` = <path>
    path to password file of the source account
  * ``target jid`` = <text>
    target account of the jabber messages

ScriptMonitoring options
------------------------

  * ``on finish`` = <command or path> (default: '')
    Specify script that is executed when grid-control is exited
  * ``on finish type`` = <enum: executable|command> (Default: executable)
    Specifiy the type of command
  * ``on output`` = <command or path> (default: '')
    Specify script that is executed when the job output is retrieved
  * ``on output type`` = <enum: executable|command> (Default: executable)
    Specifiy the type of command
  * ``on status`` = <command or path> (default: '')
    Specify script that is executed when the job status changes
  * ``on status type`` = <enum: executable|command> (Default: executable)
    Specifiy the type of command
  * ``on submit`` = <command or path> (default: '')
    Specify script that is executed when a job is submitted
  * ``on submit type`` = <enum: executable|command> (Default: executable)
    Specifiy the type of command
  * ``script timeout`` = <duration hh[:mm[:ss]]> (default: 00:00:05)
    Specify the maximal script runtime after which the script is aborted
  * ``silent`` = <boolean> (default: True)
    Do not show output of event scripts

LocalSBStorageManager options
-----------------------------

  * ``<storage channel class> path`` = <path> (default: <workdir>/sandbox)
    Specify the default transport URL that is used to transfer files over this type of storage channel

SEStorageManager options
------------------------

  * ``<storage channel class> path`` = <list of values> (default: '')
    Specify the default transport URL(s) that are used to transfer files over this type of storage channel
  * ``<storage channel> files`` = <list of values> (default: '')
    Specify the files that are transferred over this storage channel
  * ``<storage channel> force`` = <boolean> (default: True)
    Specify the files that are transferred over this storage channel
  * ``<storage channel> path`` = <list of values> (default: given by '<storage channel class> path')
    Specify the transport URLs that are used to transfer files over this storage channel
  * ``<storage channel> pattern`` = <text> (default: '@X@')
    Specify the pattern that is used to translate local to remote file names
  * ``<storage channel> timeout`` = <duration hh[:mm[:ss]]> (default: 02:00:00)
    Specify the transfer timeout for files over this storage channel

SCRAMTask options
-----------------

  * ``wall time`` = <duration hh[:mm[:ss]]>
    Requested wall time also used for checking the proxy lifetime
  * ``area files`` = <list of values> (default: '-.* -config bin lib python module */data *.xml *.sql *.db *.cf[if] *.py -*/.git -*/.svn -*/CVS -*/work.*')
    List of files that should be taken from the CMSSW project area for running the job
  * ``cpu time`` = <duration hh[:mm[:ss]]> (default: <wall time>)
    Requested cpu time
  * ``cpus`` = <integer> (default: 1)
    Requested number of cpus per node
  * ``depends`` = <list of values> (default: '')
    List of environment setup scripts that the jobs depend on
  * ``gzip output`` = <boolean> (default: True)
    Toggle the compression of the job log files for stdout and stderr
  * ``input files`` = <list of paths> (default: '')
    List of files that should be transferred to the landing zone of the job on the worker node. Only for small files - send large files via SE!
  * ``internal parameter factory`` = <plugin> (default: 'BasicParameterFactory')
    Specify the parameter factory plugin that is used to generate the basic grid-control parameters
  * ``job name generator`` = <plugin> (default: 'DefaultJobName')
    Specify the job name plugin that generates the job name that is given to the backend
  * ``landing zone space left`` = <integer> (default: 1)
    Minimum amount of disk space (in MB) that the job has to leave in the landing zone directory while running
  * ``landing zone space used`` = <integer> (default: 100)
    Maximum amount of disk space (in MB) that the job is allowed to use in the landing zone directory while running
  * ``memory`` = <integer> (default: unspecified (-1))
    Requested memory in MB. Some batch farms have very low default memory limits in which case it is necessary to specify this option!
  * ``node timeout`` = <duration hh[:mm[:ss]]> (default: disabled (-1))
    Cancel job after some time on worker node
  * ``output files`` = <list of values> (default: '')
    List of files that should be transferred to the job output directory on the submission machine. Only for small files - send large files via SE!
  * ``parameter adapter`` = <plugin> (default: 'TrackedParameterAdapter')
    Specify the parameter adapter plugin that translates parameter point to job number
  * ``project area`` = <path> (default: <depends on ``scram arch`` and ``scram project``>)
    Specify location of the CMSSW project area that should be send with the job. Instead of the CMSSW project area, it is possible to specify ``scram arch`` and ``scram project`` to use a fresh CMSSW project.
  * ``scram arch`` = <text> (default: <depends on ``project area``>)
    Specify scram architecture that should be used by the job (eg. 'slc7_amd64_gcc777'). When using an existing CMSSW project area with ``project area``, this option uses the default value taken from the project area.
  * ``scram arch requirements`` = <boolean> (default: True)
    Toggle the inclusion of the scram architecture in the job requirements
  * ``scram project`` = <list of values> (default: '')
    Specify scram project that should be used by the job (eg. 'CMSSW CMSSW_9_9_9')
  * ``scram project requirements`` = <boolean> (default: False)
    Toggle the inclusion of the scram project name in the job requirements
  * ``scram project version requirements`` = <boolean> (default: False)
    Toggle the inclusion of the scram project version in the job requirements
  * ``scram version`` = <text> (default: 'scramv1')
    Specify scram version that should be used by the job.
  * ``scratch space left`` = <integer> (default: 1)
    Minimum amount of disk space (in MB) that the job has to leave in the scratch directory while running. If the landing zone itself is the scratch space, the scratch thresholds apply
  * ``scratch space used`` = <integer> (default: 5000)
    Maximum amount of disk space (in MB) that the job is allowed to use in the scratch directory while running. If the landing zone itself is the scratch space, the scratch thresholds apply
  * ``se min size`` = <integer> (default: disabled (-1))
    SE output files below this file size (in MB) trigger a job failure
  * ``subst files`` = <list of values> (default: '')
    List of files that will be subjected to variable substituion
  * ``task date`` = <text> (default: current date: YYYY-MM-DD)
    Persistent date when the task was started.
  * ``task id`` = <text> (default: GCxxxxxxxxxxxx)
    Persistent task identifier that is generated at the start of the task

ROOTTask options
----------------

  * ``executable`` = <text>
    Path to the executable
  * ``wall time`` = <duration hh[:mm[:ss]]>
    Requested wall time also used for checking the proxy lifetime
  * ``cpu time`` = <duration hh[:mm[:ss]]> (default: <wall time>)
    Requested cpu time
  * ``cpus`` = <integer> (default: 1)
    Requested number of cpus per node
  * ``depends`` = <list of values> (default: '')
    List of environment setup scripts that the jobs depend on
  * ``gzip output`` = <boolean> (default: True)
    Toggle the compression of the job log files for stdout and stderr
  * ``input files`` = <list of paths> (default: '')
    List of files that should be transferred to the landing zone of the job on the worker node. Only for small files - send large files via SE!
  * ``internal parameter factory`` = <plugin> (default: 'BasicParameterFactory')
    Specify the parameter factory plugin that is used to generate the basic grid-control parameters
  * ``job name generator`` = <plugin> (default: 'DefaultJobName')
    Specify the job name plugin that generates the job name that is given to the backend
  * ``landing zone space left`` = <integer> (default: 1)
    Minimum amount of disk space (in MB) that the job has to leave in the landing zone directory while running
  * ``landing zone space used`` = <integer> (default: 100)
    Maximum amount of disk space (in MB) that the job is allowed to use in the landing zone directory while running
  * ``memory`` = <integer> (default: unspecified (-1))
    Requested memory in MB. Some batch farms have very low default memory limits in which case it is necessary to specify this option!
  * ``node timeout`` = <duration hh[:mm[:ss]]> (default: disabled (-1))
    Cancel job after some time on worker node
  * ``output files`` = <list of values> (default: '')
    List of files that should be transferred to the job output directory on the submission machine. Only for small files - send large files via SE!
  * ``parameter adapter`` = <plugin> (default: 'TrackedParameterAdapter')
    Specify the parameter adapter plugin that translates parameter point to job number
  * ``root path`` = <text> (default: ${ROOTSYS})
    Path to the ROOT installation
  * ``scratch space left`` = <integer> (default: 1)
    Minimum amount of disk space (in MB) that the job has to leave in the scratch directory while running. If the landing zone itself is the scratch space, the scratch thresholds apply
  * ``scratch space used`` = <integer> (default: 5000)
    Maximum amount of disk space (in MB) that the job is allowed to use in the scratch directory while running. If the landing zone itself is the scratch space, the scratch thresholds apply
  * ``se min size`` = <integer> (default: disabled (-1))
    SE output files below this file size (in MB) trigger a job failure
  * ``subst files`` = <list of values> (default: '')
    List of files that will be subjected to variable substituion
  * ``task date`` = <text> (default: current date: YYYY-MM-DD)
    Persistent date when the task was started.
  * ``task id`` = <text> (default: GCxxxxxxxxxxxx)
    Persistent task identifier that is generated at the start of the task

InactiveWMS options
-------------------

  * ``access token / proxy`` = <list of plugin[:name] ...> (default: 'TrivialAccessToken')
    Specify access token plugins that are necessary for job submission
  * access token manager = <plugin> (Default: 'MultiAccessToken')
    Specifiy compositor class to merge the different plugins given in ``access token``
  * ``job parser`` = <plugin> (default: 'JobInfoProcessor')
    Specify plugin that checks the output sandbox of the job and returns with the job status
  * ``wait idle`` = <integer> (default: 60)
    Wait for the specified duration if the job cycle was idle
  * ``wait work`` = <integer> (default: 10)
    Wait for the specified duration during the work steps of the job cycle

Local options
-------------

  * ``job parser`` = <plugin> (default: 'JobInfoProcessor')
    Specify plugin that checks the output sandbox of the job and returns with the job status
  * ``sandbox path`` = <path> (default: <workdir>/sandbox)
    Specify the sandbox path
  * ``wait idle`` = <integer> (default: 60)
    Wait for the specified duration if the job cycle was idle
  * ``wait work`` = <integer> (default: 10)
    Wait for the specified duration during the work steps of the job cycle
  * ``wms`` = <text> (default: '')
    Override automatic discovery of local backend

MultiWMS options
----------------

  * ``job parser`` = <plugin> (default: 'JobInfoProcessor')
    Specify plugin that checks the output sandbox of the job and returns with the job status
  * ``wait idle`` = <integer> (default: 60)
    Wait for the specified duration if the job cycle was idle
  * ``wait work`` = <integer> (default: 10)
    Wait for the specified duration during the work steps of the job cycle
  * ``wms broker`` = <plugin[:name]> (default: 'RandomBroker')
    Specify broker plugin to select the WMS for job submission

Condor options
--------------

  * ``classaddata`` = <list of values> (default: '')
    List of classAds to manually add to the job submission file
  * ``debuglog`` = <text> (default: '')
    Path to a debug log file
  * ``jdldata`` = <list of values> (default: '')
    List of jdl lines to manually add to the job submission file
  * ``job parser`` = <plugin> (default: 'JobInfoProcessor')
    Specify plugin that checks the output sandbox of the job and returns with the job status
  * ``notifyemail`` = <text> (default: '')
    Specify the email address for job notifications
  * ``poolargs query`` = <dictionary> (default: {})
    Specify keys for condor pool ClassAds
  * ``poolargs req`` = <dictionary> (default: {})
    Specify keys for condor pool ClassAds
  * ``poolhostlist`` = <list of values> (default: '')
    Specify list of pool hosts
  * ``remote dest`` = <text> (default: '@')
    Specify remote destination
  * ``remote type`` = <enum: LOCAL|SPOOL|SSH|GSISSH> (default: LOCAL)
    Specify the type of remote destination
  * ``remote user`` = <text> (default: '')
    Specify user at remote destination
  * ``remote workdir`` = <text> (default: '')
    Specify work directory at the remote destination
  * ``sandbox path`` = <path> (default: <workdir>/sandbox)
    Specify the sandbox path
  * ``site broker`` = <plugin[:name]> (default: 'UserBroker')
    Specify broker plugin to select the site for job submission
  * ``task id`` = <text> (default: <md5 hash>)
    Persistent condor task identifier that is generated at the start of the task
  * ``universe`` = <text> (default: 'vanilla')
    Specify the name of the Condor universe
  * ``wait idle`` = <integer> (default: 60)
    Wait for the specified duration if the job cycle was idle
  * ``wait work`` = <integer> (default: 10)
    Wait for the specified duration during the work steps of the job cycle

GridWMS options
---------------

  * ``ce`` = <text> (default: '')
    Specify CE for job submission
  * ``config`` = <path> (default: '')
    Specify the config file with grid settings
  * ``job parser`` = <plugin> (default: 'JobInfoProcessor')
    Specify plugin that checks the output sandbox of the job and returns with the job status
  * ``site broker`` = <plugin[:name]> (default: 'UserBroker')
    Specify broker plugin to select the site for job submission
  * ``vo`` = <text> (default: <group from the access token>)
    Specify the VO used for job submission
  * ``wait idle`` = <integer> (default: 60)
    Wait for the specified duration if the job cycle was idle
  * ``wait work`` = <integer> (default: 10)
    Wait for the specified duration during the work steps of the job cycle
  * ``warn sb size`` = <integer> (default: 5)
    Warning threshold for large sandboxes (in MB)

HTCondor options
----------------

  * ``append info`` = <list of values> (default: '')
    List of classAds to manually add to the job submission file
  * ``append opts`` = <list of values> (default: '')
    List of jdl lines to manually add to the job submission file
  * ``job parser`` = <plugin> (default: 'JobInfoProcessor')
    Specify plugin that checks the output sandbox of the job and returns with the job status
  * ``poolconfig`` = <list of values> (default: '')
    Specify the list of pool config files
  * ``sandbox path`` = <path> (default: <workdir>/sandbox.<wms name>)
    Specify the sandbox path
  * ``schedduri`` = <text> (default: '')
    Specify URI of the schedd
  * ``universe`` = <text> (default: 'vanilla')
    Specify the name of the Condor universe
  * ``wait idle`` = <integer> (default: 60)
    Wait for the specified duration if the job cycle was idle
  * ``wait work`` = <integer> (default: 10)
    Wait for the specified duration during the work steps of the job cycle

CreamWMS options
----------------

  * ``ce`` = <text> (default: '')
    Specify CE for job submission
  * ``config`` = <path> (default: '')
    Specify the config file with grid settings
  * ``job chunk size`` = <integer> (default: 10)
    Specify size of job submission chunks
  * ``job parser`` = <plugin> (default: 'JobInfoProcessor')
    Specify plugin that checks the output sandbox of the job and returns with the job status
  * ``site broker`` = <plugin[:name]> (default: 'UserBroker')
    Specify broker plugin to select the site for job submission
  * ``vo`` = <text> (default: <group from the access token>)
    Specify the VO used for job submission
  * ``wait idle`` = <integer> (default: 60)
    Wait for the specified duration if the job cycle was idle
  * ``wait work`` = <integer> (default: 10)
    Wait for the specified duration during the work steps of the job cycle
  * ``warn sb size`` = <integer> (default: 5)
    Warning threshold for large sandboxes (in MB)

GliteWMS options
----------------

  * ``ce`` = <text> (default: '')
    Specify CE for job submission
  * ``config`` = <path> (default: '')
    Specify the config file with grid settings
  * ``discover sites`` = <boolean> (default: False)
    Toggle the automatic discovery of matching CEs
  * ``discover wms`` = <boolean> (default: True)
    Toggle the automatic discovery of WMS endpoints
  * ``force delegate`` = <boolean> (default: False)
    Toggle the enforcement of proxy delegation to the WMS
  * ``job parser`` = <plugin> (default: 'JobInfoProcessor')
    Specify plugin that checks the output sandbox of the job and returns with the job status
  * ``site broker`` = <plugin[:name]> (default: 'UserBroker')
    Specify broker plugin to select the site for job submission
  * ``try delegate`` = <boolean> (default: True)
    Toggle the attempt to do proxy delegation to the WMS
  * ``vo`` = <text> (default: <group from the access token>)
    Specify the VO used for job submission
  * ``wait idle`` = <integer> (default: 60)
    Wait for the specified duration if the job cycle was idle
  * ``wait work`` = <integer> (default: 10)
    Wait for the specified duration during the work steps of the job cycle
  * ``warn sb size`` = <integer> (default: 5)
    Warning threshold for large sandboxes (in MB)
  * ``wms discover full`` = <boolean> (default: True)
    Toggle between full and lazy WMS endpoint discovery

GridEngine options
------------------

  * ``account`` = <text> (default: '')
    Specify fairshare account
  * ``delay output`` = <boolean> (default: False)
    Toggle between direct output of stdout/stderr to the sandbox or indirect output to local tmp during job execution
  * ``job parser`` = <plugin> (default: 'JobInfoProcessor')
    Specify plugin that checks the output sandbox of the job and returns with the job status
  * ``memory`` = <integer> (default: unspecified (-1))
    Requested memory in MB by the batch system
  * ``project name`` = <text> (default: '')
    Specify project name for batch fairshare
  * ``queue broker`` = <plugin[:name]> (default: 'UserBroker')
    Specify broker plugin to select the queue for job submission
  * ``scratch path`` = <list of values> (default: 'TMPDIR /tmp')
    Specify the list of scratch environment variables and paths to search for the scratch directory
  * ``shell`` = <text> (default: '')
    Specify the shell to use for job execution
  * ``site broker`` = <plugin[:name]> (default: 'UserBroker')
    Specify broker plugin to select the site for job submission
  * ``software requirement map`` = <lookup specifier> (default: {})
    Specify a dictionary to map job requirements into submission options
  * ``software requirement map matcher`` = <plugin> (Default: start)
    Specifiy matcher plugin that is used to match the lookup expressions
  * ``submit options`` = <text> (default: '')
    Specify additional job submission options
  * ``wait idle`` = <integer> (default: 60)
    Wait for the specified duration if the job cycle was idle
  * ``wait work`` = <integer> (default: 10)
    Wait for the specified duration during the work steps of the job cycle

PBS options
-----------

  * ``account`` = <text> (default: '')
    Specify fairshare account
  * ``delay output`` = <boolean> (default: False)
    Toggle between direct output of stdout/stderr to the sandbox or indirect output to local tmp during job execution
  * ``job parser`` = <plugin> (default: 'JobInfoProcessor')
    Specify plugin that checks the output sandbox of the job and returns with the job status
  * ``memory`` = <integer> (default: unspecified (-1))
    Requested memory in MB by the batch system
  * ``queue broker`` = <plugin[:name]> (default: 'UserBroker')
    Specify broker plugin to select the queue for job submission
  * ``scratch path`` = <list of values> (default: 'TMPDIR /tmp')
    Specify the list of scratch environment variables and paths to search for the scratch directory
  * ``server`` = <text> (default: '')
    Specify the PBS batch server
  * ``shell`` = <text> (default: '')
    Specify the shell to use for job execution
  * ``site broker`` = <plugin[:name]> (default: 'UserBroker')
    Specify broker plugin to select the site for job submission
  * ``software requirement map`` = <lookup specifier> (default: {})
    Specify a dictionary to map job requirements into submission options
  * ``software requirement map matcher`` = <plugin> (Default: start)
    Specifiy matcher plugin that is used to match the lookup expressions
  * ``submit options`` = <text> (default: '')
    Specify additional job submission options
  * ``wait idle`` = <integer> (default: 60)
    Wait for the specified duration if the job cycle was idle
  * ``wait work`` = <integer> (default: 10)
    Wait for the specified duration during the work steps of the job cycle

BasicParameterFactory options
-----------------------------

  * ``constants`` = <list of values> (default: '')
    Specify the list of constant names that is queried for values
  * ``nseeds`` = <integer> (default: 10)
    Number of random seeds to generate
  * ``parameter factory`` = <plugin> (default: 'SimpleParameterFactory')
    Specify the parameter factory plugin that is used to generate the parameter space of the task
  * ``random variables`` = <list of values> (default: 'JOB_RANDOM')
    Specify list of variable names that will contain random values on the worker node
  * ``repeat`` = <integer> (default: 1)
    Specify the number of jobs that each parameter space point spawns
  * ``seeds`` = <list of values> (default: Generate <nseeds> random seeds)
    Random seeds used in the job via @SEED_j@
	@SEED_0@ = 32, 33, 34, ... for first, second, third job
	@SEED_1@ = 51, 52, 53, ... for first, second, third job
  * ``translate requirements`` = <boolean> (default: True)
    Toggle the translation of the parameters WALLTIME, CPUTIME and MEMORY into job requirements

LFNPartitionProcessor options
-----------------------------

  * ``partition lfn modifier`` = <text> (default: '')
    Specify a LFN prefix or prefix shortcut ('/': reduce to LFN)
  * ``partition lfn modifier dict`` = <dictionary> (default: {'<xrootd>': 'root://cms-xrd-global.cern.ch/', '<xrootd:eu>': 'root://xrootd-cms.infn.it/', '<xrootd:us>': 'root://cmsxrootd.fnal.gov/'})
    Specify a dictionary with lfn modifier shortcuts

LocationPartitionProcessor options
----------------------------------

  * ``partition location check`` = <boolean> (default: True)
    Toggle the deactivation of partitions without storage locations
  * ``partition location filter`` = <filter option> (default: '')
    Specify filter for dataset locations
  * ``partition location filter matcher`` = <plugin> (Default: 'blackwhite')
    Specifiy matcher plugin that is used to match filter expressions
  * ``partition location filter plugin`` = <plugin> (Default: 'weak')
    Specifiy matcher plugin that is used to match filter expressions
  * ``partition location filter order`` = <enum: source|matcher> (Default: source)
    Specifiy the order of the filtered list
  * ``partition location preference`` = <list of values> (default: '')
    Specify dataset location preferences
  * ``partition location requirement`` = <boolean> (default: True)
    Add dataset location to job requirements

LumiPartitionProcessor options
------------------------------

  * ``lumi filter`` = <lookup specifier> (default: {})
    Specify lumi filter for the dataset (as nickname dependent dictionary)
  * ``lumi filter matcher`` = <plugin> (Default: start)
    Specifiy matcher plugin that is used to match the lookup expressions

MetaPartitionProcessor options
------------------------------

  * ``partition metadata`` = <list of values> (default: '')
    Specify list of dataset metadata to forward to the job environment

MultiPartitionProcessor options
-------------------------------

  * ``partition processor prune`` = <boolean> (default: True)
    Toggle the removal of unused partition processors from the partition processing pipeline

RequirementsPartitionProcessor options
--------------------------------------

  * ``partition cputime factor`` = <float> (default: -1.0)
    Specify how the requested cpu time scales with the number of entries in the partition
  * ``partition cputime offset`` = <float> (default: 0.0)
    Specify the offset of the requested cpu time
  * ``partition memory factor`` = <float> (default: -1.0)
    Specify how the requested memory scales with the number of entries in the partition
  * ``partition memory offset`` = <float> (default: 0.0)
    Specify the offset of the requested memory
  * ``partition walltime factor`` = <float> (default: -1.0)
    Specify how the requested wall time scales with the number of entries in the partition
  * ``partition walltime offset`` = <float> (default: 0.0)
    Specify the offset of the requested wall time

TFCPartitionProcessor options
-----------------------------

  * ``partition tfc`` = <lookup specifier> (default: {})
    Specify a dataset location dependent trivial file catalogue with file name prefixes
  * ``partition tfc matcher`` = <plugin> (Default: start)
    Specifiy matcher plugin that is used to match the lookup expressions

GridEngine_CheckJobsProcessCreator options
------------------------------------------

  * ``user`` = <text> (default: ${LOGNAME})
    Specify batch system user name

