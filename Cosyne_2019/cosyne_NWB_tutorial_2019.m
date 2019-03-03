%% Installing matnwb

%{
!git clone https://github.com/NeurodataWithoutBorders/matnwb.git
cd matnwb
addpath(genpath(pwd));
generateCore('schema/core/nwb.namespace.yaml');
%}

%% Setup nwbfile
 date = datetime(2018, 4, 25, 2, 30, 3);
 
session_start_time = datetime(date, 'Format', 'yyyy-MM-dd''T''HH:mm:ssZZ', ...
	'TimeZone', 'local');
 
nwb = nwbfile( ...
	'session_description', 'mouse in open exploration', 'identifier', 'Mouse5_Day3', ...
	'session_start_time', session_start_time);

%% Subject information
nwb.general_subject = types.core.Subject('age', '9 months', ...
    'description', 'mouse 5', ...
    'species', 'Mus musculus', ...
    'sex', 'M');

%% Position
% The |Position| object is a |MultiContainerInterface| that holds one or more 
% |SpatialSeries| objects, which are a subclass of |TimeSeries|. Here, 
% we put a |SpatialSeries| object called |'position'| in a |Position| object, 
% and put that in a |ProcessingModule| named |'behavior'|.

position_data = [linspace(0,10,100); linspace(1,8,100)]';

position_ts = types.core.SpatialSeries( ...
	'data', position_data, ...
	'reference_frame', 'unknown', ...
	'data_conversion', 1.0, ...
'data_resolution', NaN, ...
	'timestamps', linspace(0, 100)/200);

behavior_mod = types.core.ProcessingModule(...
'description',  'contains behavioral data');
Position = types.core.Position(...
'data', position_ts);
behavior_mod.nwbdatainterface.set(...
'Position', Position);

nwb.processing.set('behavior', behavior_mod);

%% Test write

nwbExport(nwb, 'ecephys_tutorial.nwb')
%% Electrode table
% Extracellular |electrodes| are stored in a electrodes, which is a 
% |DynamicTable|. |electrodes| has several required fields: x, y, z, 
% impedence, location, filtering, and electrode_group. Here, we also 
% demonstate how to add optional columns to a table by adding the |'label'|
% column.

shank_channels = [3, 4];
variables = {'x', 'y', 'z', 'imp', 'location', 'filtering', 'group', 'label'};
device_name = 'implant';
nwb.general_devices.set(device_name, types.core.Device());
device_link = types.untyped.SoftLink(['/general/devices/' device_name]);
for ishank = 1:length(shank_channels)
    nelecs = shank_channels(ishank);
    group_name = ['shank' num2str(ishank)];
    nwb.general_extracellular_ephys.set(group_name, ...
types.core.ElectrodeGroup( ...
    'description', ['electrode group for shank' num2str(ishank)], ...
    	    'location', 'brain area', ...
    	    'device', device_link));
    group_object_view = types.untyped.ObjectView( ...
    	['/general/extracellular_ephys/' group_name]);
    for ielec = 1:length(nelecs)
if ishank == 1 && ielec == 1
        	    tbl = table(NaN, NaN, NaN, NaN, {'unknown'}, {'unknown'}, ...
           	group_object_view, {[group_name 'elec' num2str(ielec)]}, ...
            	    'VariableNames', variables);
    	else
        	    tbl = [tbl; {NaN, NaN, NaN, NaN, 'unknown', 'unknown', ...
                  group_object_view, [group_name 'elec' num2str(ielec)]}];
    	end
    end
end
electrode_table = util.table2nwb(tbl, 'all electrodes');
nwb.general_extracellular_ephys_electrodes = electrode_table;

electrodes_object_view = types.untyped.ObjectView( ...
    '/general/extracellular_ephys/electrodes');

electrode_table_region = types.core.DynamicTableRegion( ...
    'table', electrodes_object_view, ...
    'description', 'all electrodes', ...
    'data', [0 height(tbl)-1]');


%% LFP
% |LFP| is another |MultiContainerInterface|. It holds one or more 
% |ElectricalSeries| objects, which are |TimeSeries|. Here, we put an 
% |ElectricalSeries| named |'lfp'| in an |LFP| object, in a
% |ProcessingModule| named  |'ecephys'|.

electrical_series = types.core.ElectricalSeries( ...
	'starting_time', 0.0, ... % seconds
	'starting_time_rate', 200., ... % Hz
	'data', randn(7, 100), ...
	'electrodes', electrode_table_region, ...
	'data_unit', 'V');
ecephys_module = types.core.ProcessingModule(...
	'description', 'extracellular electrophysiology');
ecephys_module.nwbdatainterface.set('LFP', ...
	types.core.LFP('lfp', electrical_series));
nwb.processing.set('ecephys', ecephys_module);

%% Spike times
% Spike times are stored in another |DynamicTable| of subtype |Units|. The 
% default |Units| table is at |/units| in the HDF5 file. You can add columns 
% to the |Units| table just like you did for electrodes.

all_spike_times = {};
for ishank = 1:length(shank_channels)
    for iunit = 1:poissrnd(5)
        	all_spike_times{end+1} = sort(rand(1, poissrnd(10)) * 5);
    end
end
 
[spike_times_vector, spike_times_index] = util.create_indexed_column( ...
	all_spike_times, '/units/spike_times');
 
nwb.units = types.core.Units( ...
	'colnames', {'spike_times'}, ...
	'description', 'units table', ...
	'id', types.core.ElementIdentifiers( ...
    'data', int64(0:length(all_spike_times) - 1)));
nwb.units.spike_times = spike_times_vector;
nwb.units.spike_times_index = spike_times_index;

%% Trials
% Trials is another |DynamicTable| that lives an |/intervals/trials|.
nwb.intervals_trials = types.core.TimeIntervals( ...
    'colnames', {'start_time', 'stop_time', 'correct'}, ...
    'description', 'trial data and properties', ...
    'id', types.core.ElementIdentifiers('data', 0:2), ...
    'start_time', types.core.VectorData('data', [.1, 1.5, 2.5], ...
    	'description','start time of trial'), ...
    'stop_time', types.core.VectorData('data', [1., 2., 3.], ...
    	'description','end of each trial'), ...
    'correct', types.core.VectorData('data', [false, true, false], ...
    	'description', 'my description'));
    
%% Write and read
% Data arrays are read passively from the file. That means |TimeSeries.data| 
% does not read the entire data object, but presents an h5py object that 
% can be indexed to read data. Index this array with the |load| method.
% |load| with no input arguments reads the entire dataset.

nwbExport(nwb, 'ecephys_tutorial.nwb')
 
nwb2 = nwbRead('ecephys_tutorial.nwb');
 
nwb2.processing.get('ecephys').nwbdatainterface. ...
	get('LFP').electricalseries.get('lfp').data.load;

%% Accessing data regions

nwb2 = nwbRead('ecephys_tutorial.nwb');

% read section of LFP
nwb2.processing.get('ecephys'). ...
    nwbdatainterface.get('LFP'). ...
    electricalseries.get('lfp'). ...
    data.load([1,1],[5,10])

% read spike times for first unit
util.read_indexed_column(nwb.units.spike_times_index, nwb.units.spike_times, 1)






