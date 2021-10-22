plc-log-timestamps
==================

Compare PLC-provided timestamps to what logstash sees.


Usage
=====

```bash
$ pip install -r requirements.txt
```


```bash
$ python timestamp_compare.py
HXX_VONHAMOS                  :     2461 messages; mean=   0.002 min=   0.000 max=   0.103 std=   0.006
KFE-MOTION                    :      160 messages; mean=  11.591 min=  -9.546 max= 247.564 std=  59.786
KFE-RIX-MOTION                :       25 messages; mean= 366.266 min=   0.001 max= 450.126 std= 159.941
LFE-MOTION                    :     1157 messages; mean=   1.340 min=  -5.368 max= 203.620 std=  31.583
LFE-OPTICS                    :      172 messages; mean= 408.598 min= 400.759 max= 418.809 std=   6.726
PLC-CRIX-MOT                  :      356 messages; mean=   0.002 min=   0.001 max=   0.005 std=   0.001
PLC-CRIX-VAC                  :       52 messages; mean=   0.002 min=   0.001 max=   0.003 std=   0.001
PLC-KFE-ARBITER               :       45 messages; mean=  -7.602 min=-152.878 max=  15.971 std=  36.619
PLC-KFE-GATT                  :      103 messages; mean= 417.712 min=   0.002 max= 443.696 std=  72.748
PLC-KFE-GMD-VAC               :      158 messages; mean=   0.435 min=   0.000 max=   0.894 std=   0.435
PLC-KFE-VAC-01                :      846 messages; mean=   2.525 min= -15.755 max= 159.175 std=  49.662
PLC-LAS-BTS                   :       18 messages; mean= 232.150 min= 231.719 max= 232.387 std=   0.254
PLC-LFE-ARBITER               :       16 messages; mean= 354.143 min= 343.958 max= 369.259 std=   7.387
PLC-RIX-VAC                   :     2007 messages; mean=  -5.240 min= -16.886 max=  89.614 std=   9.095
PLC-XRT-HOMS                  :        4 messages; mean=-369.304 min=-376.054 max=-362.555 std=   6.749
RIXS-OPTICS                   :       20 messages; mean=   7.022 min=   6.406 max=   7.239 std=   0.211
SDS-RAPTOR                    :       28 messages; mean=   0.001 min=   0.000 max=   0.002 std=   0.000
SDS-SABERTOOTH                :       23 messages; mean=   0.002 min=   0.001 max=   0.003 std=   0.001
TMO-MOTION                    :       22 messages; mean= 249.454 min=   0.001 max= 277.848 std=  78.946
TMO-OPTICS                    :        9 messages; mean=   0.002 min=   0.002 max=   0.003 std=   0.000
ctl-logsrv02                  :       56 messages; mean=   5.836 min=   0.001 max=  14.066 std=   4.239
plc-mfx-motion                :       22 messages; mean=   0.002 min=   0.001 max=   0.002 std=   0.000
plc-mfx-sds                   :       32 messages; mean=   0.002 min=   0.001 max=   0.015 std=   0.002
plc-tst-proto2                :     2208 messages; mean= 252.996 min=-1419.196 max=32442.323 std=2572.635
```

(and associated plot)
