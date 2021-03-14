import json

buildings = ["HEADQUARTER", "BARRACKS", "STABLE", "WORKSHOP", "ACADEMY", "SMITHY", "RALLY_POINT", "STATUE", "MARKET",
             "TIMBER_CAMP", "CLAY_PIT", "IRON_MINE", "FARM", "WAREHOUSE", "HIDING_PLACE", "WALL"]

requirements = [
    {},
    {"HEADQUARTER": 3},
    {"HEADQUARTER": 10, "BARRACKS": 5, "SMITHY": 5},
    {"HEADQUARTER": 10, "SMITHY": 10},
    {"HEADQUARTER": 20, "SMITHY": 20, "MARKET": 10},
    {"HEADQUARTER": 5, "BARRACKS": 1},
    {},
    {},
    {"HEADQUARTER": 3, "WAREHOUSE": 2},
    {},
    {},
    {},
    {},
    {},
    {},
    {"BARRACKS": 1}
]

levels = [
    [
        [[90, 80, 70, 5], 0.95],
        [[113, 102, 88, 1], 0.91],
        [[143, 130, 111, 1], 0.86],
        [[180, 166, 140, 1], 0.82],
        [[227, 211, 176, 1], 0.78],
        [[286, 270, 222, 2], 0.75],
        [[360, 344, 280, 2], 0.71],
        [[454, 438, 353, 2], 0.68],
        [[572, 559, 445, 3], 0.64],
        [[720, 712, 560, 3], 0.61],
        [[908, 908, 706, 3], 0.58],
        [[1144, 1158, 890, 4], 0.56],
        [[1441, 1476, 1121, 5], 0.53],
        [[1816, 1882, 1412, 5], 0.51],
        [[2288, 2400, 1779, 7], 0.48],
        [[2883, 3060, 2242, 8], 0.46],
        [[3632, 3902, 2825, 9], 0.44],
        [[4577, 4975, 3560, 10], 0.42],
        [[5767, 6343, 4485, 12], 0.40],
        [[7266, 8087, 5651, 15], 0.38],
        [[9155, 10, 311, 7120, 17], 0.36],
        [[11535, 13146, 8972, 19], 0.34],
        [[14534, 16762, 11304, 23], 0.33],
        [[18313, 21371, 14244, 27], 0.31],
        [[23075, 27248, 17947, 31], 0.30],
        [[29074, 34741, 22613, 37], 0.28],
        [[36633, 44295, 28493, 43], 0.27],
        [[46158, 56476, 35901, 51], 0.26],
        [[58159, 72007, 45235, 59], 0.24],
        [[73280, 91809, 56996, 69], 0.23]
    ],
    [
        [[200, 170, 90, 7], 0.63],
        [[252, 218, 113, 1], 0.59],
        [[318, 279, 143, 2], 0.56],
        [[400, 357, 180, 1], 0.53],
        [[504, 456, 227, 2], 0.50],
        [[635, 584, 286, 2], 0.47],
        [[800, 748, 360, 3], 0.44],
        [[1008, 957, 454, 3], 0.42],
        [[1271, 1225, 572, 4], 0.39],
        [[1601, 1568, 720, 4], 0.37],
        [[2017, 2007, 908, 5], 0.35],
        [[2542, 2569, 1144, 5], 0.33],
        [[3202, 3288, 1441, 7], 0.31],
        [[4035, 4209, 1816, 8], 0.29],
        [[5084, 5388, 2288, 9], 0.28],
        [[6406, 6896, 2883, 11], 0.26],
        [[8072, 8827, 3632, 12], 0.25],
        [[10170, 11298, 4577, 15], 0.23],
        [[12814, 14462, 5767, 17], 0.22],
        [[16146, 18511, 7266, 20], 0.21],
        [[20344, 23695, 9155, 24], 0.20],
        [[25634, 30329, 11535, 27], 0.19],
        [[32298, 38821, 14534, 32], 0.17],
        [[40696, 49691, 18313, 38], 0.16],
        [[51277, 63605, 23075, 44], 0.15]
    ],
    [
        [[270, 240, 260, 8], 0.63],
        [[340, 307, 328, 1], 0.59],
        [[429, 393, 413, 2], 0.56],
        [[540, 503, 520, 2], 0.53],
        [[681, 644, 655, 2], 0.5],
        [[857, 825, 826, 3], 0.47],
        [[1080, 1056, 1040, 3], 0.44],
        [[1361, 1351, 1311, 3], 0.42],
        [[1715, 1729, 1652, 4], 0.39],
        [[2161, 2214, 2081, 5], 0.37],
        [[2723, 2833, 2622, 5], 0.35],
        [[3431, 3627, 3304, 7], 0.33],
        [[4323, 4642, 4163, 8], 0.31],
        [[5447, 5942, 5246, 9], 0.29],
        [[6864, 7606, 6609, 10], 0.28],
        [[8648, 9736, 8328, 12], 0.26],
        [[10897, 12462, 10493, 15], 0.25],
        [[13730, 15951, 13221, 16], 0.23],
        [[17300, 20417, 16659, 20], 0.22],
        [[21797, 26134, 20990, 23], 0.21]
    ],
    [
        [[300, 240, 260, 8], 0.63],
        [[378, 307, 328, 1], 0.59],
        [[476, 393, 413, 2], 0.56],
        [[600, 503, 520, 2], 0.53],
        [[756, 644, 655, 2], 0.5],
        [[953, 825, 826, 3], 0.47],
        [[1200, 1056, 1040, 3], 0.44],
        [[1513, 1351, 1311, 3], 0.42],
        [[1906, 1729, 1652, 4], 0.39],
        [[2401, 2214, 2081, 5], 0.37],
        [[3026, 2833, 2622, 5], 0.35],
        [[3812, 3627, 3304, 7], 0.33],
        [[4804, 4642, 4163, 8], 0.31],
        [[6053, 5942, 5246, 9], 0.29],
        [[7626, 7606, 6609, 10], 0.28]
    ],
    [
        [[15000, 25000, 10000, 80], 0.63],
        [[30000, 50000, 20000, 14], 0.59],
        [[60000, 100000, 40000, 16], 0.56]
    ],
    [
        [[220, 180, 240, 20], 0.91],
        [[277, 230, 302, 3], 0.83],
        [[349, 293, 381, 4], 0.75],
        [[440, 373, 480, 5], 0.68],
        [[555, 476, 605, 5], 0.62],
        [[699, 606, 762, 7], 0.56],
        [[880, 773, 960, 7], 0.51],
        [[1109, 986, 1210, 9], 0.47],
        [[1398, 1257, 1525, 10], 0.42],
        [[1761, 1603, 1921, 12], 0.39],
        [[2219, 2043, 2421, 14], 0.35],
        [[2796, 2605, 3050, 16], 0.32],
        [[3523, 3322, 3843, 20], 0.29],
        [[4439, 4236, 4842, 22], 0.26],
        [[5593, 5400, 6101, 26], 0.24],
        [[7047, 6885, 7687, 31], 0.22],
        [[8879, 8779, 9686, 36], 0.2],
        [[11187, 11193, 12204, 42], 0.18],
        [[14096, 14271, 15377, 49], 0.16],
        [[17761, 18196, 19375, 57], 0.15]
    ],
    [
        [[10, 40, 30, 0], 1.0]
    ],
    [
        [[220, 220, 220, 10], 1.0]
    ],
    [
        [[100, 100, 100, 20], 1],
        [[126, 128, 126, 3], 2],
        [[159, 163, 159, 4], 3],
        [[200, 207, 200, 5], 4],
        [[252, 264, 252, 5], 5],
        [[318, 337, 318, 7], 6],
        [[400, 430, 400, 7], 7],
        [[504, 548, 504, 9], 8],
        [[635, 698, 635, 10], 9],
        [[800, 890, 800, 12], 10],
        [[1009, 1135, 1009, 14], 11],
        [[1271, 1447, 1271, 16], 14],
        [[1601, 1846, 1601, 20], 19],
        [[2018, 2353, 2018, 22], 26],
        [[2542, 3000, 2542, 26], 35],
        [[3203, 3825, 3203, 31], 46],
        [[4036, 4877, 4036, 36], 59],
        [[5085, 6218, 5085, 42], 74],
        [[6407, 7928, 6407, 49], 91],
        [[8073, 10109, 8073, 57], 110],
        [[10172, 12889, 10172, 67], 131],
        [[12817, 16433, 12817, 79], 154],
        [[16149, 20952, 16149, 92], 179],
        [[20348, 26714, 20348, 107], 206],
        [[25639, 34060, 25639, 126], 235]
    ],
    [
        [[50, 60, 40, 5], 30],
        [[63, 77, 50, 1], 35],
        [[78, 98, 62, 1], 41],
        [[98, 124, 77, 1], 47],
        [[122, 159, 96, 1], 55],
        [[153, 202, 120, 1], 64],
        [[191, 258, 149, 2], 74],
        [[238, 329, 185, 2], 86],
        [[298, 419, 231, 2], 100],
        [[373, 534, 287, 2], 117],
        [[466, 681, 358, 3], 136],
        [[582, 868, 446, 3], 158],
        [[728, 1107, 555, 4], 184],
        [[909, 1412, 691, 5], 214],
        [[1137, 1800, 860, 5], 249],
        [[1421, 2295, 1071, 5], 289],
        [[1776, 2926, 1333, 7], 337],
        [[2220, 3731, 1659, 8], 391],
        [[2776, 4757, 2066, 9], 455],
        [[3469, 6065, 2572, 10], 530],
        [[4337, 7733, 3202, 12], 616],
        [[5421, 9860, 3987, 14], 717],
        [[6776, 12571, 4963, 16], 833],
        [[8470, 16028, 6180, 19], 969],
        [[10588, 20436, 7694, 21], 1127],
        [[13235, 26056, 9578, 24], 1311],
        [[16544, 33221, 11925, 29], 1525],
        [[20680, 42357, 14847, 33], 1774],
        [[25849, 54005, 18484, 38], 2063],
        [[32312, 68857, 23013, 43], 2400]
    ],
    [
        [[65, 50, 40, 10], 30],
        [[83, 63, 50, 1], 35],
        [[105, 80, 62, 2], 41],
        [[133, 101, 76, 2], 47],
        [[169, 128, 95, 2], 55],
        [[215, 162, 117, 2], 64],
        [[273, 205, 145, 3], 74],
        [[346, 259, 180, 3], 86],
        [[440, 328, 224, 4], 100],
        [[559, 415, 277, 4], 117],
        [[709, 525, 344, 4], 136],
        [[901, 664, 426, 5], 158],
        [[1.144, 840, 529, 6], 184],
        [[1.453, 1.062, 655, 7], 214],
        [[1.846, 1.343, 813, 8], 249],
        [[2.344, 1.700, 1.008, 8], 289],
        [[2.977, 2.150, 1.250, 10], 337],
        [[3.781, 2.720, 1.550, 12], 391],
        [[4.802, 3.440, 1.922, 13], 455],
        [[6.098, 4.352, 2.383, 15], 530],
        [[7.744, 5.505, 2.955, 16], 616],
        [[9.835, 6.964, 3.664, 20], 717],
        [[12.491, 8.810, 4.543, 22], 833],
        [[15.863, 11.144, 5.633, 25], 969],
        [[20.147, 14.098, 6.985, 28], 1127],
        [[25.586, 17.833, 8.662, 33], 1311],
        [[32.495, 22.559, 10.740, 37], 1525],
        [[41.268, 28.537, 13.318, 42], 1774],
        [[52.410, 36.100, 16.515, 48], 2063],
        [[66.561, 45.666, 20.478, 55], 2400]
    ],
    [
        [[75, 65, 70, 10], 30],
        [[94, 83, 87, 2], 35],
        [[118, 106, 108, 2], 41],
        [[147, 135, 133, 2], 47],
        [[184, 172, 165, 3], 55],
        [[231, 219, 205, 3], 64],
        [[289, 279, 254, 4], 74],
        [[362, 356, 316, 4], 86],
        [[453, 454, 391, 5], 100],
        [[567, 579, 485, 6], 117],
        [[710, 738, 602, 7], 136],
        [[889, 941, 746, 8], 158],
        [[1.113, 1.200, 925, 10], 184],
        [[1.393, 1.529, 1.147, 11], 214],
        [[1.744, 1.950, 1.422, 13], 249],
        [[2.183, 2.486, 1.764, 15], 289],
        [[2.734, 3.170, 2.187, 18], 337],
        [[3.422, 4.042, 2.712, 21], 391],
        [[4.285, 5.153, 3.363, 25], 455],
        [[5.365, 6.571, 4.170, 28], 530],
        [[6.717, 8.378, 5.170, 34], 616],
        [[8.409, 10.681, 6.411, 39], 717],
        [[10.528, 13.619, 7.950, 46], 833],
        [[13.181, 17.364, 9.858, 54], 969],
        [[16.503, 22.139, 12.224, 63], 1127],
        [[20.662, 28.227, 15.158, 74], 1311],
        [[25.869, 35.990, 18.796, 86], 1525],
        [[32.388, 45.887, 23.307, 100], 1774],
        [[40.549, 58.506, 28.900, 118], 2063],
        [[50.768, 74.595, 35.837, 138], 2400]
    ],
    [
        [[45, 40, 30, 0], 240],
        [[59, 53, 39, 0], 281],
        [[76, 70, 50, 0], 329],
        [[99, 92, 64, 0], 386],
        [[129, 121, 83, 0], 452],
        [[167, 160, 107, 0], 530],
        [[217, 212, 138, 0], 622],
        [[282, 279, 178, 0], 729],
        [[367, 369, 230, 0], 854],
        [[477, 487, 297, 0], 1002],
        [[620, 642, 383, 0], 1174],
        [[806, 848, 494, 0], 1376],
        [[1048, 1119, 637, 0], 1613],
        [[1363, 1477, 822, 0], 1891],
        [[1772, 1950, 1060, 0], 2216],
        [[2303, 2574, 1368, 0], 2598],
        [[2994, 3398, 1764, 0], 3045],
        [[3893, 4486, 2276, 0], 3569],
        [[5060, 5921, 2936, 0], 4183],
        [[6579, 7816, 3787, 0], 4904],
        [[8552, 10317, 4886, 0], 5748],
        [[11118, 13618, 6302, 0], 6737],
        [[14453, 17976, 8130, 0], 7896],
        [[18789, 23728, 10488, 0], 9255],
        [[24426, 31321, 13529, 0], 10848],
        [[31754, 41344, 17453, 0], 12715],
        [[41280, 54574, 22514, 0], 14904],
        [[53664, 72037, 29043, 0], 17469],
        [[69763, 95089, 37466, 0], 20476],
        [[90692, 125517, 48331, 0], 24000]
    ],
    [
        [[60, 50, 40, 0], 1000],
        [[76, 64, 50, 0], 1229],
        [[96, 81, 62, 0], 1512],
        [[121, 102, 77, 0], 1859],
        [[154, 130, 96, 0], 2285],
        [[194, 165, 120, 0], 2810],
        [[246, 210, 149, 0], 3454],
        [[311, 266, 185, 0], 4247],
        [[393, 338, 231, 0], 5222],
        [[498, 430, 287, 0], 6420],
        [[630, 546, 358, 0], 7893],
        [[796, 693, 446, 0], 9705],
        [[1007, 880, 555, 0], 11932],
        [[1274, 1118, 691, 0], 14670],
        [[1612, 1420, 860, 0], 18037],
        [[2039, 1803, 1071, 0], 22177],
        [[2580, 2290, 1333, 0], 27266],
        [[3264, 2908, 1659, 0], 33523],
        [[4128, 3693, 2066, 0], 41217],
        [[5222, 4691, 2572, 0], 50675],
        [[6606, 5957, 3202, 0], 62305],
        [[8357, 7566, 3987, 0], 76604],
        [[10572, 9608, 4963, 0], 94184],
        [[13373, 12203, 6180, 0], 115798],
        [[16917, 15497, 7694, 0], 142373],
        [[21400, 19682, 9578, 0], 175047],
        [[27071, 24996, 11925, 0], 215219],
        [[34245, 31745, 14847, 0], 264611],
        [[43320, 40316, 18484, 0], 325337],
        [[54799, 51201, 23013, 0], 400000]
    ],
    [
        [[50, 60, 50, 2], 150],
        [[63, 75, 63, 0], 200],
        [[78, 94, 78, 1], 267],
        [[98, 117, 98, 0], 356],
        [[122, 146, 122, 1], 474],
        [[153, 183, 153, 0], 632],
        [[191, 229, 191, 1], 843],
        [[238, 286, 238, 1], 1125],
        [[298, 358, 298, 1], 1500],
        [[373, 447, 373, 1], 2000]
    ],
    [
        [[50, 100, 20, 5], 0.04],
        [[63, 128, 25, 1], 0.08],
        [[79, 163, 32, 1], 0.12],
        [[100, 207, 40, 1], 0.16],
        [[126, 264, 50, 1], 0.2],
        [[159, 337, 64, 2], 0.24],
        [[200, 430, 80, 2], 0.29],
        [[252, 548, 101, 2], 0.34],
        [[318, 698, 127, 3], 0.39],
        [[400, 890, 160, 3], 0.44],
        [[504, 1135, 202, 3], 0.49],
        [[635, 1447, 254, 4], 0.55],
        [[801, 1846, 320, 5], 0.6],
        [[1009, 2353, 404, 5], 0.66],
        [[1271, 3000, 508, 7], 0.72],
        [[1602, 3825, 641, 8], 0.79],
        [[2018, 4877, 807, 9], 0.85],
        [[2543, 6218, 1017, 10], 0.92],
        [[3204, 7928, 1281, 12], 0.99],
        [[4037, 10109, 1615, 15], 1.07]
    ],
]

