import numpy as np
import networkx as nx
import math
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns

# load GraphRicciCuravture package
from GraphRicciCurvature.OllivierRicci import OllivierRicci
from GraphRicciCurvature.FormanRicci import FormanRicci

from collections import defaultdict, Counter

vals = ["1M", "2M", "3M", "4M", "5M", "6M", "7M", "8M"]

def convertpdb(filename):
    f=open(filename, "r")
    if f.mode == 'r':
        contents = f.readlines()
    
    #recordname = []

    #atomNum = []
    atomName = []
    #altLoc = []
    #resName = []

    #chainID = []
    #resNum = []
    X = []
    Y = []
    Z = []

    #occupancy = []
    #betaFactor = []
    element = []
    #charge = []
    
    
    for i in range(len(contents)):
        thisLine = contents[i]

        if thisLine[0:4]=='ATOM':
            #recordname = np.append(recordname,thisLine[:6].strip())
            #atomNum = np.append(atomNum, float(thisLine[6:11]))
            atomName = np.append(atomName, thisLine[12:16])
            #altLoc = np.append(altLoc,thisLine[16])
            #resName = np.append(resName, thisLine[17:20].strip())
            #chainID = np.append(chainID, thisLine[21])
            #resNum = np.append(resNum, float(thisLine[23:26]))
            X = np.append(X, float(thisLine[30:38]))
            Y = np.append(Y, float(thisLine[38:46]))
            Z = np.append(Z, float(thisLine[46:54]))
            #occupancy = np.append(occupancy, float(thisLine[55:60]))
            #betaFactor = np.append(betaFactor, float(thisLine[61:66]))
            element = np.append(element,thisLine[12:14])

    #print(atomName)
    a = {'PRO': [{'atom': atomName, 'typ': element, 'pos': np.transpose([X,Y,Z])}]}
    np.savez(filename[:-4]+".npz", **a)

def gen_graph(filename, cutoff):
    data = np.load(filename, allow_pickle = True)
    for item in data['PRO']:
        coords = item['pos']
        atoms = item['atom']
    G = nx.Graph()
    for i in range(len(atoms)):
        G.add_node(i, atom = atoms[i], coords = coords[i])
    for i in range(len(coords)):
        for j in range(len(coords)):
            if i!=j:
                dist = np.linalg.norm(coords[i]-coords[j])
                if round(dist,2) <= cutoff:
                    G.add_edge(i, j) #, weight = dist)
    return G

x = np.round(np.arange(-1, 1.01, 0.01),2)
edge_mat = []
vertex_mat = []
for j in vals:
    raw_output = []
    for id in range(101):
        s = str(id)
        while len(s) < 4:
            s = '0'+ s
        print("Processing Frame ", id, ": ", j)
        convertpdb("tmao/md_"+j+"_tmao_4p_tf_"+s+"_OW.pdb")
        data = np.load("tmao/md_"+j+"_tmao_4p_tf_"+s+"_OW.npz", allow_pickle=True)
        G = gen_graph("tmao/md_"+j+"_tmao_4p_tf_"+s+"_OW.npz", 4)
        
        y = np.zeros(len(x))
        vertices = np.zeros(G.number_of_nodes())
        cnts = defaultdict(int)
        if G.number_of_edges() > 0:
            orc = OllivierRicci(G, alpha=0.5)
            orc.compute_ricci_curvature()
    
            e_temp, v_temp = nx.get_edge_attributes(orc.G, "ricciCurvature"), nx.get_node_attributes(orc.G, "ricciCurvature")
            raw_output.append(list(v_temp.values()))
            raw_output.append(list(e_temp.values()))
    
    np.savez("tmao_raw_op_"+j+".npz", raw_output)

