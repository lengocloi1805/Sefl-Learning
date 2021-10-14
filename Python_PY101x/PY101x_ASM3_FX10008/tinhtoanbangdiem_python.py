
class BANGDIEM:
    def __init__(self, path_in, path_out):
        self.path_in = path_in
        self.path_out = path_out

    def load_dulieu(self):
        self.file_in_1 = open(self.path_in, encoding='utf8')
        self.file_out = open(self.path_out,'w', encoding='utf8')
        self.file_in_2 = open(self.path_out, encoding='utf8')
        self.file_in_3 = open(self.path_out, encoding='utf8')
        return [self.file_in_1, self.file_out, self.file_in_2, self.file_in_3]

    def tinhdiem_trungbinh(self):
        ds_hsinh, ds_diem  = [], []
        for line in self.file_in_1:
            if line.startswith('Mã HS'):
                mon_hoc = line.strip().split(',')[1:]
            else:
                ds_hsinh.append(line.strip().split(';')[0])
                ds_diem.append(line.strip().split(';')[1:])
        for i,diem in enumerate(ds_diem):
            for j,diem_tp in enumerate(diem):
                diem_tp = list(map(int, diem_tp.split(',')))
                if len(diem_tp) == 4:
                    diem_tp = '%.2f' % (diem_tp[0]*0.05 + diem_tp[1]*0.1 + diem_tp[2]*0.15 + diem_tp[3]*0.7)
                elif len(diem_tp) == 5:
                    diem_tp = '%.2f' % (diem_tp[0]*0.05 + diem_tp[1]*0.1 + diem_tp[1]*0.1 + diem_tp[2]*0.15 + diem_tp[3]*0.6)
                diem[j] = diem_tp
            ds_diem[i] = diem
        self.output_1 = {}
        for j, k in enumerate(ds_hsinh):
            dic = {}
            for i, v in enumerate(mon_hoc):
                dic[v.strip()] = ds_diem[j][i]
            self.output_1[k] = dic
        self.file_in_1.close()
        return print(self.output_1)    

    def luudiem_trungbinh(self):
        self.file_out.write('Mã HS, Toán, Lý, Hóa, Sinh, Văn, Anh, Sử, Địa\n')
        for k,v in self.output_1.items():
            x = str(list(v.values()))
            x = x.replace('[', '')
            x = x.replace(']', '')
            x = x.replace('\'', '')
            x = x.replace(',', ';')
            self.file_out.write(k + ': ' + x +'\n')
        self.file_out.close()
    
class DANHGIA(BANGDIEM):
    def xeploai_hocsinh(self):
        result_a = dict()
        for line_a in self.file_in_2:
            if not line_a.startswith('Mã HS'):
                name = line_a.strip().split(':')[0]
                x = (line_a.strip().split(':')[1:])[0]
                x = x.split(';')
                diem_tb = list(map(float, x))
                chinh = [0,4,5]
                phu = [1,2,3,6,7]
                tbm = (sum([diem_tb[i] for i in chinh])*2.0 + sum([diem_tb[i] for i in phu])*1.0)/11.0
                if tbm >= 9.0 and all([i >= 8.0 for i in diem_tb]):
                    result_a[name] = 'Xuat Sac'
                elif tbm >= 8.0 and all([i >= 6.5 for i in diem_tb]):
                    result_a[name] = 'Gioi'
                elif tbm >= 6.5 and all([i >= 5.0 for i in diem_tb]):
                    result_a[name] = 'Kha'
                elif tbm >= 6.0 and all([i >= 4.5 for i in diem_tb]):
                    result_a[name] = 'TB Kha'
                else:
                    result_a[name] = 'TB'
        self.file_in_2.close()
        return print(result_a)
        
    # def xeploai_thidaihoc_hocsinh(self):
        # self.output_2 = dict()
        # for line_b in self.file_in_3:
        #     if not line_b.startswith('Mã HS'):
        #         name = line_b.strip().split(':')[0]
        #         x = (line_b.strip().split(':')[1:])[0]
        #         x = x.split(';')
        #         diem_tb = list(map(float, x))
        #         xeploai = []
        #         khois= [[0,1,2], [0,1,5], [0,2,3], [4,6,7], [0,4,5]]
        #         for i,v in enumerate(khois):
        #             if i in [0,1,2,3]:
        #                 xeploai.append(sum([diem_tb[j] for j in v]))
        #             elif i == 4:
        #                 xeploai.append(sum([diem_tb[j] for j in v]) + diem_tb[5])  
            
        #         for i, v in enumerate(xeploai):
        #             if i in [0,1,2]:
        #                 if v >= 24: xeploai[i] = 1
        #                 elif v >= 18: xeploai[i] = 2
        #                 elif v >= 12: xeploai[i] = 3
        #                 else: xeploai[i] = 4
        #             elif i == 3:
        #                 if v >= 21: xeploai[i] = 1
        #                 elif v >= 15: xeploai[i] = 2
        #                 elif v >= 12: xeploai[i] = 3
        #                 else: xeploai[i] = 4
        #             else:
        #                 if v >= 32: xeploai[i] = 1
        #                 elif v >= 24: xeploai[i] = 2
        #                 elif v >= 20: xeploai[i] = 3
        #                 else: xeploai[i] = 4
        #         self.output_2[name] = xeploai
        # self.file_in_3.close()        
        # return print(self.output_2)

