from training_utils import decompress, load_json_climbs

print('Decompressing climb data.')
decompress.main()

print('Converting climb data to LSTM input format.')
load_json_climbs.main()

print('Finished preparing datasets for training.')