x = np.round(np.arange(-1, 1.01, 0.01),2)
edge_mat = []
vertex_mat = []
for j in vals:
    raw_output = []
    for id in range(101):
        s = str(id)
        while len(s) < 4:
            s = '0'+ s
        print("Processing Frame ", id, ": ", j)
        convertpdb("urea/md_"+j+"_urea_4p_tf_"+s+"_OW.pdb")
        data = np.load("urea/md_"+j+"_urea_4p_tf_"+s+"_OW.npz", allow_pickle=True)
        G = gen_graph("urea/md_"+j+"_urea_4p_tf_"+s+"_OW.npz", 4)
        
        y = np.zeros(len(x))
        vertices = np.zeros(G.number_of_nodes())
        cnts = defaultdict(int)
        if G.number_of_edges() > 0:
            orc = OllivierRicci(G, alpha=0.5)
            orc.compute_ricci_curvature()

            e_temp, v_temp = nx.get_edge_attributes(orc.G, "ricciCurvature"), nx.get_node_attributes(orc.G, "ricciCurvature")
            raw_output.append(list(v_temp.values()))
            raw_output.append(list(e_temp.values()))
        
    np.savez("urea_raw_op_"+j+".npz", raw_output)


def plot_tmao_avg_vertex():
    conc = ["1M", "2M", "3M", "4M", "5M", "6M", "7M", "8M"]
    plt.figure(figsize=(5,5), dpi=150)
    for i in range(len(conc)):
        data = np.load("tmao_raw_op_"+conc[i]+".npz", allow_pickle=True)
        edge_data = data["arr_0"][1::2]
        vertex_data = data["arr_0"][::2]
        
        e_ = []
        for j in range(len(edge_data)):
            for k in range(len(edge_data[j])):
                e_.append(edge_data[j][k])
        
        v_ = []
        for j in range(len(vertex_data)):
            for k in range(len(vertex_data[j])):
                v_.append(vertex_data[j][k])

        color = plt.cm.jet(i/8)
        sns.kdeplot(v_, color=color, label = conc[i], gridsize=200)
    plt.xticks(fontsize=11)
    plt.yticks( fontsize=11)
    plt.legend()
    plt.axis([-1, 1, 0, 6])
    plt.xlabel("Vertex Curvature", fontsize=12)
    plt.ylabel("Average Density", fontsize=12)
    plt.title("$H_{2}O$ (Tmao) - TIP4P")
    #plt.savefig("tmao_avg_vertex.pdf", dpi=200)
    plt.show()

def plot_tmao_avg_edge():
    conc = ["1M", "2M", "3M", "4M", "5M", "6M", "7M", "8M"]
    plt.figure(figsize=(5,5), dpi=150)
    for i in range(len(conc)):
        data = np.load("tmao_raw_op_"+conc[i]+".npz", allow_pickle=True)
        edge_data = data["arr_0"][1::2]
        vertex_data = data["arr_0"][::2]
        
        e_ = []
        for j in range(len(edge_data)):
            for k in range(len(edge_data[j])):
                e_.append(edge_data[j][k])
        
        v_ = []
        for j in range(len(vertex_data)):
            for k in range(len(vertex_data[j])):
                v_.append(vertex_data[j][k])

        color = plt.cm.jet(i/8)
        sns.kdeplot(e_, color=color, label = conc[i])
    plt.xticks(fontsize=11)
    plt.yticks( fontsize=11)
    plt.legend()
    plt.axis([-1, 1, 0, 4.5])
    plt.xlabel("Edge Curvature", fontsize=12)
    plt.ylabel("Average Density", fontsize=12)
    plt.title("$H_{2}O$ (Tmao) - TIP4P")
    plt.savefig("tmao_avg_edge.pdf", dpi=200)
    plt.show()

def plot_urea_avg_vertex():
    conc = ["1M", "2M", "3M", "4M", "5M", "6M", "7M", "8M"]
    plt.figure(figsize=(5,5), dpi=150)
    for i in range(len(conc)):
        data = np.load("urea_raw_op_"+conc[i]+".npz", allow_pickle=True)
        edge_data = data["arr_0"][1::2]
        vertex_data = data["arr_0"][::2]
        
        e_ = []
        for j in range(len(edge_data)):
            for k in range(len(edge_data[j])):
                e_.append(edge_data[j][k])
        
        v_ = []
        for j in range(len(vertex_data)):
            for k in range(len(vertex_data[j])):
                v_.append(vertex_data[j][k])

        color = plt.cm.jet(i/8)
        sns.kdeplot(v_, color=color, label = conc[i])
    plt.xticks(fontsize=11)
    plt.yticks( fontsize=11)
    plt.legend()
    plt.axis([-1, 1, 0, 6])
    plt.xlabel("Vertex Curvature", fontsize=12)
    plt.ylabel("Average Density", fontsize=12)
    plt.title("$H_{2}O$ (Urea) - TIP4P")
    plt.savefig("urea_avg_vertex.pdf", dpi=200)
    plt.show()

