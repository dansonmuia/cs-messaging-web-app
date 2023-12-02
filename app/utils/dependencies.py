MAX_LIMIT = 100


def get_pagination(offset: int = 0, limit: int = 50):
    limit = min(limit, MAX_LIMIT)
    return dict(
        offset=offset,
        limit=limit
    )
