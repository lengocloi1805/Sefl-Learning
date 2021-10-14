from math import *

toado = []
n = int(input())
for i in range(1, n+1):
    toado.append(float(input()))
print(toado)
xAB, yAB = (toado[2] - toado[0], toado[3] - toado[1])
xCA, yCA = (toado[4] - toado[0], toado[5] - toado[1])
xBC, yBC = (toado[4] - toado[2], toado[5] - toado[3])
AB = round(sqrt(xAB**2 + yAB**2), 2)
BC = round(sqrt(xBC**2 + yBC**2), 2)
CA = round(sqrt(xCA**2 + yCA**2), 2)
if AB == 0 or BC == 0 or CA == 0:
    print('Error: hai diem trung nhau?')
    exit()
gocA = round(((acos((AB**2 + CA**2 - BC**2) / (2*AB*CA)))*180/pi), 2)
gocB = round(((acos((AB**2 + BC**2 - CA**2) / (2*AB*BC)))*180/pi), 2)
gocC = round(((acos((CA**2 + BC**2 - AB**2) / (2*CA*BC)))*180/pi), 2)

def kiemtra_tamgiac(xAB, yAB, xCA, yCA):
    if (xAB == 0 and xCA == 0) or (yAB == 0 and yCA == 0):
        return False
    try:
        return (((xCA/xAB) is not (yCA/yAB)) or ((xAB/xCA) is not (yAB/yCA)))
    except ZeroDivisionError as e:
        return True
    
def goccanh_tamgiac(AB, BC, CA, gocA, gocB, gocC):
    return [AB, BC, CA, gocA, gocB, gocC]

def xet_tamgiac(AB, BC, CA, gocA, gocB, gocC):
    lis_goc = [gocA, gocB, gocC]
    if round(gocA) < 90 and round(gocB) < 90 and round(gocC) < 90:
        if AB == CA:
            print('ABC là tam giac can tai dinh A')
        elif AB == BC:
            print('ABC là tam giac can tai dinh B')
        elif CA == BC:
            print('ABC là tam giac can tai dinh C')
        else:
            print('ABC la tam giac nhon va la tam giac binh thuong')
    elif AB == BC == CA:
        print('ABC là tam giac deu')
    else:
        for i, goc in enumerate(lis_goc):
            if round(goc) == 90:
                if i == 0:
                    if AB == CA:
                        print('ABC la tam giac vuong can tai dinh A')
                    else:
                        print('ABC la tam giac vuong tai dinh A va la tam giac binh thuong')
                elif i == 1:
                    if AB == BC:
                        print('ABC la tam giac vuong can tai dinh B')
                    else:
                        print('ABC la tam giac vuong tai dinh B va la tam giac binh thuong')
                elif i == 2:
                    if CA == BC:
                        print('ABC la tam giac vuong can tai dinh C')
                    else: 
                        print('ABC la tam giac vuong tai dinh C va la tam giac binh thuong')
            elif round(goc) > 90:
                if i == 0:
                    if AB == CA:
                        print('ABC la tam giac tu va can tai dinh A')
                    else: 
                        print('ABC la tam giac tu tai dinh A va la tam giac binh thuong')
                elif i == 1:
                    if AB == BC:
                        print('ABC la tam giac tu va can tai dinh B')
                    else: 
                        print('ABC la tam giac tu tai dinh B va la tam giac binh thuong')
                elif i == 2:
                    if CA == BC:
                        print('ABC la tam giac tu va can tai dinh C')
                    else: 
                        print('ABC la tam giac tu tai dinh C va la tam giac binh thuong')
            
def dientich_tamgiac(AB, BC, CA):
    p = 1/2 * (AB + BC + CA)
    return round(sqrt(p*(p-AB)*(p-BC)*(p-CA)), 2)

def duongcao_tamgiac(AB, BC, CA):
    S = dientich_tamgiac(AB, BC, CA)
    return [round(2*S/BC, 2), round(2*S/CA, 2), round(2*S/AB, 2)]