data = {
    "requirements": {},
    "levels": []
}


def create_files():
    for i, name in enumerate(buildings):
        f = open(f"{name}.json", "w")
        data["requirements"].clear()
        data["requirements"].update(requirements[i])
        data["levels"] = levels[i]
        f.write(json.dumps(data))
        f.close()


def json_parser_for_buildings():
    s = """[
  [1,"{{Res|50|100|20}}","{{Workers|5|5}}","4%"  ],
  [2,"{{Res|63|128|25}}","{{Workers|1|6}}","8%"  ],
  [3,"{{Res|79|163|32}}","{{Workers|1|7}}","12%"  ],
  [4,"{{Res|100|207|40}}","{{Workers|1|8}}","16%"  ],
  [5,"{{Res|126|264|50}}","{{Workers|1|9}}","20%"  ],
  [6,"{{Res|159|337|64}}","{{Workers|2|11}}","24%"  ],
  [7,"{{Res|200|430|80}}","{{Workers|2|13}}","29%"  ],
  [8,"{{Res|252|548|101}}","{{Workers|2|15}}","34%"  ],
  [9,"{{Res|318|698|127}}","{{Workers|3|18}}","39%"  ],
  [10,"{{Res|400|890|160}}","{{Workers|3|21}}","44%"  ],
  [11,"{{Res|504|1135|202}}","{{Workers|3|24}}","49%"  ],
  [12,"{{Res|635|1447|254}}","{{Workers|4|28}}","55%"  ],
  [13,"{{Res|801|1846|320}}","{{Workers|5|33}}","60%"  ],
  [14,"{{Res|1009|2353|404}}","{{Workers|5|38}}","66%"  ],
  [15,"{{Res|1271|3000|508}}","{{Workers|7|45}}","72%"  ],
  [16,"{{Res|1602|3825|641}}","{{Workers|8|53}}","79%"  ],
  [17,"{{Res|2018|4877|807}}","{{Workers|9|62}}","85%"  ],
  [18,"{{Res|2543|6218|1017}}","{{Workers|10|72}}","92%"  ],
  [19,"{{Res|3204|7928|1281}}","{{Workers|12|84}}","99%"  ],
  [20,"{{Res|4037|10109|1615}}","{{Workers|15|99}}","107%"  ]
]"""
    json_object = json.loads(s)
    result = ""
    for index, element in enumerate(json_object):
        wood, clay, iron = str(element[1][6:-2]).split("|")
        pop = str(element[2][10:-2]).split("|")[0]
        factor = float(element[3][0:-1]) / 100
        print(f"[[{wood},{clay},{iron},{pop}], {factor}],")


