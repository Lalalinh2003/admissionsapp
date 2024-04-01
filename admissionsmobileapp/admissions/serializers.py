from admissions.models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    avatar = serializers.SerializerMethodField(source='avatar')

    def get_avatar(self, user):
        if user.avatar:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri('/static/%s' % user.avatar.name)
            return '/static/%s' % user.avatar.name

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'avatar']
        extra_kwargs = {
            'password': {'write_only': 'true'}
        }

    def create(self, validated_data):
        user = User(**validated_data)
        if permissions.AllowAny():
            user.isCandidate = True
        user.is_staff = True
        user.set_password(validated_data['password'])
        user.save()

        return user


class MajorSerializer(ModelSerializer):
    class Meta:
        model = Major
        fields = ["id", "code", "name", "faculty"]


class FacultySerializer(ModelSerializer):
    image = serializers.SerializerMethodField(source='image')
    #majors = MajorSerializer(many=True)

    def get_image(self, faculty):
        if faculty.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri('/static/%s' % faculty.image.name)
            return '/static/%s' % faculty.image.name

    class Meta:
        model = Faculty
        fields = ["id", "name", "website", "introduction", "program", "created_date", "updated_date", "image"]


class YearSerializer(ModelSerializer):
    class Meta:
        model = Year
        fields = ["id", "year"]


class MarkSerializer(ModelSerializer):
    major = MajorSerializer()
    year = YearSerializer()
    class Meta:
        model = Mark
        fields = ["id", "mark", "major", "year"]


class InformationSerializer(ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, info):
        if info.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri('/static/%s' % info.image.name)
            return '/static/%s' % info.image.name

    class Meta:
        model = Information
        fields = ["id", "title", "description", "infosection", "image", "created_date", "updated_date"]


class InformationSecSerializer(ModelSerializer):
    infos = InformationSerializer(many=True)
    class Meta:
        model = InformationSection
        fields = ["id", "name", "infos"]


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = ["id", "content", "time", "info", "user"]


class QuestionsSerializer(ModelSerializer):
    class Meta:
        model = Questions
        fields = ["id", "content", "time", "livestream", "user"]

    """
    def create(self, validated_data):
        question = Questions(**validated_data)
        live = Livestream.objects.all()
        try:
            for l in live:
                if l.id == question.livestream:
                    if l.isActive == True:
                        question.save()
                        return question
        except:
            return "Can't create"
    """



class BannerSerializer(ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, banner):
        if banner.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri('/static/%s' % banner.image.name)
            return '/static/%s' % banner.image.name

    class Meta:
        model = BannerImage
        fields = ["id", "image"]


class UniversitySerializer(ModelSerializer):
    class Meta:
        model = UniversityInfo
        fields = ["introduction"]


class LivestreamSerializer(ModelSerializer):
    class Meta:
        model = Livestream
        fields = ["id", "title", "announce", "time"]