def trungtuyen_tamgiac(AB, BC, CA):
    ttA = round(2/3 * (sqrt(((AB**2 + CA**2)/2) - (BC**2 / 4))), 2)
    ttB = round(2/3 * (sqrt(((AB**2 + BC**2)/2) - (CA**2 / 4))), 2)
    ttC = round(2/3 * (sqrt(((CA**2 + BC**2)/2) - (AB**2 / 4))), 2)
    return [ttA, ttB, ttC]

def tam_tamgiac(xAB, yAB, xCA, yCA, xBC, yBC, toado):
    x_trong = round(((toado[0]+toado[2]+toado[4])/3), 2)
    y_trong = round(((toado[1]+toado[3]+toado[5])/3), 2)
    #H la truc tam khi vecto AH.BC=0 va BH.CA=0,
    #ta giai he ptr 2 an bang phuong phap dinh thuc
    a1, b1, c1 = xBC, yBC, xBC*toado[0] + yBC*toado[1]
    a2, b2, c2 = xCA, yCA, xCA*toado[2] + yCA*toado[3]
    D = a1*b2 - a2*b1
    Dx = b2*c1 - b1*c2
    Dy = a1*c2 - a2*c1
    x_truc = round(Dx/D)
    y_truc = round(Dy/D)
    return [x_trong, y_trong, x_truc, y_truc]

def giaima_tamgiac(xAB, yAB, xAC, yAC, AB, BC, CA, gocA, gocB, gocC, toado):
    result_a = kiemtra_tamgiac(xAB, yAB, xAC, yAC)
    if result_a == True:
        print('A, B, C hop thanh mot tam giac')
    else: 
        print('A, B, C khong hop thanh mot tam giac')
        exit()

    result_b = goccanh_tamgiac(AB, BC, CA, gocA, gocB, gocC)
    print('1. So do co ban cua tam giac:')
    print('Chieu dai canh AB: ', result_b[0])
    print('Chieu dai canh BC: ', result_b[1])
    print('Chieu dai canh AC: ', result_b[2])
    print('Goc A: ', result_b[3])
    print('Goc B: ', result_b[4])
    print('Goc C: ', result_b[5])

    xet_tamgiac(AB, BC, CA, gocA, gocB, gocC)

    S = dientich_tamgiac(AB, BC, CA)
    print('2. Dien tich cua tam giac ABC: ', S)

    dc = duongcao_tamgiac(AB, BC, CA)
    tt = trungtuyen_tamgiac(AB, BC, CA)
    print('3. So do nang cao tam giac ABC')
    print('Do dai duong cao tu dinh A: ', dc[0])
    print('Do dai duong cao tu dinh B: ', dc[1])
    print('Do dai duong cao tu dinh C: ', dc[2])
    print('Khoang cach den trong tam tu dinh A: ', tt[0])
    print('Khoang cach den trong tam tu dinh B: ', tt[1])
    print('Khoang cach den trong tam tu dinh C: ', tt[2])

    tam = tam_tamgiac(xAB, yAB, xAC, yCA, xBC, yBC, toado)
    print('4. Toa do mot so diem dac biet cua tam giac ABC')
    print('Toa do trong tam: ', tam[:2])
    print('Toa do truc tam: ', tam[2:])

#########################################################
a = kiemtra_tamgiac(xAB, yAB, xCA, yCA)
print('a. kiemtra: ',a)
b = goccanh_tamgiac(AB, BC, CA, gocA, gocB, gocC)
print('b. gocanh: ',b)
print('c. xet_tamgiac:')
xet_tamgiac(AB, BC, CA, gocA, gocB, gocC)
d = dientich_tamgiac(AB, BC, CA)
print('d. dientich: ', d)
e = duongcao_tamgiac(AB, BC, CA)
print('e. duongcao:', e)
f = trungtuyen_tamgiac(AB, BC, CA)
print('f. trungtuyen: ', f)
g = tam_tamgiac(xAB, yAB, xCA, yCA, xBC, yBC, toado)
print('g. tam: ', g)
print('h. Final')
giaima_tamgiac(xAB, yAB, xCA, yCA, AB, BC, CA, gocA, gocB, gocC, toado)