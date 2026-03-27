notifications = []

def add_notification(message, target):
    notifications.append({
        "message": message,
        "target": target
    })

def get_notifications(target):
    return [n for n in notifications if n["target"] == target]