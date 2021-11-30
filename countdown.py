import random
from datetime import datetime


def main():
    print("""\n
=============================================
                !!WARNING!!
=============================================

- Please run this program with caution.
- Never run this program in unsafe places and
  conditions.
- This program contains a high dose of 'uwu'
  (Potentially can make you smile all day 
  long)""")
    enter()


def read_me():
    print("""\n
=============================================
                   Readme
=============================================

dear bit,

kaya yang udah pernah aku janjiin, ini aku
buatin program sederhana yang bisa di-"run"
di console. karena aku masih bimbang antara
balik tanggal 6/7 di sini estimasi tanggal
pulangku aku bikin tanggal 7/1/2022 flight
jam 9:05 WITA ya.

emang awalnya countdown doang, tapi kok kaya
hambar gitu aku ngerasanya. jadi aku tambahin
beberapa hal biar seru. hehe

maaf ya, aku baru bisa bikin yang console
based, nanti buat event selanjutnya aja aku 
bikinin yang ada interfacenya. 

semoga kamu suka. semoga bisa menghibur kalo 
kamu lagi sedih, suntuk, atau bete. enjoy this 
apps yah.

i love you so much, bit sayang
<3 <3 <3

                                   with love,
                                   mas""")
    enter()


def countdown():
    print("""\n
=============================================
                  Countdown
=============================================""")
    current_time = datetime.now()
    # current_time = datetime(2022, 1, 18, 13, 15, 0, 0)
    flight_time = datetime(2022, 1, 7, 8, 5, 0, 0)
    diff = flight_time - current_time
    hour = str((diff.seconds // 3600)).zfill(2)
    minute = str((3720 // 60) % 60).zfill(2)
    second = str((diff.seconds % 3600) % 60).zfill(2)
    # print(type(diff.days))
    if diff.days < -11:
        print("""
sayang, kayanya kamu harus kontak hotline deh.
ini scriptnya udah harus maintenance.""")
    elif diff.seconds < 0 and diff.days > -11:
        print("""yeay! mas udah pulang yahh.
ayo redeem voucher kamu sayang""")
    else:
        print(f"\nSayang sabar yahh. bentar lagi mas pulang kok.")
        print(f"Tinggal {diff.days} hari {hour}:{minute}:{second} sebelum flight mas\nke surabaya")
        refresh_countdown()


def random_facts():
    print("""\n
=============================================
                Random Facts
=============================================""")
    fact_list = ["Mas nemuin profil bit di tinder tanggal 21/10/21",
                 "Kita match di tinder tanggal 22/10/21",
                 "Tanggal 25/10/21 adalah hari pertama kita\nketemu setelah 10 tahun",
                 '"I love you" pertama kita bertepatan\ndengan hari sumpah pemuda',
                 "Pajero, sepasang gelang, jaket denim, dan\nlampu jalan kupang jaya adalah saksi bisu",
                 "Kita pernah pake badge sbi 7b-8a-9b",
                 "Golongan darah kita B",
                 '"Ga pengen settled di satu kota?" adalah\nsebuah percobaan tes ombak pertama',
                 '"Kamu orangnya well prepared banget ya"\nadalah pujian pertama yang mas terima sejak\nawal kita tau'
                 "sama tau",
                 '"Ini nih" = "deng"',
                 'Sejauh ini, tercatat ada 3 foto kita\n(yang kelihatan jelas mukanya) dalam satu\nframe'
                 'sebelum kita kenal kaya sekarang',
                 'post foto wisuda di ig tanggal 21/09/21 adalah\nfoto pertama yang mas like dan\npertama kali juga mas'
                 'scroll ig bit',
                 '"aku kagum" adalah salah satu pemantik\nspark di hari itu']
    print(f"\n{random.choice(fact_list)}")
    refresh_random()


def faq():
    print("""\n
=============================================
          Frequently Asked Question
=============================================

Q : Mas kenapa niat banget siiiih?
A : Masa buat kamu ngaasihnya yang setengah2

Q : Ini kalo bit makin kangen gimana?
A : Nanti aku bakal pulang sayang, tenang.
    Sembari nunggu aku pulang, kamu juga bisa
    banget buat minta selfie, telfon, vc,
    zoom, apapun.

Q : Mas kapan bit bisa redeem vouchernya?
A : Nanti kalo mas pulang ya sayaang, cash

Q : Kalo ternyata ada trouble waktu di-run?
A : Tinggal kontak hotline aja yaah, nanti
    ceritain kenapa troublenya

Q : Mungkin ga buat request fitur tambahan?
A : Bisa, kontak hotline aja. bit tinggal
    bilang, "Mas sayang, bit mau minta tambah
    fitur boleh?". Nanti dijelasin lebih
    dalem lagi specsnya

For further question and affection,
Whatsapp: 081334455285""")
    enter()


def menu():
    print("""\n
v 1.0.1    
=============================================
           Special Count Down <3
=============================================
1 - Read Me
2 - Countdown
3 - Random Facts
4 - FAQ
q - Quit""")


def selection():
    sel = input("\nCoba kamu mau pilih yang mana sayang? ")
    if sel == "1":
        read_me()
    elif sel == "2":
        countdown()
    elif sel == "3":
        random_facts()
    elif sel == "4":
        faq()
    elif sel == "q" or sel == "Q":
        pass
    else:
        input("""\nSayang, inputnya yang beneer :(
Pencet enter ya buat balik ke menu: """)
        menu()
        selection()


def refresh_countdown():
    cont = input("\nmau di-refresh? (y/n): ")
    if cont == 'y' or cont == 'Y':
        countdown()
    elif cont == 'n' or cont == 'N':
        enter()
    else:
        print("\nSayang, inputnya yang beneer :(")
        print("cobain lagi yah")
        refresh_countdown()


def refresh_random():
    cont = input("\nmau di-refresh? (y/n): ")
    if cont == 'y' or cont == 'Y':
        random_facts()
    elif cont == 'n' or cont == 'N':
        enter()
    else:
        print("\nSayang, inputnya yang beneer :(")
        print("cobain lagi yah")
        refresh_random()


def enter():
    input("\nPress enter to continue: ")
    menu()
    selection()


if __name__ == "__main__":
    main()
