import sys
import requests
import re
class PDB:
    def __init__(self,fix,index,atom,aminoAcid,chain,aaNumber,x,y,z,c,r,atom_nospecific):
        self.fix = fix
        self.index = index
        self.atom = atom
        self.aminoAcid = aminoAcid
        self.chain = chain
        self.aaNumber = aaNumber
        self.x = x
        self.y = y
        self.z = z
        self.c = c
        self.r = r
        self.atom_nospecific = atom_nospecific

def downloadPDB( PDBID ):
    pdb_list = []
    urlName = ''.join(['https://files.rcsb.org/view/',PDBID,'.pdb'])
    page = requests.get(urlName).text.split('\n')
    line_index = 0
    atom_line = []
    for line in page:
        if re.match(r'^(ATOM).+$', line):
            line = line.split()
            pdb_list.append(
                PDB(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11]))
            atom_line.append(line_index)
        line_index += 1
    header = []
    trailor = []
    for index in range(0,len(page)):
        if index < atom_line[0]:
            header.append(page[index])
        if index > atom_line[len(atom_line)-1]:
            trailor.append(page[index])
    return pdb_list,header,trailor

def titrResDict(res,status):
    titr_res_dict_on = {'AR0':'ARG','ASP':'ASH','GLU':'GLH','HIE':'HIP','HIS':'HIP','LYN':'LYS','TYM':'TYR'} # 'CYX':'CYM',
    titr_res_dict_off = {'ARG':'AR0','ASH':'ASP','GLH':'GLU','HIP':'HIE','HIS':'HIE','LYS':'LYN','TYR':'TYM'}
    for site in titr_res_dict_on:
        if (res==site):
            if (status == 'on'):
                return titr_res_dict_on[site]
            if (status == 'off'):
                return res
    for site in titr_res_dict_off:
        if (res==site):
            if (status == 'off'):
                return titr_res_dict_off[site]
            if (status == 'on'):
                return res

def main(PBDID):
    pdb_list, header, trailor = downloadPDB(PBDID)
    titr_res_name = ['ARG','ASP','GLU','HIS','LYS','TYR'] # 'CYS'

    # collect all the titratable sites in each protein
    titr_site = {}
    for titr in titr_res_name:
        # the reason to use set is that the RSDID is corresponding to atom which shows repeatedly
        titr_site[titr] = set()
    for atom in pdb_list:
        for titr in titr_res_name:
            if titr == atom.aminoAcid:
                titr_site[titr].add(atom.aaNumber)
    # change the map's value(set) into a list, then we can iterate item in list with order
    for res in titr_site:
        to_list = []
        for ele in titr_site[res]:
            to_list.append(int(ele))
        to_list.sort()
        print(to_list)
        titr_site[res] = to_list
    # for item in titr_res_name:
    #     print(titr_site[item])
    # print('tell different!')
    # print(titr_site)

    out = open(''.join([PBDID,'.names']),'w')
    # all mute goes first
    out.write(''.join([PBDID,'_all_mute','.pqr']))
    out.write('\n')
    # intrinsic items for each titratable site
    for item in titr_res_name:
        for num in titr_site[item]:
            pro = titrResDict(item,'on')
            dep = titrResDict(item,'off')
            out.write(''.join([PBDID,'_',pro,str(num),'.pqr'])) # first are the protonated one titratable site on the protein
            out.write('\n')
            out.write(''.join(['aalone_',PBDID,'_',pro,str(num),'.pqr'])) # follows are the protonated one titritable sites off protein
            out.write('\n')
            out.write(''.join(['aalone_',PBDID,'_',dep,str(num),'.pqr']))  # last are the deprotonated one titritable site off protein
            out.write('\n')

    # site-site interaction: I knew for wrapper, it uese a detour to solve
    # for core, the situation is possible to avoid, thus, I just need the final energies
    site_site = []
    for site in titr_res_name:
        for i in titr_site[site]:
            site_site.append(''.join([site,str(i)]))
    for each in site_site:
        for site in site_site:
            if(each != site):
                out.write(''.join([PBDID,'_',each,'_',site,'.pqr']))
                out.write('\n')
            else:
                out.write(''.join([PBDID,'_',each,'_s_s.pqr\n']))
    out.close()

if __name__ == "__main__":
    PBDID = sys.argv[1]
    main(PBDID)
