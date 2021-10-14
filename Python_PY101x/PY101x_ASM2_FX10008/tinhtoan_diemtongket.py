def tinhdiem_trungbinh(path_a):
    ds_hsinh, ds_diem  = [], []
    for line in path_a:
        if line.startswith('Mã HS'):
            mon_hoc = line.strip().split(',')[1:]
        else:
            ds_hsinh.append(line.strip().split(';')[0])
            ds_diem.append(line.strip().split(';')[1:])
    for i,diem in enumerate(ds_diem):
        for j,diem_tp in enumerate(diem):
            diem_tp = list(map(int, diem_tp.split(',')))
            #print('#######',*diem_tp)
            if len(diem_tp) == 4:
                diem_tp = '%.2f' % (diem_tp[0]*0.05 + diem_tp[1]*0.1 + diem_tp[2]*0.15 + diem_tp[3]*0.7)
            elif len(diem_tp) == 5:
                diem_tp = '%.2f' % (diem_tp[0]*0.05 + diem_tp[1]*0.1 + diem_tp[1]*0.1 + diem_tp[2]*0.15 + diem_tp[3]*0.6)
            diem[j] = diem_tp
        ds_diem[i] = diem
    result = {}
    for j, k in enumerate(ds_hsinh):
        dic = {}
        for i, v in enumerate(mon_hoc):
            dic[v.strip()] = ds_diem[j][i]
        #print('############', dic)
        result[k] = dic
    return result

def luudiem_trungbinh(output, path_b):
    path_b.write('Mã HS, Toán, Lý, Hóa, Sinh, Văn, Anh, Sử, Địa\n')
    for k,v in output.items():
        x = str(list(v.values()))
        x = x.replace('[', '')
        x = x.replace(']', '')
        x = x.replace('\'', '')
        x = x.replace(',', ';')
        path_b.write(k + ': ' + x +'\n')
    return path_b
    
def main():
    path_a = open('diem_chitiet.txt', encoding='utf8')
    path_b = open('diem_trungbinh.txt','w', encoding='utf8')
    output = tinhdiem_trungbinh(path_a)
    print(output)
    luudiem_trungbinh(output, path_b)
    path_a.close()
    path_b.close()
########################
if __name__ == '__main__':
    main()
