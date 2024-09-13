from datetime import datetime
import numpy as np

flight_scalars = {
    "1_1": [
        2.108136251,
        0.7272650279
    ],
    "1_2": [
        1.890624168,
        0.7995495579
    ],
    "1_3": [
        1.735700817,
        0.8105189508
    ],
    "1_4": [
        2.029790534,
        0.7294698956
    ],
    "1_5": [
        2.109553225,
        0.7659221397
    ],
    "1_6": [
        1.357624921,
        0.8240067484
    ],
    "1_7": [
        0.7149054897,
        0.103414145
    ],
    "1_8": [
        0.6139711659,
        0.1114409079
    ],
    "1_9": [
        0.6432764489,
        0.09889512399
    ],
    "1_10": [
        0.7947045883,
        0.182680768
    ],
    "1_11": [
        0.8042774788,
        0.1270447397
    ],
    "1_12": [
        1.037199687,
        0.1275470197
    ],
    "1_13": [
        0.7958353237,
        0.1653721479
    ],
    "1_14": [
        0.6017045549,
        0.1091846253
    ],
    "1_15": [
        0.5585397816,
        0.07870712662
    ],
    "1_16": [
        0.7240336266,
        0.1898268205
    ],
    "1_17": [
        0.8664195169,
        0.2891467659
    ],
    "1_18": [
        0.7564000204,
        0.1301774032
    ],
    "1_19": [
        1.163621789,
        0.1834622909
    ],
    "1_20": [
        1.221159785,
        0.1405208039
    ],
    "1_21": [
        0.7615802516,
        0.1801799985
    ],
    "1_22": [
        0.6149700762,
        0.1024641888
    ],
    "1_23": [
        0.5770710245,
        0.07462690507
    ],
    "1_24": [
        0.5908037398,
        0.1192420516
    ],
    "1_25": [
        0.6099300117,
        0.08381573787
    ],
    "1_26": [
        0.9364977679,
        0.1352096224
    ],
    "1_27": [
        0.6926029227,
        0.1044912001
    ],
    "1_28": [
        0.5413986282,
        0.06059653178
    ],
    "1_29": [
        0.5347598269,
        0.06152924031
    ],
    "1_30": [
        0.5805817772,
        0.08132436293
    ],
    "1_31": [
        0.6105317791,
        0.119687006
    ],
    "2_1": [
        0.7567667562,
        0.1857750496
    ],
    "2_2": [
        0.8820843409,
        0.115133391
    ],
    "2_3": [
        0.6698894517,
        0.07337558466
    ],
    "2_4": [
        0.5310880007,
        0.05814215037
    ],
    "2_5": [
        0.5374066742,
        0.065512672
    ],
    "2_6": [
        0.5761100701,
        0.0771608009
    ],
    "2_7": [
        0.6101416054,
        0.1008135014
    ],
    "2_8": [
        0.6708135909,
        0.177535648
    ],
    "2_9": [
        0.8962751001,
        0.1407860483
    ],
    "2_10": [
        0.7532085724,
        0.1161589562
    ],
    "2_11": [
        0.6265632618,
        0.1969552619
    ],
    "2_12": [
        0.6465549459,
        0.1372671114
    ],
    "2_13": [
        0.7176049399,
        0.1256648382
    ],
    "2_14": [
        0.8021754003,
        0.1611010068
    ],
    "2_15": [
        0.7435088412,
        0.184730781
    ],
    "2_16": [
        1.157487771,
        0.1864486906
    ],
    "2_17": [
        1.34807893,
        0.1623339863
    ],
    "2_18": [
        0.7363726005,
        0.146080286
    ],
    "2_19": [
        0.6732884495,
        0.1597562404
    ],
    "2_20": [
        0.8889633614,
        0.1260286742
    ],
    "2_21": [
        1.181283244,
        0.1227394841
    ],
    "2_22": [
        1.523787395,
        0.1243327206
    ],
    "2_23": [
        1.785250786,
        0.133531836
    ],
    "2_24": [
        1.188119912,
        0.1227552309
    ],
    "2_25": [
        0.6493114113,
        0.1107838859
    ],
    "2_26": [
        0.638357862,
        0.1045300158
    ],
    "2_27": [
        0.7713003701,
        0.1673350618
    ],
    "2_28": [
        0.8651232917,
        0.1572229714
    ],
    "3_1": [
        0.911705967,
        0.1550512584
    ],
    "3_2": [
        1.160115287,
        0.1334960793
    ],
    "3_3": [
        0.863345904,
        0.1110259926
    ],
    "3_4": [
        0.6475219987,
        0.1268627806
    ],
    "3_5": [
        0.6889578532,
        0.1537833552
    ],
    "3_6": [
        0.8376467291,
        0.1701063122
    ],
    "3_7": [
        1.151606463,
        0.1810169929
    ],
    "3_8": [
        1.16360696,
        0.1898812379
    ],
    "3_9": [
        1.230542727,
        0.1420387594
    ],
    "3_10": [
        0.8707143958,
        0.1263098659
    ],
    "3_11": [
        0.7075782585,
        0.1691688084
    ],
    "3_12": [
        0.7421051668,
        0.2175388713
    ],
    "3_13": [
        0.9791257891,
        0.2219326106
    ],
    "3_14": [
        1.210027914,
        0.2549679373
    ],
    "3_15": [
        1.271378701,
        0.1959918007
    ],
    "3_16": [
        1.313885921,
        0.146998665
    ],
    "3_17": [
        0.9670421763,
        0.1416190488
    ],
    "3_18": [
        0.689630037,
        0.1548858737
    ],
    "3_19": [
        0.6782640198,
        0.1580740542
    ],
    "3_20": [
        0.8945344607,
        0.1852332253
    ],
    "3_21": [
        1.153559082,
        0.182904719
    ],
    "3_22": [
        1.217569874,
        0.1853503414
    ],
    "3_23": [
        1.240472805,
        0.1241975286
    ],
    "3_24": [
        0.929083702,
        0.1301763278
    ],
    "3_25": [
        0.6900883442,
        0.1343240552
    ],
    "3_26": [
        0.7736978448,
        0.192541265
    ],
    "3_27": [
        0.9145977373,
        0.1783832807
    ],
    "3_28": [
        1.154467364,
        0.1896690562
    ],
    "3_29": [
        1.237459844,
        0.1969741858
    ],
    "3_30": [
        1.685857951,
        0.7328988561
    ],
    "3_31": [
        1.393683218,
        0.7625196124
    ],
    "4_1": [
        1.099485387,
        0.7550867811
    ],
    "4_2": [
        1.087379531,
        0.7677226728
    ],
    "4_3": [
        1.313203859,
        0.7559575144
    ],
    "4_4": [
        1.448314487,
        0.7403853671
    ],
    "4_5": [
        1.458206418,
        0.6400268603
    ],
    "4_6": [
        1.618423735,
        0.6268350674
    ],
    "4_7": [
        1.28863326,
        0.6311460282
    ],
    "4_8": [
        1.058712611,
        0.6408985382
    ],
    "4_9": [
        1.065258573,
        0.6666344637
    ],
    "4_10": [
        1.274368846,
        0.6586256507
    ],
    "4_11": [
        1.357548067,
        0.6358400633
    ],
    "4_12": [
        1.453351734,
        0.6343921186
    ],
    "4_13": [
        1.629389501,
        0.6188042937
    ],
    "4_14": [
        1.272598333,
        0.641319548
    ],
    "4_15": [
        1.025240595,
        0.629923292
    ],
    "4_16": [
        1.072253928,
        0.624359482
    ],
    "4_17": [
        1.391617649,
        0.6654357448
    ],
    "4_18": [
        1.464005766,
        0.6572602817
    ],
    "4_19": [
        1.540227561,
        0.6117333306
    ],
    "4_20": [
        1.758714157,
        0.600052804
    ],
    "4_21": [
        1.519765788,
        0.6190525344
    ],
    "4_22": [
        1.045426987,
        0.654892965
    ],
    "4_23": [
        0.9842465875,
        0.6741394539
    ],
    "4_24": [
        1.183750461,
        0.6413611018
    ],
    "4_25": [
        1.152110127,
        0.669711123
    ],
    "4_26": [
        1.220232711,
        0.6154004567
    ],
    "4_27": [
        1.592718553,
        0.6158715167
    ],
    "4_28": [
        1.25243121,
        0.6504105161
    ],
    "4_29": [
        1.161091688,
        0.7543428379
    ],
    "4_30": [
        0.820430896,
        0.1453268394
    ],
    "5_1": [
        0.89410543,
        0.1370218134
    ],
    "5_2": [
        0.9121154467,
        0.1784039407
    ],
    "5_3": [
        0.9239194735,
        0.1439823111
    ],
    "5_4": [
        1.23207088,
        0.1588979206
    ],
    "5_5": [
        1.028500688,
        0.1496265498
    ],
    "5_6": [
        0.7840951946,
        0.1429228365
    ],
    "5_7": [
        0.7938698146,
        0.1340408348
    ],
    "5_8": [
        0.9554481807,
        0.159602454
    ],
    "5_9": [
        0.9229919944,
        0.1433125045
    ],
    "5_10": [
        0.9500327814,
        0.1519538697
    ],
    "5_11": [
        1.237344679,
        0.1555172242
    ],
    "5_12": [
        0.9345898381,
        0.1200059762
    ],
    "5_13": [
        0.8142134735,
        0.1297053311
    ],
    "5_14": [
        0.9238334164,
        0.1917987658
    ],
    "5_15": [
        1.154220531,
        0.1540575555
    ],
    "5_16": [
        1.116812498,
        0.1474836505
    ],
    "5_17": [
        1.020576681,
        0.1590479021
    ],
    "5_18": [
        1.370054211,
        0.1534351804
    ],
    "5_19": [
        0.9684795207,
        0.1290770343
    ],
    "5_20": [
        0.7895233054,
        0.1385925869
    ],
    "5_21": [
        0.9117700227,
        0.1644648834
    ],
    "5_22": [
        1.251001558,
        0.1655841433
    ],
    "5_23": [
        1.251707913,
        0.1602477562
    ],
    "5_24": [
        0.9734151727,
        0.1538359914
    ],
    "5_25": [
        1.247554352,
        0.200063953
    ],
    "5_26": [
        1.647416879,
        0.1611077095
    ],
    "5_27": [
        1.056721195,
        0.1187474278
    ],
    "5_28": [
        0.8330550754,
        0.1237361961
    ],
    "5_29": [
        0.959652855,
        0.1641334546
    ],
    "5_30": [
        0.9811905421,
        0.1542286403
    ],
    "5_31": [
        1.009536062,
        0.1835528024
    ],
    "6_1": [
        1.277866979,
        0.1692436907
    ],
    "6_2": [
        0.9509511645,
        0.1386784382
    ],
    "6_3": [
        0.7954018699,
        0.1444532609
    ],
    "6_4": [
        0.8637401171,
        0.1523449046
    ],
    "6_5": [
        0.9309810116,
        0.1344539442
    ],
    "6_6": [
        0.9631913891,
        0.1546095277
    ],
    "6_7": [
        1.020381348,
        0.1587770906
    ],
    "6_8": [
        1.239561026,
        0.1502745371
    ],
    "6_9": [
        0.9214162797,
        0.1412446522
    ],
    "6_10": [
        0.8051539912,
        0.1276219786
    ],
    "6_11": [
        0.9163851351,
        0.1640622737
    ],
    "6_12": [
        0.9436855247,
        0.1424517815
    ],
    "6_13": [
        0.9834027341,
        0.1557056429
    ],
    "6_14": [
        1.051484915,
        0.1818582106
    ],
    "6_15": [
        1.175105895,
        0.1533210897
    ],
    "6_16": [
        0.9586868846,
        0.1532097411
    ],
    "6_17": [
        0.8575271452,
        0.1592404198
    ],
    "6_18": [
        0.8689503457,
        0.1472656686
    ],
    "6_19": [
        1.231429633,
        0.1917192135
    ],
    "6_20": [
        1.136532353,
        0.1597228279
    ],
    "6_21": [
        1.028946608,
        0.1633978419
    ],
    "6_22": [
        1.244967652,
        0.1473737692
    ],
    "6_23": [
        0.8924462253,
        0.1496977127
    ],
    "6_24": [
        0.7600268402,
        0.1337017511
    ],
    "6_25": [
        0.8179446889,
        0.136849228
    ],
    "6_26": [
        1.226921152,
        0.183610945
    ],
    "6_27": [
        1.225696627,
        0.1720093318
    ],
    "6_28": [
        1.053971883,
        0.1691046788
    ],
    "6_29": [
        1.173681605,
        0.1467876544
    ],
    "6_30": [
        0.8670018856,
        0.1541849607
    ],
    "7_1": [
        0.7883654769,
        0.1758045702
    ],
    "7_2": [
        0.7791526992,
        0.1403430592
    ],
    "7_3": [
        1.048279384,
        0.1427147384
    ],
    "7_4": [
        0.9100179105,
        0.1699823196
    ],
    "7_5": [
        1.069923288,
        0.1956496243
    ],
    "7_6": [
        1.672164448,
        0.1590543091
    ],
    "7_7": [
        1.076623015,
        0.1578239841
    ],
    "7_8": [
        0.8098454284,
        0.1583667617
    ],
    "7_9": [
        1.149166545,
        0.1594647896
    ],
    "7_10": [
        1.228845607,
        0.1593005938
    ],
    "7_11": [
        1.261192112,
        0.1599023371
    ],
    "7_12": [
        1.109323801,
        0.160052219
    ],
    "7_13": [
        1.223772098,
        0.1592734336
    ],
    "7_14": [
        1.013857461,
        0.1594860173
    ],
    "7_15": [
        0.836745124,
        0.15971017
    ],
    "7_16": [
        0.9959108834,
        0.1597269468
    ],
    "7_17": [
        1.014808869,
        0.2029709772
    ],
    "7_18": [
        1.011697971,
        0.2030131625
    ],
    "7_19": [
        1.186963048,
        0.203321422
    ],
    "7_20": [
        0.9346660234,
        0.2035549853
    ],
    "7_21": [
        1.067496243,
        0.2035999601
    ],
    "7_22": [
        1.356534904,
        0.2040178506
    ],
    "7_23": [
        1.011687415,
        0.204308022
    ],
    "7_24": [
        1.14925319,
        0.2045344616
    ],
    "7_25": [
        0.9594720714,
        0.2045680112
    ],
    "7_26": [
        1.00713773,
        0.2045976127
    ],
    "7_27": [
        1.282834433,
        0.204644713
    ],
    "7_28": [
        1.129161803,
        0.2072000974
    ],
    "7_29": [
        1.199749546,
        0.2100218338
    ],
    "7_30": [
        1.237522655,
        0.2129702384
    ],
    "7_31": [
        1.108027325,
        0.2159746798
    ],
    "8_1": [
        1.401189262,
        0.2187760091
    ],
    "8_2": [
        1.228593113,
        0.2216261376
    ],
    "8_3": [
        1.269079929,
        0.2246894478
    ],
    "8_4": [
        1.26303468,
        0.2278927577
    ],
    "8_5": [
        1.018583113,
        0.2312308391
    ],
    "8_6": [
        1.140316773,
        0.1299320143
    ],
    "8_7": [
        1.319903137,
        0.1311849831
    ],
    "8_8": [
        1.206277126,
        0.1303224198
    ],
    "8_9": [
        0.8943196112,
        0.1286330919
    ],
    "8_10": [
        1.170241162,
        0.1283556318
    ],
    "8_11": [
        0.8016850653,
        0.1276805422
    ],
    "8_12": [
        1.05312335,
        0.1264786371
    ],
    "8_13": [
        0.9397050277,
        0.1268087351
    ],
    "8_14": [
        1.193587865,
        0.1229660461
    ],
    "8_15": [
        0.7860968979,
        0.122219051
    ],
    "8_16": [
        0.8019008939,
        0.1209111611
    ],
    "8_17": [
        1.05435085,
        0.1227158851
    ],
    "8_18": [
        0.9057121383,
        0.122410481
    ],
    "8_19": [
        1.009500718,
        0.1213529036
    ],
    "8_20": [
        0.9087563289,
        0.1218309954
    ],
    "8_21": [
        1.180774975,
        0.1252594883
    ],
    "8_22": [
        1.066287791,
        0.1235901028
    ],
    "8_23": [
        0.9595521446,
        0.1224324521
    ],
    "8_24": [
        1.388388397,
        0.1240466468
    ],
    "8_25": [
        1.153445271,
        0.1232090314
    ],
    "8_26": [
        1.123393946,
        0.1648757734
    ],
    "8_27": [
        0.8316765358,
        0.1582178983
    ],
    "8_28": [
        0.9348312585,
        0.1827608587
    ],
    "8_29": [
        1.270455851,
        0.1631001692
    ],
    "8_30": [
        1.30020685,
        0.1440915779
    ],
    "8_31": [
        1.254136027,
        0.1425386179
    ],
    "9_1": [
        1.327977101,
        0.1549241419
    ],
    "9_2": [
        1.444510262,
        0.1455589432
    ],
    "9_3": [
        0.7769076053,
        0.0968356567
    ],
    "9_4": [
        0.5893105112,
        0.09072855591
    ],
    "9_5": [
        0.5621988267,
        0.07769946251
    ],
    "9_6": [
        0.6119034956,
        0.11647635
    ],
    "9_7": [
        0.6468749001,
        0.1476081662
    ],
    "9_8": [
        0.9214438978,
        0.1712799856
    ],
    "9_9": [
        0.631307515,
        0.1027203921
    ],
    "9_10": [
        0.5149398056,
        0.07457459988
    ],
    "9_11": [
        0.5450876021,
        0.119476909
    ],
    "9_12": [
        0.6506551274,
        0.1060776766
    ],
    "9_13": [
        0.5873664362,
        0.08801767234
    ],
    "9_14": [
        0.6771213074,
        0.1373718706
    ],
    "9_15": [
        1.0,
        0.0
    ],
    "9_16": [
        0.6762235208,
        0.09831520617
    ],
    "9_17": [
        0.5267466243,
        0.07905868303
    ],
    "9_18": [
        0.5946810182,
        0.1804670534
    ],
    "9_19": [
        0.6418299907,
        0.1126375511
    ],
    "9_20": [
        0.5968611767,
        0.08751042636
    ],
    "9_21": [
        0.6896011348,
        0.1371299344
    ],
    "9_22": [
        1.013212792,
        0.2349712594
    ],
    "9_23": [
        0.5664297016,
        0.07016976648
    ],
    "9_24": [
        0.5201501091,
        0.08538763188
    ],
    "9_25": [
        0.5452188446,
        0.175700876
    ],
    "9_26": [
        0.6198402815,
        0.09640533806
    ],
    "9_27": [
        0.5980318982,
        0.09272538079
    ],
    "9_28": [
        0.6830315053,
        0.1477617277
    ],
    "9_29": [
        0.894027064,
        0.1308787687
    ],
    "9_30": [
        0.6322836971,
        0.1059973181
    ],
    "10_1": [
        0.5557530641,
        0.08414354457
    ],
    "10_2": [
        0.6207697906,
        0.1930880907
    ],
    "10_3": [
        0.614528773,
        0.1016124193
    ],
    "10_4": [
        0.6296340209,
        0.0994351121
    ],
    "10_5": [
        0.6479572596,
        0.1146119422
    ],
    "10_6": [
        0.9650241661,
        0.1418949849
    ],
    "10_7": [
        0.5936093227,
        0.09535008619
    ],
    "10_8": [
        0.4983547159,
        0.07199491638
    ],
    "10_9": [
        0.5416947097,
        0.09553372448
    ],
    "10_10": [
        0.7585803368,
        0.1392743654
    ],
    "10_11": [
        0.7712343078,
        0.1397364526
    ],
    "10_12": [
        0.702107248,
        0.1397018179
    ],
    "10_13": [
        0.9083863275,
        0.1494940902
    ],
    "10_14": [
        0.8590227079,
        0.1208160351
    ],
    "10_15": [
        0.558091186,
        0.08794080867
    ],
    "10_16": [
        0.56439767,
        0.07645466832
    ],
    "10_17": [
        0.6691546197,
        0.1020998062
    ],
    "10_18": [
        0.6660949563,
        0.1229366696
    ],
    "10_19": [
        0.8143627673,
        0.1262911681
    ],
    "10_20": [
        1.385246391,
        0.1949598525
    ],
    "10_21": [
        0.9204116908,
        0.1620689526
    ],
    "10_22": [
        0.5204394914,
        0.07621997365
    ],
    "10_23": [
        0.5088919289,
        0.07458175875
    ],
    "10_24": [
        0.6152620644,
        0.1216596374
    ],
    "10_25": [
        0.6763071483,
        0.1275286496
    ],
    "10_26": [
        0.7008336366,
        0.1407457422
    ],
    "10_27": [
        0.8673110163,
        0.1177519466
    ],
    "10_28": [
        0.5953720657,
        0.07459311641
    ],
    "10_29": [
        0.5081709617,
        0.08969547773
    ],
    "10_30": [
        0.4932060273,
        0.07497266595
    ],
    "10_31": [
        0.6233514489,
        0.1206421458
    ],
    "11_1": [
        0.556367246,
        0.1057886386
    ],
    "11_2": [
        0.6244143192,
        0.1172115086
    ],
    "11_3": [
        0.7958624169,
        0.132947822
    ],
    "11_4": [
        0.5625421667,
        0.104470267
    ],
    "11_5": [
        0.5093837129,
        0.07245018244
    ],
    "11_6": [
        0.5222917764,
        0.07768825159
    ],
    "11_7": [
        0.5992704289,
        0.088292982
    ],
    "11_8": [
        0.6304473078,
        0.1208588735
    ],
    "11_9": [
        0.6654720648,
        0.1282009097
    ],
    "11_10": [
        0.9340158584,
        0.1660907112
    ],
    "11_11": [
        0.6983775927,
        0.1057586612
    ],
    "11_12": [
        0.533339015,
        0.0856375853
    ],
    "11_13": [
        0.5786048679,
        0.1141012341
    ],
    "11_14": [
        0.5635650185,
        0.09136227452
    ],
    "11_15": [
        0.6250416746,
        0.1087236519
    ],
    "11_16": [
        0.6970925986,
        0.1396747006
    ],
    "11_17": [
        0.8853715312,
        0.1546164097
    ],
    "11_18": [
        0.5938699481,
        0.1001210745
    ],
    "11_19": [
        0.5406285897,
        0.0960654607
    ],
    "11_20": [
        0.6698617222,
        0.1498507869
    ],
    "11_21": [
        1.019699123,
        0.2143023205
    ],
    "11_22": [
        1.309692387,
        0.1824416791
    ],
    "11_23": [
        1.17086144,
        0.1912634665
    ],
    "11_24": [
        1.004242615,
        0.1577804453
    ],
    "11_25": [
        0.8810207086,
        0.1625378864
    ],
    "11_26": [
        1.036202471,
        0.1853051265
    ],
    "11_27": [
        0.9609687717,
        0.216404072
    ],
    "11_28": [
        0.7840194846,
        0.2104324537
    ],
    "11_29": [
        1.12262585,
        0.2244910166
    ],
    "11_30": [
        2.058222723,
        0.2920248831
    ],
    "12_1": [
        2.130072087,
        0.1453109099
    ],
    "12_2": [
        1.326736113,
        0.1501089588
    ],
    "12_3": [
        0.5493456,
        0.07894939324
    ],
    "12_4": [
        0.5899191205,
        0.1346877892
    ],
    "12_5": [
        0.6777369024,
        0.1767174091
    ],
    "12_6": [
        0.6480515399,
        0.1496972829
    ],
    "12_7": [
        0.6921354494,
        0.2287419614
    ],
    "12_8": [
        0.8650957833,
        0.2702092503
    ],
    "12_9": [
        0.6873507228,
        0.1084495657
    ],
    "12_10": [
        0.5999784274,
        0.1429723679
    ],
    "12_11": [
        0.5627978401,
        0.09819774417
    ],
    "12_12": [
        0.6149985021,
        0.1308929036
    ],
    "12_13": [
        0.6905185418,
        0.1709234627
    ],
    "12_14": [
        0.699101718,
        0.1230060661
    ],
    "12_15": [
        0.8539245988,
        0.1424312127
    ],
    "12_16": [
        0.6728987168,
        0.1125308471
    ],
    "12_17": [
        0.6353384849,
        0.1548080489
    ],
    "12_18": [
        0.6490429118,
        0.1287655452
    ],
    "12_19": [
        1.32031741,
        0.18192610052
    ],
    "12_20": [
        1.788754096,
        0.1831686001
    ],
    "12_21": [
        1.714915089,
        0.18620644734
    ],
    "12_22": [
        1.565375036,
        0.18695159245
    ],
    "12_23": [
        1.37367605,
        0.18252437628
    ],
    "12_24": [
        1.0661342,
        0.18355497037
    ],
    "12_25": [
        1.23836826,
        0.18311851466
    ],
    "12_26": [
        1.843001582,
        0.18481232805
    ],
    "12_27": [
        1.862788968,
        0.18622948564
    ],
    "12_28": [
        1.80636659,
        0.18701835077
    ],
    "12_29": [
        1.726335638,
        0.18534553598
    ],
    "12_30": [
        1.708211049,
        0.17791161859
    ],
    "12_31": [
        1.537303063,
        0.18083490921
    ]
}

def generate_scalars(date_string, flight_result_len):

    # Convert the string to a datetime object
    date_obj = datetime.strptime(date_string, "%Y-%m-%d")

    # Extract month and day
    month = date_obj.month
    day = date_obj.day

    key = str(month) + "_" + str(day)

    if(key=="9_15"):
        return [1.0] * flight_result_len

    elif(key in flight_scalars):
        return list(np.round(np.random.normal(flight_scalars[key][0], flight_scalars[key][1], size=flight_result_len),2))

    else:
        return [1.0] * flight_result_len