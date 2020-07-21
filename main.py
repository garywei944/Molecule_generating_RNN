no_gpu = True
train_model = False
generate_smile = True
no_warning = True

if no_warning:
    import os
    os.environ['TF_CPP_MIN_LOG_LEVEL']='3'

if no_gpu:
    import os
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICES"] = ""

if train_model:
    # TODO
    pass

if generate_smile:
    # TODO
    pass
