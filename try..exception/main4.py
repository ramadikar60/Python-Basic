nilai = -999999
try:
    print("baris ini akan di print")
    if nilai < 0:
        raise ValueError(nilai)
    print("baris ini tidak akan di print")
except Exception as err:
    print(err)
finally:
    print("Ada error nih !!!")