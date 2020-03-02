from celery import group
from celery.utils.log import get_task_logger
from django.core.management.base import BaseCommand
from django.db.models import Q

from explorer.models import Query
from explorer.tasks import snapshot_query_on_bucket


logger = get_task_logger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        logger.info("Starting query snapshots...")
        queries = Query.objects.exclude(
            Q(bucket__exact='') |
            Q(bucket__isnull=True)
        ).order_by('id').distinct().values_list('pk', flat=True)

        query_group = group(
            [snapshot_query_on_bucket.s(query_id=pk) for pk queries]
        )
        query_group()
