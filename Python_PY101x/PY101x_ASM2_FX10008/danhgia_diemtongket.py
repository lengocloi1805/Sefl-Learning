#path = open('diem_trungbinh.txt', encoding='utf8')
output_path = open('danhgia_hocsinh.txt','w', encoding='utf8')
def xeploai_hocsinh(path_a):
    result_a = dict()
    for line_a in path_a:
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
    return result_a

def xeploai_thidaihoc_hocsinh(path_b):
    result_b = dict()
    for line_b in path_b:
        if not line_b.startswith('Mã HS'):
            name = line_b.strip().split(':')[0]
            x = (line_b.strip().split(':')[1:])[0]
            x = x.split(';')
            diem_tb = list(map(float, x))
            xeploai = []
            khois= [[0,1,2], [0,1,5], [0,2,3], [4,6,7], [0,4,5]]
            for i,v in enumerate(khois):
                if i in [0,1,2,3]:
                    xeploai.append(sum([diem_tb[j] for j in v]))
                elif i == 4:
                    xeploai.append(sum([diem_tb[j] for j in v]) + diem_tb[5])
            for i, v in enumerate(xeploai):
                if i in [0,1,2]:
                    if v >= 24: xeploai[i] = 1
                    elif v >= 18: xeploai[i] = 2
                    elif v >= 12: xeploai[i] = 3
                    else: xeploai[i] = 4
                elif i == 3:
                    if v >= 21: xeploai[i] = 1
                    elif v >= 15: xeploai[i] = 2
                    elif v >= 12: xeploai[i] = 3
                    else: xeploai[i] = 4
                else:
                    if v >= 32: xeploai[i] = 1
                    elif v >= 24: xeploai[i] = 2
                    elif v >= 20: xeploai[i] = 3
                    else: xeploai[i] = 4
            result_b[name] = xeploai
    return result_b

def main(output_path):
    path_a = open('diem_trungbinh.txt', encoding='utf8')
    path_b = open('diem_trungbinh.txt', encoding='utf8')
    result_a = xeploai_hocsinh(path_a)
    result_b = xeploai_thidaihoc_hocsinh(path_b)
    print('{} \n{}'.format(result_a, result_b))
    path_a.close()
    path_b.close()

    output_path.write('“Ma HS”, “xeploai_TB chuan”, “xeploai_A”, “xeploai_A1”, “xeploai_B ”, “xeploai_C”, xeploai_D”\n')
    for k,v in result_a.items():
        x = str(result_b[k])
        x = x.replace('[', '')
        x = x.replace(']', '')
        x = x.replace('\'', '')
        x = x.replace(',', ';')
        output_path.write(k + ';' + v + ';' + x +'\n')
    return output_path
#########################
if __name__ == '__main__':
    main(output_path)
    output_path.close()