def plot_urea_avg_edge():
    conc = ["1M", "2M", "3M", "4M", "5M", "6M", "7M", "8M"]
    plt.figure(figsize=(5,5), dpi=150)
    for i in range(len(conc)):
        data = np.load("urea_raw_op_"+conc[i]+".npz", allow_pickle=True)
        edge_data = data["arr_0"][1::2]
        vertex_data = data["arr_0"][::2]
        
        e_ = []
        for j in range(len(edge_data)):
            for k in range(len(edge_data[j])):
                e_.append(edge_data[j][k])
        
        v_ = []
        for j in range(len(vertex_data)):
            for k in range(len(vertex_data[j])):
                v_.append(vertex_data[j][k])

        color = plt.cm.jet(i/8)
        sns.kdeplot(e_, color=color, label = conc[i])
    plt.xticks(fontsize=11)
    plt.yticks( fontsize=11)
    plt.legend()
    plt.axis([-1, 1, 0, 4.5])
    plt.xlabel("Edge Curvature", fontsize=12)
    plt.ylabel("Average Density", fontsize=12)
    plt.title("$H_{2}O$ (Urea) - TIP4P")
    plt.savefig("urea_avg_edge.pdf", dpi=200)
    plt.show()

def plot_tmao_3d():
    vals = ["1M", "2M", "3M", "4M", "5M", "6M", "7M", "8M"]
    for i in range(len(vals)):
        edge_data, vertex_data = [], []
        x, y = [], []
        data = np.load("tmao_raw_op_"+vals[i]+".npz", allow_pickle=True)
        edge_data = data["arr_0"][1::2]
        vertex_data = data["arr_0"][::2]
        
        x = np.outer(range(0, 101), np.ones(128))
        y, z = [], []
        for j in range(101):
            ax = sns.kdeplot(vertex_data[j])
            y.append(list(ax.lines[j].get_data()[0]))
            z.append(list(ax.lines[j].get_data()[1]))
        
        fig = plt.figure(figsize=(10,5), dpi=200)
        ax= fig.add_subplot(111, projection= '3d')
        ax.plot_trisurf(np.reshape(y, (128*101)), np.reshape(x, (128*101)), np.reshape(z, (128*101)), cmap='jet', vmin = 0., vmax = 6.)
        #fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
        #fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                        #highlightcolor="limegreen", project_z=True))
        #surf = ax.plot_surface(np.array(y), np.array(x), np.array(z),cmap='jet',linewidth=0,antialiased='True',rstride=3,cstride=3)
        ax.contourf(np.array(y), np.array(x), np.array(z), 100, zdir='z', offset=-2,cmap='jet', vmin = 0., vmax = 6.)
        #ax.set_title('$H_{2}O$ (Tmao) - TIP4P - '+vals[i])
        ax.view_init(elev=10., azim=-120)
        ax.set_xlabel('Vertex Curvature', rotation=0, labelpad=15)
        ax.set_ylabel('Frame Index', rotation=0, labelpad=15)
        ax.set_zlabel('Density', rotation=90,labelpad=15)
        #ax.tick_params(axis='z', pad=10)
        ax.zaxis.set_rotate_label(False)
        ax.grid(False)
        #ax.set_xlim([-0.6, 1])
        ax.set_ylim([0, 100])
        ax.set_zlim([-2, 6.1])
        m = plt.cm.ScalarMappable(cmap=plt.cm.jet)
        m.set_clim(0, 6.)
        plt.colorbar(m, extend="both", shrink=0.75, pad=-0.05)
        plt.tight_layout()
        plt.savefig("tmao_3d_vertex_"+vals[i]+".pdf")
        #fig.colorbar(surf)
        plt.show()

