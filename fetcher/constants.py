FETCH_STATUS_SUCCESS = 1
FETCH_STATUS_CONNECTION_ERROR = 2
FETCH_STATUS_NO_METADATA_RECEIVED = 3
FETCH_STATUS_NO_METADATA_MATCH = 3
FETCH_STATUS_LOW_RELEVANCY_MATCH = 4
FETCH_STATUS_UNKNOWN_ERROR = 999
FETCH_STATUS_CHOICES = (
    (FETCH_STATUS_SUCCESS,'Success',),
    (FETCH_STATUS_CONNECTION_ERROR,'Connection Error',),
    (FETCH_STATUS_NO_METADATA_RECEIVED,'No Metadata',),
    (FETCH_STATUS_NO_METADATA_RECEIVED,'No Match for Metadata',),
    (FETCH_STATUS_LOW_RELEVANCY_MATCH,'Low Relevancy Match',),
    (FETCH_STATUS_UNKNOWN_ERROR,'Unknown Error'),
)

#TODO: what do the scores represent?
MUSICBRAINZ_TRACK_RESULT_SCORE_LOW = 80


