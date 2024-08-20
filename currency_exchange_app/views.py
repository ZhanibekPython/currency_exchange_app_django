from django.shortcuts import render
import requests

MY_API_KEY = "11704122ee872bf1da59faca"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/127.0.0.0 Safari/537.36"
}


def exchange(request):
    response = requests.get(url=f'https://v6.exchangerate-api.com/v6/{MY_API_KEY}/latest/USD',
                            headers=HEADERS).json()
    all_curs = response['conversion_rates']

    if request.method == 'GET':
        return render(request=request, template_name='currency_exchange_app/index.html', context={'all_curs': all_curs})

    if request.method == 'POST':
        entered_sum = float(request.POST.get('entered_sum'))
        from_cur = request.POST.get('from_cur').strip()
        to_cur = request.POST.get('to_cur').strip()

        # response2 = requests.get(url=f'https://v6.exchangerate-api.com/v6/{MY_API_KEY}/latest/{from_cur}',
        #                          headers=HEADERS)

        converted_sum = all_curs[to_cur] / all_curs[from_cur] * entered_sum
        context = {
            'all_curs': all_curs,
            'entered_sum': entered_sum,
            'from_cur': from_cur,
            'to_cur': to_cur,
            'converted_sum': converted_sum
        }
        return render(request=request, template_name='currency_exchange_app/index.html', context=context)