def plot_urea_3d():
    vals = ["1M", "2M", "3M", "4M", "5M", "6M", "7M", "8M"]
    for i in range(len(vals)):
        edge_data, vertex_data = [], []
        x, y = [], []
        data = np.load("urea_raw_op_"+vals[i]+".npz", allow_pickle=True)
        edge_data = data["arr_0"][1::2]
        vertex_data = data["arr_0"][::2]
        
        x = np.outer(range(0, 101), np.ones(128))
        y, z = [], []
        for j in range(101):
            ax = sns.kdeplot(vertex_data[j])
            y.append(list(ax.lines[j].get_data()[0]))
            z.append(list(ax.lines[j].get_data()[1]))
        
        fig = plt.figure(figsize=(10,5), dpi=200)
        ax= fig.add_subplot(111, projection= '3d')
        ax.plot_trisurf(np.reshape(y, (128*101)), np.reshape(x, (128*101)), np.reshape(z, (128*101)), cmap='jet', vmin = 4., vmax = 6.)
        #fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
        #fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                        #highlightcolor="limegreen", project_z=True))
        #surf = ax.plot_surface(np.array(y), np.array(x), np.array(z),cmap='jet',linewidth=0,antialiased='True',rstride=3,cstride=3)
        ax.contourf(np.array(y), np.array(x), np.array(z), 100, zdir='z', offset=-2,cmap='jet', vmin = 4., vmax = 6.)
        #ax.set_title('$H_{2}O$ (Urea) - TIP4P - '+vals[i])
        ax.view_init(elev=10., azim=-120)
        ax.set_xlabel('Vertex Curvature', rotation=0, labelpad=15, fontsize=20)
        ax.set_ylabel('Frame Index', rotation=0, labelpad=15, fontsize=20)
        ax.set_zlabel('Density', rotation=90,labelpad=15, fontsize=20)
        ax.tick_params(axis='z', pad=10)
        ax.zaxis.set_rotate_label(False)
        ax.grid(False)
        #ax.set_xlim([-0.6, 1])
        ax.set_ylim([0, 100])
        ax.set_zlim([-2, 6.1])
        m = plt.cm.ScalarMappable(cmap=plt.cm.jet)
        m.set_clim(4., 6.)
        plt.colorbar(m, extend="both", shrink=0.75, pad=-0.05)
        plt.tight_layout()
        plt.savefig("Urea_3d_vertex_"+vals[i]+".pdf")
        #fig.colorbar(surf)
        plt.show()

