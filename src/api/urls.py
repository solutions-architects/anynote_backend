"""All API's urls. Collect from the dedicated api apps folders."""

# Import APIs modules
import src.api.v1.anynote
import src.api.v1.authentication

# Add urlpatterns from api apps folders
urlpatterns = []
urlpatterns += src.api.v1.anynote.urlpatterns  # Anynote api urls
urlpatterns += src.api.v1.authentication.urlpatterns  # Auth api urls
