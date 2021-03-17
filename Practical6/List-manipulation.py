# define np
import numpy as np
#introduce matplotlib
import matplotlib.pyplot as plt
gene_lengths=np.array([9410,394141,4442,105338,19149,76779,126550,36296,842,15981])
exon_counts= np.array([51,1142,42,216,25,650,32533,57,1,523])
#calculate and print average_exon_length
average_exon_length=gene_lengths/exon_counts
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



#genes=['gene1','gene2','gene3','gene4','gene5','gene6','gene7','gene8','gene9','gene10']
#width=0.35
#fig, ax=plt.subplots()
#ax.bar(genes,average_exon_length,width,yerr=[0,0,0,0,0,0,0,0,0,0],label='')
#ax.set_ylabel('average_exon_length')
#ax.set_title('the boxplot of average_exon_length')
#ax.legend()
#plt.show()

#score=np.random.uniform(0,100,average_exon_length)
#plt.boxplot(score,
#            vert=True,
#            whis=1.5,
#            patch_artist=True,
#            meanline=False,
#            showbox=True,
#            showcaps=True,
#            showfliers=True,
#            notch=False
#              )
#plt.show()
