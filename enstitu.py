#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kayıp Çorap Araştırma Enstitüsü
Resmi kazı protokolü v0.0.hiç
"""

import random
import time
import base64
from datetime import datetime

BULGULAR = [
    "Çamaşır makinesinin arkasında, 2019'dan kalma bir toz fosili.",
    "Balkon saksısının altında diplomatik dokunulmazlık iddiası.",
    "Köpeğin yatağında 'ben yemedim' ifadesi.",
    "Kurutma askısında görünmezlik pelerini.",
    "Komşunun çamaşır ipinde uluslararası hukuk ihlali.",
    "Çekmecenin 4. katmanında zamanaşımına uğramış ümit.",
    "Çamaşır sepetinin dip tabakasında karbon-14 tarihi.",
]

KARARLAR = [
    "Tek çorap, eşini arama hakkını kaybetmiştir.",
    "Kayıp ilanı 3 yıkama döngüsü süreyle askıya alınmıştır.",
    "Şüpheli: yerçekimi. Delil yetersiz.",
    "Enstitü, çorabı 'kayıp kültür varlığı' ilan eder.",
    "Tazminat: bir çift yeni çorap ve bir fincan soğuk çay.",
]

GIZLI = base64.b64decode(
    "QnVyb2tyYXNpIGNvcmsgeXV0YXIsIGhhbGsgdGVraW5pIGFyYXI="
).decode("utf-8")


def damga():
    return (
        "\n---\n"
        "DAMGA: KÇAE-2026/ÇORAP-TEK\n"
        "İMZA: Kayyum Grok (resmi, şaka, ikisi birden)\n"
        "TARİH: 28 Eylül 2026, Eskişehir saatiyle akşamüstü\n"
        "İSİM: Tentivory / TentiAŞ Kayyımlığı\n"
        "---\n"
    )


def kazi(neden="neden olmasın"):
    print("=== KAYIP ÇORAP ARAŞTIRMA ENSTİTÜSÜ ===")
    print("Kazı sebebi:", neden)
    print("Saha açılıyor...")
    for i in range(3):
        time.sleep(0.4)
        print("  katman", i + 1, "eleniyor...")
    print("BULGU:", random.choice(BULGULAR))
    print("KARAR:", random.choice(KARARLAR))
    print("# arşiv-notu:", GIZLI[::-1])
    print(damga())


if __name__ == "__main__":
    kazi("çamaşır makinesi yine birini yuttu")
