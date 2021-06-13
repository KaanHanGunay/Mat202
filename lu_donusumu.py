def lu_donusumu(matris, sonuclar):
    l, u = lu_uygula(matris)
    z = z_matrisi_bul(l, sonuclar)
    x = x_matrisi_bul(u, z)
    print(f'x sonuç matrisi => {x}')


def x_matrisi_bul(u, z):
    print('Ux = Z')
    print(f'{u} * x = {z}')
    x = [None, None, None]
    x[2] = z[2] / u[2][2]
    print(f'{u[2][2]} * x3 = {z[2]} => x3 = {x[2]}')
    x[1] = (z[1] - (u[1][2] * x[2])) / u[1][1]
    print(f'{u[1][1]} * x2 + {u[1][2]} * x3 = {z[1]} => {u[1][1]} * x2 + {u[1][2] * x[2]} = {z[1]} => x2 = {x[1]}')
    x[0] = (z[0] - (u[0][2] * x[2]) - (u[0][1] * x[1])) / u[0][0]
    print(f'{u[0][0]} * x1 + {u[0][1]} * x2 + {u[0][2]} * x3 = {z[0]} => {u[0][0]} * x1 + {u[0][1] * x[1]} + '
          f'{u[0][2] * x[2]} = {z[0]} => x1 = {x[0]}')
    return x


def z_matrisi_bul(l, sonuclar):
    z = [None, None, None]
    print('Lz = b')
    print(f'{l} * z = {sonuclar}')
    z[0] = sonuclar[0]
    print(f'z1 = {z[0]}')
    z[1] = sonuclar[1] - (l[1][0] * z[0])
    print(f'{l[1][0]} * z1 + z2 = {sonuclar[1]} => {l[1][0] * z[0]} + z2 = {sonuclar[1]} => z2 = {z[1]}')
    z[2] = sonuclar[2] - (l[2][0] * z[0]) - (l[2][1] * z[1])
    print(f'{l[2][0]} * {z[0]} + {l[2][1]} * {z[1]} + z3 = {sonuclar[2]} => {l[2][0] * z[0]} + {l[2][1] * z[1]} + z3 = '
          f'{sonuclar[2]} => z3 = {z[2]}')
    print('z => ', z)
    return z


def lu_uygula(matris):
    l = [[1, 0, 0], [None, 1, 0], [None, None, 1]]
    u = [[None, None, None], [0, None, None], [0, 0, None]]
    u[0][0] = matris[0][0]
    print(f'u11 = {u[0][0]}')
    u[0][1] = matris[0][1]
    print(f'u12 = {u[0][1]}')
    u[0][2] = matris[0][2]
    print(f'u13 = {u[0][2]}')

    l[1][0] = matris[1][0] / u[0][0]
    print(f'l21 * u11 = {matris[1][0]} => l21 * {u[0][0]} = {matris[1][0]} => l21 = {l[1][0]}')
    u[1][1] = matris[1][1] - (l[1][0] * u[0][1])
    print(f'l21 * u12 + u22 = {matris[1][1]} => {l[1][0]} * {u[0][1]} + u22 = {matris[1][1]} => u22 = {u[1][1]}')
    u[1][2] = matris[1][2] - (l[1][0] * u[0][2])
    print(f'l21 * u13 + u23 = {matris[1][2]} => {l[1][0]} * {u[0][2]} + u23 = {matris[1][2]} => u23 = {u[1][2]}')

    l[2][0] = matris[2][0] / u[0][0]
    print(f'l31 * u11 = {matris[2][0]} => l31 * {u[0][0]} = {matris[2][0]} => l31 = {l[2][0]}')
    l[2][1] = (matris[2][1] - (l[2][0] * u[0][1])) / u[1][1]
    print(f'l31 * u12 + l32 * u22 = {matris[2][1]} => {l[2][1]} * {u[0][1]} + l32 * {u[1][1]} = '
          f'{matris[2][1]} => l32 = {l[2][1]}')
    u[2][2] = matris[2][2] - (l[2][0] * u[0][2]) - (l[2][1] * u[1][2])
    print(f'l31 * u13 + l32 * u23 + u33 = {matris[2][2]} => {l[2][0]} * {u[0][2]} + {l[2][1]} * {u[1][2]} + u33 = '
          f'{matris[2][2]} => u33 = {u[2][2]}')

    print('l => ', l)
    print('u => ', u)
    return l, u
