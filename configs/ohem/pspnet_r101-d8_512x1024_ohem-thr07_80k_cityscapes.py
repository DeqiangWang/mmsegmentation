_base_ = '../pspnet/pspnet_r101-d8_512x1024_80k_cityscapes.py'
model = dict(
    decode_head=dict(
        sampler=dict(type='OHEMPixelSampler', thresh=0.7, min_kept=100000)))
