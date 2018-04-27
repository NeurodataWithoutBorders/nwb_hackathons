cd matnwb-master/
mkdir namespaces
mkdir ext
nwb_file = nwbRead('test_output.nwb');
chbo = permute(nwb_file.acquisition.get('chbo').data,[3 2 1]);
chbr = permute(nwb_file.acquisition.get('chbo').data,[3 2 1]);
gcamp = permute(nwb_file.acquisition.get('gcamp').data,[3 2 1]);
webcam = permute(nwb_file.acquisition.get('webcam').data,[3 2 1]);
