import nmrglue as ng
import numpy as np
import os
import scipy.io as scio

train_num_samp = 10000


train_path_350 = "C:/Users/s4548361/Desktop/LW_MRS_NOISE_FREE/train_dataset_350_noise_free/"
mask_path = 'C:/Users/s4548361/Desktop/T_10000_350_64/'

data_path = 'C:/Users/s4548361/Desktop/T_10000_350_64/'
if not os.path.exists(train_path_350):
    os.makedirs(train_path_350)



# for i in range(train_num_samp):
#     ### Extract real mask
#     _, data = ng.fileio.rnmrtk.read(
#         mask_path + '1D_Time_Full/IN_TF_C_' + str(i+1) + '.sec')
#
#     # _, noise_free_data = ng.fileio.rnmrtk.read(
#     #     data_path + '1D_Time_Full_NL/IN_TF_C_' + str(i + 1) + '.sec')
#
#     _, data_sub = ng.fileio.rnmrtk.read(
#         mask_path + '1D_Time_Subset/IN_TS_C_' + str(i+1) + '.sec')
#
#     mask = data - data_sub
#
#     for a in range(len(mask)):
#         if data_sub[a] == 0j:
#             mask[a] = 0
#         else:
#             mask[a] = 1
#     mask = np.real(mask)
#
#     ### Normalization
#
#     _, data = ng.fileio.rnmrtk.read(
#         data_path + '1D_Time_Full/IN_TF_C_' + str(i+1) + '.sec')
#
#     # _, noise_free_data = ng.fileio.rnmrtk.read(
#     #     data_path + '1D_Time_Full_NL/IN_TF_C_' + str(i + 1) + '.sec')
#
#     _, data_sub = ng.fileio.rnmrtk.read(
#         data_path + '1D_Time_Subset/IN_TS_C_' + str(i+1) + '.sec')
#
#     data_sub[0] = 0.5 * data_sub[0]
#
#     data[0] = 0.5 * data[0]
#     ## Normalization
#     abs_data = np.absolute(data)
#
#     _range = max(abs_data)
#
#     data = data / _range
#
#
#
#     os.chdir(train_path_350)
#     scio.savemat('train_data_' + str(i+1) + '.mat', {'real': np.real(data), 'imag': np.imag(data), 'mask': mask})

for i in range(train_num_samp):
    ### Extract real mask
    _, data = ng.fileio.rnmrtk.read(
        mask_path + '1D_Time_Full/IN_TF_C_' + str(i+1) + '.sec')

    # _, noise_free_data = ng.fileio.rnmrtk.read(
    #     data_path + '1D_Time_Full_NL/IN_TF_C_' + str(i + 1) + '.sec')

    _, data_sub = ng.fileio.rnmrtk.read(
        mask_path + '1D_Time_Subset/IN_TS_C_' + str(i+1) + '.sec')

    mask = data - data_sub

    for a in range(len(mask)):
        if data_sub[a] == 0j:
            mask[a] = 0
        else:
            mask[a] = 1
    mask = np.real(mask)

    ### Normalization

    _, data = ng.fileio.rnmrtk.read(
        data_path + '1D_Time_Full_NL/IN_TF_C_' + str(i+1) + '.sec')

    # _, noise_free_data = ng.fileio.rnmrtk.read(
    #     data_path + '1D_Time_Full_NL/IN_TF_C_' + str(i + 1) + '.sec')

    # _, data_sub = ng.fileio.rnmrtk.read(
    #     data_path + '1D_Time_Subset/IN_TS_C_' + str(i+1) + '.sec')

    # data_sub[0] = 0.5 * data_sub[0]

    data[0] = 0.5 * data[0]
    ## Normalization
    abs_data = np.absolute(data)

    _range = max(abs_data)

    data = data / _range
    data_sub = data * mask



    os.chdir(train_path_350)
    scio.savemat('train_data_' + str(i+1) + '.mat', {'real': np.real(data), 'imag': np.imag(data),
                                                     'mask': mask})

# path2 = 'C:/Users/s4548361/Desktop/ML_test_data_easy_hsqc.tar/ML_test_data_easy_hsqc/Exp_Easy_HSQC/Raw_data/Subsampled/f2_proc_sub.sec'
#
#
# _, data = ng.fileio.rnmrtk.read(path2)
# data = np.transpose(data)
#
# data = data[:, 0::2] + 1j * data[:, 1::2]
# data = np.fft.fftshift(np.fft.fft(data, axis=-1), -1)
# data = np.transpose(data)
# scio.savemat('Sub_test.mat', {'sub_data': data})

print('Done')

