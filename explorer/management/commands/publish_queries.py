from celery import group
from celery.utils.log import get_task_logger
from django.core.management.base import BaseCommand
from django.db.models import F, Q

from explorer.models import Query, FTPExport
from explorer.tasks import snapshot_query_on_bucket


logger = get_task_logger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info("Starting query snapshots...")
        queries = Query.objects.exclude(
            Q(bucket__exact='') |
            Q(bucket__isnull=True)
        )
        priority = queries.filter(priority=True).values_list('pk', flat=True)
        no_priority = queries.filter(priority=False).values_list('pk', flat=True)
        
        group_priority = group([snapshot_query_on_bucket.s(pk) for pk in priority])
        group_no_priority = group([snapshot_query_on_bucket.s(pk) for pk in no_priority])
        canvas = group_priority | group_no_priority
        canvas()
