from celery import shared_task

from django.core.exceptions import ObjectDoesNotExist

from adventure.adventure_gpt import adventure_maker
from adventure.models import Adventure, Report

from users.models import User


@shared_task(bind=True)
def adventure_background_tasks(self, user_id, adventure_id, user_input):
    try:
        try:
            user = User.objects.get(id=user_id)
            adventure = Adventure.objects.get(id=adventure_id)
        except ObjectDoesNotExist:
            # 오류 로깅 추가하기
            return
        try:
            report_content = adventure_maker(*user_input)
            report = Report(
                user=user, adventure=adventure, report_content=report_content
            )
            report.save()
        except Exception as e:
            # 오류 로깅 추가하기
            return
    except Exception as e:
        self.retry(exc=e, max_retries=3)
