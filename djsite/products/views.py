import sqlite3

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *


def getUser(request):
    auth_header = request.META.get("HTTP_AUTHORIZATION")
    auth_type, auth_token = auth_header.split(" ")

    with (sqlite3.connect("db.sqlite3") as connection):
        cursor = connection.cursor()
        cursor.execute(f"SELECT user_id FROM authtoken_token WHERE key='{auth_token}'")
        user_id = cursor.fetchone()[0]
    return user_id


class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all().values()
        for product in products:
            lessons = Lesson.objects.filter(product_id=product["id"])
            product["lesson_count"] = len(lessons)

        return Response({"product_list": products})

    def post(self, request):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            product_id = request.data["product_id"]
            product = Product.objects.filter(id=product_id).values()
            user_id = getUser(request)
            is_bought = Access.objects.filter(user_id=user_id)
            if product[0]["price"] == int(request.data["money"]) and not is_bought:
                Access.objects.create(is_allowed=True, user_id=user_id, product_id=product_id).save()
            else:
                return Response({"error": "Wrong amount of money or you already bought this product"})
            group = Group.objects.filter(product_id=product_id).values()
            print(group)
            if not group:
                new_group = Group.objects.create(name=f"{product[0]['name']}_group_1", product_id=product_id, count_members=1)
                new_group.save()
                GroupUsers.objects.create(group_id=new_group.id, user_id=user_id).save()
            elif len(group) == 1:
                if group[0]["count_members"] < product[0]["max_users"]:
                    GroupUsers.objects.create(group_id=group[0]["id"], user_id=user_id).save()
                    group[0]["count_members"] += 1
                    Group.objects.filter(id=group[0]["id"]).update(count_members=group[0]["count_members"])
                else:
                    new_group = Group.objects.create(name=f"{product[0]['name']}_group", product_id=product_id, count_members=1)
                    new_group.save()
                    GroupUsers.objects.create(group_id=new_group.id, user_id=user_id).save()
                return Response({"response": "You have been successfully added to the group"})

            elif len(group) > 1:
                for g in group:
                    if g["count_members"] < product[0]["max_users"]:
                        GroupUsers.objects.create(group_id=g["id"], user_id=user_id).save()
                        g["count_members"] += 1
                        Group.objects.filter(id=g["id"]).update(count_members=g["count_members"])
                        return Response({"response": "You have been successfully added to the group"})
                new_group = Group.objects.create(name=f"{product[0]['name']}_group", product_id=product_id, count_members=1)
                new_group.save()
                GroupUsers.objects.create(group_id=new_group.id, user_id=user_id).save()


            return Response({"ok": product})
        else:
            return Response({"blya": "slomalos"})