import requests

cookies = {
    '_ga': 'GA1.1.1498436310.1684335268',
    '_ga_WWM6MDNY8G': 'GS1.1.1684492489.9.1.1684492576.0.0.0',
    '_ym_visorc': 'w',
    'XSRF-TOKEN': 'eyJpdiI6Ilc0UTBuU1RocCsxU3pwd3Z4ZGhWRlE9PSIsInZhbHVlIjoiVC9uajkvMHRjMjcvQmloeXh5MzNPdWhDRkFiWDdibHN1b1NjdlZNb1hxOXNaZnlhN3FHZ2NWZDNrSS8rOTlmdWd2UmU2V0JvazN4VDRPenNEYWUvaGJGaks0SFRlS2VQcVVFRksySjBPUEVjd0RLbGIyQmFhSkhDNHFyN1o3OFgiLCJtYWMiOiIyN2EzMDczYTZlYmUzNjA4N2ZlNWQ1OGIxNjAyYTExNzQ2YTVkYzRhOTAxNDU2ZmVjYWY0ZjQxMzExNGJiMWNkIiwidGFnIjoiIn0%3D',
    'ultramining_session': 'eyJpdiI6IkdSWlJlVWEyeTcxNVQ3MDczU0NhQnc9PSIsInZhbHVlIjoidkNvMnRxb1dzMGtBQy92Y3FpQVJtQ01wdkh4WjBDd2FtTW9wdEx0RGVDMUtQTDJEZHhrdk02VzVJQjk4L1d1OE1wbU5xZHRrMlo4UDJ5MkJVR2JSMytsRE0wN09RbmR4eDlXek94S2VMZUZ5Z1FndDc5bU5QajJpYXh4WmhabFoiLCJtYWMiOiI4MDFiYmM5NTMzYTkzMmFmMmRjMjE5NDRkZWY4ZGYzOWNhNjY5MDhhOWNkOThlZDlmMmFiYTAxNjQyZjFiOGYwIiwidGFnIjoiIn0%3D',
    '_ym_isad': '2',
    '_ym_d': '1684335269',
    '_ym_uid': '1684335269609173002',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Sec-Fetch-Site': 'same-origin',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'ultramining.com',
    'Sec-Fetch-Mode': 'navigate',
    'Accept-Language': 'ru',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
    'Connection': 'keep-alive',
    'Referer': 'https://ultramining.com/crypto-calc/bitcoin/',
    # 'Cookie': '_ga=GA1.1.1498436310.1684335268; _ga_WWM6MDNY8G=GS1.1.1684492489.9.1.1684492576.0.0.0; _ym_visorc=w; XSRF-TOKEN=eyJpdiI6Ilc0UTBuU1RocCsxU3pwd3Z4ZGhWRlE9PSIsInZhbHVlIjoiVC9uajkvMHRjMjcvQmloeXh5MzNPdWhDRkFiWDdibHN1b1NjdlZNb1hxOXNaZnlhN3FHZ2NWZDNrSS8rOTlmdWd2UmU2V0JvazN4VDRPenNEYWUvaGJGaks0SFRlS2VQcVVFRksySjBPUEVjd0RLbGIyQmFhSkhDNHFyN1o3OFgiLCJtYWMiOiIyN2EzMDczYTZlYmUzNjA4N2ZlNWQ1OGIxNjAyYTExNzQ2YTVkYzRhOTAxNDU2ZmVjYWY0ZjQxMzExNGJiMWNkIiwidGFnIjoiIn0%3D; ultramining_session=eyJpdiI6IkdSWlJlVWEyeTcxNVQ3MDczU0NhQnc9PSIsInZhbHVlIjoidkNvMnRxb1dzMGtBQy92Y3FpQVJtQ01wdkh4WjBDd2FtTW9wdEx0RGVDMUtQTDJEZHhrdk02VzVJQjk4L1d1OE1wbU5xZHRrMlo4UDJ5MkJVR2JSMytsRE0wN09RbmR4eDlXek94S2VMZUZ5Z1FndDc5bU5QajJpYXh4WmhabFoiLCJtYWMiOiI4MDFiYmM5NTMzYTkzMmFmMmRjMjE5NDRkZWY4ZGYzOWNhNjY5MDhhOWNkOThlZDlmMmFiYTAxNjQyZjFiOGYwIiwidGFnIjoiIn0%3D; _ym_isad=2; _ym_d=1684335269; _ym_uid=1684335269609173002',
    'Sec-Fetch-Dest': 'document',
    'Priority': 'u=0, i',
}

response = requests.get('https://ultramining.com/crypto-calc/bitcoin/', cookies=cookies, headers=headers)


with open('resultic.html', 'w') as file:
    file.write(response.text)
