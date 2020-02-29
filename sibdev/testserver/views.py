from django.db.models import Sum
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Deal


@api_view(('GET',))
def get(request):
    customers = [i.get('customer') for i in Deal.objects.values('customer').distinct()]
    for i, cust in enumerate(customers):
        customertotal = Deal.objects.filter(customer=cust).aggregate(Sum('total')).get('total__sum')
        stones = [i.get('item') for i in Deal.objects.filter(customer=cust).values('item').distinct()]
        stones.sort()
        customers[i] = dict(username=customers[i], spent_money=customertotal, gems=stones)
    customers.sort(key=lambda customer: customer['spent_money'], reverse=True)
    # all gems of 5 users
    allgems = []
    for i in range(0, 5):
        allgems += customers[i].get('gems')

    for i in range(0, 5):
        arr = customers[i].get('gems')
        for j in arr.copy():
            if (allgems.count(j) < 2):
                arr.remove(j)
    return Response({"response": customers[0:5]})


@api_view(('POST',))
def post(request):
    file = request.FILES['deals']
    data_set = file.read().decode('UTF-8')
    if not file.name.endswith('.csv'):
        return Response({'Desc': 'you send not scv file'}, status=status.HTTP_418_IM_A_TEAPOT)
    deals = data_set.split('\n')

    for i in range(1, len(deals)):
        try:
            temp = deals[i].split(',')
            x = Deal.objects.filter(customer=temp[0]).filter(item=temp[1]).filter(total=temp[2]).filter(
                quantity=temp[3]).filter(
                date=temp[4]).exists()
            # check exists deal in db  or not
            if (not x):
                deal = Deal(customer=temp[0], item=temp[1], total=temp[2], quantity=temp[3],
                            date=temp[4])
                deal.save()

        except BaseException as ex:
            return Response({'Desc': str(ex)}, status=status.HTTP_400_BAD_REQUEST)

    return Response('file successfully processed and fully added to the database', status=status.HTTP_200_OK)
