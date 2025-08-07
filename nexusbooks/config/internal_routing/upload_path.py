def media_upload_path(instance, filename):
    # Use book_id if already set, or use 'temp' as fallback
    folder_name = instance.book_id if instance.book_id else 'temp'
    return f'covers/{folder_name}/{filename}'