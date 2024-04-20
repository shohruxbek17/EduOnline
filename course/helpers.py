from django.db.models import TextChoices
import uuid

class SaveMediaFiles(object):
    def speciality_image_path(instance, filename):
        image_extention = filename.split('.')[-1]
        return f'course/speciality/{uuid.uuid4()}{image_extention}'


class Choises(object):

    class PriceType(TextChoices):
        d = 'USD' , '$'
        s = 'UZS' , 'sum'


    class CourseStatus(TextChoices):

        DRAFT = "df", "draft"
        PUBLISHER = "pb", "published"