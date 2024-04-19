# Home cooked example.

import numpy
import matplotlib.pyplot as plt

structureStiffnessMin= 1e4 
structureStiffnessMax= 6e4

distances= numpy.arange(start= 0.5, stop= 6.0, step= 0.1)
horizontalForcesMin=  [4.3040788117306406, 5.158925112839662, 6.010495697547319, 6.858228057628808, 7.701551843265492, 8.539887595323865, 9.37264541457596, 10.199223557281275, 11.01900694546317, 11.831365578916724, 12.635652834448045, 13.431203636029228, 14.217332477399673, 14.993331276098987, 15.758467034894325, 16.511979282975698, 17.253077265013925, 17.98093684106229, 18.694697054147884, 19.39345631501045, 20.076268144509893, 20.74213640336454, 21.390009925621023, 22.018776455974, 22.627255770948956, 23.214191838983638, 23.778243843210372, 24.317975851414943, 24.83184486776301, 25.318186937104443, 25.77520089042735, 26.200929213025344, 26.593235376339525, 26.949776787738, 27.267972261752064, 27.54496257534962, 27.777562199986026, 27.96219964613621, 28.094842922311035, 28.170905259998634, 28.185124263761693, 28.13140464216526, 28.002610034737653, 27.790282079878406, 27.484252788717722, 27.07209576218126, 26.53832540787591, 25.86318556376116, 25.02073505755521, 23.9756532738151, 22.677526768192823, 21.04964333519078, 18.96397385732273, 16.173044473227655, 12.043716582424894]
horizontalForcesMax=  [10.54279690146461, 12.636734147687301, 14.72264756018458, 16.799159280829567, 18.864872243591705, 20.91836706926711, 22.9581988057476, 24.98289348791304, 26.990944488568637, 28.980808628674474, 30.950902011349676, 32.89959553968572, 34.825210073128645, 36.726011170954685, 38.60020336396048, 40.44592388669731, 42.26123579209726, 44.04412035781424, 45.79246867857414, 47.50407232073175, 49.176612893341655, 50.807650363451, 52.394609910839065, 53.93476707754406, 55.425230918270934, 56.86292479659138, 58.24456439534108, 59.56663241328994, 60.8253492979686, 62.01663920830438, 63.13609019927763, 64.1789073586937, 65.1398572817624, 66.01320181186041, 66.7926183616579, 67.47110329366541, 68.0408536883875, 68.49312121886605, 68.81802956330544, 69.00434347928334, 69.03917278315353, 68.90758712106688, 68.59210605124717, 68.0720109037133, 67.322395294024, 66.31282088510693, 65.00535587723424, 63.35160775413092, 61.28803388037696, 58.72811677073603, 55.54836921037928, 51.5608854387941, 46.45205944592036, 39.615706546747305, 29.500960233637453]
verticalForcesMin=  [0.3599251516750561, 0.5184914824494258, 0.7060459959946045, 0.9226686858778146, 1.1684526537115714, 1.4435044672182489, 1.74794457620726, 2.08190779065942, 2.445543825849693, 2.8390179202727146, 3.2625115330850543, 3.716223128868811, 4.200369058779614, 4.715184548604917, 5.260924805965948, 5.837866260901951, 6.446307956440803, 7.086573108565842, 7.759010858332126, 8.463998242890924, 9.201942417003785, 9.973283162465783, 10.778495729963938, 11.618094066596367, 12.492634492992714, 13.402719907256815, 14.349004609522735, 15.332199861737013, 16.35308032364085, 17.412491539566062, 18.511358693957106, 19.650696909769003, 20.831623437655743, 22.055372181641175, 23.32331113805645, 24.636963502467758, 25.99803344410971, 27.40843788906971, 28.870346138251445, 30.38622984614177, 31.95892691715681, 33.5917244276145, 35.28846807382681, 37.05370943983785, 38.89290858390723, 40.812719968966206, 42.82140838310406, 44.92947610828489, 47.15065086286656, 49.503528817545806, 52.01450326966684, 54.723488926883995, 57.696656329039406, 61.060980369204046, 65.13869564948104]
verticalForcesMax=  [0.8816329671977297, 1.2700395679803125, 1.7294524251219165, 2.2600674820449416, 2.8621127901942796, 3.535849386112797, 4.281572310373172, 5.099611778640636, 5.990334516945554, 6.954145275285644, 7.991488536003662, 9.10285043605776, 10.288760925384496, 11.549796187137474, 12.886581349767171, 14.299793525819313, 15.790165218123336, 17.35848814091513, 19.005617511627847, 20.73247687889616, 22.540063564132222, 24.429454808332114, 26.40181473317895, 28.4584022468179, 30.60058005092498, 32.82982493822147, 35.14773961017448, 37.55606629562648, 40.056702515667666, 42.65171942246594, 45.34338324582814, 48.13418051902026, 51.026847936059376, 54.02440793219551, 57.130211400409934, 60.347989392618295, 63.68191625388075, 67.13668747498608, 70.71761673624685, 74.43075832997633, 78.28306367393282, 82.28258442784085, 86.43874058537044, 90.76268120495104, 95.26778064328457, 99.97033893906493, 104.89060060594299, 110.0542908758657, 115.49503565414243, 121.25838607014994, 127.40899223501101, 134.04462481571116, 141.32736787086816, 149.56824509865032, 159.55656685167904]

# Create figure
fig, ax = plt.subplots()
ax.plot(distances, horizontalForcesMin, label = 'fuerza horiz. k= '+'{0:.1f}'.format(structureStiffnessMin/1e3)+' kN/m')
ax.plot(distances, horizontalForcesMax, label = 'fuerza horiz. k= '+'{0:.1f}'.format(structureStiffnessMax/1e3)+' kN/m')
ax.plot(distances, verticalForcesMin, label = 'fuerza vert. k= '+'{0:.1f}'.format(structureStiffnessMin/1e3)+' kN/m', ls='dotted')
ax.plot(distances, verticalForcesMax, label = 'fuerza vert. k= '+'{0:.1f}'.format(structureStiffnessMax/1e3)+' kN/m', ls='dotted')
plt.axvline(x = 4.14, color = 'gray', ls='--', label = 'impacto en barra superior')
plt.axvline(x = 6.0, color = 'brown', ls='--', label = 'pantalla fuera de alcance')
ax.set(xlabel='distancia (m)', ylabel='fuerza (kN)',
       title= 'Fuerza del impacto en función de la distancia a la pantalla.')
plt.legend()#bbox_to_anchor = (1.0, 1))#, loc = 'upper left')
ax.grid()
 
# Show graph
#fig.savefig("test.png")
plt.show()
