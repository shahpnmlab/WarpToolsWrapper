#!/bin/bash

WarpTools create_settings --output warp_frameseries.settings --folder_processing warp_frameseries --folder_data frames --extension "*.eer" --angpix 1.18 --gain_path 20240409_110724_EER_GainReference.gain --exposure 3.2 --eer_groupexposure 0.7 --tomo_dimensions 4096x4096x2500
WarpTools fs_motion_and_ctf --settings previous.settings --m_grid 1x1x10 --c_grid 2x2x1 --c_range_max 7 --c_defocus_max 10 --c_amplitude 0.1 --c_use_sum --out_averages --out_average_halves --perdevice 4 --device_list 0 1 2 3 --c_window 768
WarpTools filter_quality --settings warp_frameseries.settings --histograms
WarpTools ts_import --mdocs mdoc --frameseries warp_frameseries --tilt_exposure 3.2 --min_intensity 0.2 --output tomostar
WarpTools create_settings --output warp_tiltseries.settings --folder_processing warp_tiltseries --folder_data tomostar --extension "*.tomostar" --angpix 0.7894 --gain_path gain_ref.mrc --exposure 2.64 --tomo_dimensions 4400x6000x1000
WarpTools ts_stack --settings warp_frameseries.settings --device_list 0 1 2 3 --perdevice 4
WarpTools ts_ctf --settings warp_tiltseries.settings --range_high 7 --defocus_max 8 --perdevice 4
WarpTools ts_etomo_patches --settings warp_tiltseries.settings --angpix 10 --patch_size 250 --initial_axis 84.7 --perdevice 5
WarpTools ts_defocus_hand --settings warp_tiltseries.settings --check
WarpTools ts_reconstruct --settings warp_tiltseries.settings --angpix 10 --perdevice 4
