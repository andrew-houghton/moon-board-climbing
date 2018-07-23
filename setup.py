from training_utils import decompress, prep_lstm, prep_hypergan

print('Decompressing climb data.')
decompress.main()

print('Converting climb data to LSTM input format.')
prep_lstm.main()

print('Creating images for the hypergan to train on.')
prep_hypergan.main()

print('Finished preparing datasets for training.')
