import uuid

from apps.models import Applications


def generate_random_app_name(request):
    random_uuid = "-" + str(uuid.uuid4()).split("-")[0]
    request.data["name"] += random_uuid
    return request.data["name"]


def handle_related_subscription(request, subscription):
    app = Applications.objects.create(**request.data)
    app.subscription_app.add(subscription)
    app.save()
    return app
