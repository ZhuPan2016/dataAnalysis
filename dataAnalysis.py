import numpy as np
import matplotlib.pyplot as plt
A_true = [827, 544, 534, 638, 558, 600, 571, 620, 652, 570, 624, 982, 642, 696, 639, 587, 625, 640, 609, 560, 577, 584]
A_false = [347, 630, 640, 536, 616, 574, 603, 554, 522, 604, 550, 192, 532, 478, 535, 587, 549, 534, 565, 614, 597, 590]
B_true = [395, 713, 809, 624, 739, 743, 765, 743, 738, 717, 721, 276, 696, 535, 683, 731, 715, 713, 748, 759, 753, 792]
B_false = [839, 521, 425, 610, 495, 491, 469, 491, 496, 517, 513, 958, 538, 699, 551, 503, 519, 521, 486, 475, 481, 442]
TP = []
for i in range(0,len(A_false)):
    TP.append(float(A_true[i])/(A_true[i]+A_false[i]))
FP = []
for m in range(0,len(B_false)):
    FP.append(1-(float(B_true[m])/(B_false[m]+B_true[m])))
print TP
print "\n"
print FP

plt.xlim(xmax = 1,xmin = 0)
plt.ylim(ymax = 1,ymin = 0)
plt.plot(FP,TP,'ro')

plt.show()