def plot_urea_sample():
    data = np.load("urea_raw_op.npz", allow_pickle=True)

    conc = ["1M", "2M", "3M", "4M", "5M", "6M", "7M", "8M"]
    plt.figure(figsize=(5,5), dpi=150)
    for i in range(len(data["arr_0"])//2):
        color = plt.cm.jet(i/(len(data["arr_0"])//2))
        sns.distplot(data["arr_0"][2*i], color=color, label = conc[i], kde_kws={'linewidth': 1} , norm_hist=False, kde=True, hist=False)
    plt.xticks(fontsize=11)
    plt.yticks( fontsize=11)
    plt.legend()
    plt.axis([-1, 1, 0, 6])
    plt.title("$H_{2}O$ (Urea) - TIP4P")
    plt.xlabel("Vertex Curvature", fontsize=12)
    plt.ylabel("Density", fontsize=12)
    plt.savefig("urea_vertex.eps", dpi=200)
    plt.show()

    plt.figure(figsize=(5,5), dpi=150)
    for i in range(len(vals)):
        color = plt.cm.jet(i/len(vals))
        sns.kdeplot(data["arr_0"][2*i+1], color=color, label = conc[i], linewidth = 1)
    plt.xticks(fontsize=11)
    plt.yticks( fontsize=11)
    plt.legend()
    plt.axis([-1, 1, 0, 3.1])
    plt.title("$H_{2}O$ (Urea) - TIP4P")
    plt.xlabel("Edge Curvature", fontsize=12)
    plt.ylabel("Density", fontsize=12)
    plt.savefig("urea_edge.eps", dpi=200)
    plt.show()

def plot_tmao_sample():
    data = np.load("tmao_raw_op.npz", allow_pickle=True)

    conc = ["1M", "2M", "3M", "4M", "5M", "6M", "7M", "8M"]
    plt.figure(figsize=(5,5), dpi=150)
    for i in range(len(data["arr_0"])//2):
        color = plt.cm.jet(i/(len(data["arr_0"])//2))
        sns.distplot(data["arr_0"][2*i], color=color, label = conc[i], kde_kws={'linewidth': 1} , kde=True, hist=False, norm_hist=True)
    plt.xticks(fontsize=11)
    plt.yticks( fontsize=11)
    plt.legend()
    plt.axis([-1, 1, 0, 6])
    plt.xlabel("Vertex Curvature", fontsize=12)
    plt.ylabel("Density", fontsize=12)
    plt.title("$H_{2}O$ (Tmao) - TIP4P")
    plt.savefig("tmao_vertex.eps", dpi=200)
    plt.show()

    conc = ["1M", "2M", "3M", "4M", "5M", "6M", "7M", "8M"]
    plt.figure(figsize=(5,5), dpi=150)
    for i in range(len(data["arr_0"])//2):
        color = plt.cm.jet(i/(len(data["arr_0"])//2))
        sns.kdeplot(data["arr_0"][2*i+1], color=color, label = conc[i], linewidth = 1)
    plt.xticks(fontsize=11)
    plt.yticks( fontsize=11)
    plt.legend()
    plt.axis([-1, 1, 0, 3.1])
    plt.xlabel("Edge Curvature", fontsize=12)
    plt.ylabel("Density", fontsize=12)
    plt.title("$H_{2}O$ (Tmao) - TIP4P")
    plt.savefig("tmao_edge.eps", dpi=200)
    plt.show()

    x = np.round(np.arange(-1, 1.01, 0.01),2)
    f, axes = plt.subplots(2, 4, figsize=(15, 5), sharex=True, sharey=True, dpi=200)
    plt.xlim(-1,1)
    f.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
    plt.xlabel("Vertex Curvature", fontsize=14)
    plt.ylabel("Density", fontsize=14)
    for j in range(len(data["arr_0"])//2):
        if j >=4:
            sns.distplot(data["arr_0"][2*j], bins=50, hist_kws=dict(edgecolor="k", lw=.5, alpha=0.7), color='tab:blue', kde_kws={"color":"tab:red", "lw": 2}, ax=axes[1][j-4], kde=False, norm_hist=True)
        else:
            sns.distplot(data["arr_0"][2*j], bins=50, hist_kws=dict(edgecolor="k", lw=.5, alpha=.7), color='tab:blue', kde_kws={"color":"tab:red", "lw": 2}, ax=axes[0][j], kde=False, norm_hist=True)
    #plt.plot(x, y_, color='red')
    #plt.xticks()
    #plt.yticks()
    for j in range(4):
        axes[0][j].xaxis.set_tick_params(which='both', labelbottom=True)
        axes[0][j].yaxis.set_tick_params(which='both', labelbottom=True)
        axes[1][j].yaxis.set_tick_params(which='both', labelbottom=True)
    #plt.ylim(0, 4)
    plt.savefig("tmao_vertex_subplots.pdf", dpi=200)
    #plt.show()

    x = np.round(np.arange(-1, 1.01, 0.01),2)
    f, axes = plt.subplots(2, 4, figsize=(15, 5), sharex=True, sharey=True, dpi=200)
    plt.xlim(-1,1)
    f.add_subplot(111, frameon=False)
    plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
    plt.xlabel("Edge Curvature", fontsize=14)
    plt.ylabel("Density", fontsize=14)
    for j in range(len(data["arr_0"])//2):
        if j >=4:
            sns.distplot(data["arr_0"][2*j+1], bins=50, hist_kws=dict(edgecolor="k", lw=.5, alpha=0.7), color='tab:blue', kde_kws={"color":"tab:red", "lw": 2}, ax=axes[1][j-4], kde=False, norm_hist=True)
        else:
            sns.distplot(data["arr_0"][2*j+1], bins=50, hist_kws=dict(edgecolor="k", lw=.5, alpha=.7), color='tab:blue', kde_kws={"color":"tab:red", "lw": 2}, ax=axes[0][j], kde=False, norm_hist=True)
    #plt.plot(x, y_, color='red')
    #plt.xticks()
    #plt.yticks()
    for j in range(4):
        axes[0][j].xaxis.set_tick_params(which='both', labelbottom=True)
        axes[0][j].yaxis.set_tick_params(which='both', labelbottom=True)
        axes[1][j].yaxis.set_tick_params(which='both', labelbottom=True)
    #plt.ylim(0, 4)
    plt.savefig("tmao_edge_subplots.pdf", dpi=200)
    #plt.show()

def plot_tmao_des():
    data = np.load("tmao_raw_op.npz", allow_pickle=True)
    
    conc = ["1M", "2M", "3M", "4M", "5M", "6M", "7M", "8M"]
    plt.figure()
    f, axes = plt.subplots(2,1, figsize=(5, 5), dpi=200, sharex=True)
    plt.xlim(-1,1)
    plt.subplots_adjust(hspace=.3)
    sns.distplot(data["arr_0"][14], bins=50, hist_kws=dict(edgecolor="k", lw=.5, alpha=0.7), color='tab:blue', kde_kws={"color":"tab:red", "lw": 2}, ax=axes[1], kde=False)
    axes[1].set(xlabel="Vertex Curvature", ylabel="No. of Vertices")
    sns.distplot(data["arr_0"][15], bins=50, hist_kws=dict(edgecolor="k", lw=.5, alpha=0.7), color='tab:blue', kde_kws={"color":"tab:red", "lw": 2}, ax=axes[0], kde=False)
    axes[0].xaxis.set_tick_params(which='both', labelbottom=True)
    axes[0].set(xlabel="Edge Curvature", ylabel="No. of Edges")
    #plt.xticks(fontsize=11)
    #plt.yticks( fontsize=11)
    #plt.legend()
    #plt.axis([-1, 1, 0, 6])
    #plt.xlabel("Vertex Curvature", fontsize=12)
    #plt.ylabel("Density", fontsize=12)
    #plt.title("$H_{2}O$ (Tmao) - TIP4P")
    plt.tight_layout()
    plt.savefig("tmao_8M.pdf", dpi=200)

    conc = ["1M", "2M", "3M", "4M", "5M", "6M", "7M", "8M"]
    plt.figure()
    f, axes = plt.subplots(2,1, figsize=(5, 5), dpi=200, sharex=True)
    plt.xlim(-1,1)
    plt.subplots_adjust(hspace=.3)
    sns.distplot(data["arr_0"][14], bins=50, hist_kws=dict(edgecolor="k", lw=.5, alpha=0.7), color='tab:blue', kde_kws={"color":"tab:blue", "lw": 2}, ax=axes[1], hist=False)
    axes[1].set(xlabel="Vertex Curvature", ylabel="Density")
    sns.distplot(data["arr_0"][15], bins=50, hist_kws=dict(edgecolor="k", lw=.5, alpha=0.7), color='tab:blue', kde_kws={"color":"tab:blue", "lw": 2}, ax=axes[0], hist=False)
    axes[0].xaxis.set_tick_params(which='both', labelbottom=True)
    axes[0].set(xlabel="Edge Curvature", ylabel="Density")
    #plt.xticks(fontsize=11)
    #plt.yticks( fontsize=11)
    #plt.legend()
    #plt.axis([-1, 1, 0, 6])
    #plt.xlabel("Vertex Curvature", fontsize=12)
    #plt.ylabel("Density", fontsize=12)
    #plt.title("$H_{2}O$ (Tmao) - TIP4P")
    plt.tight_layout()
    plt.savefig("tmao_8M_density.pdf", dpi=200)