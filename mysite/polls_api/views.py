# from django.shortcuts import render, get_object_or_404
# from rest_framework.decorators import api_view
from polls.models import Question
from polls_api.serializers import QuestionSerializer
# from rest_framework.response import Response
from rest_framework import generics
# from rest_framework.views import APIView

class QuestionList(generics.ListCreateAPIView):
    # mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    #     # questions = Question.objects.all()
    #     # serializer = QuestionSerializer(questions, many=True)
    #     # return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    #     # serializer = QuestionSerializer(data=request.data)
    #     # if serializer.is_valid():
    #     #     serializer.save()
    #     #     return Response(serializer.data)
    #     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def question_list(request):
#     if request.method == 'GET':
#         questions = Question.objects.all()
#         serializer = QuestionSerializer(questions, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     if request.method == 'POST':
#         serializer = QuestionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    # mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    #     # question = get_object_or_404(Question, pk=id)
    #     # serializer = QuestionSerializer(question)
    #     # return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #     # question = get_object_or_404(Question, pk=id)
    #     # serializer = QuestionSerializer(question, data=request.data)
    #     # if serializer.is_valid():
    #     #     serializer.save()
    #     #     return Response(serializer.data, status=status.HTTP_200_OK)
    #     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
    #     # question = get_object_or_404(Question, pk=id)
    #     # question.delete()
    #     # return Response(status=status.HTTP_204_NO_CONTENT)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def question_detail(request, id):
#     if request.method == 'GET':
#         question = get_object_or_404(Question, pk=id)
#         serializer = QuestionSerializer(question)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     if request.method == 'PUT':
#         question = get_object_or_404(Question, pk=id)
#         serializer = QuestionSerializer(question, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         question = get_object_or_404(Question, pk=id)
#         question.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
