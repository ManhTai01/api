
from rest_framework import routers
from .blog.views import BlogViewSet
from .job.views import JobViewSet
from .service.views import ServiceViewSet
from .talent.views import TalentViewSet
from .jobSubmission.views import SubmissionViewSet
from .jobSubmission.views import EmailView


router = routers.SimpleRouter()
router.register('blog', BlogViewSet)
router.register('job', JobViewSet)
router.register('talent', TalentViewSet)
router.register('service', ServiceViewSet)
router.register('jobSubmission', SubmissionViewSet)

app_name = 'api'
urlpatterns = router.urls
