import matplotlib.pyplot as plt
from matplotlib import rcParams

class Chart:
    def __init__(self):
        rcParams['axes.spines.top'] = False
        rcParams['axes.spines.right'] = False
        plt.figure(figsize=(12, 4))
    
    def addAxisInfos(self, colX, colY):
        plt.xlabel(colX, fontsize=13)
        plt.xticks(fontsize=9)
        plt.ylabel(colY, fontsize=13)
        plt.yticks(fontsize=9)
        plt.xticks(rotation=45)
        
    def line(self, _data, _colX, _colY):
        plt.grid(color='#F2F2F2', alpha=1, zorder=0)
        plt.plot(_data[_colX], _data[_colY], color='#087E8B', lw=3, zorder=5)
        self.addAxisInfos(_colX, _colY)
        plt.savefig("line.jpg", dpi=300, bbox_inches='tight', pad_inches=0)
        plt.close()
        
    def bar(self, _data, _colX, _colY):
        plt.bar(_data[_colX], _data[_colY], color ='#087E8B')
        self.addAxisInfos(_colX, _colY)
        plt.savefig("bar.jpg", dpi=300, bbox_inches='tight', pad_inches=0)
        plt.close()
    