def json_parser_for_points():
    s = """[
  ["1,10,16,20,24,10,10,42,512,19,0,24,10,6,6,6,5,6,5,8","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["2,2,3,4,5,2,,8,,4,,,2,1,1,1,1,1,1,2","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["3,2,4,5,6,2,,10,,4,,,2,2,2,2,1,2,1,2","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["4,3,5,6,6,,,13,,6,,,3,1,1,1,2,1,2,2","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["5,4,5,6,9,,,14,,6,,,4,2,2,2,1,2,1,3","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["6,4,7,9,10,,,18,,8,,,4,3,3,3,2,3,2,3","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["7,5,8,10,12,,,20,,10,,,5,3,3,3,3,3,3,4","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["8,6,9,12,14,,,25,,11,,,6,3,3,3,3,3,3,5","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["9,7,12,14,17,,,31,,14,,,7,5,5,5,3,5,3,5","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["10,9,14,17,21,,,36,,16,,,9,5,5,5,5,5,5,7","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["11,10,16,21,25,,,43,,20,,,10,6,6,6,5,6,,9","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["12,12,20,25,29,,,52,,23,,,12,8,8,8,6,8,,9","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["13,15,24,29,36,,,62,,28,,,15,8,8,8,8,8,,12","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["14,18,28,36,43,,,75,,34,,,18,11,11,11,8,11,,15","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["15,21,34,43,51,,,90,,41,,,21,13,13,13,11,13,,17","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["16,26,42,51,,,,108,,49,,,26,15,15,15,13,15,,20","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["17,31,49,62,,,,130,,58,,,31,19,19,19,15,19,,25","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["18,37,59,74,,,,155,,71,,,37,22,22,22,19,22,,29","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["19,44,71,88,,,,186,,84,,,44,27,27,27,22,27,,36","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["20,53,85,107,,,,224,,101,,,53,32,32,32,27,32,,43","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["21,64,102,,,,,,,,,,64,38,38,38,32,38,,","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["22,77,123,,,,,,,,,,77,46,46,46,38,46,,","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["23,92,147,,,,,,,,,,92,55,55,55,46,55,,","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["24,110,177,,,,,,,,,,110,66,66,66,55,66,,","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["25,133,212,,,,,,,,,,133,80,80,80,66,80,,","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["26,159,,,,,,,,,,,,95,95,95,80,95,,","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["27,191,,,,,,,,,,,,115,115,115,95,115,,","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["28,229,,,,,,,,,,,,137,137,137,115,137,,","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["29,274,,,,,,,,,,,,165,165,165,137,165,,","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ],
  ["30,330,,,,,,,,,,,,198,198,198,165,198,,","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""  ]
]"""
    json_object = json.loads(s)
    matrix = [[0 for x in range(16)] for y in range(30)]
    y = 0
    x = 0
    for index_y, element_y in enumerate(json_object):
        l = str(element_y[0][1:]).split("'")[0].split(",")
        print(l)
        for index_x, element_x in enumerate(l):
            if index_x == 0 or 5 <= index_x <= 7:
                continue

            print(element_x)
            print(f"y: {y} | x: {x}")
            matrix[y][x] = 0 if element_x == '' else int(element_x)
            x += 1

        y += 1
        x = 0

    f = open(f"POINTS.json", "w")
    f.write(json.dumps(matrix))
    f.close()


# create_files()
# json_parser_for_buildings()
# json_parser_for_points()
