# define np
import numpy as np
#introduce matplotlib
import matplotlib.pyplot as plt
gene_lengths=np.array([9410,394141,4442,105338,19149,76779,126550,36296,842,15981])
exon_counts= np.array([51,1142,42,216,25,650,32533,57,1,523])
#calculate, sort and print average_exon_length
average_exon_length=gene_lengths/exon_counts
average_exon_length.sort()
print("average_exon_length=",average_exon_length)


#input the data
plt.boxplot(average_exon_length,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False
              )
plt.show()
