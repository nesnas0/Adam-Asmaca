def yer(x, y):
	liste = []
	artır = 0
	while y in x:
		liste.append(x.index(y) + artır)
		x = list(x)
		x.remove(x[x.index(y)])
		x = ''.join(x)
		artır += 1
	return liste

cumle = ''

kalan = 5

def alt(x):
    x = list(x)
    for i in range(0,len(x)):
        if x[i] != ' ':
            x[i] = '_'
    x = ''.join(x)
    return x
    
sonuc = alt(cumle)

print('Cümle: ', sonuc)


while '_' in sonuc:
	tahmin = input('Bir harf giriniz: ')
	print('')

	if tahmin in cumle:
		print('Doğru tahmin!')

		for a in yer(cumle, tahmin):
			sonuc = list(sonuc)
			sonuc[a] = tahmin
			sonuc = ''.join(sonuc)
		
		print('Cümle: ', sonuc)
		print('')
	else:
		kalan -= 1
		if kalan == 0:
			print('Kaybettiniz. Cümle "{}" idi.'.format(cumle))
			break
		else:
			mesaj = 'Girdiğiniz harf cümlede bulunmuyor. {} hakkınız kaldı.'
			print(mesaj.format(kalan)

if '_' not in sonuc:
	print('Cümleyi bildiniz!')