class TUNHIEN(DANHGIA):
    def xeploai_thidaihoc_hocsinh(self):
        self.output_2 = dict()
        for line_b in self.file_in_3:
            if not line_b.startswith('Mã HS'):
                name = line_b.strip().split(':')[0]
                x = (line_b.strip().split(':')[1:])[0]
                x = x.split(';')
                diem_tb = list(map(float, x))
                xeploai = []
                khois= [[0,1,2], [0,1,5], [0,2,3]]
                for i,v in enumerate(khois):
                    xeploai.append(sum([diem_tb[j] for j in v]))
                for i, v in enumerate(xeploai):
                    if v >= 24: xeploai[i] = 1
                    elif v >= 18: xeploai[i] = 2
                    elif v >= 12: xeploai[i] = 3
                    else: xeploai[i] = 4
                self.output_2[name] = xeploai
        self.file_in_3.close()
        return print(self.output_2)
class XAHOI(DANHGIA):
    def xeploai_thidaihoc_hocsinh(self):
        self.output_2 = dict()
        for line_b in self.file_in_3:
            if not line_b.startswith('Mã HS'):
                name = line_b.strip().split(':')[0]
                x = (line_b.strip().split(':')[1:])[0]
                x = x.split(';')
                diem_tb = list(map(float, x))
                xeploai = []
                xeploai.append(sum([diem_tb[j] for j in [4,6,7]]))
                for i, v in enumerate(xeploai):
                    if v >= 24: xeploai[i] = 1
                    elif v >= 18: xeploai[i] = 2
                    elif v >= 12: xeploai[i] = 3
                    else: xeploai[i] = 4
                self.output_2[name] = xeploai
        self.file_in_3.close()
        return print(self.output_2)
class COBAN(DANHGIA):
    def xeploai_thidaihoc_hocsinh(self):
        self.output_2 = dict()
        for line_b in self.file_in_3:
            if not line_b.startswith('Mã HS'):
                name = line_b.strip().split(':')[0]
                x = (line_b.strip().split(':')[1:])[0]
                x = x.split(';')
                diem_tb = list(map(float, x))
                xeploai = []
                xeploai.append(sum([diem_tb[j] for j in [0,4,5]]))
                for i, v in enumerate(xeploai):
                    if v >= 24: xeploai[i] = 1
                    elif v >= 18: xeploai[i] = 2
                    elif v >= 12: xeploai[i] = 3
                    else: xeploai[i] = 4
                self.output_2[name] = xeploai
        self.file_in_3.close()
        return print(self.output_2)










def main():
    path_in = 'diem_chitiet.txt'
    path_out = 'diem_trungbinh.txt'
    result = TUNHIEN(path_in, path_out)
    result.load_dulieu()
    result.tinhdiem_trungbinh()
    result.luudiem_trungbinh()
    result.xeploai_hocsinh()
    result.xeploai_thidaihoc_hocsinh()
    

########################
if __name__ == '__main__':
    main()
