from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer, CommentSerializer

# Create your views here.
class BlogList(APIView):
    permission_classes = [AllowAny]
    serializer_class = ArticleSerializer

    def get(self, request):
        # 1) db에서 저장된 글을 가져오고
        article = Article.objects.all()
        # 2) 글을 직렬화하고,
        serialized_article_data = ArticleSerializer(article, many=True).data
        # 3) 그 데이터를 응답으로 return
        return Response(serialized_article_data, status=status.HTTP_200_OK)
    
    def post(self, request):
        # data=request.data
        # 1) 유저가 보낸 글 제목/내용을 받아오고 → data=request.data
        #    그 데이터는 dictionary 형태로 구성되어 있음 : {title: "제목~~", "content": "내용~~"}
        # 2) 그 데이터를 역직렬화
        article_serializer = ArticleSerializer(data=request.data)
        if article_serializer.is_valid(): # 유효성 검사 -> 시리얼라이저는 유효성 검사 기능도 가지고 있음.
            # 3) 글을 db에 저장
            article_serializer.save()
            return Response({"message":"정상"}, status=status.HTTP_200_OK)
        return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class BlogDetail(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk): # url 에 있는 숫자를 pk 라는 변수로 받아옴
        article = Article.objects.get(pk=pk) # pk가 1이라면 글 id가 1인 글을 찾아서 가져옴
        serialized_article_data = ArticleSerializer(article).data # 해당 글을 직렬화함
        return Response(serialized_article_data, status=status.HTTP_200_OK) # 직렬화한 글 데이터를 응답으로 보냄

    def post(self, request, pk):
        article = Article.objects.get(pk=pk) # 우선 실제로 존재하는 글에 대해서 댓글을 달고자 하는 것인지 확인
        comment_serializer = CommentSerializer(data=request.data, partial=True) # partial=True 라고 하면, 일부 데이터가 없어도 validation을 통과함
        if comment_serializer.is_valid():
            comment_serializer.save(article=article) # 유저가 작성한 댓글을 db에 저장할 때, 앞서 db에서 찾은 article과 연결하면서 저장함
            return Response({"message": "정상"}, status=status.HTTP_200_OK)
        return Response(comment_serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk): # put 은 수정을 요청할 때 쓰는 Method 입니다
        article = Article.objects.get(pk=pk) # 기존의 글 데이터를 db 에서 찾아옴
        # 원래라면 여기서 권한 체크
        article_serializer = ArticleSerializer(article, data=request.data) # 기존의 글과 함께, 현재 유저가 보낸 수정할 데이터 (request.data) 를 명시
        if article_serializer.is_valid(): # 유효성 검사
            article_serializer.save() # 유효하다면 수정작업 완료
            return Response(article_serializer.data) # 수정한 글 데이터를 응답으로 보냄
        return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = Article.objects.get(pk=pk) # 글을 db 에서 찾아옴
        # 원래라면 여기서 권한 체크
        article.delete() # 해당 글을 db 에서 삭제함
        return Response(status=status.HTTP_204_NO_CONTENT)